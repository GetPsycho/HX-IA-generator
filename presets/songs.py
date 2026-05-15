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
    """Lenny Kravitz - Are You Gonna Go My Way (130 BPM) — Craig Ross

    Craig Ross a joue TOUTES les parties (riff, rhythm, solo) — une seule prise.
    Guitare : Gibson Les Paul Goldtop 1953 (appartenant a Kravitz).
    Ampli : Gibson Skylark (petit combo tube annees 50) pousse a fond.
    Pas de pedale de distorsion — saturation naturelle de l'ampli uniquement.
    Flanger : tape flanging studio (Henry Hirsch). Discret sur le riff, prononce sur le bridge.

    Arbitrator Fuzz (Fuzz Face germanium, always-on) = simulation Gibson Skylark.
    Le Fuzz Face a gain modere reproduit le cote "fuzz sur les bords" d'un petit
    ampli tube sature : saturation asymetrique, harmoniques impaires.
    Matching documente : Gibson Skylark -> Arbitrator Fuzz.

    Fuzz=0.62 pour Riff/Bridge. Solo : Fuzz=0.50 (bridge, moins baveux).
    Level=1.0 (max) : le Fuzz Face a un deficit d'output structurel, meme
    au Level maximum il reste en dessous du signal clean.
    KinkyBoost always-on (+6 dB) compense ce deficit sur tous les snaps
    distorsion. Clean snap exclut le KinkyBoost (reference niveau accordage).

    Chaine : Gate > ArbitratorFuzz > GrayFlanger > Reverb > KinkyBoost
    Slots  :  0       1                 2             3        4

    Snap 0 Riff   : ArbitratorFuzz + flanger discret (Mix=0.28) + reverb + boost
    Snap 1 Bridge : ArbitratorFuzz + flanger prononce (Mix=0.48) + reverb + boost
    Snap 2 Solo   : ArbitratorFuzz (Fuzz=0.50) + reverb + boost — bridge
    Snap 3 Clean  : reverb seule (accordage, reference volume)
    """
    pb = PresetBuilder("AYGGMW", tempo=130.0, styles=["hard_rock", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Arbitrator Fuzz = Fuzz Face germanium : simulation Gibson Skylark pousse a fond
    # Fuzz=0.62 : modere — "fuzz sur les bords" sans mur de fuzz
    # Level=1.0 : max — le Fuzz Face a un output structurellement bas (deficit connu)
    # enabled_default=True : canal d'ampli permanent (pas de pedale de disto sur ce titre)
    pb.add_block("HD2_DistArbitratorFuzz", slot=1,
                 overrides={"Fuzz": 0.62, "Level": 0.90})

    # Gray Flanger = approximation du tape flanging studio (Henry Hirsch)
    # Mix variable par snapshot : Riff=0.28 discret, Bridge=0.48 prononce (via params)
    pb.add_block("HD2_FlangerGrayFlanger", slot=2, enabled_default=False,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.28})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.16})

    # KinkyBoost always-on : compense le deficit d'output du Fuzz Face (+6 dB)
    # Actif sur tous les snaps distorsion, exclu du snap Clean (reference)
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2, 3, 4], color="yellow")

    pb.add_snapshot(1, "Bridge", blocks_on=[0, 1, 2, 3, 4],
                    params={2: {"Mix": 0.48}},
                    color="blue")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 3, 4],
                    params={1: {"Fuzz": 0.70}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="green")

    return pb


def preset_beggin():
    """Maneskin - Beggin' (134 BPM) — Thomas Raggi

    Ton funky compresse tout au long du morceau : pas de section propre.
    Ross Compressor + OCD low gain toujours actifs (enabled_default=True).
    Sensitivity abaissee a 0.50 : Super Distortion chevalet Eric
    = sortie plus elevee qu'une Telecaster single-coil de reference.

    Chaine : Gate > RedSqueeze > CompulsiveDrive > Ganymede
    Slots  :  0      1            2                  3

    Snap 0 Verse  : OCD Gain=0.18 (funky minimal, attaque seche)
    Snap 1 Refrain: OCD Gain=0.24 (meme ton, legerement plus de corps)
    """
    pb = PresetBuilder("Beggin'", tempo=134.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.40})

    # Red Squeeze = Ross Compressor : squish funky, regularise l'attaque
    # Sensitivity 0.50 : compense la sortie elevee du Super Distortion d'Eric
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.50, "Mix": 1.0, "Level": 2.0})

    # OCD always-on : grain minimal fondu dans le compresseur, pas de saturation
    # LPHP=True (HP) : attaque percussive et seche, colle avec le Mesa Boogie tight
    # Gain variable par snapshot
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.18, "Tone": 0.60, "LPHP": True, "Level": 0.77})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.15})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 2, 3], color="green")

    pb.add_snapshot(1, "Refrain", blocks_on=[0, 1, 2, 3],
                    params={2: {"Gain": 0.24}},
                    color="orange")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="white")

    return pb


# ─────────────────────────────────────────────────────────
# PRESETS — nom de fichier -> fonction
# Utilise par generate_presets.py pour les .hlx individuels.
# ─────────────────────────────────────────────────────────

def preset_be_yourself():
    """Audioslave - Be Yourself (117 BPM) — Tom Morello

    JCM800 canal overdrive permanent — pas de pedale OD externe.
    OCD always-on simule ce canal gain. Gain variable par snapshot
    (simule le potentiometre de volume guitare qui nettoie le JCM800).

    Volume : Level different par snapshot pour compenser l'interaction
    Gain/volume de l'OCD — faible Gain = faible output naturel.
    Level eleve sur Intro/Verse pour atteindre la reference clean.
    Pas de KinkyBoost : Level par snap est le levier le plus direct.

    Chaine : Gate > CompulsiveDrive > Ganymede
    Slots  :  0       1                 2

    Snap 0 Intro  : Gain=0.03, Level=0.85, LPHP=False (quasi-clair, reverb large)
    Snap 1 Verse  : Gain=0.22, Level=0.75, LPHP=False (crunch leger)
    Snap 2 Chorus : Gain=0.38, Level=0.68, LPHP=True  (crunch present)
    Snap 3 Solo   : Gain=0.55, Level=0.65, LPHP=True  (lead, wah = pedale externe)
    """
    pb = PresetBuilder("Be Yourself", tempo=117.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.32})

    # CompulsiveDrive = OCD : simule canal overdrive permanent JCM800
    # Level variable par snapshot : compense l'output plus faible a faible Gain
    # Base = valeurs du Chorus (snap de reference inter-preset)
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.38, "Tone": 0.58, "LPHP": True, "Level": 0.73})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.22})

    # Intro : Gain=0.02 (quasi-clair, moins de drive que 0.03)
    # Level=0.92 : +0.07 vs decalage global pour compenser la baisse de Gain
    pb.add_snapshot(0, "Intro", blocks_on=[0, 1, 2],
                    params={1: {"Gain": 0.02, "Tone": 0.50, "LPHP": False, "Level": 0.92},
                            2: {"Mix": 0.32, "Decay": 0.58}},
                    color="green")

    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 2],
                    params={1: {"Gain": 0.22, "Tone": 0.55, "LPHP": False, "Level": 0.80}},
                    color="yellow")

    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 2],
                    color="orange")

    # Wah = pedale externe (Cry Baby MC404 CAE d'Eric)
    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 2],
                    params={1: {"Gain": 0.55, "Tone": 0.60, "LPHP": True, "Level": 0.70}},
                    color="red")

    return pb


def preset_black_hole_sun():
    """Soundgarden - Black Hole Sun (105 BPM) — Kim Thayil

    Son signature : H&K Rotosphere emule le Leslie Model 16 de l'enregistrement.
    Rotary FAST sur le verse clean, SLOW sur le refrain (avec Big Muff).
    Source : "fast setting for the verses, slow setting for the choruses" (Premier Guitar).
    Intro : arpèges clean Cornell sans rotary. Slapback 80ms differencie le solo.

    Chaine : Gate > BigMuff > Rotary > Reverb > KinkyBoost > Slapback > OD-Intro
    Slots  :  0      1         2        3        4             5          6

    Snap 0 Intro  : clean + reverb + KinkyBoost (arpèges Cornell, pas de rotary)
    Snap 1 Verse  : clean + rotary FAST + reverb + KinkyBoost
    Snap 2 Refrain: Big Muff + rotary SLOW (Speed=False via params) + reverb
    Snap 3 Solo   : Big Muff pousse + slapback 80ms + reverb
    """
    pb = PresetBuilder("Black Hole Sun", tempo=105.0, styles=["grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Bighorn Fuzz = Ram's Head Big Muff : distorsion epaisse pour refrain/solo
    # enabled_default=False : bypasse en Intro et Verse
    pb.add_block("HD2_DistRamsHead", slot=1, enabled_default=False,
                 overrides={"Sustain": 0.75, "Tone": 0.45, "Level": 0.50})

    # Rotary Drum/Horn = Leslie 145 : simule le H&K Rotosphere de Kim Thayil
    # Speed=True (fast), Mix=0.85 pour un swirl bien perceptible
    # enabled_default=False : doit etre explicitement dans blocks_on pour etre actif
    pb.add_block("HD2_MM4RotaryDrumHorn", slot=2, enabled_default=False,
                 overrides={"Speed": True, "Depth": 0.82, "Horn Depth": 0.88,
                            "Drive": 0.5, "Mix": 0.85, "Level": 4.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.22})

    # Kinky Boost = Xotic EP Booster : corps et harmoniques sur le verse clean
    # Drive reduit (1.0->0.80) + Boost=False : verse un peu moins fort
    # enabled_default=False : actif uniquement sur Verse
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Slapback 80ms : differencie le Solo du Refrain
    # enabled_default=False : actif uniquement sur Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=5, enabled_default=False,
                 overrides={"Time": 0.08, "Feedback": 0.0, "Mix": 0.18,
                            "TempoSync1": False})

    # Compulsive Drive = OCD : OD epaisse pour l'intro (riff grave Cornell)
    # Gain monte (0.35->0.48) pour plus de grain et de corps
    # enabled_default=False : actif uniquement sur Intro
    pb.add_block("HD2_DistCompulsiveDrive", slot=6, enabled_default=False,
                 overrides={"Gain": 0.50, "Tone": 0.50, "Level": 0.80})

    pb.add_snapshot(0, "Intro", blocks_on=[0, 3, 4, 6],
                    params={6: {"Gain": 0.05}},
                    color="yellow")

    pb.add_snapshot(1, "Verse", blocks_on=[0, 2, 3, 4], color="green")

    # Rotary SLOW sur le refrain : Speed=False via params
    # KinkyBoost (4) : compense le deficit d'output du Big Muff (meme cause qu'Arbitrator Fuzz)
    pb.add_snapshot(2, "Refrain", blocks_on=[0, 1, 2, 3, 4],
                    params={1: {"Level": 0.42}, 2: {"Speed": False}},
                    color="orange")

    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 3, 4, 5],
                    params={1: {"Sustain": 0.85, "Level": 0.48}},
                    color="red")

    return pb


def preset_creep():
    """Radiohead - Creep (93 BPM) — Jonny Greenwood

    Son : Fender Telecaster Plus → Marshall ShredMaster (Vermin Dist)
    → Fender Eighty-Five clean (solid-state, tres scoop : Bass 11, Mid 1, Treble 11).
    Verse : Roland Dimension D (chorus large et transparent, mode SW4).
    Stabs : compresseur Dyna Comp + dist gain pousse = "gros coup" produit, fort.

    Chaine : Gate > VerminDist > Dimension > Reverb > RedSqueeze > KinkyBoost
    Slots  :  0      1            2            3        4             5

    Snap 0 Verse  : clean + Roland Dimension D + reverb discrete + KinkyBoost (ref volume)
    Snap 1 Stabs  : dist gain pousse + compresseur (gros coup mute, sec et fort)
    Snap 2 Chorus : dist + reverb (plein sustain, G-B-C-Cm)
    Snap 3 Clean  : accordage / attente

    Volume : RAT sous unity a Level=0.52 → Level monte a 0.68 (Chorus = ref).
    Verse clean + KinkyBoost = ref. Stabs Level=0.80 via params + RedSqueeze = le plus fort.
    """
    pb = PresetBuilder("Creep", tempo=93.0, styles=["grunge", "alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Vermin Dist = Pro Co RAT : plus proche du Marshall ShredMaster disponible
    # (meme architecture opamp, gain eleve, filtre passe-bas = ton mi-grave agressif)
    # Filter=0.38 : coupe les aigus pour renforcer les mids, caractere britannique
    # Level 0.52 → 0.68 : RAT sous unity a faible Level, 0.68 amene le Chorus a ref
    # enabled_default=False : bypasse au chargement (verse clean par defaut)
    pb.add_block("HD2_DistVerminDist", slot=1, enabled_default=False,
                 overrides={"Gain": 0.75, "Filter": 0.38, "Level": 0.85})

    # MM4 Dimension = Roland Dimension D : chorus transparent sur le verse clean
    # SW4=True (mode 4) : le plus spacieux, signature son clean Radiohead debut 90s
    pb.add_block("HD2_MM4Dimension", slot=2,
                 overrides={"SW1": False, "SW2": False, "SW3": False, "SW4": True,
                            "Mix": 1.0, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.16})

    # Red Squeeze = MXR Dyna Comp : compression forte + makeup gain pour les Stabs
    # Sensitivity haute = ecrase l'attaque, sustain le coup mute
    # Level +6 dB = makeup, donne le "gros coup fort" demande
    # enabled_default=False : actif uniquement sur Stabs
    pb.add_block("HD2_CompressorRedSqueeze", slot=4, enabled_default=False,
                 overrides={"Sensitivity": 0.78, "Mix": 1.0, "Level": 6.0})

    # KinkyBoost = Xotic EP Booster : boost volume sur Verse, Chorus et Stabs
    # enabled_default=False : exclu du snap Clean (reference)
    pb.add_block("HD2_DistKinkyBoost", slot=5, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3, 5], color="green")

    # Stabs : dist + KinkyBoost seul (pas de compresseur), Gain=0.85 + Level=1.0 via params
    pb.add_snapshot(1, "Stabs", blocks_on=[0, 1, 5],
                    params={1: {"Gain": 0.85, "Level": 1.0}},
                    color="orange")

    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 3, 5], color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_dani_california():
    """RHCP - Dani California (97 BPM) — John Frusciante

    Son : Fender Strat 1954/1962 → Moog MF-101 LPF (verse lick)
    → Boss DS-2 Turbo (Deez One Mod, chorus/solo) → Marshall Major 200W bridgé.
    Wah (solo) : pédale externe (MC404 CAE).

    Verse clean : confirme par Butch Vig / interviews — "straight into amp, no pedal".
    Filtre verse : Doepfer A-100 modular studio, reproduit live avec Moog MF-101.
    KinkyBoost : compense le delta RMS clean/distordu sur Verse et Lick (pas Chorus/Solo).

    Chaine : Gate > AutoFilter > DeezOneMod > Reverb > KinkyBoost
    Slots  :  0      1            2              3        4

    Snap 0 Verse  : clean pur + reverb + KinkyBoost (+6 dB RMS)
    Snap 1 Lick   : clean + AutoFilter (MF-101) + reverb + KinkyBoost
    Snap 2 Chorus : DS-2 Turbo + reverb
    Snap 3 Solo   : DS-2 Turbo gain pousse + reverb (wah = pedale externe)
    """
    pb = PresetBuilder("Dani California", tempo=97.0, styles=["funk_rock", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # Auto Filter = Moog MF-101 LPF (approximation live du Doepfer A-100 studio)
    # Mode BP (1) retenu : Mode LP (0) trop grave sur le lick (valide par test)
    # Le MF-101 original est un LPF mais le BP est plus fonctionnel sur le HX
    pb.add_block("HD2_FilterAutoFilter", slot=1, enabled_default=False,
                 overrides={"Mode": 1, "FilterGain": 14.0, "FilterQ": 6.0,
                            "Sens": 0.55, "Attack": 0.01, "Decay": 0.30,
                            "Frequency": 200.0, "FreqDepth": 4500.0,
                            "Direction": True, "Mix": 1.0, "Level": 0.0})

    # Deez One Mod = approx. Boss DS-2 Turbo Distortion (mode Turbo II)
    # DS-2 non modelise en HX ; DS-1 Keeley est l'approximation la plus proche
    # Drive 0.65 = Turbo mode (plus de saturation que DS-1 standard)
    pb.add_block("HD2_DistDeezOneMod", slot=2, enabled_default=False,
                 overrides={"Drive": 0.65, "Tone": 0.52, "Level": 0.52})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.16})

    # Kinky Boost = Xotic EP Booster : boost de volume +6 dB sur les snaps clean
    # Drive=0 = pas de coloration / Boost=True = +6 dB interne
    # Place apres la reverb : agit comme trimmer de volume pur, ne recolore pas la queue
    # enabled_default=False : actif sur Verse/Lick, bypasse sur Chorus/Solo
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Verse : clean pur + boost RMS pour tenir dans le mix live
    pb.add_snapshot(0, "Verse", blocks_on=[0, 3, 4], color="green")

    # Lick : AutoFilter dynamique + boost RMS (signal clean filtre dans les mids)
    pb.add_snapshot(1, "Lick", blocks_on=[0, 1, 3, 4], color="yellow")

    # Chorus : DS-2 Turbo engage — pas de KinkyBoost (distorsion = RMS naturellement haut)
    pb.add_snapshot(2, "Chorus", blocks_on=[0, 2, 3], color="orange")

    # Solo : DS-2 gain pousse — wah externe MC404 CAE, pas dans la chaine
    pb.add_snapshot(3, "Solo", blocks_on=[0, 2, 3],
                    params={2: {"Drive": 0.72, "Level": 0.55}},
                    color="red")

    return pb


def preset_drive():
    """Incubus - Drive (91 BPM) — Mike Einziger

    Morceau majoritairement acoustique : Intro/Verse/Chorus joues a la guitare acoustique.
    Solo : guitare electrique (PRS McCarty) avec H&K Tube Rotosphere MkII (Leslie simulator),
    Boss PH-2 Super Phaser, overdrive leger germanium-style, delay sparse.

    Micro manche recommande pour le snap Acoustique (plus chaud, meilleur rendu sim).

    Chaine : Gate > AcousSim > Phaser > Rotosphere > KinkyBoost > Delay > Reverb
    Slots  :  0      1          2         3             4            5       6

    Snap 0 Acoustique : simulation acoustique + reverb ambiante (Intro/Verse/Chorus)
    Snap 1 Solo       : Phaser + Rotosphere FAST + KinkyBoost (Drive=0.3) + delay + reverb
    Snap 2 Clean      : accordage / attente
    Snap 3 Clean      : accordage / attente
    """
    pb = PresetBuilder("Drive", tempo=91.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Acoustic Sim : simulation caisse de resonance sur guitare electrique
    # Mode=1 (Medium body), micro manche recommande pour maximiser l'effet
    # Level en dB (range -60/+6) : 0.0 = unite
    pb.add_block("L6SPB_AcousGtrSim", slot=1, enabled_default=False,
                 overrides={"Mode": 1, "Body": 0.65, "Top": 0.55,
                            "Shimmer": 0.25, "Level": 0.0})

    # Deluxe Phaser = Boss PH-2 Super Phaser : sweep organique sur le solo
    # Mix=0.75 : bien present, contribue au caractere avec le Rotosphere
    pb.add_block("HD2_PhaserDeluxePhaser", slot=2, enabled_default=False,
                 overrides={"Rate": 0.6, "Depth": 0.82, "Feedback": 0.28,
                            "Stages": 4, "Mix": 0.75, "Level": 0.0})

    # Rotary Drum/Horn = H&K Tube Rotosphere MkII : signature du solo de Drive
    # Speed=True (fast) : rotation rapide, swirl present
    # Mix=0.88 : effet dominant
    pb.add_block("HD2_MM4RotaryDrumHorn", slot=3, enabled_default=False,
                 overrides={"Speed": True, "Depth": 0.85, "Horn Depth": 0.90,
                            "Drive": 0.3, "Mix": 0.88, "Level": 4.0})

    # KinkyBoost = Xotic EP Booster : boost + leger grain (Drive=0.3) pour gonfler le solo
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.3, "Boost": True, "Bright": False})

    # Delay sparse : eco unique, profondeur sans surcharger le Rotosphere
    pb.add_block("HD2_DelaySimpleDelay", slot=5, enabled_default=False,
                 overrides={"Time": 0.40, "Feedback": 0.15, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=6,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.22})

    pb.add_snapshot(0, "Acoustique", blocks_on=[0, 1, 6], color="green")

    # Solo : Phaser + Rotosphere (FAST) + KinkyBoost + delay + reverb
    pb.add_snapshot(1, "Solo", blocks_on=[0, 2, 3, 4, 5, 6], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 6],
                    params={6: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 6],
                    params={6: {"Mix": 0.10}},
                    color="white")

    return pb


def preset_even_flow():
    """Pearl Jam - Even Flow (103 BPM) — Mike McCready / Stone Gossard

    Accordage : Drop D (D A D G B E). Enregistrement un quart de ton plus bas.
    Son : Fender Strat 1958 + Ibanez TS9 → Marshall JCM800 cranked.
    Scream 808 always-on a gain eleve : simule le JCM800 + TS9 comme push.
    Le son ne change pas entre Verse/Chorus/Bridge — un seul snap principal.
    Wah (licks et solo) : pedale externe (MC404 CAE d'Eric).

    Gain stacking : Scream808 (TS9, push mid) → CompulsiveDrive (OCD, JCM800 cranked).
    Les deux always-on : le TS9 pousse l'entree de l'OCD comme dans le rig original.

    Chaine : Gate > Scream808 > CompulsiveDrive > ScriptModPhase > SimpleDelay > Reverb
    Slots  :  0      1           2                 3                 4              5

    Snap 0 Principal : TS9 + OCD + reverb (Intro/Verse/Chorus/Bridge/Licks)
    Snap 1 Solo      : + Phase 90 + DD-3 delay (wah = pedale externe)
    Snap 2 Clean     : accordage / attente
    Snap 3 Clean     : accordage / attente
    """
    pb = PresetBuilder("Even Flow", tempo=103.0, styles=["grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.32})

    # Scream 808 = Ibanez TS9 : role de "push" → mid boost + compression
    # Gain modere : le TS9 n'est pas la source de saturation principale
    # Level eleve : pousse fort dans l'entree de l'OCD (comme dans le rig original)
    pb.add_block("HD2_DistScream808", slot=1,
                 overrides={"Gain": 0.40, "Tone": 0.62, "Level": 0.70})

    # Compulsive Drive = OCD : simule le canal preamp JCM800 cranked
    # LPHP=True (HP) : punch britannique, attack seche
    # Gain=0.72 : JCM800 a gain eleve, pas de canal clean
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.85, "Tone": 0.58, "LPHP": True, "Level": 0.58})

    # Script Mod Phase = MXR Phase 90 (script logo) : modulation sur le solo
    # enabled_default=False : actif uniquement sur Solo
    pb.add_block("HD2_PhaserScriptModPhase", slot=3, enabled_default=False,
                 overrides={"Rate": 0.25, "Mix": 0.32, "Level": 0.0})

    # Simple Delay = Boss DD-3 : delay sparse sur le solo
    # Time 0.29s ≈ double croche a 103 BPM
    # enabled_default=False : actif uniquement sur Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=4, enabled_default=False,
                 overrides={"Time": 0.29, "Feedback": 0.12, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.18})

    pb.add_snapshot(0, "Principal", blocks_on=[0, 1, 2, 5], color="orange")

    # Solo : Phase90 + DD-3 sparse + wah externe MC404 CAE
    pb.add_snapshot(1, "Solo", blocks_on=[0, 1, 2, 3, 4, 5], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 5],
                    params={5: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 5],
                    params={5: {"Mix": 0.10}},
                    color="white")

    return pb


def preset_how_you_remind_me():
    """Nickelback - How You Remind Me (86 BPM) — Chad Kroeger + Ryan Peake

    Accordage : standard (E A D G B E). Source : Ultimate Guitar.
    Deux guitaristes distincts :
    - Chad Kroeger : accords clairs (intro/chorus) via Fender Super 60 rack + Boss CH-1/BF-2
    - Ryan Peake : arpeges propres sur le verse + les deux saturent sur le verse (HM-2)
    Pas de solo guitare dans ce morceau.

    KinkyBoost Bright=True : approxime le caractere brillant/metallique du Fender Super 60
    de Kroeger (clean tres propre et scintillant, pas la chaleur d'un tube).

    Chaine : Gate > SwedishChainsaw > Chorus70s > Reverb > KinkyBoost
    Slots  :  0       1                 2           3         4

    Snap 0 Chorus : clean brillant + KinkyBoost (Bright=True) + reverb (intro/refrain)
    Snap 1 Verse  : HM-2 chainsaw plein + reverb seche (saturation massive serree)
    Snap 2 Arpeges: clean + 70s Chorus (Boss CH-1) + KinkyBoost + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("How You Remind Me", tempo=86.0, styles=["post_grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Swedish Chainsaw = Boss HM-2 : tous params dimes = son chainsaw signature
    # enabled_default=False : uniquement sur Verse
    pb.add_block("HD2_DistSwedishChainsaw", slot=1, enabled_default=False,
                 overrides={"Drive": 0.95, "Bass": 0.90, "Treble": 0.80,
                            "Level": 0.50})

    # 70s Chorus = approx. Boss CH-1 Super Chorus (Kroeger) : modulation legere arpeges
    # Intensity bas = effet subtil et transparent
    # enabled_default=False : uniquement sur Arpeges
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.30, "VibratoRate": 0.32,
                            "VibratoDepth": 0.28, "Mix": 0.35, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.12})

    # KinkyBoost Bright=True : simule le caractere scintillant du Fender Super 60 rack
    # enabled_default=False : actif sur Chorus + Arpeges, exclu Verse et Clean
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": True})

    # Chorus : clean + reverb plus ouverte + KinkyBoost brillant
    pb.add_snapshot(0, "Chorus", blocks_on=[0, 3, 4],
                    params={3: {"Mix": 0.20}},
                    color="green")

    # Verse : HM-2 chainsaw plein, reverb seche (base Mix=0.12)
    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 3], color="red")

    # Arpeges : clean + chorus leger + reverb ouverte + KinkyBoost
    pb.add_snapshot(2, "Arpeges", blocks_on=[0, 2, 3, 4],
                    params={3: {"Mix": 0.20}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_hysteria():
    """Muse - Hysteria (93 BPM) — Matt Bellamy

    Son : Manson custom → KWB (high gain) → Diezel VH4.
    Note : Hysteria est une chanson de basse ; la guitare joue en soutien.
    Son mur de distorsion compresse et epais.

    Chaine : Gate > KWB > SimpleDelay > Reverb
    Slots  :  0     1      2              3

    Snap 0 Riff   : dist haute + reverb (riff principal)
    Snap 1 Chorus : dist + delay court + reverb
    Snap 2 Solo   : dist pousse + delay + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Hysteria", tempo=93.0, styles=["nu_metal"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.25})

    # KWB = Kowloon Walled Bunny Dist : high-gain, caractere Diezel
    pb.add_block("HD2_DistKWB", slot=1,
                 overrides={"Gain": 0.72, "Bass": 2.0, "Treble": 1.0, "Level": 0.52})

    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.16, "Feedback": 0.08, "Mix": 0.15,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.15, "Mix": 0.14})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 3], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.82, "Level": 0.58}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_i_wanna_be_your_slave():
    """Maneskin - I Wanna Be Your Slave (131 BPM) — Thomas Raggi

    Son : Telecaster → Klon (Minotaur) → OCD (Compulsive Drive) → Marshall Plexi.
    Rock glam agressif, saturation stackee.

    Chaine : Gate > Minotaur > CompulsiveDrive > Reverb
    Slots  :  0      1          2                  3

    Snap 0 Verse  : Klon crunch + reverb
    Snap 1 Chorus : Klon + OCD = saturation stackee + reverb
    Snap 2 Solo   : Klon + OCD pousse + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("I Wanna Be Slave", tempo=131.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Minotaur = Klon Centaur : boost transparent mid-heavy, crunch pour le verse
    pb.add_block("HD2_DistMinotaur", slot=1,
                 overrides={"Gain": 0.48, "Tone": 0.60, "Level": 0.55})

    # Compulsive Drive = OCD : saturation additionnelle pour chorus/solo
    # enabled_default=False : bypasse en Verse
    pb.add_block("HD2_DistCompulsiveDrive", slot=2, enabled_default=False,
                 overrides={"Gain": 0.45, "Tone": 0.58, "Level": 0.52})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.18, "Mix": 0.14})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3], color="yellow")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3], color="orange")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.55}, 2: {"Gain": 0.55, "Level": 0.58}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_le_reste():
    """Clara Luciani - Le Reste (113 BPM) — Sage (Ambroise Willaume)

    Son : Strat clean compressée, inspiration Nile Rodgers.
    Red Squeeze (Dyna Comp) = compression snappy, attaque articulee.
    Pas de distorsion, reverb ambiante.

    Chaine : Gate > RedSqueeze > Reverb
    Slots  :  0      1            2

    Snap 0 Verse  : Strat compressee + reverb
    Snap 1 Chorus : meme son + reverb plus ouverte
    Snap 2 Clean  : accordage / attente
    """
    pb = PresetBuilder("Le Reste", tempo=113.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Red Squeeze = MXR Dyna Comp : compression Nile Rodgers
    # Sensitivity moderee = attaque snappy sans ecraser les transitoires
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.62, "Mix": 1.0, "Level": 4.0})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.68, "Modulation": 0.12, "Mix": 0.22})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 2], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2],
                    params={2: {"Mix": 0.30, "Decay": 0.60}},
                    color="yellow")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_no_one_knows():
    """Queens of the Stone Age - No One Knows (171 BPM) — Josh Homme

    Son : Epiphone Dot baritone → SD-1 (Level/Tone max, Drive min) → Ampeg V4B.
    Pas de reverb sur l'enregistrement. Son epais et mid-heavy, palm-muting serre.

    Chaine : Gate > StuporOD > EQ10Band > Reverb
    Slots  :  0      1          2           3

    Snap 0 Riff   : SD-1 boost + EQ mids + reverb minimal
    Snap 1 Chorus : meme son, Level legerement plus haut
    Snap 2 Solo   : SD-1 + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("No One Knows", tempo=171.0, styles=["stoner_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Stupor OD = BOSS SD-1 : reglage Josh Homme = Level/Tone max, Drive minimal
    # Son clean boost mid-heavy plutot que distorsion
    pb.add_block("HD2_DistStuporOD", slot=1,
                 overrides={"Drive": 0.18, "Tone": 0.88, "Level": 0.68})

    # 10 Band Graphic = MXR 10-Band EQ : boost mids (800 Hz-1 kHz) comme Josh
    pb.add_block("HD2_EQGraphic10Band", slot=2,
                 overrides={"500Hz": 3.0, "1kHz": 4.0, "2kHz": 2.0,
                            "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.55, "Modulation": 0.10, "Mix": 0.08})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2, 3], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3],
                    params={1: {"Level": 0.75}},
                    color="red")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 3],
                    params={1: {"Drive": 0.28, "Level": 0.70}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_nue():
    """Clara Luciani - Nue (132 BPM) — Sage (Ambroise Willaume)

    Son : Strat clean compressée, inspiration Nile Rodgers.
    Chorus discret (CE-1) sur le refrain pour le shimmer.

    Chaine : Gate > RedSqueeze > Chorus70s > Reverb
    Slots  :  0      1            2            3

    Snap 0 Verse  : Strat compressee + reverb
    Snap 1 Chorus : Strat compressee + chorus leger + reverb plus large
    Snap 2 Clean  : accordage / attente
    """
    pb = PresetBuilder("Nue", tempo=132.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Red Squeeze = MXR Dyna Comp : compression Nile Rodgers (son snappy et articule)
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.62, "Mix": 1.0, "Level": 4.0})

    # 70s Chorus = CE-1 : shimmer discret sur le refrain
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.40, "VibratoRate": 0.35,
                            "VibratoDepth": 0.35, "Mix": 0.35, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.68, "Modulation": 0.12, "Mix": 0.22})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3],
                    params={3: {"Mix": 0.28, "Decay": 0.58}},
                    color="yellow")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_plug_in_baby():
    """Muse - Plug In Baby (136 BPM) — Matt Bellamy

    Son signature : Z.Vex Fuzz Factory (Industrial Fuzz) pour le riff.
    Fuzz gated et instable, tres agressif. Gate eleve pour effet saccade.

    Chaine : Gate > IndustrialFuzz > Reverb
    Slots  :  0      1                2

    Snap 0 Riff   : fuzz gated (le riff signature)
    Snap 1 Chorus : fuzz + reverb plus ouverte
    Snap 2 Solo   : fuzz pousse + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Plug In Baby", tempo=136.0, styles=["nu_metal", "alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.20})

    # Industrial Fuzz = Z.Vex Fuzz Factory : Compress + Gate pour effet "gated fuzz"
    # Gate eleve = coupure nette entre les notes (caracteristique du riff)
    # Stability bas = instabilite voulue du Fuzz Factory
    pb.add_block("HD2_DistIndustrialFuzz", slot=1,
                 overrides={"Compress": 0.72, "Gate": 0.68, "Drive": 0.90,
                            "Stability": 0.58, "Oscillator": False, "Level": 0.52})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.15, "Mix": 0.14})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2],
                    params={2: {"Mix": 0.20, "Decay": 0.48}},
                    color="red")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2],
                    params={1: {"Drive": 1.0, "Level": 0.58}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_radio_song():
    """Superbus - Radio Song (158 BPM) — Patrice Focone

    Son : Fender Telecaster → OD legere → pop-rock entrainent.
    Brillant et punchy, delay pour l'espace.

    Chaine : Gate > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :  0      1                  2              3

    Snap 0 Verse  : OD legere + delay discret + reverb
    Snap 1 Chorus : OD plus presente + reverb
    Snap 2 Lead   : OD + delay + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Radio Song", tempo=158.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.28, "Tone": 0.62, "Level": 0.52})

    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.19, "Feedback": 0.10, "Mix": 0.16,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.15, "Mix": 0.16})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3],
                    params={1: {"Gain": 0.38, "Level": 0.58}},
                    color="orange")

    pb.add_snapshot(2, "Lead", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.42, "Level": 0.60}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_sex_on_fire():
    """Kings of Leon - Sex on Fire (153 BPM) — Matthew Followill

    Son : Gibson ES-335 → OCD (Compulsive Drive) → Vox AC30.
    Reverb ambiante importante (Holy Grail). Phaser pour le bridge.

    Chaine : Gate > CompulsiveDrive > PebblePhaser > Reverb
    Slots  :  0      1                  2              3

    Snap 0 Verse  : OCD crunch leger + reverb ample
    Snap 1 Chorus : OCD plus chaud + reverb
    Snap 2 Bridge : OCD + phaser + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Sex on Fire", tempo=153.0, styles=["indie_rock", "post_grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.38, "Tone": 0.55, "Level": 0.52})

    # Pebble Phaser = EHX Small Stone : Bad Stone Phaser de Followill
    pb.add_block("HD2_PhaserPebblePhaser", slot=2, enabled_default=False,
                 overrides={"Rate": 0.30, "Color": False, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.55, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.28})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3],
                    params={1: {"Gain": 0.48, "Level": 0.58}},
                    color="orange")

    pb.add_snapshot(2, "Bridge", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.45, "Level": 0.55}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_toxicity():
    """System of a Down - Toxicity (115 BPM) — Daron Malakian

    Son : Ibanez Iceman (Drop C) → Boss HM-2 (Swedish Chainsaw) → Mesa Boogie.
    Gate serre pour le palm-muting rapide caracteristique.

    Chaine : Gate > SwedishChainsaw > Reverb
    Slots  :  0      1                  2

    Snap 0 Riff   : HM-2 + gate serre + reverb (palm-muting serre)
    Snap 1 Chorus : HM-2 + reverb (full saturation)
    Snap 2 Solo   : HM-2 + reverb (lead)
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Toxicity", tempo=115.0, styles=["nu_metal"])

    # Gate tres serre pour le palm-muting rapide de Malakian
    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -46.0, "Decay": 0.18})

    # Swedish Chainsaw = Boss HM-2 : son chainsaw de Malakian
    # Drive et basses un peu moins que Nickelback pour garder la lisibilite en Drop C
    pb.add_block("HD2_DistSwedishChainsaw", slot=1,
                 overrides={"Drive": 0.90, "Bass": 0.75, "Treble": 0.75,
                            "Level": 0.50})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.52, "Modulation": 0.10, "Mix": 0.10})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2],
                    params={1: {"Level": 0.55}},
                    color="red")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2],
                    params={1: {"Drive": 0.80, "Bass": 0.65, "Level": 0.58}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_travel_the_world():
    """Superbus - Travel The World (120 BPM) — Patrice Focone

    Son : Fender Telecaster → clean a crunch leger → pop-rock.
    Chorus CE-1 pour le bridge, delay pour la profondeur.

    Chaine : Gate > CompulsiveDrive > Chorus70s > Reverb
    Slots  :  0      1                  2           3

    Snap 0 Verse  : clean leger + reverb
    Snap 1 Chorus : OD + reverb
    Snap 2 Bridge : OD + CE-1 chorus + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Travel The World", tempo=120.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    pb.add_block("HD2_DistCompulsiveDrive", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.58, "Level": 0.52})

    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.45, "VibratoRate": 0.38,
                            "VibratoDepth": 0.38, "Mix": 0.40, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.18, "Mix": 0.20})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3],
                    color="orange")

    pb.add_snapshot(2, "Bridge", blocks_on=[0, 1, 2, 3],
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_lithium():
    """Nirvana - Lithium (124 BPM) — Kurt Cobain

    Son : Fender Mustang 1969 → EHX Big Muff Pi → Fender Bassman (Butch Vig, Nevermind).
    Verse : quasi-clean + EHX Small Clone discret (Chorus70s = approx. Small Clone).
    Chorus : Big Muff plein, pas de modulation — explosion dynamique quiet/loud.

    Chaine : Gate > RamsHead > Chorus70s > Reverb
    Slots  :  0      1          2            3

    Snap 0 Verse  : quasi-clean + Small Clone + reverb
    Snap 1 Chorus : Big Muff + reverb (drop distorsion)
    Snap 2 Clean  : accordage / attente
    """
    pb = PresetBuilder("Lithium", tempo=124.0, styles=["grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.30})

    # Bighorn Fuzz = EHX Big Muff Pi : confirme par Butch Vig pour Lithium
    # Big Muff → Fender Bassman = son sombre et epais → Tone bas (0.45)
    # enabled_default=False : verse quasi-clean par defaut
    pb.add_block("HD2_DistRamsHead", slot=1, enabled_default=False,
                 overrides={"Sustain": 0.80, "Tone": 0.45, "Level": 0.50})

    # 70s Chorus = approx. EHX Small Clone : chorus analogique du verse clean
    # Cobain : 5 exemplaires du Small Clone, utilise sur les parties clean Nevermind
    # enabled_default=False : uniquement sur Verse, bypasse sur Chorus distordu
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.45, "VibratoRate": 0.35,
                            "VibratoDepth": 0.35, "Mix": 0.40, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.20})

    # Verse : quasi-clean + Small Clone + reverb
    # Contraste volontaire avec le chorus — ne pas compenser le delta de volume
    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3], color="green")

    # Chorus : Big Muff plein, pas de modulation = drop dynamique quiet/loud
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_figure_it_out():
    """Royal Blood - Figure It Out (108 BPM) — Mike Kerr

    Instrument original : basse → signal splitté (chemin basse + chemin guitare/fuzz).
    Dans le groupe d'Eric, le bassiste joue les parties basse de Kerr.
    Eric reproduit uniquement le chemin "guitare" : Industrial Fuzz (EHX Bass Big Muff)
    simule l'ampli guitare du rig de Kerr. Pas de Boctaver necessaire.

    Chaine : Gate > IndustrialFuzz > Reverb > KinkyBoost
    Slots  :  0      1                2         3

    Snap 0 Riff  : fuzz plein (Intro/Verse/Chorus — son identique tout au long)
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Volume : Industrial Fuzz (Bass Big Muff) = deficit output structurel
    → KinkyBoost always-on compense, exclu du snap Clean.
    """
    pb = PresetBuilder("Figure It Out", tempo=108.0, styles=["hard_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.30})

    # Industrial Fuzz = EHX Bass Big Muff Pi : chemin "guitare" du rig de Kerr
    # Drive=0.85, Gate bas (0.15) : sustain long sans coupure gated
    pb.add_block("HD2_DistIndustrialFuzz", slot=1,
                 overrides={"Compress": 0.65, "Gate": 0.15, "Drive": 0.85,
                            "Stability": 0.75, "Oscillator": False, "Level": 0.90})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.50, "Modulation": 0.20, "Mix": 0.16})

    # KinkyBoost : compense le deficit d'output du Bass Big Muff
    pb.add_block("HD2_DistKinkyBoost", slot=3,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(1, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    return pb


def preset_fly_away():
    """Lenny Kravitz - Fly Away (80 BPM) — Craig Ross (live) / Kravitz (studio)

    Accordage : standard. Son simple : guitare branchee directement dans le Park head,
    pas de pedales sur le signal guitare (philosophie Kravitz : "guitar into amp, nothing in between").
    Le flanger entendu sur l'enregistrement est sur la BASSE, pas la guitare.
    La section bridge est une partie basse seule (pas de solo guitare).

    Park head (fabrique par Marshall, circuit Plexi/JTM45) = canal unique toujours crunch.
    OCD always-on simule le preamp Park : Gain=0.48 (moins sature que JCM800 Gain=0.72),
    LPHP=True pour le punch britannique.

    Chaine : Gate > CompulsiveDrive > Reverb
    Slots  :  0      1                 2

    Snap 0 Riff  : son unique tout au long (Intro/Verse/Chorus)
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente
    """
    pb = PresetBuilder("Fly Away", tempo=80.0, styles=["hard_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.30})

    # OCD always-on : simule le Park head (Plexi/JTM45) — canal unique crunch
    # Gain=0.48 : Plexi plus modere que JCM800, crunch rock sans haute saturation
    # LPHP=True (HP) : punch et attaque britannique
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.48, "Tone": 0.55, "LPHP": True, "Level": 0.72})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.18})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2], color="orange")

    pb.add_snapshot(1, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    return pb


PRESETS = {
    "Are You Gonna Go My Way - Lenny Kravitz": preset_are_you_gonna_go_my_way,
    "Beggin - Maneskin":                       preset_beggin,
    "Be Yourself - Audioslave":                preset_be_yourself,
    "Black Hole Sun - Soundgarden":            preset_black_hole_sun,
    "Creep - Radiohead":                       preset_creep,
    "Dani California - Red Hot Chili Peppers": preset_dani_california,
    "Drive - Incubus":                         preset_drive,
    "Even Flow - Pearl Jam":                   preset_even_flow,
    "Figure It Out - Royal Blood":             preset_figure_it_out,
    "Fly Away - Lenny Kravitz":                preset_fly_away,
    "How You Remind Me - Nickelback":          preset_how_you_remind_me,
    "Hysteria - Muse":                         preset_hysteria,
    "I Wanna Be Slave - Maneskin":             preset_i_wanna_be_your_slave,
    "Le Reste - Clara Luciani":                preset_le_reste,
    "No One Knows - QOTSA":                    preset_no_one_knows,
    "Nue - Clara Luciani":                     preset_nue,
    "Plug In Baby - Muse":                     preset_plug_in_baby,
    "Radio Song - Superbus":                   preset_radio_song,
    "Sex on Fire - Kings of Leon":             preset_sex_on_fire,
    "Toxicity - System of a Down":             preset_toxicity,
    "Lithium - Nirvana":                        preset_lithium,
    "Travel The World - Superbus":             preset_travel_the_world,
}
