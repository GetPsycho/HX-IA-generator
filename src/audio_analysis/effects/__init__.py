"""
effects
Detecteurs d'effets sur signal guitare isole (post-Demucs htdemucs_6s).

Lot 1 (v3.2.0) :
- eq : repartition energetique par bandes (basses/mids/aigus)
- compression : crest factor + dynamic range
- saturation : score 0-1 via spectral features
- delay : autocorrelation temporelle

Lot 2 (v3.2.1, a venir) :
- modulation : detection chorus/flanger via oscillations pitch/spectre
- reverb : RT60 sur queues de notes
"""

from .eq import detect_eq
from .compression import detect_compression
from .saturation import detect_saturation
from .delay import detect_delay
from .section_effects import analyze_effects_per_section


def analyze_effects(y, sr: int) -> dict:
    """
    Analyse complete des effets sur un signal guitare isole.

    Args:
        y  : signal audio (numpy array, mono ou stereo (2, samples))
        sr : sample rate

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
    }


__all__ = ["analyze_effects", "analyze_effects_per_section",
           "detect_eq", "detect_compression",
           "detect_saturation", "detect_delay"]
