"""
generate_setlist.py
Genere le fichier .hls importable dans HX Edit (setlist complete).

USAGE : python setlists/generate_setlist.py

Les morceaux sont definis dans presets/songs.py.
Modifier SETLIST ci-dessous pour choisir quels presets
vont dans quels slots (0-127).
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "presets"))

from hls_codec import decode_hls, encode_hls
from preset_builder import get_catalog
from songs import PRESETS


SOURCE_FILE = str(_ROOT / "data" / "HX Effects.hls")
OUTPUT_FILE = str(_ROOT / "output" / "setlist_output.hls")

META = {
    "application":    "HX Edit",
    "appversion":     58851328,
    "build_sha":      "d972399",
    "device":         2162693,
    "device_version": 58720256,
    "modifieddate":   1778328154,
    "name":           "HX Effects",
}

# ─────────────────────────────────────────────────────────
# SETLIST — slot (0-127) -> nom du preset dans PRESETS
# ─────────────────────────────────────────────────────────

SETLIST = {
    0: "AYGGMW",
}


def main():
    print("=" * 55)
    print("  HX Effects Setlist Generator")
    print("=" * 55)

    cat = get_catalog()
    print(f"\n{len(cat)} modeles disponibles")

    print(f"\nChargement : {SOURCE_FILE}")
    inner = decode_hls(SOURCE_FILE)

    print(f"\nGeneration de {len(SETLIST)} preset(s)...")
    for slot, preset_name in SETLIST.items():
        builder_fn = PRESETS[preset_name]
        pb = builder_fn()
        print(pb.summary())
        inner["presets"][slot] = pb.build()
        print(f"  -> Injecte au slot [{slot:03d}]")

    print(f"\nEcriture vers : {OUTPUT_FILE}")
    encode_hls(inner, META, OUTPUT_FILE)

    print("\nTermine. Importer setlist_output.hls dans HX Edit.")


if __name__ == "__main__":
    main()
