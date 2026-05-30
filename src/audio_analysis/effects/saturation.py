"""
saturation.py
Estimation du niveau de saturation/distortion via features spectrales.

Approche multi-indices :
- Spectral flatness : signal sature -> plus de plat (energie repartie sur toutes freqs)
- Spectral centroid eleve : saturation ajoute des harmoniques hautes
- Zero-crossing rate eleve : saturation = plus de transitions par seconde
- Harmonics-to-noise ratio (HNR) : saturation reduit le HNR

Limites :
- Approximations sur signal mixe (le HM-2 d'un autre instrument peut polluer)
- Sur stem guitare isole (Demucs), bien plus fiable
"""

import numpy as np
import librosa


def detect_saturation(y: np.ndarray, sr: int) -> dict:
    """
    Estime le niveau de saturation/distortion d'un signal.

    Returns:
        {
          "level_0_1":          0.65,
          "level_label":        "moderate" | "low" | "high" | "extreme",
          "spectral_flatness":  0.32,
          "spectral_centroid_hz": 2150.0,
          "zero_crossing_rate": 0.12,
          "method":             "...",
        }
    """
    if len(y) == 0:
        return {"level_0_1": 0.0, "level_label": "unknown",
                "method": "empty signal"}

    # Spectral flatness (mediane sur le temps)
    flatness = librosa.feature.spectral_flatness(y=y)
    flatness_med = float(np.median(flatness))

    # Spectral centroid (mediane)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    centroid_med = float(np.median(centroid))

    # Zero-crossing rate (mediane)
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_med = float(np.median(zcr))

    # Score combine 0-1
    # Heuristique calibree sur guitares electriques :
    # - flatness > 0.2 = bcp de saturation
    # - centroid > 2500 Hz = pousse vers les aigus (signe de saturation typique)
    # - zcr > 0.10 = beaucoup de transitions
    flatness_score = min(flatness_med / 0.35, 1.0)
    centroid_score = min(max((centroid_med - 800) / 2500, 0.0), 1.0)
    zcr_score = min(zcr_med / 0.20, 1.0)
    # Combine (poids legerement plus eleve sur flatness)
    level = float(0.45 * flatness_score + 0.30 * centroid_score + 0.25 * zcr_score)
    level = max(0.0, min(1.0, level))

    # Label
    if level < 0.25:
        label = "low"     # clean ou crunch tres leger
    elif level < 0.50:
        label = "moderate"  # crunch / OD modere
    elif level < 0.75:
        label = "high"    # distortion prononcee
    else:
        label = "extreme"  # fuzz / high gain metal

    return {
        "level_0_1":            round(level, 2),
        "level_label":          label,
        "spectral_flatness":    round(flatness_med, 3),
        "spectral_centroid_hz": round(centroid_med, 1),
        "zero_crossing_rate":   round(zcr_med, 3),
        "method":               "weighted: flatness(0.45)+centroid(0.30)+ZCR(0.25)",
    }
