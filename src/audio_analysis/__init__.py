"""
audio_analysis
Module d'analyse audio pour enrichir la creation des presets HX Effects.

v3.0 - Tonalite, mode (majeur/mineur), tempo (BPM)
v3.1 - Sections (intro/verse/chorus/bridge/outro) avec timestamps
v3.2 - Analyse des effets (saturation, reverb, modulation, delay, EQ)  [a venir]

Usage :
    from audio_analysis import analyze_file
    result = analyze_file("songs/Hysteria.mp3")
    # -> {"file": ..., "duration_s": ..., "key": {...}, "tempo_bpm": ...}
"""

from .pipeline import analyze_file

__all__ = ["analyze_file"]
