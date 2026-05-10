"""
generate_presets.py
Genere les fichiers .hlx importables dans HX Edit (presets individuels).

USAGE : python presets/generate_presets.py
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from hlx_codec import encode_hlx
from songs import PRESETS

OUTPUT_DIR = _ROOT / "output"


def main():
    print("=" * 55)
    print("  HX Effects Preset Generator")
    print("=" * 55)

    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"\nGeneration de {len(PRESETS)} preset(s)...")
    for filename, builder_fn in PRESETS.items():
        pb = builder_fn()
        print(pb.summary())
        preset = pb.build()
        encode_hlx(preset, str(OUTPUT_DIR / f"{filename}.hlx"))

    print("\nTermine. Importer les .hlx dans HX Edit.")


if __name__ == "__main__":
    main()
