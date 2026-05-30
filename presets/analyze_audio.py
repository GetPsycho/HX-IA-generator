"""
analyze_audio.py
Lance le pipeline d'analyse audio sur un fichier et sauvegarde le rapport
dans audio_analysis/<nom>_analysis.json.

USAGE :
  python presets/analyze_audio.py <chemin_audio>
  python presets/analyze_audio.py "songs/Hysteria.mp3"

Le rapport JSON peut ensuite etre lu par le skill /new-preset pour enrichir
l'analyse (tonalite, BPM, sections, effets selon la version du pipeline).
"""

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from audio_analysis import analyze_file

ANALYSIS_DIR = _ROOT / "audio_analysis"


def _fmt_time(seconds: float) -> str:
    """Format mm:ss"""
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    audio_path = sys.argv[1]
    print(f"Analyse en cours : {audio_path}")
    print("(librosa charge le fichier, calcul chromagram + tempo — ~10-30s selon duree)")

    try:
        result = analyze_file(audio_path)
    except FileNotFoundError as e:
        print(f"ERREUR : {e}")
        sys.exit(1)

    # Affichage console resume
    print()
    print("=" * 65)
    print(f"  Rapport d'analyse audio  (pipeline v{result['pipeline_version']})")
    print("=" * 65)
    print(f"  Fichier  : {result['filename']}")
    print(f"  Duree    : {result['duration_s']:.1f}s")
    print(f"  Tonalite : {result['key']['name_fr']:<15} "
          f"(confiance {result['key']['confidence']:.2f}, "
          f"score {result['key']['score']:.2f})")
    print(f"  Tempo    : {result['tempo']['bpm']:.1f} BPM   "
          f"(arrondi : {result['tempo']['bpm_int']})")
    print(f"  Beats    : {result['tempo']['n_beats']}")
    if "sections" in result and result["sections"]:
        print()
        print(f"  Sections detectees ({len(result['sections'])}) :")
        for i, s in enumerate(result["sections"]):
            start = _fmt_time(s["start"])
            end = _fmt_time(s["end"])
            dur = s["duration_s"]
            print(f"    [{i}] {start} -> {end} ({dur:>5.1f}s) "
                  f"cluster={s['cluster']}  label={s['label']}")
    print("=" * 65)

    # Sauvegarde JSON
    ANALYSIS_DIR.mkdir(exist_ok=True)
    out_name = Path(audio_path).stem + "_analysis.json"
    out_path = ANALYSIS_DIR / out_name
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"\nRapport sauve : {out_path.relative_to(_ROOT)}")


if __name__ == "__main__":
    main()
