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
          "bpm":      132.5,    # tempo principal estime
          "bpm_int":  132,      # arrondi (utile pour PRESETS)
          "n_beats":  287,      # nombre de battements detectes sur le morceau
        }
    """
    tempo_arr, beats = librosa.beat.beat_track(y=y, sr=sr)
    # librosa renvoie un array (parfois 0-D parfois 1-D selon version)
    tempo_val = float(tempo_arr) if np.isscalar(tempo_arr) or tempo_arr.ndim == 0 else float(tempo_arr[0])

    return {
        "bpm":     round(tempo_val, 1),
        "bpm_int": int(round(tempo_val)),
        "n_beats": int(len(beats)),
    }
