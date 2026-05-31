"""
tempo_detection.py
Detection du tempo (BPM) via librosa.beat.beat_track.

L'algorithme combine une onset detection function (ODF) et de la dynamic
programming pour trouver la grille rythmique la plus probable.
"""

import numpy as np
import librosa


def detect_tempo(y: np.ndarray, sr: int) -> dict:
    """
    Detecte le tempo (BPM) d'un signal audio.

    Args:
        y : signal audio mono (numpy array)
        sr : sample rate (Hz)

    Returns:
        {
          "bpm":             132.5,    # tempo principal estime (apres auto-correction)
          "bpm_int":         132,      # arrondi (utile pour PRESETS)
          "bpm_raw":         132.5,    # valeur brute librosa (avant correction extreme)
          "n_beats":         287,      # nombre de battements detectes sur le morceau
          "alternatives":    [86.0, 264.0],  # candidats /2 et *2 (utile car
                                              # librosa confond souvent moitie/double)
          "note":            "...",    # present si auto-correction appliquee
        }

    Auto-correction :
    - Si BPM > 180 -> divise par 2 (peu de morceaux > 180 reels)
    - Si BPM < 60  -> multiplie par 2 (peu de morceaux < 60 reels)
    - Sinon : laisse tel quel mais expose alternatives /2 et *2 pour interpretation
    """
    tempo_arr, beats = librosa.beat.beat_track(y=y, sr=sr)
    tempo_val = float(tempo_arr) if np.isscalar(tempo_arr) or tempo_arr.ndim == 0 else float(tempo_arr[0])
    tempo_raw = tempo_val

    note = None
    if tempo_val > 180:
        tempo_val = tempo_val / 2
        note = f"Auto-correction : tempo brut {tempo_raw:.1f} > 180, divise par 2"
    elif tempo_val < 60 and tempo_val > 0:
        tempo_val = tempo_val * 2
        note = f"Auto-correction : tempo brut {tempo_raw:.1f} < 60, multiplie par 2"

    result = {
        "bpm":          round(tempo_val, 1),
        "bpm_int":      int(round(tempo_val)),
        "bpm_raw":      round(tempo_raw, 1),
        "n_beats":      int(len(beats)),
        "alternatives": [round(tempo_val / 2, 1), round(tempo_val * 2, 1)],
    }
    if note:
        result["note"] = note
    return result
