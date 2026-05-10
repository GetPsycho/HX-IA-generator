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

    # Gate adapte au Bighorn Fuzz : seuil plus haut pour couper le bruit
    # residuel de la fuzz quand on ne joue pas
    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Bighorn Fuzz (Ram's Head Big Muff) : fuzz epais et crasseux
    # Regie sur le son Riff ; snapshots affinent via params
    pb.add_block("HD2_DistRamsHead", slot=1,
                 overrides={"Sustain": 0.82, "Tone": 0.58, "Level": 0.75})

    # enabled_default=False : bypasse au chargement, actif uniquement sur Bridge
    pb.add_block("HD2_FlangerGrayFlanger", slot=2, enabled_default=False,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.40})

    pb.add_block("HD2_EQSimple3Band", slot=3)

    # enabled_default=False : bypasse au chargement, actif uniquement sur Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=4, enabled_default=False,
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

    Jeu funky rythmique : compresseur Ross + OCD a tres faible gain.
    Le Red Squeeze apporte le "squish" funk et regularise l'attaque
    du Super Distortion. L'OCD donne juste le grain du mordant sans saturer.

    Chaine : Gate > RedSqueeze > CompulsiveDrive > Reverb
    1 seul snapshot actif.
    """
    pb = PresetBuilder("Beggin'", tempo=134.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.40})

    # Red Squeeze = Ross Compressor : squish funky, regularise l'attaque
    # Sensitivity moderee pour ne pas ecraser la dynamique
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.60, "Mix": 1.0, "Level": 3.0})

    # Compulsive Drive = Fulltone OCD, gain tres bas
    # Le compresseur en amont regularise le signal du Super Distortion
    # LPHP=True (mode HP) : attaque seche et percussive
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.22, "Tone": 0.60, "LPHP": True, "Level": 0.73})

    # Reverb discrete : meme reglages pour coherence de volume
    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.15})

    pb.add_snapshot(0, "Beggin", blocks_on=[0, 1, 2, 3],
                    color="yellow")

    return pb


# ─────────────────────────────────────────────────────────
# PRESETS — nom de fichier -> fonction
# Utilise par generate_presets.py pour les .hlx individuels.
# ─────────────────────────────────────────────────────────

def preset_be_yourself():
    """Audioslave - Be Yourself (117 BPM) — Tom Morello

    Son : Marshall JCM800 crunch. Be Yourself est sobre pour Morello :
    clean + delay en verse, crunch + delay en chorus, crunch en solo.
    Wah uniquement sur le solo → pedal externe (Cry Baby MC404), pas dans le preset.

    Delay : quarter note a 117 BPM = 512ms = 0.51s (interne)

    Chaine : Gate > OD > Delay > Reverb
    Slots  :  0     1    2       3

    Snap 0 Verse   : clean + delay atmosph.  (intro/couplets)
    Snap 1 Chorus  : crunch leger + delay    (refrain)
    Snap 2 Solo    : crunch + boost volume   (solo, wah ext.)
    Snap 3 Standby : gate + reverb seuls
    """
    pb = PresetBuilder("Be Yourself", tempo=117.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.35})

    # Compulsive Drive = Fulltone OCD : crunch JCM800 leger
    # enabled_default=False : bypasse en Verse (son clean)
    pb.add_block("HD2_DistCompulsiveDrive", slot=1, enabled_default=False,
                 overrides={"Gain": 0.40, "Tone": 0.58, "LPHP": True, "Level": 0.73})

    # Delay atmospherique : quarter note a 117 BPM (0.51s)
    # Feedback modere, mix discret — laisse la voix respirer
    pb.add_block("HD2_DelaySimpleDelay", slot=2,
                 overrides={"Time": 0.51, "Feedback": 0.25, "Mix": 0.28,
                            "TempoSync1": False})

    # Reverb hall legere : coherence volume avec les autres presets
    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.18})

    # Snap 0 — Verse : clean + delay + reverb (intro et couplets)
    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3],
                    color="green")

    # Snap 1 — Chorus : crunch OCD + delay + reverb
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3],
                    color="yellow")

    # Snap 2 — Solo : crunch + boost gain/level (wah = pedale externe)
    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.55, "Level": 0.80}},
                    color="red")

    # Snap 3 — Standby : accordage / attente
    pb.add_snapshot(3, "Standby", blocks_on=[0, 3],
                    color="blue")

    return pb


PRESETS = {
    "Lenny Kravitz - Are You Gonna Go My Way": preset_are_you_gonna_go_my_way,
    "Maneskin - Beggin":                       preset_beggin,
    "Audioslave - Be Yourself":                preset_be_yourself,
}
