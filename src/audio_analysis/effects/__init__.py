"""
effects
Detecteurs d'effets sur signal guitare isole (post-Demucs htdemucs_6s).

Lot 1 (v3.2.0) :
- eq : repartition energetique par bandes (basses/mids/aigus)
- compression : crest factor + dynamic range
- saturation : score 0-1 via spectral features
- delay : autocorrelation temporelle

Lot 2 (v3.2.2) :
- modulation : detection chorus/flanger via oscillations pitch/spectre
                (avec masquage des harmoniques du tempo pour eviter faux positifs)
- reverb : RT60 sur queues de notes (Schroeder simplifie)
"""

from .eq import detect_eq
from .compression import detect_compression
from .saturation import detect_saturation
from .delay import detect_delay
from .modulation import detect_modulation
from .reverb import detect_reverb
from .section_effects import analyze_effects_per_section


def analyze_effects(y, sr: int, tempo_bpm: float = None) -> dict:
    """
    Analyse complete des effets sur un signal guitare isole.

    Args:
        y         : signal audio (numpy array, mono ou stereo (2, samples))
        sr        : sample rate
        tempo_bpm : tempo du morceau (optionnel) — passe a detect_modulation
                    pour exclure les harmoniques du tempo de la detection LFO

    Returns:
        dict structure avec un sous-dict par effet detecte.
    """
    # Si stereo, on travaille en mono pour la plupart des analyses
    if y.ndim == 2 and y.shape[0] == 2:
        y_mono = y.mean(axis=0)
    else:
        y_mono = y.flatten() if y.ndim > 1 else y

    return {
        "eq":          detect_eq(y_mono, sr),
        "compression": detect_compression(y_mono, sr),
        "saturation":  detect_saturation(y_mono, sr),
        "delay":       detect_delay(y_mono, sr),
        "modulation":  detect_modulation(y_mono, sr, tempo_bpm=tempo_bpm),
        "reverb":      detect_reverb(y_mono, sr),
    }


__all__ = ["analyze_effects", "analyze_effects_per_section",
           "detect_eq", "detect_compression",
           "detect_saturation", "detect_delay",
           "detect_modulation", "detect_reverb"]
