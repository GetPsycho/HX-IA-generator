"""
saturation.py
Estimation du niveau de saturation/distortion d'un signal guitare.

Approche (validee sur 3 morceaux references) :
- Harmonic-to-Percussive Ratio (H_ratio) : la saturation cree des harmoniques
  soutenues -> ratio energie harmonique / total eleve
- Crest factor sur fenetres courtes (50ms) : la saturation compresse les
  transitoires -> crest plus bas
- Spectral flatness en bande mid (500-3000 Hz) : zone des harmoniques
  guitare independante du tuning, plus plate = plus sature

Score combine sur [0, 1] avec poids ponderes :
- H_ratio : 0.50  (l'indicateur le plus discriminant)
- CrestSW : 0.30
- FlatMid : 0.20

NB : sur signal mixe (non isole par Demucs), les valeurs sont polluees par
basse/batterie. Ce detecteur est calibre pour fonctionner sur stem guitare.
"""

import numpy as np
import librosa


def detect_saturation(y: np.ndarray, sr: int,
                       analysis_window_s: float = 30.0) -> dict:
    """
    Estime le niveau de saturation/distortion d'un signal guitare.

    Args:
        y  : signal audio mono
        sr : sample rate
        analysis_window_s : fenetre d'analyse au milieu du morceau (defaut 30s)
                            -> plus rapide et representatif de l'etat permanent

    Returns:
        {
          "level_0_1":        0.55,
          "level_label":      "moderate" | "low" | "high" | "extreme",
          "harmonic_ratio":   0.886,
          "crest_short_db":   9.7,
          "flatness_mid":     0.73,
          "spectral_centroid_hz": 2045.0,
          "method":           "weighted: h_ratio(0.50) + crest_sw_inv(0.30) + flat_mid(0.20)",
        }
    """
    if len(y) == 0:
        return {"level_0_1": 0.0, "level_label": "unknown",
                "method": "empty signal"}

    # Prendre une fenetre centrale (rapide + representatif de l'etat regime)
    win_samples = int(analysis_window_s * sr)
    if len(y) > win_samples:
        mid = len(y) // 2
        seg = y[max(0, mid - win_samples // 2): mid + win_samples // 2]
    else:
        seg = y

    # --- 1. Harmonic-to-Percussive Ratio ---
    h, p = librosa.effects.hpss(seg)
    h_energy = float(np.sum(h ** 2))
    p_energy = float(np.sum(p ** 2))
    h_ratio = h_energy / (h_energy + p_energy + 1e-9)

    # --- 2. Crest factor short window (50ms) ---
    win = int(0.05 * sr)
    n_w = len(seg) // win
    crests_db = []
    for i in range(n_w):
        w = seg[i * win:(i + 1) * win]
        peak = float(np.max(np.abs(w)))
        rms_w = float(np.sqrt(np.mean(w ** 2)))
        if rms_w > 1e-6:
            crests_db.append(20 * np.log10(peak / rms_w))
    crest_sw = float(np.median(crests_db)) if crests_db else 14.0

    # --- 3. Spectral flatness en bande mid (500-3000 Hz) ---
    stft = np.abs(librosa.stft(seg))
    freqs = librosa.fft_frequencies(sr=sr)
    mask = (freqs >= 500) & (freqs <= 3000)
    spec_mid = stft[mask]
    if spec_mid.size > 0:
        geo = np.exp(np.mean(np.log(spec_mid + 1e-9), axis=0))
        arith = np.mean(spec_mid, axis=0) + 1e-9
        flat_mid = float(np.median(geo / arith))
    else:
        flat_mid = 0.5

    # --- Indicateur secondaire : spectral centroid (info, pas dans le score) ---
    centroid = float(np.median(librosa.feature.spectral_centroid(y=seg, sr=sr)))

    # --- Score combine sur [0, 1] ---
    # Calibrage empirique sur references :
    # H_ratio : 0.75 = clean, 0.95 = tres sature -> map vers [0, 1]
    h_score = max(0.0, min((h_ratio - 0.75) / 0.20, 1.0))
    # Crest SW : 14 dB = clean, 8 dB = heavy -> inverse
    crest_score = max(0.0, min((14.0 - crest_sw) / 6.0, 1.0))
    # Flatness mid : 0.55 = clean, 0.85 = sature
    flat_score = max(0.0, min((flat_mid - 0.55) / 0.30, 1.0))

    level = 0.50 * h_score + 0.30 * crest_score + 0.20 * flat_score
    level = max(0.0, min(1.0, level))

    if level < 0.30:
        label = "low"      # clean ou crunch tres leger
    elif level < 0.55:
        label = "moderate"  # crunch / OD modere
    elif level < 0.78:
        label = "high"     # distortion prononcee
    else:
        label = "extreme"   # fuzz / high gain metal

    return {
        "level_0_1":            round(level, 2),
        "level_label":          label,
        "harmonic_ratio":       round(h_ratio, 3),
        "crest_short_db":       round(crest_sw, 1),
        "flatness_mid":         round(flat_mid, 3),
        "spectral_centroid_hz": round(centroid, 1),
        "method":               "weighted: h_ratio(0.50) + crest_sw_inv(0.30) + flat_mid(0.20)",
    }
