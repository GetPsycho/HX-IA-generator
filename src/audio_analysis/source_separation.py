"""
source_separation.py
Wrapper Demucs pour isoler la piste guitare d'un mix complet.

Utilise htdemucs_6s (modele 6-stems) qui separe :
  drums, bass, vocals, other, guitar, piano

Cache : la sortie est sauvegardee dans audio_analysis/cache/<filename>_<stem>.wav
       pour eviter de relancer la separation (lourde) a chaque analyse.
"""

from pathlib import Path
import numpy as np
import torch
import librosa
import soundfile


_MODEL_NAME = "htdemucs_6s"
_CACHE_DIR_DEFAULT = Path("audio_analysis") / "cache"

# Cache du modele charge (singleton, evite de recharger a chaque appel)
_MODEL_CACHE = {"model": None, "name": None}


def _get_model():
    """Charge le modele Demucs (singleton)."""
    if _MODEL_CACHE["model"] is None or _MODEL_CACHE["name"] != _MODEL_NAME:
        from demucs.pretrained import get_model
        print(f"  [demucs] Chargement du modele '{_MODEL_NAME}' (premiere fois "
              f"= telechargement ~1.5 GB)...")
        model = get_model(_MODEL_NAME)
        model.eval()
        _MODEL_CACHE["model"] = model
        _MODEL_CACHE["name"] = _MODEL_NAME
    return _MODEL_CACHE["model"]


def separate_guitar(audio_path: str,
                    cache_dir: Path = None,
                    force: bool = False) -> tuple:
    """
    Isole le stem 'guitar' d'un fichier audio via Demucs htdemucs_6s.

    Args:
        audio_path : chemin du fichier audio (mp3/wav/flac/...)
        cache_dir  : dossier de cache (defaut : audio_analysis/cache/)
        force      : True = re-separe meme si cache existe

    Returns:
        (guitar_audio, sample_rate)
            guitar_audio : numpy array stereo (shape [2, samples])
            sample_rate  : int (typiquement 44100)
    """
    audio_path_obj = Path(audio_path)
    if cache_dir is None:
        cache_dir = _CACHE_DIR_DEFAULT
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)

    cache_file = cache_dir / f"{audio_path_obj.stem}_guitar.wav"

    # Si cache existe et pas de force -> charger directement
    if cache_file.exists() and not force:
        print(f"  [demucs] Cache trouve : {cache_file.name}")
        guitar, sr = soundfile.read(str(cache_file), always_2d=True)
        # soundfile renvoie (samples, channels) -> on veut (channels, samples)
        return guitar.T, int(sr)

    # Sinon : charger le modele + le fichier audio + separer
    model = _get_model()

    print(f"  [demucs] Chargement audio : {audio_path_obj.name}")
    # Chargement via librosa (mono=False -> stereo si dispo) au sample rate du modele
    audio_np, sr = librosa.load(str(audio_path_obj), sr=model.samplerate, mono=False)
    # librosa renvoie (channels, samples) en stereo ou (samples,) en mono
    if audio_np.ndim == 1:
        # Duplique mono -> stereo pour demucs
        audio_np = np.stack([audio_np, audio_np], axis=0)
    elif audio_np.shape[0] == 1:
        audio_np = np.repeat(audio_np, 2, axis=0)
    # Conversion en tenseur torch
    audio = torch.from_numpy(audio_np).float()

    # Separation (forme attendue : batch, channels, samples)
    print(f"  [demucs] Separation en cours (peut prendre 1-3 min sur CPU)...")
    from demucs.apply import apply_model
    with torch.no_grad():
        sources = apply_model(
            model,
            audio.unsqueeze(0),
            shifts=1,         # 1 shift = standard, 5 = meilleur mais lent
            split=True,       # decoupe en chunks (memoire)
            overlap=0.25,
            progress=True,
        )
    # Forme : (batch, n_sources, channels, samples)
    sources = sources[0]  # batch dim

    # Index du stem "guitar" dans htdemucs_6s
    source_names = list(model.sources)
    if "guitar" not in source_names:
        raise RuntimeError(
            f"Le modele '{_MODEL_NAME}' n'a pas de stem 'guitar'. "
            f"Stems disponibles : {source_names}"
        )
    guitar_idx = source_names.index("guitar")
    guitar = sources[guitar_idx]  # (channels, samples)

    # Sauvegarde dans le cache (via soundfile : evite la dep torchcodec)
    guitar_np = guitar.cpu().numpy()
    # soundfile attend (samples, channels)
    soundfile.write(str(cache_file), guitar_np.T, sr)
    print(f"  [demucs] Cache sauve : {cache_file.name}")

    return guitar_np, int(sr)


def get_cache_path(audio_path: str, stem: str = "guitar",
                    cache_dir: Path = None) -> Path:
    """Retourne le chemin du fichier cache pour un stem donne."""
    if cache_dir is None:
        cache_dir = _CACHE_DIR_DEFAULT
    return Path(cache_dir) / f"{Path(audio_path).stem}_{stem}.wav"
