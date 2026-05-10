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

    Son : Marshall JCM800 crunch. Sobre pour Morello.
    Wah uniquement sur le solo → pedale externe (Cry Baby MC404).

    Delay "reverb" : feedback tres bas (0.07) = une seule repetition
    qui se noie dans la reverb, pas d'echos distincts perceptibles.
    Delay quarter note 117 BPM = 512ms = 0.51s (interne).

    Chaine : Gate > OD > Delay > Reverb
    Slots  :  0     1    2       3

    Snap 0 Intro  : quasi clean, reverb seule (pas de delay)
    Snap 1 Verse  : clean + delay "reverb" (feedback tres bas)
    Snap 2 Chorus : crunch leger + delay + reverb
    Snap 3 Solo   : crunch + boost gain + delay "reverb"
    """
    pb = PresetBuilder("Be Yourself", tempo=117.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.35})

    # Compulsive Drive = Fulltone OCD : crunch JCM800 leger
    # enabled_default=False : bypasse en Intro et Verse (son clean)
    pb.add_block("HD2_DistCompulsiveDrive", slot=1, enabled_default=False,
                 overrides={"Gain": 0.40, "Tone": 0.58, "LPHP": True, "Level": 0.73})

    # Delay "reverb" : quarter note a 117 BPM (0.51s)
    # Feedback 0.07 = une seule repetition discrete, effet ambiance
    # pas de succession d'echos perceptibles
    # enabled_default=False : pas actif sur l'Intro
    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.51, "Feedback": 0.07, "Mix": 0.10,
                            "TempoSync1": False})

    # Reverb plus presente sur l'ensemble
    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.25})

    # Bloc de boost propre pour l'Intro : bypasse par defaut
    # Compense la perte de densite sonore percue du son clean vs sature
    pb.add_block("HD2_VolPanGain", slot=4, enabled_default=False,
                 overrides={"Gain": 10.0})

    # Snap 0 — Intro : clean + reverb ouverte + boost volume (+10 dB)
    pb.add_snapshot(0, "Intro", blocks_on=[0, 3, 4],
                    params={3: {"Mix": 0.32, "Decay": 0.58}},
                    color="green")

    # Snap 1 — Verse : OD ultra-discret, lisse et chaud.
    # Gain=0.02 + LPHP=False (mode LP, plus chaud) + Level reduit
    # = grain a peine perceptible, signal lisse sans mordant
    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.02, "Tone": 0.48,
                                "LPHP": False, "Level": 0.35}},
                    color="yellow")

    # Snap 2 — Chorus : crunch present
    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.32, "Tone": 0.58, "Level": 0.45}},
                    color="orange")

    # Snap 3 — Solo : crunch pousse (wah = pedale externe)
    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.62, "Level": 0.80}},
                    color="red")

    return pb


def preset_black_hole_sun():
    """Soundgarden - Black Hole Sun (105 BPM) — Kim Thayil

    Son signature : H&K Rotosphere (rotary fast) exclusivement sur le verse clean.
    Big Muff pour refrain/solo, sans rotary (le rotary noie la BigMuff sur HX Effects).
    Slapback 80ms sur le solo pour se distinguer du refrain.

    Chaine : Gate > BigMuff > Rotary > Reverb > Boost > Slapback
    Slots  :  0      1         2        3        4       5

    Snap 0 Verse  : clean + rotary fort + reverb + boost (+8 dB, compense l'absence de dist)
    Snap 1 Refrain: Big Muff + reverb (sans rotary)
    Snap 2 Solo   : Big Muff pousse + slapback 80ms + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Black Hole Sun", tempo=105.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Bighorn Fuzz = Ram's Head Big Muff : distorsion epaisse pour refrain/solo
    # enabled_default=False : bypasse en Verse (son clean)
    pb.add_block("HD2_DistRamsHead", slot=1, enabled_default=False,
                 overrides={"Sustain": 0.75, "Tone": 0.45, "Level": 0.50})

    # Rotary Drum/Horn = Leslie 145 : simule le H&K Rotosphere de Kim Thayil
    # Speed=True (fast), Mix=0.85 et Depth/Horn eleves pour un swirl bien perceptible
    # Bypasse sur Refrain et Solo : le rotary noie la BigMuff sans ampli tube
    pb.add_block("HD2_MM4RotaryDrumHorn", slot=2,
                 overrides={"Speed": True, "Depth": 0.82, "Horn Depth": 0.88,
                            "Drive": 0.08, "Mix": 0.85})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.22})

    # Boost clean verse : compense l'absence de BigMuff face aux autres presets
    # enabled_default=False : actif uniquement sur Verse
    pb.add_block("HD2_VolPanGain", slot=4, enabled_default=False,
                 overrides={"Gain": 8.0})

    # Slapback 80ms : differencie le Solo du Refrain
    # enabled_default=False : actif uniquement sur Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=5, enabled_default=False,
                 overrides={"Time": 0.08, "Feedback": 0.0, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3, 4], color="green")

    pb.add_snapshot(1, "Refrain", blocks_on=[0, 1, 3], color="orange")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 3, 5],
                    params={1: {"Sustain": 0.85, "Level": 0.60}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3], color="blue")

    return pb


def preset_creep():
    """Radiohead - Creep (93 BPM) — Jonny Greenwood

    Son : Fender Telecaster Plus → Marshall ShredMaster (Vermin Dist)
    → Fender Eighty-Five clean (solid-state, tres scoop : Bass 11, Mid 1, Treble 11).
    Verse : Roland Dimension D (chorus large et transparent, mode SW4).
    Les "stabs" percussifs avant le refrain = jeu mute agressif + kill-switch,
    pas de reglage specifique (technique de jeu).

    Chaine : Gate > VerminDist > Dimension > Reverb
    Slots  :  0      1            2            3

    Snap 0 Verse  : clean + Roland Dimension D + reverb discrete (G-B-C-Cm arpege)
    Snap 1 Stabs  : dist seule, son sec et percussif (avant le refrain)
    Snap 2 Chorus : dist + reverb (plein sustain, G-B-C-Cm)
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Creep", tempo=93.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Vermin Dist = Pro Co RAT : plus proche du Marshall ShredMaster disponible
    # (meme architecture opamp, gain eleve, filtre passe-bas = ton mi-grave agressif)
    # Filter=0.38 : coupe les aigus pour renforcer les mids, caractere britannique
    # enabled_default=False : bypasse au chargement (verse clean par defaut)
    pb.add_block("HD2_DistVerminDist", slot=1, enabled_default=False,
                 overrides={"Gain": 0.75, "Filter": 0.38, "Level": 0.52})

    # MM4 Dimension = Roland Dimension D : chorus transparent sur le verse clean
    # SW4=True (mode 4) : le plus spacieux, signature son clean Radiohead debut 90s
    pb.add_block("HD2_MM4Dimension", slot=2,
                 overrides={"SW1": False, "SW2": False, "SW3": False, "SW4": True,
                            "Mix": 1.0, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.16})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3], color="green")

    # Stabs : dist seule sans reverb = son sec, impact direct
    pb.add_snapshot(1, "Stabs", blocks_on=[0, 1], color="orange")

    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 3], color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_dani_california():
    """RHCP - Dani California (97 BPM) — John Frusciante

    Son : Fender Strat 1954 → Moog MF-101 LPF (Auto Filter, verse)
    → Boss DS-2 Turbo (Deez One Mod, chorus/solo) → Marshall Major 200W bridgé.
    Verse : filtre passe-bas avec envelope follower = son "wobbly" signature.
    Wah (solo) : pédale externe (Ibanez WH-10 de Frusciante / MC404 d'Eric).

    Chaine : Gate > AutoFilter > DeezOneMod > Reverb
    Slots  :  0      1            2              3

    Snap 0 Verse  : filter envelope + reverb, dist bypasse (intro + couplets)
    Snap 1 Chorus : dist + reverb, filter bypasse
    Snap 2 Solo   : dist gain plus eleve + reverb (wah = pedale externe)
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Dani California", tempo=97.0)

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # Auto Filter = Moog MF-101 Low-Pass Filter approx. : envelope follower LP
    # Mode=0 (LP), s'ouvre dynamiquement selon l'intensite du jeu (Sens=0.55)
    # enabled_default=False : bypasse au chargement, actif uniquement sur Verse
    pb.add_block("HD2_FilterAutoFilter", slot=1, enabled_default=False,
                 overrides={"Mode": 0, "FilterGain": 14.0, "FilterQ": 6.0,
                            "Sens": 0.55, "Attack": 0.01, "Decay": 0.30,
                            "Frequency": 80.0, "FreqDepth": 4500.0,
                            "Direction": True, "Mix": 1.0, "Level": 0.0})

    # Deez One Mod = BOSS DS-1 Keeley modded : approx. Boss DS-2 Turbo Distortion
    # (DS-2 non modelise directement dans HX Effects)
    # enabled_default=False : bypasse au chargement
    pb.add_block("HD2_DistDeezOneMod", slot=2, enabled_default=False,
                 overrides={"Drive": 0.62, "Tone": 0.52, "Level": 0.52})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.14})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 2, 3], color="orange")

    # Solo : gain un peu plus eleve pour les leads (wah = pedale externe)
    pb.add_snapshot(2, "Solo", blocks_on=[0, 2, 3],
                    params={2: {"Drive": 0.72, "Level": 0.55}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_drive():
    """Incubus - Drive (91 BPM) — Mike Einziger

    Son : PRS McCarty Archtop II → Boss PH-2 Super Phaser (Deluxe Phaser)
    → Boss CE-2 Chorus (70s Chorus, intro et refrain) → Mesa Boogie Dual Rectifier clean.
    Morceau entierement clean : le phaser est l'effet signature du titre.
    Rate du phaser en Hz (range 0-10) : 0.3 Hz intro (dreamy), 0.8 Hz verse/refrain.

    Chaine : Gate > Phaser > Chorus > Reverb
    Slots  :  0      1         2        3

    Snap 0 Intro  : phaser tres lent (0.3 Hz) + CE-2 + reverb large (arpeges swell)
    Snap 1 Verse  : phaser modere (0.8 Hz) sans chorus (couplets directs)
    Snap 2 Refrain: phaser modere + CE-2 + reverb (son plus large et ouvert)
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Drive", tempo=91.0)

    # Seuil bas : morceau clean et doux, ne pas couper les queues de reverb
    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Deluxe Phaser = approx. Boss PH-2 Super Phaser : Stages=4, Feedback=0.28
    # Rate en Hz (0-10) : regle sur le son Verse (0.8 Hz), ajuste par snapshot
    pb.add_block("HD2_PhaserDeluxePhaser", slot=1,
                 overrides={"Rate": 0.8, "Depth": 0.80, "Feedback": 0.28,
                            "Stages": 4, "Mix": 0.50, "Level": 0.0})

    # 70s Chorus = BOSS CE-1 : tres proche du CE-2 (version directe du CE-1)
    # enabled_default=False : bypasse au chargement, actif sur Intro et Refrain
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.50, "VibratoRate": 0.40,
                            "VibratoDepth": 0.40, "Mix": 0.45, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.20, "Mix": 0.22})

    # Intro : phaser tres lent + CE-2 + reverb plus large (arpeges atmospheriques)
    pb.add_snapshot(0, "Intro", blocks_on=[0, 1, 2, 3],
                    params={
                        1: {"Rate": 0.3, "Depth": 0.85},
                        3: {"Decay": 0.62, "Mix": 0.26},
                    },
                    color="green")

    # Verse : phaser seul, son plus sec et direct
    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 3], color="yellow")

    # Refrain : phaser + CE-2 = son plus large, reverb legerement plus ouverte
    pb.add_snapshot(2, "Refrain", blocks_on=[0, 1, 2, 3],
                    params={3: {"Mix": 0.24}},
                    color="orange")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


PRESETS = {
    "Are You Gonna Go My Way - Lenny Kravitz": preset_are_you_gonna_go_my_way,
    "Beggin - Maneskin":                       preset_beggin,
    "Be Yourself - Audioslave":                preset_be_yourself,
    "Black Hole Sun - Soundgarden":            preset_black_hole_sun,
    "Creep - Radiohead":                       preset_creep,
    "Dani California - Red Hot Chili Peppers": preset_dani_california,
    "Drive - Incubus":                         preset_drive,
}
