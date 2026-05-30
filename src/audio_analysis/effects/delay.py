"""
delay.py
Detection de la presence et du temps d'un delay via autocorrelation.

Principe :
- Si un delay est present, le signal "ressemble" a lui-meme decale en temps
- Autocorrelation -> pics aux multiples du temps de delay
- On cherche un pic significatif dans la plage 50-1500 ms (plage typique guitare)

Limites :
- Beaucoup de delays subtils ne creent pas de pic clair dans l'autocorrelation
- Les delays en feedback eleve donnent plusieurs pics (echos multiples)
- Les delays modulis (chorus-y) sont plus difficiles a detecter
"""

import numpy as np
import scipy.signal


_MIN_DELAY_MS = 50
_MAX_DELAY_MS = 1500


def detect_delay(y: np.ndarray, sr: int) -> dict:
    """
    Detecte si un delay est present et estime son temps.

    Returns:
        {
          "detected":      True | False,
          "time_ms":       320 | None,
          "confidence":    0.45,
          "peak_strength": 0.32,
          "method":        "autocorrelation in 50-1500ms range",
        }
    """
    if len(y) == 0:
        return {"detected": False, "time_ms": None, "confidence": 0.0,
                "method": "empty signal"}

    # On limite a un extrait (15s max) pour acceleration et stabilite
    max_samples = 15 * sr
    if len(y) > max_samples:
        # On prend un segment au milieu (souvent representatif)
        start = (len(y) - max_samples) // 2
        y_seg = y[start:start + max_samples]
    else:
        y_seg = y

    # Normalisation
    y_seg = y_seg - np.mean(y_seg)
    y_seg = y_seg / (np.max(np.abs(y_seg)) + 1e-9)

    # Autocorrelation (utilisation de scipy.signal.correlate, "full" mode)
    n = len(y_seg)
    autocorr = scipy.signal.correlate(y_seg, y_seg, mode="full")
    autocorr = autocorr[n - 1:]  # ne garde que les lags positifs
    autocorr = autocorr / (autocorr[0] + 1e-9)  # normalise par r[0]

    # Plage de recherche en samples
    lag_min = int(_MIN_DELAY_MS * sr / 1000)
    lag_max = int(_MAX_DELAY_MS * sr / 1000)
    lag_max = min(lag_max, len(autocorr) - 1)

    if lag_max <= lag_min:
        return {"detected": False, "time_ms": None, "confidence": 0.0,
                "method": "signal too short"}

    search = autocorr[lag_min:lag_max]

    # Recherche du pic le plus fort
    peaks, props = scipy.signal.find_peaks(search, height=0.1, distance=int(0.02 * sr))
    if len(peaks) == 0:
        return {"detected": False, "time_ms": None, "confidence": 0.0,
                "peak_strength": 0.0,
                "method": "autocorrelation no significant peak"}

    # Pic le plus fort
    peak_heights = props["peak_heights"]
    best_idx = int(np.argmax(peak_heights))
    best_lag = peaks[best_idx] + lag_min
    best_strength = float(peak_heights[best_idx])

    # Conversion en ms
    time_ms = round(best_lag * 1000 / sr, 1)

    # Confidence : on regarde le ratio entre le pic principal et le 2eme pic le plus fort
    if len(peak_heights) >= 2:
        sorted_h = sorted(peak_heights, reverse=True)
        confidence = float((sorted_h[0] - sorted_h[1]) / max(sorted_h[0], 1e-9))
    else:
        confidence = 1.0

    # Seuil de detection : pic significatif (strength > 0.2)
    detected = best_strength > 0.20

    return {
        "detected":      bool(detected),
        "time_ms":       time_ms if detected else None,
        "confidence":    round(confidence, 2),
        "peak_strength": round(best_strength, 3),
        "method":        "autocorrelation peak in 50-1500ms range",
    }
