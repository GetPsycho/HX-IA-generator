"""
generate_setlist.py (v2)
Génère le fichier .hls importable dans HX Edit.

USAGE : python generate_setlist.py
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from hls_codec import decode_hls, encode_hls
from preset_builder import PresetBuilder, get_catalog


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
# DÉFINITION DES MORCEAUX
# Chaque fonction retourne un PresetBuilder configuré.
# Voir REFERENCE.md pour la liste complète des modèles & params.
# ─────────────────────────────────────────────────────────

def preset_smells_like_teen_spirit():
    """Nirvana – Smells Like Teen Spirit (116 BPM)"""
    pb = PresetBuilder("Smells LT Spirit", tempo=116.0)

    pb.add_block("HD2_GateNoiseGate",     slot=0)
    pb.add_block("HD2_DistVerminDist",    slot=1)   # ProCo Rat
    pb.add_block("HD2_Chorus",            slot=2)   # Small Clone-style
    pb.add_block("HD2_DelaySimpleDelay",  slot=3)
    pb.add_block("HD2_ReverbTile",        slot=4)

    pb.add_snapshot(0, "Intro Clean", blocks_on=[0, 4],
                    color="green")

    pb.add_snapshot(1, "Couplet",     blocks_on=[0, 1, 2, 4],
                    params={1: {"Gain": 0.55}},
                    color="yellow")

    pb.add_snapshot(2, "Refrain",     blocks_on=[0, 1, 4],
                    params={1: {"Gain": 0.75}},
                    color="orange")

    pb.add_snapshot(3, "Solo",        blocks_on=[0, 1, 3, 4],
                    params={1: {"Gain": 0.80}, 3: {"Mix": 0.20}},
                    color="red")

    return pb


# ─────────────────────────────────────────────────────────
# SETLIST — index → fonction
# ─────────────────────────────────────────────────────────

SETLIST = {
    0: preset_smells_like_teen_spirit,
}


def main():
    print("=" * 55)
    print("  HX Effects Setlist Generator v2")
    print("=" * 55)

    cat = get_catalog()
    print(f"\n{len(cat)} modeles disponibles")

    print(f"\nChargement : {SOURCE_FILE}")
    inner = decode_hls(SOURCE_FILE)

    print(f"\nGeneration de {len(SETLIST)} preset(s)...")
    for idx, builder_fn in SETLIST.items():
        pb = builder_fn()
        print(pb.summary())
        inner["presets"][idx] = pb.build()
        print(f"  -> Injecte au slot [{idx:03d}]")

    print(f"\nEcriture vers : {OUTPUT_FILE}")
    encode_hls(inner, META, OUTPUT_FILE)

    print("\nTermine. Importer setlist_output.hls dans HX Edit.")


if __name__ == "__main__":
    main()
