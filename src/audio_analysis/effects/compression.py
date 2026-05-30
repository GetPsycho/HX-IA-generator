"""
compression.py
Estimation du niveau de compression via crest factor et dynamic range.

Crest factor (peak/RMS, en dB) :
- Signal acoustique non compresse : 12-20 dB
- Pop/rock modere : 8-12 dB
- Heavily compressed : 4-8 dB
- "Loudness war" : < 4 dB

Dynamic Range (EBU R128 inspire, simplifie) :
- Differerce entre les 10% les plus forts et les 10% les plus faibles (en dB).
"""

import numpy as np


def detect_compression(y: np.ndarray, sr: int) -> dict:
    """
    Estime le niveau de compression du signal.

    Returns:
        {
          "crest_factor_db":   8.5,
          "dynamic_range_db":  10.2,
          "level":             "moderate" | "light" | "heavy" | "extreme",
          "method":            "...",
        }
    """
    if len(y) == 0:
        return {"crest_factor_db": 0.0, "dynamic_range_db": 0.0,
                "level": "unknown", "method": "empty signal"}

    # Crest factor : peak / RMS
    peak = float(np.max(np.abs(y)))
    rms = float(np.sqrt(np.mean(y ** 2)))
    crest_db = 20 * np.log10(peak / rms) if rms > 0 else 0.0

    # Dynamic range : sur des fenetres glissantes de 1s
    window_size = sr  # 1 seconde
    if len(y) >= window_size:
        # Loudness par fenetre (RMS)
        n_windows = len(y) // window_size
        if n_windows == 0:
            n_windows = 1
        window_rms = []
        for i in range(n_windows):
            start = i * window_size
            end = start + window_size
            w = y[start:end]
            if len(w) > 0:
                w_rms = float(np.sqrt(np.mean(w ** 2)))
                if w_rms > 1e-6:
                    window_rms.append(20 * np.log10(w_rms))
        if len(window_rms) >= 10:
            window_rms = np.array(window_rms)
            # Top 10% vs bottom 10%
            top_10 = np.percentile(window_rms, 90)
            bot_10 = np.percentile(window_rms, 10)
            dr_db = float(top_10 - bot_10)
        else:
            dr_db = float(np.ptp(window_rms)) if len(window_rms) > 0 else 0.0
    else:
        dr_db = 0.0

    # Classification heuristique
    if crest_db >= 12:
        level = "light"
    elif crest_db >= 8:
        level = "moderate"
    elif crest_db >= 4:
        level = "heavy"
    else:
        level = "extreme"

    return {
        "crest_factor_db":  round(crest_db, 1),
        "dynamic_range_db": round(dr_db, 1),
        "level":            level,
        "method":           "crest_factor (peak/RMS) + DR (1s windows, p90-p10)",
    }
