"""
reverb.py
Estimation du temps de reverberation (RT60) et du niveau wet.

Principe (methode Schroeder simplifiee adaptee a un mix musical) :
1. Detecter les onsets (attaques de notes)
2. Pour chaque onset, isoler la "decroissance" qui suit (~2s apres l'attaque)
3. Sur l'enveloppe energetique log, fit une regression lineaire
4. RT60 = temps pour decroitre de 60 dB (extrapolation de la pente)
5. Mediane sur plusieurs onsets pour robustesse

Limites :
- Sur signal continu (riffs sans silence), les decroissances se superposent
- Plus precis sur des morceaux avec notes espacees ou queues isolees
- Sur stem guitare isole, c'est mieux que sur mix complet
"""

import numpy as np
import librosa
import scipy.stats


_ONSET_MIN_GAP_S = 0.5       # ecart min entre onsets analysables
_DECAY_WINDOW_S = 1.5        # duree apres onset analysee pour la decroissance
_MIN_DECAY_DB = 6            # decroissance min mesurable pour fit fiable
_MAX_DECAY_DB = 25           # decroissance max consideree pour la regression


def detect_reverb(y: np.ndarray, sr: int,
                   analysis_window_s: float = 30.0) -> dict:
    """
    Estime le RT60 et le niveau wet d'une reverb dans le signal.

    Returns:
        {
          "detected":      True | False,
          "rt60_s":        1.8,           # temps reverb estime (None si non detecte)
          "wet_estimate_0_1": 0.25,       # niveau wet estime (rough)
          "n_decays_analyzed": 12,
          "confidence":    0.45,
          "method":        "...",
        }
    """
    if len(y) == 0:
        return {"detected": False, "rt60_s": None, "wet_estimate_0_1": 0.0,
                "n_decays_analyzed": 0, "confidence": 0.0,
                "method": "empty signal"}

    # Fenetre d'analyse centrale
    win_samples = int(analysis_window_s * sr)
    if len(y) > win_samples:
        mid = len(y) // 2
        seg = y[max(0, mid - win_samples // 2): mid + win_samples // 2]
    else:
        seg = y

    # Detection des onsets
    hop = 512
    onset_frames = librosa.onset.onset_detect(
        y=seg, sr=sr, hop_length=hop, units="frames")
    onset_times = librosa.frames_to_time(onset_frames, sr=sr, hop_length=hop)

    if len(onset_times) < 3:
        return {"detected": False, "rt60_s": None, "wet_estimate_0_1": 0.0,
                "n_decays_analyzed": 0, "confidence": 0.0,
                "method": "not enough onsets detected"}

    # Filtrer les onsets trop proches (decroissances superposees inanalysables)
    valid_onsets = [onset_times[0]]
    for t in onset_times[1:]:
        # Garde si suffisamment isole du suivant aussi
        if t - valid_onsets[-1] >= _ONSET_MIN_GAP_S:
            valid_onsets.append(t)

    # Pour chaque onset valide, calculer la decroissance
    rt60_estimates = []
    for i, t_onset in enumerate(valid_onsets):
        # Fin de la fenetre de decroissance : min entre onset+decay_window et next_onset
        t_end = t_onset + _DECAY_WINDOW_S
        if i + 1 < len(valid_onsets):
            t_end = min(t_end, valid_onsets[i + 1])
        # Skip si la fenetre est trop courte
        if t_end - t_onset < 0.3:
            continue
        s_start = int(t_onset * sr)
        s_end = min(int(t_end * sr), len(seg))
        slice_y = seg[s_start:s_end]
        if len(slice_y) < int(0.3 * sr):
            continue

        rt60 = _estimate_rt60_from_decay(slice_y, sr)
        if rt60 is not None and 0.05 <= rt60 <= 15.0:
            rt60_estimates.append(rt60)

    if not rt60_estimates:
        return {"detected": False, "rt60_s": None, "wet_estimate_0_1": 0.0,
                "n_decays_analyzed": 0, "confidence": 0.0,
                "method": "no usable decay segments"}

    # Mediane robuste
    rt60_median = float(np.median(rt60_estimates))
    # Confidence : nombre d'onsets analyses et dispersion
    if len(rt60_estimates) >= 5:
        # Plus la dispersion est faible, plus la confidence est haute
        std = float(np.std(rt60_estimates))
        # Coefficient de variation : std / mediane. Faible = bonne stabilite.
        cv = std / max(rt60_median, 1e-9)
        # Confidence base sur CV : cv=0 -> 1.0, cv=1+ -> 0
        confidence = max(0.0, min(1.0 - cv, 1.0))
        # Modulation par nombre d'onsets (au moins 5 = facteur 0.5, 10+ = facteur 1.0)
        confidence *= min(len(rt60_estimates) / 10.0, 1.0)
    else:
        confidence = 0.0  # trop peu d'onsets pour avoir confiance

    # Estimation grossiere du wet : plus de variations RMS apres l'attaque = plus de wet
    # On utilise le ratio energie "tail" (200ms-800ms apres peak) / energie "head" (0-200ms)
    wet_estimates = []
    for t_onset in valid_onsets:
        s_start = int(t_onset * sr)
        s_head_end = min(s_start + int(0.2 * sr), len(seg))
        s_tail_end = min(s_start + int(0.8 * sr), len(seg))
        if s_tail_end - s_head_end < int(0.1 * sr):
            continue
        head_rms = float(np.sqrt(np.mean(seg[s_start:s_head_end] ** 2)))
        tail_rms = float(np.sqrt(np.mean(seg[s_head_end:s_tail_end] ** 2)))
        if head_rms > 1e-6:
            wet_estimates.append(min(tail_rms / head_rms, 1.0))
    wet_median = float(np.median(wet_estimates)) if wet_estimates else 0.0

    # Detection : reverb consideree presente si :
    # - RT60 >= 0.3s (sinon c'est juste l'enveloppe naturelle)
    # - confidence >= 0.35 (assez d'onsets coherents)
    # - n_decays_analyzed >= 5
    detected = (rt60_median >= 0.3
                and confidence >= 0.35
                and len(rt60_estimates) >= 5)

    return {
        "detected":          bool(detected),
        "rt60_s":            round(rt60_median, 2) if detected else None,
        "wet_estimate_0_1":  round(wet_median, 2) if detected else None,
        "n_decays_analyzed": len(rt60_estimates),
        "confidence":        round(confidence, 2),
        "method":            "Schroeder-style decay on isolated onsets",
    }


def _estimate_rt60_from_decay(slice_y: np.ndarray, sr: int) -> float:
    """
    Estime le RT60 a partir d'une fenetre post-onset.

    Methode : envelope log -> regression lineaire sur la portion descendante
    -> extrapolation a -60 dB.
    """
    # Envelope RMS sur fenetres de 10ms
    win = int(0.010 * sr)
    if win < 1 or len(slice_y) < 3 * win:
        return None
    n_win = len(slice_y) // win
    env = np.array([
        np.sqrt(np.mean(slice_y[i * win:(i + 1) * win] ** 2))
        for i in range(n_win)
    ])
    if env.max() < 1e-6:
        return None
    # Normalise en dB par rapport au peak
    env_db = 20 * np.log10(env / (env.max() + 1e-9) + 1e-9)
    # Trouve le peak (souvent fenetre 0 ou 1)
    peak_idx = int(np.argmax(env))
    # Decroissance apres le peak
    decay = env_db[peak_idx:]
    if len(decay) < 5:
        return None

    # On garde la portion ou la decroissance est entre -_MIN_DECAY_DB et -_MAX_DECAY_DB
    times_s = np.arange(len(decay)) * win / sr
    mask = (decay <= -_MIN_DECAY_DB) & (decay >= -_MAX_DECAY_DB)
    if mask.sum() < 3:
        return None

    # Regression lineaire : decay_db = a * t + b
    t_fit = times_s[mask]
    d_fit = decay[mask]
    slope, intercept, r_value, _, _ = scipy.stats.linregress(t_fit, d_fit)
    # Fit insuffisant ?
    if abs(r_value) < 0.5 or slope >= 0:
        return None
    # RT60 = (-60 - intercept) / slope - 0 (on part du peak a 0dB)
    # Soit : RT60 = -60 / slope (en supposant intercept ~ 0)
    rt60 = -60.0 / slope
    return float(rt60)
