"""
eq.py
Detection de la repartition energetique par bandes de frequences.

Bandes :
- low  : <  250 Hz
- low_mid : 250-800 Hz
- mid : 800-2500 Hz
- high_mid : 2500-6000 Hz
- high : > 6000 Hz

Valeurs en dB relatives a une distribution neutre (energie egale dans les 5 bandes).
"""

import numpy as np


_BANDS = [
    ("low",      0,    250),
    ("low_mid",  250,  800),
    ("mid",      800,  2500),
    ("high_mid", 2500, 6000),
    ("high",     6000, 20000),
]


def detect_eq(y: np.ndarray, sr: int) -> dict:
    """
    Calcule la repartition d'energie par bandes.

    Returns:
        {
          "bands_db": {"low": +2.1, "low_mid": -0.5, "mid": +1.2, ...},
          "balance":  "bright" | "balanced" | "warm" | "scooped" | "mid_focused",
          "method":   "FFT energy per band",
        }
    """
    # FFT
    spectrum = np.abs(np.fft.rfft(y * np.hanning(len(y))))
    freqs = np.fft.rfftfreq(len(y), 1.0 / sr)
    energy_total = (spectrum ** 2).sum() + 1e-9

    # Energie par bande
    band_energy = {}
    for name, f_lo, f_hi in _BANDS:
        mask = (freqs >= f_lo) & (freqs < f_hi)
        band_energy[name] = float((spectrum[mask] ** 2).sum())

    # Conversion dB relatif a la distribution uniforme
    n_bands = len(_BANDS)
    uniform_share = energy_total / n_bands
    bands_db = {}
    for name in band_energy:
        ratio = band_energy[name] / uniform_share if uniform_share > 0 else 1.0
        bands_db[name] = round(10 * np.log10(ratio + 1e-9), 1)

    # Heuristique de balance
    # NB : on EXCLUT la bande "high" du calcul car Demucs coupe systematiquement
    # les hautes frequences des stems (artefact de separation). La bande "high"
    # est conservee dans bands_db pour information mais n'entre pas dans la balance.
    low_avg = (bands_db["low"] + bands_db["low_mid"]) / 2.0
    high_avg = bands_db["high_mid"]  # bande high exclue
    mid = bands_db["mid"]
    mid_score = mid - (low_avg + high_avg) / 2.0  # mid vs moyenne bas/haut

    if mid_score > 2.0:
        balance = "mid_focused"   # mids dominent
    elif low_avg > 1.5 and high_avg > 1.5 and mid_score < -1.0:
        balance = "scooped"       # V-shape : bas + aigus, mids creux
    elif low_avg > high_avg + 2.5:
        balance = "warm"          # bas dominent
    elif high_avg > low_avg + 2.5:
        balance = "bright"        # aigus dominent
    else:
        balance = "balanced"

    return {
        "bands_db": bands_db,
        "balance":  balance,
        "method":   "FFT energy per band, dB relative to uniform distribution",
    }
