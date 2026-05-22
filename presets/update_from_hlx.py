"""
update_from_hlx.py
Compare les .hlx modifies sur l'appareil (deposes dans output/modified/)
avec les presets generes par le code Python source.

USAGE :
  python presets/update_from_hlx.py "Hysteria - Muse"
  python presets/update_from_hlx.py --all

Affiche un rapport diff lisible. N'applique aucun changement automatiquement —
les modifications de presets/songs.py doivent etre faites manuellement (ou par Claude).
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from hlx_decoder import decode_preset, decode_built_preset
from preset_diff import diff_presets, format_diff
from songs import PRESETS

MODIFIED_DIR = _ROOT / "output" / "modified"


def _resolve_preset_name(hlx_path) -> str | None:
    """Resout le nom de preset PRESETS depuis un .hlx :
    1. nom de fichier exact
    2. meta.name interne du .hlx (HX Edit utilise le nom court du PresetBuilder)
       -> chercher une cle PRESETS qui commence par '{meta_name} -'
    """
    import json
    stem = hlx_path.stem
    if stem in PRESETS:
        return stem
    try:
        with open(hlx_path, encoding="utf-8") as f:
            meta_name = json.load(f)["data"]["meta"].get("name", "").strip()
    except Exception:
        return None
    if not meta_name:
        return None
    # Cherche "{meta_name} - <artist>"
    for key in PRESETS:
        if key == meta_name or key.startswith(f"{meta_name} -"):
            return key
    return None


def diff_one(preset_name: str, hlx_path=None) -> bool:
    """
    Compare un preset specifique : code Python vs .hlx (chemin auto si non specifie).
    Retourne True si des differences sont detectees, False sinon.
    """
    if preset_name not in PRESETS:
        print(f"ERREUR : preset '{preset_name}' inconnu dans PRESETS.")
        print(f"  Presets disponibles : {sorted(PRESETS.keys())}")
        return False

    if hlx_path is None:
        # Tente 'PRESETS_key.hlx' puis le nom court (PresetBuilder name)
        candidate1 = MODIFIED_DIR / f"{preset_name}.hlx"
        # nom court = partie avant " - "
        short = preset_name.split(" - ")[0] if " - " in preset_name else preset_name
        candidate2 = MODIFIED_DIR / f"{short}.hlx"
        if candidate1.exists():
            hlx_path = candidate1
        elif candidate2.exists():
            hlx_path = candidate2
        else:
            print(f"ERREUR : fichier introuvable. Cherche :")
            print(f"  {candidate1}")
            print(f"  {candidate2}")
            return False

    # Build du preset version code
    pb = PRESETS[preset_name]()
    code_built = pb.build()
    code_preset = decode_built_preset(code_built)

    # Decode du .hlx modifie
    disk_preset = decode_preset(str(hlx_path))

    # Diff
    changes = diff_presets(code_preset, disk_preset)
    report = format_diff(preset_name, changes)
    print(report)
    return len(changes) > 0


def diff_all() -> None:
    """
    Compare tous les presets pour lesquels un .hlx existe dans output/modified/.
    Ignore silencieusement les presets sans fichier dans le dossier.
    """
    if not MODIFIED_DIR.exists():
        print(f"ERREUR : dossier introuvable : {MODIFIED_DIR}")
        print(f"  Creer le dossier et y deposer les .hlx modifies depuis HX Edit.")
        return

    files = sorted(MODIFIED_DIR.glob("*.hlx"))
    if not files:
        print(f"Aucun .hlx dans {MODIFIED_DIR}/")
        return

    print(f"Comparaison de {len(files)} preset(s) modifie(s)...\n")
    total_diffs = 0
    for hlx_path in files:
        preset_name = _resolve_preset_name(hlx_path)
        if preset_name is None:
            print(f"=== {hlx_path.name} ===")
            print(f"  IGNORE : impossible de trouver le preset correspondant\n")
            continue
        if diff_one(preset_name, hlx_path=hlx_path):
            total_diffs += 1

    print(f"\nTermine. {total_diffs}/{len(files)} preset(s) avec differences.")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]
    if arg == "--all":
        diff_all()
    else:
        diff_one(arg)


if __name__ == "__main__":
    main()
