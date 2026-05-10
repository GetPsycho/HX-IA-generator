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


def preset_beggin():
    """Maneskin - Beggin' (134 BPM)

    Son : crunch mid-gain OCD (Compulsive Drive = Fulltone OCD),
    caractere Marshall Plexi sec et percussif.
    Gain modere : DiMarzio Super Distortion pousse deja fort le circuit.

    Chaine : Gate > CompulsiveDrive > Chorus > Delay > Reverb
    Slots  :  0          1              2         3       4

    Snap 0 Rythme     : crunch sec verse/refrain
    Snap 1 Pre-chorus : crunch + chorus subtil
    Snap 2 Lead       : crunch + delay 250ms pour le climax
    Snap 3 Clean      : accordage / attente
    """
    pb = PresetBuilder("Beggin'", tempo=134.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -55.0, "Decay": 0.35})

    # Compulsive Drive = Fulltone OCD : gain modere (humbucker chaud)
    # LPHP=True : mode HP, attaque seche et dynamique (style Plexi)
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.55, "Tone": 0.58, "LPHP": True, "Level": 0.73})

    # Chorus subtil : sections pre-chorus uniquement, bypasse par defaut
    pb.add_block("HD2_Chorus", slot=2, enabled_default=False,
                 overrides={"Speed": 0.20, "Depth": 0.55, "Mix": 0.25})

    # Delay analogique : lead / climax final, bypasse par defaut
    # 250ms = 0.25s, quelques repetitions courtes
    pb.add_block("HD2_DelaySimpleDelay", slot=3, enabled_default=False,
                 overrides={"Time": 0.25, "Feedback": 0.20, "Mix": 0.28,
                            "TempoSync1": False})

    # Reverb hall legere : meme reglages que AYGGMW pour coherence de volume
    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.18})

    pb.add_snapshot(0, "Rythme", blocks_on=[0, 1, 4],
                    color="yellow")

    pb.add_snapshot(1, "Pre-chorus", blocks_on=[0, 1, 2, 4],
                    color="blue")

    pb.add_snapshot(2, "Lead", blocks_on=[0, 1, 3, 4],
                    params={1: {"Gain": 0.65, "Level": 0.78}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 4],
                    color="green")

    return pb


# ─────────────────────────────────────────────────────────
# PRESETS — nom de fichier -> fonction
# Utilise par generate_presets.py pour les .hlx individuels.
# ─────────────────────────────────────────────────────────

PRESETS = {
    "Lenny Kravitz - Are You Gonna Go My Way": preset_are_you_gonna_go_my_way,
    "Maneskin - Beggin":                       preset_beggin,
}
