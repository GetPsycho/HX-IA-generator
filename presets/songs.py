"""
songs.py
Definitions des presets (morceaux).
Importe par generate_presets.py (-> .hlx) et generate_setlist.py (-> .hls).

Ajouter un morceau :
  1. Ecrire une fonction preset_mon_morceau() qui retourne un PresetBuilder
  2. L'ajouter dans PRESETS avec le nom de fichier souhaite
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from preset_builder import PresetBuilder


# ─────────────────────────────────────────────────────────
# MORCEAUX
# ─────────────────────────────────────────────────────────

def preset_are_you_gonna_go_my_way():
    """Lenny Kravitz - Are You Gonna Go My Way (130 BPM)

    Chaine : Gate > OD > Flanger > EQ > Delay > Reverb
    Slots  :  0      1     2        3    4        5

    Snap 0 Riff   : son principal, intro/couplet/refrain/outro
    Snap 1 Bridge : flanger + EQ chaud (Drive reduit)
    Snap 2 Solo   : boost sustain + EQ lead + slapback 120ms
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("AYGGMW", tempo=130.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -60.0, "Decay": 0.3})

    # Bighorn Fuzz (Ram's Head Big Muff) : fuzz epais et crasseux
    # Regie sur le son Riff ; snapshots affinent via params
    pb.add_block("HD2_DistRamsHead", slot=1,
                 overrides={"Sustain": 0.82, "Tone": 0.58, "Level": 0.75})

    # enabled_default=False : bypasse au chargement, actif uniquement sur Bridge
    pb.add_block("HD2_FlangerGrayFlanger", slot=2, enabled_default=False,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.40})

    pb.add_block("HD2_EQSimple3Band", slot=3)

    pb.add_block("HD2_DelaySimpleDelay", slot=4,
                 overrides={"Time": 0.12, "Feedback": 0.0, "Mix": 0.22,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.18})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 5], color="yellow")

    pb.add_snapshot(1, "Bridge", blocks_on=[0, 1, 2, 3, 5],
                    params={
                        1: {"Sustain": 0.75, "Level": 0.70},
                        3: {"MidFreq": 800.0, "MidGain": -2.0, "HighGain": -3.0},
                    },
                    color="blue")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 3, 4, 5],
                    params={
                        1: {"Sustain": 0.90, "Level": 0.82},
                        3: {"MidFreq": 1000.0, "MidGain": 4.0, "HighGain": 2.0},
                    },
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 5], color="green")

    return pb


# ─────────────────────────────────────────────────────────
# PRESETS — nom de fichier -> fonction
# Utilise par generate_presets.py pour les .hlx individuels.
# ─────────────────────────────────────────────────────────

PRESETS = {
    "Lenny Kravitz - Are You Gonna Go My Way": preset_are_you_gonna_go_my_way,
}
