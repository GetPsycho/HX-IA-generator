"""
key_detection.py
Detection de la tonalite (tonique + mode majeur/mineur) via l'algorithme
de Krumhansl-Schmuckler : chromagram + correlation avec profils empiriques.

Reference : Krumhansl, C. L. (1990). "Cognitive Foundations of Musical Pitch."
Les profils encodent la "hierarchie tonale" percue dans chaque mode.
"""

import numpy as np
import librosa

# Profils Krumhansl-Kessler (empiriques, normalises sur la tonique = C)
# Index = position dans la gamme chromatique (C=0, C#=1, ..., B=11)
_MAJOR_PROFILE = np.array([
    6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
    2.52, 5.19, 2.39, 3.66, 2.29, 2.88,
])
_MINOR_PROFILE = np.array([
    6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
    2.54, 4.75, 3.98, 2.69, 3.34, 3.17,
])

_NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# Equivalents francais pour la fiche morceau
_NOTE_NAMES_FR = ["Do", "Do#", "Re", "Re#", "Mi", "Fa",
                  "Fa#", "Sol", "Sol#", "La", "La#", "Si"]


def detect_key(y: np.ndarray, sr: int,
                low_confidence_threshold: float = 0.10) -> dict:
    """
    Detecte la tonalite (tonique + mode) d'un signal audio.

    Args:
        y : signal audio mono (numpy array)
        sr : sample rate (Hz)
        low_confidence_threshold : si confidence < threshold, le rapport inclut
                                    les top 3 candidats (pas seulement le best)

    Returns:
        {
          "tonic": "A",                    # nom anglais
          "tonic_fr": "La",                # nom francais
          "mode": "minor",                 # "major" | "minor"
          "name": "A minor",               # tonalite complete
          "name_fr": "La mineur",
          "confidence": 0.42,              # ecart relatif entre best et 2nd best
          "score": 0.87,                   # correlation absolue du best
          "alternatives": [...],           # present si confidence faible :
                                            # top-3 candidats avec leurs scores
        }
    """
    # Chromagram CQT : plus stable harmoniquement que STFT pour la detection de cles
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    # Moyenne temporelle : vecteur 12-D des energies par classe de pitch
    chroma_mean = chroma.mean(axis=1)
    # Normalisation (pour correlation pure)
    chroma_mean = chroma_mean / (chroma_mean.sum() + 1e-9)

    # Test des 24 tonalites (12 maj + 12 min) par correlation
    scores = []
    for tonic in range(12):
        major_shifted = np.roll(_MAJOR_PROFILE, tonic)
        minor_shifted = np.roll(_MINOR_PROFILE, tonic)
        major_corr = float(np.corrcoef(chroma_mean, major_shifted)[0, 1])
        minor_corr = float(np.corrcoef(chroma_mean, minor_shifted)[0, 1])
        scores.append(("major", tonic, major_corr))
        scores.append(("minor", tonic, minor_corr))

    # Tri par correlation decroissante
    scores.sort(key=lambda x: -x[2])
    best_mode, best_tonic, best_score = scores[0]
    second_score = scores[1][2]

    # Confidence : ecart relatif entre best et 2nd
    confidence = (best_score - second_score) / max(abs(best_score), 1e-9)

    tonic_en = _NOTE_NAMES[best_tonic]
    tonic_fr = _NOTE_NAMES_FR[best_tonic]
    mode_fr = "mineur" if best_mode == "minor" else "majeur"

    result = {
        "tonic":      tonic_en,
        "tonic_fr":   tonic_fr,
        "mode":       best_mode,
        "name":       f"{tonic_en} {best_mode}",
        "name_fr":    f"{tonic_fr} {mode_fr}",
        "confidence": round(confidence, 3),
        "score":      round(best_score, 3),
    }

    # Si confidence faible -> top 3 candidats (utile car maj/min relatifs partagent les notes,
    # l'algo peut hesiter entre G major et E minor par ex.)
    if confidence < low_confidence_threshold:
        alternatives = []
        for mode_alt, tonic_alt, score_alt in scores[:3]:
            t_en = _NOTE_NAMES[tonic_alt]
            t_fr = _NOTE_NAMES_FR[tonic_alt]
            m_fr = "mineur" if mode_alt == "minor" else "majeur"
            alternatives.append({
                "name":    f"{t_en} {mode_alt}",
                "name_fr": f"{t_fr} {m_fr}",
                "score":   round(float(score_alt), 3),
            })
        result["alternatives"] = alternatives
        result["note"] = ("confidence faible : les modes majeur et mineur relatifs "
                          "partagent les memes notes — verifier avec UG ou audition.")

    return result
