"""
pipeline.py
Orchestrateur du pipeline d'analyse audio.

Charge le fichier audio, lance les detecteurs activcs (key, tempo, ...)
et compile le rapport JSON final.
"""

from pathlib import Path
import librosa

from .key_detection import detect_key
from .tempo_detection import detect_tempo
from .section_detection import detect_sections

# Version du pipeline (incrementer a chaque ajout d'une nouvelle etape)
PIPELINE_VERSION = "3.1"


def analyze_file(audio_path: str, sr: int = 22050) -> dict:
    """
    Analyse complete d'un fichier audio.

    Args:
        audio_path : chemin vers le fichier audio (mp3/wav/flac/ogg/...)
        sr         : sample rate de chargement (22050 = standard librosa,
                     suffisant pour key/tempo, plus rapide que 44100)

    Returns:
        dict structure avec les resultats des detecteurs disponibles
        dans la version courante du pipeline.
    """
    audio_path = str(audio_path)
    path_obj = Path(audio_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"Fichier audio introuvable : {audio_path}")

    # Chargement audio (mono par defaut)
    y, sr = librosa.load(audio_path, sr=sr, mono=True)
    duration_s = float(len(y)) / sr

    # Detecteurs v3.0
    key_info = detect_key(y, sr)
    tempo_info = detect_tempo(y, sr)

    # Detecteur v3.1
    sections = detect_sections(y, sr)

    return {
        "pipeline_version": PIPELINE_VERSION,
        "file":             audio_path,
        "filename":         path_obj.name,
        "duration_s":       round(duration_s, 2),
        "sample_rate":      sr,
        "key":              key_info,
        "tempo":            tempo_info,
        "sections":         sections,
    }
