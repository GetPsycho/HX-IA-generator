"""
file_matcher.py
Recherche fuzzy d'un fichier audio dans audio_analysis/sources/
matchant un titre de morceau donne.

Strategie de normalisation :
- Lowercase
- Suppression accents (NFD)
- Suppression numerotation prefixe (01, 02 -, 03., 01_, etc.)
- Suppression apostrophes/punctuation
- Decoupe en tokens

Matching : si tous les tokens du titre cherche sont dans le nom du fichier,
c'est un match. Le best match minimise les tokens superflus dans le filename.
"""

import unicodedata
import re
from pathlib import Path


_AUDIO_EXTENSIONS = {".flac", ".mp3", ".wav", ".ogg", ".m4a", ".aac"}


def _normalize(s: str) -> list:
    """Normalise une chaine en liste de tokens (lowercase, sans accents, sans ponctuation)."""
    # Lowercase
    s = s.lower()
    # Suppression accents
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn")
    # Suppression numerotation prefixe : "01 -", "01.", "01_", "track 02"
    s = re.sub(r"^\s*(?:track\s*)?\d{1,3}\s*[.\-_]?\s*", "", s)
    # Remplace tout ce qui n'est pas alphanumerique par espace
    s = re.sub(r"[^a-z0-9]+", " ", s)
    # Tokens (mots)
    tokens = [t for t in s.split() if t]
    return tokens


def find_audio_file(song_title: str,
                    sources_dir: Path = None) -> Path:
    """
    Cherche un fichier audio dans sources_dir matchant song_title.

    Args:
        song_title : ex "Hysteria", "Are You Gonna Go My Way", "Killing in the Name"
        sources_dir : defaut audio_analysis/sources/

    Returns:
        Path du meilleur fichier match, ou None si aucun.
    """
    if sources_dir is None:
        sources_dir = Path("audio_analysis") / "sources"
    sources_dir = Path(sources_dir)
    if not sources_dir.exists():
        return None

    target_tokens = set(_normalize(song_title))
    if not target_tokens:
        return None

    candidates = []
    for f in sources_dir.iterdir():
        if not f.is_file() or f.suffix.lower() not in _AUDIO_EXTENSIONS:
            continue
        file_tokens = set(_normalize(f.stem))
        # Tous les tokens du titre doivent apparaitre dans le filename
        if target_tokens.issubset(file_tokens):
            # Score : nombre de tokens superflus dans le filename (moins = mieux)
            extras = len(file_tokens - target_tokens)
            candidates.append((extras, f))

    if not candidates:
        return None
    # Best match = moins de tokens superflus
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]


def find_analysis_report(song_title: str,
                          reports_dir: Path = None) -> Path:
    """
    Cherche un rapport JSON existant pour un morceau.

    Args:
        song_title : ex "Hysteria"
        reports_dir : defaut audio_analysis/

    Returns:
        Path du rapport JSON, ou None.
    """
    if reports_dir is None:
        reports_dir = Path("audio_analysis")
    reports_dir = Path(reports_dir)
    if not reports_dir.exists():
        return None

    target_tokens = set(_normalize(song_title))
    if not target_tokens:
        return None

    candidates = []
    for f in reports_dir.glob("*_analysis.json"):
        # Retirer le suffixe "_analysis" pour la comparaison
        stem = f.stem
        if stem.endswith("_analysis"):
            stem = stem[: -len("_analysis")]
        file_tokens = set(_normalize(stem))
        if target_tokens.issubset(file_tokens):
            extras = len(file_tokens - target_tokens)
            candidates.append((extras, f))

    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]
