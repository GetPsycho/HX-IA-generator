"""
analyze_song.py
Recupere ou genere l'analyse audio d'un morceau a partir de son titre.

Workflow :
1. Cherche un rapport JSON existant dans audio_analysis/ (matching fuzzy)
   -> si trouve, sort le chemin du rapport
2. Sinon, cherche un fichier audio dans audio_analysis/sources/ (matching fuzzy)
   -> si trouve, lance l'analyse, puis sort le chemin du nouveau rapport
3. Sinon, sort "no audio available" (le skill /new-preset continue sans)

USAGE :
  python presets/analyze_song.py "Hysteria"
  python presets/analyze_song.py "Be Yourself"

Sortie console :
  REPORT: <chemin/vers/report.json>     -> si analyse disponible
  NO_AUDIO                              -> sinon

Exit code 0 si rapport produit/trouve, 1 sinon.
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from audio_analysis.file_matcher import find_audio_file, find_analysis_report


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    song_title = sys.argv[1]
    print(f"Recherche d'analyse audio pour : {song_title}")

    # 1. Rapport existant ?
    report = find_analysis_report(song_title, reports_dir=_ROOT / "audio_analysis")
    if report:
        print(f"  Rapport existant trouve : {report.name}")
        print(f"REPORT: {report.resolve()}")
        sys.exit(0)

    # 2. Fichier audio dans sources/ ?
    audio = find_audio_file(song_title, sources_dir=_ROOT / "audio_analysis" / "sources")
    if not audio:
        print(f"  Aucun rapport ni fichier audio trouve pour '{song_title}'.")
        print(f"  Deposer le fichier audio dans audio_analysis/sources/ pour activer "
              f"l'analyse.")
        print(f"NO_AUDIO")
        sys.exit(1)

    # 3. Lancer l'analyse
    print(f"  Fichier audio trouve : {audio.name}")
    print(f"  Lancement de l'analyse...")
    from audio_analysis import analyze_file
    import json

    try:
        result = analyze_file(str(audio))
    except Exception as e:
        print(f"  ERREUR pendant l'analyse : {e}")
        sys.exit(1)

    # Sauvegarde du rapport
    out_dir = _ROOT / "audio_analysis"
    out_dir.mkdir(exist_ok=True)
    out_name = audio.stem + "_analysis.json"
    out_path = out_dir / out_name
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"  Rapport sauve : {out_path.name}")
    print(f"REPORT: {out_path.resolve()}")
    sys.exit(0)


if __name__ == "__main__":
    main()
