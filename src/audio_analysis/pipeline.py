"""
pipeline.py
Orchestrateur du pipeline d'analyse audio.

Charge le fichier audio, isole la guitare (Demucs si dispo), lance les
detecteurs (key, tempo, sections, effets) et compile le rapport JSON final.
"""

from pathlib import Path
import numpy as np
import librosa

from .key_detection import detect_key
from .tempo_detection import detect_tempo
from .section_detection import detect_sections

# Version du pipeline (incrementer a chaque ajout d'une nouvelle etape)
PIPELINE_VERSION = "3.2.0"


def analyze_file(audio_path: str, sr: int = 22050,
                 use_demucs: bool = True) -> dict:
    """
    Analyse complete d'un fichier audio.

    Args:
        audio_path : chemin vers le fichier audio (mp3/wav/flac/ogg/...)
        sr         : sample rate pour key/tempo/sections (22050 = standard)
        use_demucs : True = separe la guitare via Demucs avant l'analyse effets
                     False = analyse effets sur le mix complet (degrade)

    Returns:
        dict structure avec les resultats des detecteurs disponibles.
    """
    audio_path = str(audio_path)
    path_obj = Path(audio_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"Fichier audio introuvable : {audio_path}")

    # ----- Phase 1 : analyse globale sur mix (key, tempo, sections) -----
    # Chargement audio mono basse-resolution pour analyse rapide
    y, sr_loaded = librosa.load(audio_path, sr=sr, mono=True)
    duration_s = float(len(y)) / sr_loaded

    key_info = detect_key(y, sr_loaded)
    tempo_info = detect_tempo(y, sr_loaded)
    sections_info = detect_sections(y, sr_loaded)

    result = {
        "pipeline_version": PIPELINE_VERSION,
        "file":             audio_path,
        "filename":         path_obj.name,
        "duration_s":       round(duration_s, 2),
        "sample_rate":      sr_loaded,
        "key":              key_info,
        "tempo":            tempo_info,
        "sections":         sections_info,
    }

    # ----- Phase 2 : analyse des effets sur guitare isolee -----
    if use_demucs:
        try:
            from .source_separation import separate_guitar
            from .effects import analyze_effects

            guitar_audio, guitar_sr = separate_guitar(audio_path)
            print(f"  [effects] Analyse des effets sur stem guitare isole...")
            effects_info = analyze_effects(guitar_audio, guitar_sr)
            result["effects"] = effects_info
            result["effects_source"] = "demucs htdemucs_6s guitar stem"
        except Exception as e:
            print(f"  [effects] WARNING : separation/analyse echouee ({e})")
            print(f"  [effects] Fallback : analyse sur le mix complet")
            try:
                from .effects import analyze_effects
                effects_info = analyze_effects(y, sr_loaded)
                result["effects"] = effects_info
                result["effects_source"] = "full mix (degraded)"
                result["effects_warning"] = str(e)
            except Exception as e2:
                result["effects_warning"] = f"Toutes analyses effets echouees: {e2}"
    else:
        from .effects import analyze_effects
        effects_info = analyze_effects(y, sr_loaded)
        result["effects"] = effects_info
        result["effects_source"] = "full mix (use_demucs=False)"

    return result
