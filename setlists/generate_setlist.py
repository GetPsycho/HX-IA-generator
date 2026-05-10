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
    pb.add_block("HD2_ReverbGanymede",    slot=4)

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


def preset_are_you_gonna_go_my_way():
    """Lenny Kravitz - Are You Gonna Go My Way (130 BPM)

    Chaine : Gate > OD > Flanger > EQ > Delay > Reverb
    Slots  :  0      1     2        3    4        5
    """
    pb = PresetBuilder("AYGGMW", tempo=130.0)

    # [0] Gate serre pour les riffs secs
    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -60.0, "Decay": 0.3})

    # [1] Distorsion principale : Marshall pousse, mid-forward
    pb.add_block("HD2_DistStuporOD", slot=1,
                 overrides={"Drive": 0.72, "Tone": 0.55, "Level": 0.72})

    # [2] Flanger : bridge uniquement — sweep lent, moderement profond
    pb.add_block("HD2_FlangerGrayFlanger", slot=2,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.40})

    # [3] EQ : flat par defaut, shape via snapshots (bridge + solo)
    pb.add_block("HD2_EQSimple3Band", slot=3)

    # [4] Slapback delay : solo uniquement (120ms, pas de repeat)
    pb.add_block("HD2_DelaySimpleDelay", slot=4,
                 overrides={"Time": 0.12, "Feedback": 0.0, "Mix": 0.22,
                            "TempoSync1": False})

    # [5] Reverbe de salle subtile : toujours presente
    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.18})

    # Snap 0 — Riff : son principal, intro/couplet/refrain/outro
    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 5],
                    color="yellow")

    # Snap 1 — Bridge : flanger + EQ chaud
    pb.add_snapshot(1, "Bridge", blocks_on=[0, 1, 2, 3, 5],
                    params={
                        1: {"Drive": 0.60, "Level": 0.68},
                        3: {"MidFreq": 800.0, "MidGain": -2.0, "HighGain": -3.0},
                    },
                    color="blue")

    # Snap 2 — Solo : boost sustain + EQ lead + slapback
    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 3, 4, 5],
                    params={
                        1: {"Drive": 0.80, "Level": 0.82},
                        3: {"MidFreq": 1000.0, "MidGain": 4.0, "HighGain": 2.0},
                    },
                    color="red")

    # Snap 3 — Clean : accordage / attente entre les morceaux
    pb.add_snapshot(3, "Clean", blocks_on=[0, 5],
                    color="green")

    return pb


# ─────────────────────────────────────────────────────────
# SETLIST — index → fonction
# ─────────────────────────────────────────────────────────

SETLIST = {
    0: preset_smells_like_teen_spirit,
    1: preset_are_you_gonna_go_my_way,
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
