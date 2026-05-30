"""
section_effects.py
Analyse des effets par section du morceau.

Pour chaque section detectee (intro/verse/chorus/...), on calcule les effets
(saturation, compression, EQ) sur le slice correspondant du stem guitare.

Resout le probleme de la moyenne globale qui lisse les variations
de saturation entre sections (clean verse vs chorus distordu).
"""

import numpy as np

from .saturation import detect_saturation
from .compression import detect_compression
from .eq import detect_eq


# Duree minimum d'une section pour analyser ses effets (en secondes)
# Trop court = stats non significatives
_MIN_SECTION_DURATION = 5.0


def _compute_rms(y: np.ndarray) -> float:
    """RMS energie d'un signal."""
    if len(y) == 0:
        return 0.0
    return float(np.sqrt(np.mean(y ** 2)))


def _intensity_label(rms_ratio: float) -> str:
    """Classification de l'intensite musicale relative."""
    if rms_ratio < 0.35:
        return "very_quiet"
    elif rms_ratio < 0.55:
        return "quiet"
    elif rms_ratio < 0.80:
        return "moderate"
    elif rms_ratio < 0.95:
        return "loud"
    else:
        return "peak"


def analyze_effects_per_section(y_guitar: np.ndarray, sr: int,
                                 sections: list,
                                 y_mix_fallback: np.ndarray = None,
                                 sr_mix: int = None,
                                 silent_threshold: float = 0.10) -> list:
    """
    Calcule les effets pour chaque section du morceau.

    Args:
        y_guitar         : signal guitare mono (stem isole de preference)
        sr               : sample rate du stem guitare
        sections         : liste des sections detectees [{"start", "end", ...}, ...]
        y_mix_fallback   : signal du mix complet (mono), utilise en fallback
                           pour les sections ou Demucs n'a quasi rien extrait
                           (cas typique : parties tres clean noyees dans le mix)
        sr_mix           : sample rate du mix (peut differer du stem)
        silent_threshold : ratio RMS section/song en-dessous duquel on bascule
                           sur le mix (defaut 0.10 = 10% du max)

    Returns:
        Liste de dicts par section avec "effects_source" indiquant la source utilisee
        ("guitar_stem" ou "full_mix_fallback").
    """
    if not sections or len(y_guitar) == 0:
        return []

    # Premiere passe : extraire les RMS de chaque section pour determiner le max
    # (utile pour calculer un ratio normalise par section)
    section_rms = []
    for sec in sections:
        start_s = sec.get("start", 0.0)
        end_s = sec.get("end", 0.0)
        start_sample = int(start_s * sr)
        end_sample = min(int(end_s * sr), len(y_guitar))
        slice_y = y_guitar[start_sample:end_sample]
        section_rms.append(_compute_rms(slice_y))
    max_rms = max(section_rms) if section_rms else 1e-9

    results = []
    for sec, rms in zip(sections, section_rms):
        start_s = sec.get("start", 0.0)
        end_s = sec.get("end", 0.0)
        duration_s = end_s - start_s
        rms_ratio = rms / max_rms if max_rms > 0 else 0.0

        # Skip les sections trop courtes (stats non significatives)
        if duration_s < _MIN_SECTION_DURATION:
            results.append({
                "label":      sec.get("label", "?"),
                "cluster":    sec.get("cluster", "?"),
                "start":      round(start_s, 2),
                "end":        round(end_s, 2),
                "duration_s": round(duration_s, 2),
                "rms":        round(rms, 4),
                "rms_ratio":  round(rms_ratio, 3),
                "intensity":  _intensity_label(rms_ratio),
                "effects":    None,
                "skip_reason": f"section too short (<{_MIN_SECTION_DURATION}s)",
            })
            continue

        # Extraction du slice audio
        start_sample = int(start_s * sr)
        end_sample = int(end_s * sr)
        end_sample = min(end_sample, len(y_guitar))
        slice_y = y_guitar[start_sample:end_sample]

        if len(slice_y) < int(sr * 1):  # moins de 1s d'audio utilisable
            results.append({
                "label":      sec.get("label", "?"),
                "cluster":    sec.get("cluster", "?"),
                "start":      round(start_s, 2),
                "end":        round(end_s, 2),
                "duration_s": round(duration_s, 2),
                "effects":    None,
                "skip_reason": "audio slice too short after extraction",
            })
            continue

        # Analyse des effets sur le slice
        # NB : on adapte analysis_window_s a la duree du slice (max 30s)
        analysis_win = min(duration_s, 30.0)

        # Fallback : si le stem guitare est tres bas sur cette section
        # (Demucs n'a pas su extraire), on bascule sur le mix complet
        used_fallback = False
        if (rms_ratio < silent_threshold and y_mix_fallback is not None
                and sr_mix is not None):
            mix_start = int(start_s * sr_mix)
            mix_end = min(int(end_s * sr_mix), len(y_mix_fallback))
            mix_slice = y_mix_fallback[mix_start:mix_end]
            if len(mix_slice) >= int(sr_mix * 1):
                slice_y = mix_slice
                sr_used = sr_mix
                used_fallback = True
            else:
                sr_used = sr
        else:
            sr_used = sr

        results.append({
            "label":          sec.get("label", "?"),
            "cluster":        sec.get("cluster", "?"),
            "start":          round(start_s, 2),
            "end":            round(end_s, 2),
            "duration_s":     round(duration_s, 2),
            "rms":            round(rms, 4),
            "rms_ratio":      round(rms_ratio, 3),
            "intensity":      _intensity_label(rms_ratio),
            "effects_source": "full_mix_fallback" if used_fallback else "guitar_stem",
            "effects": {
                "saturation":  detect_saturation(slice_y, sr_used,
                                                  analysis_window_s=analysis_win),
                "compression": detect_compression(slice_y, sr_used),
                "eq":          detect_eq(slice_y, sr_used),
            },
        })

    return results
