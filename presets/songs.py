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

    Accordage : standard (E A D G B E). Tonalite : Mi mineur (Em)
    — confirme par analyse audio v3.2 (confidence 0.26).
    Craig Ross a joue TOUTES les parties (riff, rhythm, solo) — une seule prise.
    Guitare : Gibson Les Paul Goldtop 1953 (appartenant a Kravitz).
    Ampli : Gibson Skylark (petit combo tube annees 50) pousse a fond.
    Pas de pedale de distorsion — saturation naturelle de l'ampli uniquement.
    Flanger : tape flanging studio (Henry Hirsch). Discret sur le riff, prononce sur le bridge.
    Solo : court (~16s, valide par analyse audio : pic d'intensite a 2:33).

    Gain stacking : Klon (Minotaur) en push + OCD (CompulsiveDrive) en saturation.
    Le Klon en front pousse l'OCD plus fort -> saturation perçue plus forte
    sans monter le volume global. KinkyBoost retire (gain stacking le remplace,
    cf. regle calibration projet : KWB peut etre omis avec gain stacking).

    Klon : Gain=0.40, Level=0.86 (push transparent mid-heavy)
    OCD  : LPHP=True (High Peak — output plus eleve, coherent avec Beggin'/autres
            presets utilisant l'OCD), Gain=0.65, Level=0.80 (Riff/Bridge)
    Solo : OCD Gain=0.78, Level=0.82 (plus de push, sustain accru)

    Flanger uniquement sur Bridge (absent du morceau original sur Riff/Solo).

    Chaine : Gate > Minotaur > CompulsiveDrive > GrayFlanger > Reverb
    Slots  :  0      1          2                  3             4

    Snap 0 Riff   : Klon + OCD + reverb (pas de flanger)
    Snap 1 Bridge : Klon + OCD + flanger (Mix=0.48) + reverb
    Snap 2 Solo   : Klon + OCD (Gain=0.78, Level=0.90) + reverb
    Snap 3 Clean  : reverb seule (accordage, reference volume)
    """
    pb = PresetBuilder("AYGGMW", tempo=130.0, styles=["hard_rock", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Klon Minotaur = boost transparent mid-heavy en front (push pour l'OCD)
    # Tone=0.45 : adouci pour compenser le Super Distortion brillant
    # Level=0.86 : bump global pour atteindre le volume cible (tous snaps uniformement)
    pb.add_block("HD2_DistMinotaur", slot=1,
                 overrides={"Gain": 0.40, "Tone": 0.45, "Level": 0.86})

    # OCD = simulation Gibson Skylark cranked
    # LPHP=True (High Peak) : output plus eleve, cohere avec autres presets OCD
    #   (LPHP=False sortait trop bas par rapport au Clean de reference)
    # Tone=0.35 : adouci pour donner du coffre et reduire les aigus agressifs
    # Gain=0.65 + push Klon = saturation prononcee qui "deborde" aux limites
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.35, "LPHP": True, "Level": 0.80})

    # Gray Flanger = approximation du tape flanging studio (Henry Hirsch)
    # Mix variable par snapshot : Riff=0.28 discret, Bridge=0.48 prononce (via params)
    pb.add_block("HD2_FlangerGrayFlanger", slot=3, enabled_default=False,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.28})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.16})

    # Riff : pas de flanger (absent du morceau original sur cette section)
    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2, 4], color="yellow")

    # Bridge : flanger active (Mix prononce)
    pb.add_snapshot(1, "Bridge", blocks_on=[0, 1, 2, 3, 4],
                    params={3: {"Mix": 0.48}},
                    color="blue")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 4],
                    params={2: {"Gain": 0.78, "Level": 0.82}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
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

    Snap 0 Verse  : OCD Gain=0.30 (crunch leger funky, valide via analyse audio)
    Snap 1 Refrain: OCD Gain=0.40 (plus de corps, validation analyse audio sur stem)

    Note : l'analyse audio v3.2 a revele un crunch perceptible sur le stem
    guitare original (saturation 0.60). Gain remonte par rapport a la version
    initiale (0.18/0.24) qui sous-evaluait la saturation de Raggi.
    """
    pb = PresetBuilder("Beggin'", tempo=134.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.40})

    # Red Squeeze = Ross Compressor : squish funky, regularise l'attaque
    # Sensitivity 0.50 : compense la sortie elevee du Super Distortion d'Eric
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.50, "Mix": 1.0, "Level": 2.0})

    # OCD always-on : crunch funky leger (validé via analyse audio v3.2)
    # LPHP=True (HP) : attaque percussive et seche, colle avec le Mesa Boogie tight
    # Gain variable par snapshot
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.30, "Tone": 0.60, "LPHP": True, "Level": 0.77})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.15})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 2, 3], color="green")

    pb.add_snapshot(1, "Refrain", blocks_on=[0, 1, 2, 3],
                    params={2: {"Gain": 0.40}},
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

    Accordage : standard (E A D G B E).
    Capo : case 2 — Eric joue avec capo (chord shapes Am sonnent en Bm).
    Tonalite sonnante : Si mineur (Bm) — confirme analyse audio v3.2
    (confidence 0.36, score 0.94).

    JCM800 canal overdrive permanent — pas de pedale OD externe.
    OCD always-on simule ce canal gain. Gain variable par snapshot
    (simule le potentiometre de volume guitare qui nettoie le JCM800).

    Volume : Level different par snapshot pour compenser l'interaction
    Gain/volume de l'OCD — faible Gain = faible output naturel.
    Level eleve sur Intro/Verse pour atteindre la reference clean.
    Pas de KinkyBoost : Level par snap est le levier le plus direct.

    Delay subtil sur Verse : "presque un delay leger en fond" entendu sur
    le stem guitare isole (early reflections studio probablement). Mix tres
    bas pour rester discret.

    Chaine : Gate > CompulsiveDrive > SimpleDelay > Ganymede
    Slots  :  0       1                 2              3

    Snap 0 Intro  : Gain=0.01, Level=0.87, Tone=0.40 (quasi-clair, sat doucie)
    Snap 1 Verse  : Gain=0.22, Level=0.80 + delay subtle (crunch leger)
    Snap 2 Chorus : Gain=0.38, Level=0.75 (crunch present) — calibre live
    Snap 3 Solo   : Gain=0.55, Level=0.75 (lead, wah = pedale externe) — calibre live

    NB : LPHP=True uniformise sur tous snaps (convention projet).
    Tous Level baisses de 0.05 vs version precedente (preset etait trop fort
    par rapport a la reference AYGGMW Clean). Tone Intro baisse a 0.40
    (adouci, intro etait perçue trop saturee).
    """
    pb = PresetBuilder("Be Yourself", tempo=117.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.32})

    # CompulsiveDrive = OCD : simule canal overdrive permanent JCM800
    # Level variable par snapshot : compense l'output plus faible a faible Gain
    # Base = valeurs du Chorus (snap de reference inter-preset)
    # Level=0.75 (auparavant 0.80) : preset etait trop fort vs AYGGMW Clean (ref)
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.38, "Tone": 0.58, "LPHP": True, "Level": 0.75})

    # Simple Delay : actif uniquement sur Verse (slap subtil "en fond")
    # 8eme note a 117 BPM = 256ms, Mix tres bas (0.10) pour rester subtle
    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.26, "Feedback": 0.10, "Mix": 0.12,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.22})

    # Intro : Gain=0.01 (quasi-clair)
    # Level=0.87 : compense baisse Gain mais reduit (preset etait trop fort global)
    # Tone=0.40 : adouci (intro etait perçue trop saturee)
    # LPHP herite du default (True) — uniformisation projet
    pb.add_snapshot(0, "Intro", blocks_on=[0, 1, 3],
                    params={1: {"Gain": 0.01, "Tone": 0.40, "Level": 0.87},
                            3: {"Mix": 0.32, "Decay": 0.58}},
                    color="green")

    # Verse : delay actif (slap subtil), Level 0.80 (baisse vs 0.85 precedent)
    # LPHP herite du default (True) — uniformisation projet
    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.22, "Tone": 0.55, "Level": 0.80}},
                    color="yellow")

    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 3],
                    color="orange")

    # Wah = pedale externe (Cry Baby MC404 CAE d'Eric)
    # Level=0.75 (auparavant 0.80) : preset etait trop fort global
    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 3],
                    params={1: {"Gain": 0.55, "Tone": 0.60, "Level": 0.75}},
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
    # Gain=0.50 default (snap Intro override a 0.03 = quasi-clean)
    # Tone=0.40 : adouci (intro etait perçue trop saturee)
    # LPHP=True (High Peak) : output plus eleve, uniformisation projet
    # enabled_default=False : actif uniquement sur Intro
    pb.add_block("HD2_DistCompulsiveDrive", slot=6, enabled_default=False,
                 overrides={"Gain": 0.50, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Intro : Gain OCD remonte legerement (0.03 -> 0.06) suite test live
    # KinkyBoost retire de l'intro pour moins d'effet
    pb.add_snapshot(0, "Intro", blocks_on=[0, 3, 6],
                    params={6: {"Gain": 0.06}},
                    color="yellow")

    # Verse : KinkyBoost Drive=0.35 (override snap) pour epaissir le son
    # sans monter le volume (Drive ajoute des harmoniques chaudes)
    pb.add_snapshot(1, "Verse", blocks_on=[0, 2, 3, 4],
                    params={4: {"Drive": 0.35}},
                    color="green")

    # Refrain : retire le Rotary (effet trop present en live, demande utilisateur)
    # KinkyBoost (4) : compense le deficit d'output du Big Muff
    # Big Muff Level 0.65 (deja monte de 0.42), Tone 0.65 (de 0.45) — encore + clarte
    pb.add_snapshot(2, "Refrain", blocks_on=[0, 1, 3, 4],
                    params={1: {"Level": 0.65, "Tone": 0.65}},
                    color="orange")

    # Solo : Big Muff aligne sur le Refrain (Tone=0.65 pour coherence sonore)
    # + Sustain monte (0.85) et Level au-dessus du Refrain (0.72 vs 0.65)
    # = meme couleur que le Refrain mais plus de sustain et de presence (caractere solo)
    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 3, 4, 5],
                    params={1: {"Sustain": 0.85, "Tone": 0.65, "Level": 0.72}},
                    color="red")

    return pb


def preset_creep():
    """Radiohead - Creep (93 BPM) — Jonny Greenwood

    Son : Fender Telecaster Plus → Marshall ShredMaster (Vermin Dist)
    → Fender Eighty-Five clean (solid-state, tres scoop : Bass 11, Mid 1, Treble 11).
    Verse : Roland Dimension D (chorus large et transparent, mode SW4).
    Stabs : compresseur Dyna Comp + dist gain pousse = "gros coup" produit, fort.

    Chaine : Gate > VerminDist > Dimension > Reverb > RedSqueeze > KinkyBoost > SimpleDelay
    Slots  :  0      1            2            3        4             5            6

    Snap 0 Verse  : clean + Dimension D + reverb + KinkyBoost Drive (epaissi le son)
    Snap 1 Stabs  : dist gain pousse + compresseur (gros coup mute, sec et fort)
    Snap 2 Chorus : dist + reverb (plein sustain, G-B-C-Cm), Level monte
    Snap 3 Solo   : Chorus + SimpleDelay 300ms (continuite tremolo picking Greenwood)
                    Remplace le Clean (sacrifie pour avoir le solo essentiel du morceau)

    Volume : RAT a Level=0.95 (Chorus = ref). KinkyBoost Drive=0.35 sur Verse.
    Solo identifie via analyse audio (sections les plus intenses peak a 152-177s).
    """
    pb = PresetBuilder("Creep", tempo=93.0, styles=["grunge", "alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Vermin Dist = Pro Co RAT : plus proche du Marshall ShredMaster disponible
    # (meme architecture opamp, gain eleve, filtre passe-bas = ton mi-grave agressif)
    # Filter=0.38 : coupe les aigus pour renforcer les mids, caractere britannique
    # Level=0.88 : compromis (0.85 etait sous la ref, 0.95 etait trop fort)
    #              KinkyBoost reste actif sur Chorus pour compenser le deficit RAT
    # enabled_default=False : bypasse au chargement (verse clean par defaut)
    pb.add_block("HD2_DistVerminDist", slot=1, enabled_default=False,
                 overrides={"Gain": 0.75, "Filter": 0.38, "Level": 0.88})

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
    # enabled_default=False : active selectivement par snap
    pb.add_block("HD2_DistKinkyBoost", slot=5, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Simple Delay pour le solo : continuite du tremolo picking Greenwood
    # 300ms = entre 8eme et dotted 8th a 93 BPM, Feedback bas, Mix modere
    # enabled_default=False : actif uniquement sur snap Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=6, enabled_default=False,
                 overrides={"Time": 0.30, "Feedback": 0.15, "Mix": 0.22,
                            "TempoSync1": False})

    # Verse : KinkyBoost Drive=0.35 (override snap) pour epaissir le son
    # sans monter le volume (memes harmoniques chaudes que BHS Verse)
    pb.add_snapshot(0, "Verse", blocks_on=[0, 2, 3, 5],
                    params={5: {"Drive": 0.35}},
                    color="green")

    # Stabs : dist + KinkyBoost seul (pas de compresseur), Gain=0.85 + Level=1.0 via params
    pb.add_snapshot(1, "Stabs", blocks_on=[0, 1, 5],
                    params={1: {"Gain": 0.85, "Level": 1.0}},
                    color="orange")

    pb.add_snapshot(2, "Chorus", blocks_on=[0, 1, 3, 5], color="red")

    # Solo : Chorus + SimpleDelay 300ms pour continuite tremolo picking
    # Snap identifie via analyse audio (sections les plus intenses a 152-177s)
    # Remplace l'ancien snap Clean (sacrifie pour le solo essentiel du morceau)
    pb.add_snapshot(3, "Solo", blocks_on=[0, 1, 3, 5, 6], color="blue")

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

    Chorus : Heavy Dist seule (Boss Metal Zone Legacy) — suffisamment massive sans gain stacking.
    Reglages valides a l'oreille : Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80.

    Chaine : Gate > HeavyDist > Chorus70s > Reverb > KinkyBoost
    Slots  :  0       1           2           3         4

    Snap 0 Verse  : clean brillant + KinkyBoost (Bright=True) + reverb (intro/verse/bridge)
    Snap 1 Chorus : Metal Zone — saturation metal massive
    Snap 2 Arpeges: clean + CE-1 vibrato + KinkyBoost + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("How You Remind Me", tempo=86.0, styles=["post_grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Heavy Dist = Boss Metal Zone (Legacy DM4) : saturation metal massive validee
    # Reglages confirmes a l'oreille : Drive=0.85, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80
    # enabled_default=False : uniquement sur Chorus
    pb.add_block("HD2_DM4HeavyDistortion", slot=1, enabled_default=False,
                 overrides={"Drive": 0.70, "Bass": 0.80, "Mid": 0.40,
                            "Treble": 0.55, "Output": 0.80})

    # 70s Chorus (CE-1) en mode Vibrato : ChorusIntensity=0 = vibrato pur (pas de chorus)
    # VibratoRate=0.60 (6), VibratoDepth=0.50 (5), Mix=0.50 (5)
    # enabled_default=False : uniquement sur Arpeges
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.0, "VibratoRate": 0.60,
                            "VibratoDepth": 0.50, "Mix": 0.50, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.12})

    # KinkyBoost Bright=True : simule le caractere scintillant du Fender Super 60 rack
    # enabled_default=False : actif sur Verse + Arpeges, exclu Chorus et Clean
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": True})

    # Verse/Intro : clean brillant + KinkyBoost (Bright=True) + reverb ouverte
    pb.add_snapshot(0, "Verse", blocks_on=[0, 3, 4],
                    params={3: {"Mix": 0.20}},
                    color="green")

    # Chorus : Metal Zone seule = saturation metal massive
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3], color="red")

    # Arpeges : clean + CE-1 vibrato + reverb ouverte + KinkyBoost
    pb.add_snapshot(2, "Arpeges", blocks_on=[0, 2, 3, 4],
                    params={3: {"Mix": 0.20}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_hysteria():
    """Muse - Hysteria (93 BPM) — Matt Bellamy

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    Guitare studio : Gibson SG Standard (rouge, Absolution 2003).
    Ampli : Marshall JCM 2000 DSL 100 — Bellamy : "gain really low, volume on full"
    = saturation de power amp naturelle, caractere Marshall britannique.
    Note : Diezel VH4 = ere posterieure, pas sur Absolution.
    OCD = simulation JCM 2000 DSL (meme lignee que JCM800, canal Lead low-gain + vol fort).

    Hysteria est principalement une chanson de basse (Chris Wolstenholme).
    La guitare joue en soutien — le bassiste du groupe d'Eric couvre la ligne de basse.

    Chaine : Gate > CompulsiveDrive > DuckedDelay > Reverb > KinkyBoost
    Slots  :  0       1                 2             3         4

    Snap 0 Riff   : OCD + reverb (riff principal)
    Snap 1 Chorus : OCD + delay (subtle) + reverb
    Snap 2 Solo   : OCD gain monte + DuckedDelay (duck quand on joue, monte entre phrases) + reverb ample
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Hysteria", tempo=93.0, styles=["alt_rock", "hard_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.25})

    # Compulsive Drive = OCD : simule Marshall JCM 2000 DSL (canal Lead, gain bas + vol fort)
    # LPHP=True : punch britannique, attaque seche
    # Gain=0.68 = saturation power amp naturelle, pas de preamp extreme
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.68, "Tone": 0.58, "LPHP": True, "Level": 0.72})

    # Ducked Delay : duck quand on joue (note seche et presente), remonte entre les phrases
    # LowCut=150Hz / HighCut=6000Hz : repeats plus chauds et moins envahissants
    # Defaults orientés Chorus (subtle) — overrides Solo ci-dessous
    # enabled_default=False : actif uniquement sur Chorus et Solo
    pb.add_block("HD2_DelayDuckedDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.16, "Feedback": 0.06, "LowCut": 150.0,
                            "HighCut": 6000.0, "Mix": 0.25, "Threshold": 0.45,
                            "Ducking": 0.75, "DynAttack": 0.02, "DynRel": 0.30,
                            "TempoSync1": False, "@trails": True})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.15, "Mix": 0.14,
                            "@trails": True})

    # KinkyBoost : compense le volume OCD vs reference clean
    # enabled_default=False : exclu du snap Clean
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 3, 4], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 3, 4],
                    params={1: {"Gain": 0.78, "Level": 0.92},
                            2: {"Time": 0.32, "Feedback": 0.04, "Mix": 0.55},
                            3: {"Decay": 0.55, "Predelay": 0.05, "Mix": 0.28}},
                    color="yellow")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_i_wanna_be_your_slave():
    """Maneskin - I Wanna Be Your Slave (131 BPM) — Thomas Raggi

    Accordage : standard (E A D G B E). Tonalite : Do# mineur (C#m).
    Guitare : Fender Telecaster / Stratocaster (single-coils). Ampli : Marshall 1987X Plexi.

    Klon (Minotaur) + OCD (CompulsiveDrive) always-on : stack Klon→Plexi permanent.
    Fiche Raggi : Verse = Klon + OCD crunch / Chorus = Klon + OCD pousse.
    DS-1 (DeezOneVintage) toggle uniquement sur le solo.

    2 sons : Verse (crunch leger) et Chorus (OCD pousse).
    Pas de solo dans ce morceau.

    Chaine : Gate > Minotaur > CompulsiveDrive > Reverb > KinkyBoost
    Slots  :  0      1          2                  3         4

    Snap 0 Verse  : Klon + OCD crunch leger (Gain=0.38, Level=0.70)
    Snap 1 Chorus : Klon + OCD pousse (Gain=0.52, Level=0.90)
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("I Wanna Be Slave", tempo=131.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Minotaur = Klon Centaur : boost mid-heavy transparent, always-on
    pb.add_block("HD2_DistMinotaur", slot=1,
                 overrides={"Gain": 0.48, "Tone": 0.60, "Level": 0.55})

    # Compulsive Drive = OCD : always-on, Gain/Level varie par snap
    # Level=0.70 sur Verse = reference clean (valide a l'oreille)
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.38, "Tone": 0.58, "LPHP": True, "Level": 0.70})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.18, "Mix": 0.14})

    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 2, 3, 4], color="yellow")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3, 4],
                    params={2: {"Gain": 0.52, "Level": 0.90}},
                    color="orange")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_killing_in_the_name():
    """RATM - Killing in the Name (85 BPM) — Tom Morello

    Accordage : Drop D (D A D G B E). Eric descend le Mi grave en Re physiquement.
    Studio : Fender Telecaster (neck pickup) → Marshall JCM800 50W canal overdrive.

    JCM800 = canal sature permanent → OCD always-on (Gain=0.72, LPHP=True).
    Reverb tres minimale : l'enregistrement studio est tres sec.

    Solo : Whammy +2 octaves bindee a EXP 1 (Mission EP1-L6-BK port externe).
    Talon = unisson (0 semitone), pointe = +24 semitones (2 octaves up).
    Effet "DJ scratching" caracteristique du solo de Morello.

    Chaine : Gate > CompulsiveDrive > PitchWham > SimpleDelay > Reverb > KinkyBoost
    Slots  :  0      1                 2            3              4         5

    Snap 0 Riff   : OCD cranked + Reverb minimal + KWB (intro/verse/chorus/"Fuck you")
    Snap 1 Solo   : OCD + Whammy +2oct (EXP 1) + Delay 350ms + Reverb + KWB
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Killing in the Name", tempo=85.0,
                       styles=["alt_metal", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Compulsive Drive = JCM800 canal overdrive (haut gain permanent)
    # LPHP=True : punch britannique JCM800
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.72, "Tone": 0.55, "LPHP": True, "Level": 0.70})

    # Pitch Wham : Heel=0 (unisson), Toe=+24 (+2 octaves) — solo seulement
    # Le param "Pedal" est bindee a EXP 1 (cf. bind_exp_pedal ci-dessous)
    pb.add_block("HD2_PitchPitchWham", slot=2, enabled_default=False,
                 overrides={"Heel": 0, "Toe": 24, "Mix": 1.0, "Level": 0.0})

    # Simple Delay : ~350ms (entre 8eme et dotted 8th a 85 BPM) — solo seulement
    pb.add_block("HD2_DelaySimpleDelay", slot=3, enabled_default=False,
                 overrides={"Time": 0.35, "Feedback": 0.20, "Mix": 0.25,
                            "TempoSync1": False})

    # Reverb minimale : "no reverb" sur l'enregistrement studio
    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.55, "Modulation": 0.10, "Mix": 0.08})

    # KinkyBoost : compensation volume (regle calibration OCD)
    pb.add_block("HD2_DistKinkyBoost", slot=5,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Bind du param "Pedal" du Pitch Wham (slot 2) a EXP 1
    # Valeur snapshot par defaut = 0.0 (talon = unisson, pas d'effet pitch)
    pb.bind_exp_pedal(slot=2, param_name="Pedal", exp_id=1, value=0.0)

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 4, 5], color="orange")

    pb.add_snapshot(1, "Solo", blocks_on=[0, 1, 2, 3, 4, 5], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_le_reste():
    """Clara Luciani - Le Reste (113 BPM) — Sage (Ambroise Willaume)

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    Micro recommande : micro milieu (single-coil) — plus proche du son Nile Rodgers.

    Son : Strat clean compressee, inspiration Nile Rodgers ("riffs de guitare funky a la Nile Rodgers").
    Red Squeeze (Dyna Comp) = compression snappy, attaque articulee.
    CE-1 Chorus permanent (Verse + Chorus) : shimmer Nile Rodgers tout au long du morceau.
    Pas de distorsion. Reverb discrete (guide Funk : Mix 0.08-0.15, adapte live).

    Chaine : Gate > RedSqueeze > Chorus70s > Reverb
    Slots  :  0      1            2            3

    Snap 0 Verse  : Strat compressee + CE-1 chorus + reverb discrete (Mix=0.14)
    Snap 1 Chorus : meme son + reverb un peu plus ouverte (Mix=0.22)
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Le Reste", tempo=113.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Red Squeeze = MXR Dyna Comp : compression Nile Rodgers
    # Sensitivity moderee = attaque snappy sans ecraser les transitoires
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.62, "Mix": 1.0, "Level": 8.5})

    # 70s Chorus = CE-1 : shimmer discret permanent (Verse + Chorus)
    # Memes reglages que Nue pour coherence
    pb.add_block("HD2_Chorus70sChorus", slot=2,
                 overrides={"ChorusIntensity": 0.40, "VibratoRate": 0.35,
                            "VibratoDepth": 0.35, "Mix": 0.35, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.68, "Modulation": 0.12, "Mix": 0.14})

    # Double Tank (test) : plate reverb modulee style dream pop / Cigarette After Sex
    # Decay long (0.85), Mix substantiel (0.40), modulation audible = son qui dure
    # SANS shimmer/pitch-shift — juste une grosse reverb lush
    # enabled_default=False : actif uniquement sur snap "Verse+Amb"
    pb.add_block("HD2_ReverbDoubleTank", slot=4, enabled_default=False,
                 overrides={"Decay": 0.85, "Predelay": 0.04,
                            "Rate": 0.25, "Modulation": 0.50,
                            "Mix": 0.40, "Level": 0.0,
                            "LowCut": 200.0, "HighCut": 8000.0,
                            "@trails": True})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 2, 3], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3],
                    params={3: {"Mix": 0.22, "Decay": 0.60}},
                    color="yellow")

    # Test : Verse + Double Tank (reverb dream pop qui dure derriere le jeu)
    pb.add_snapshot(2, "Verse+Amb", blocks_on=[0, 1, 2, 3, 4], color="cyan")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_no_one_knows():
    """Queens of the Stone Age - No One Knows (171 BPM) — Josh Homme

    Accordage : C standard (C F Bb Eb G C) — baritone tuning.
    Guitare Eric : Lag Roxanne (Seymour Duncan humbuckers, micro chevalet)
                  — accordee en C standard, pas de pitch shift necessaire.

    Original : Epiphone Dot baritone → SD-1 (Level/Tone max, Drive min) → Ampeg V4B.
    Chez Homme la saturation venait de l'Ampeg V4B pousse + SD-1 = clean boost mid-heavy.

    Adaptation rig d'Eric (Mesa clean qui ne sature pas) : SD-1 Drive=0.65 fournit
    directement la saturation. Tone et Level restent eleves (philosophie Homme conservee
    pour le caractere mid-heavy/percutant).

    EQ 10-Band : boost mids 1 kHz (signature Josh Homme).
    Pas de reverb sur l'enregistrement studio, mix tres bas pour le live.

    2 sons : Principal (Riff/Verse/Chorus) et Solo (Drive monte).

    Chaine : Gate > StuporOD > EQ10Band > Reverb > KinkyBoost
    Slots  :  0      1          2           3         4

    Snap 0 Principal : SD-1 boost + EQ mids + Reverb minimal + KWB
    Snap 1 Solo      : SD-1 (Drive monte) + EQ + Reverb + KWB
    Snap 2 Clean     : accordage / attente
    Snap 3 Clean     : accordage / attente
    """
    pb = PresetBuilder("No One Knows", tempo=171.0, styles=["stoner_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Stupor OD = BOSS SD-1 : adapte au rig d'Eric (Mesa clean, pas d'Ampeg V4B sature)
    # Drive=0.65 (vs philo Homme Drive=0.18) : SD-1 fournit la saturation principale
    # car le Mesa clean ne sature pas (contrairement a la chaine originale Homme)
    pb.add_block("HD2_DistStuporOD", slot=1,
                 overrides={"Drive": 0.65, "Tone": 0.88, "Level": 0.70})

    # 10 Band Graphic = MXR/GE-7 EQ : boost mids signature Josh Homme
    pb.add_block("HD2_EQGraphic10Band", slot=2,
                 overrides={"500Hz": 3.0, "1kHz": 4.0, "2kHz": 2.0,
                            "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.55, "Modulation": 0.10, "Mix": 0.08})

    # KinkyBoost : compensation volume SD-1 vs reference clean (regle calibration)
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Principal", blocks_on=[0, 1, 2, 3, 4], color="orange")

    # Solo : Drive monte + Level un peu plus haut, EQ conserve (caractere Josh Homme)
    pb.add_snapshot(1, "Solo", blocks_on=[0, 1, 2, 3, 4],
                    params={1: {"Drive": 0.78, "Level": 0.80}},
                    color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_nue():
    """Clara Luciani - Nue (132 BPM) — Sage (Ambroise Willaume)

    Accordage : standard (E A D G B E). Tonalite : Do majeur (C).
    Micro recommande : micro milieu (single-coil) — style Nile Rodgers.

    Structure : la guitare ne joue que sur le chorus — lick funk simple
    (2 notes alternees sur 1 corde avec ghost notes). Verse = attente clean.
    CE-1 Chorus permanent sur le snap actif.

    Chaine : Gate > RedSqueeze > Chorus70s > Reverb
    Slots  :  0      1            2            3

    Snap 0 Lick  : lick funk chorus — Comp + CE-1 + Reverb
    Snap 1 Clean : accordage / attente (verse et reste)
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente
    """
    pb = PresetBuilder("Nue", tempo=132.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Red Squeeze = MXR Dyna Comp : compression Nile Rodgers
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.62, "Mix": 1.0, "Level": 6.0})

    # 70s Chorus = CE-1 : shimmer permanent sur le snap actif (lick chorus)
    pb.add_block("HD2_Chorus70sChorus", slot=2, enabled_default=False,
                 overrides={"ChorusIntensity": 0.40, "VibratoRate": 0.35,
                            "VibratoDepth": 0.35, "Mix": 0.35, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.68, "Modulation": 0.12, "Mix": 0.22})

    # Lick funk : seul snap actif — chorus, comp, reverb
    pb.add_snapshot(0, "Lick", blocks_on=[0, 1, 2, 3], color="yellow")

    pb.add_snapshot(1, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_nappes_test():
    """TEST - Nappes piano/synth (Nue ou autres)

    Preset de test pour comparer 4 approches de "nappes pad" qui remplacent
    le son de la guitare par un effet pur (Mix=1.0 sur les blocs synth/shimmer).

    Snap 0 : Shimmer pur — VIC_ReverbShimmer Mix=1.0, octave+quinte, decay tres long.
             Ambient ethere style U2/Sigur Ros.
    Snap 1 : Synth String FM4 — pad synth analogique style Roland Juno.
    Snap 2 : String Theory — pad lush "keys/strings", plus proche timbre clavier.
    Snap 3 : String Theory + Shimmer combine — pad clavier + ambient layer.

    Chaine : Gate > FM4SynthString > StringTheory > Ganymede > Shimmer
    Slots  :  0      1                 2              3          4

    Toutes les options ont Mix=1.0 sur le bloc principal pour effacer la guitare seche.
    """
    pb = PresetBuilder("Nappes Test", tempo=132.0, styles=["pop_rock_fr"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Synth String FM4 : convertit la guitare en pad strings synth analogique
    # Mix=1.0 = guitare seche effacee, on n'entend que le synth
    # Attack=0.7 = swell modere (pad qui monte progressivement)
    pb.add_block("HD2_FM4SynthString", slot=1, enabled_default=False,
                 overrides={"Speed": 0.69, "Freq": 0.89, "Attack": 0.70,
                            "Pitch": 0.0, "Mix": 1.0, "Level": 0.0})

    # String Theory : synth pad "lush keys" — plus proche d'un piano-pad
    # Wave=4 (sawtooth-ish), Filter=0.76 brillant, Attack=0.63 swell modere
    pb.add_block("SynthString", slot=2, enabled_default=False,
                 overrides={"Wave": 4, "Filter": 0.76, "Attack": 0.63,
                            "Mix": 1.0, "Level": 0.0})

    # Ganymede ambient : ajoute de l'espace derriere les pads (B et C)
    pb.add_block("HD2_ReverbGanymede", slot=3, enabled_default=False,
                 overrides={"Decay": 0.65, "Predelay": 0.03,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.35,
                            "@trails": True})

    # Shimmer reverb : LA reference pour pad ambient ethere
    # Shift1=+12 octave, Shift2=+7 quinte, Decay 15s, Mix=1.0 = pads purs
    pb.add_block("VIC_ReverbShimmer", slot=4, enabled_default=False,
                 overrides={"Mode": True, "Shift1": 12.0, "Shift2": 7.0,
                            "Intensity": 0.90, "Feedback": 0.90,
                            "Mix": 1.0, "Balance": 0.5,
                            "Decay": 15.0, "Predelay": 0.05,
                            "Damping": 5000.0, "Diffusion": 0.70,
                            "Motion": 0.30, "LowCut": 200.0, "HighCut": 8000.0,
                            "@trails": True})

    # Snap 0 — A : Shimmer pur (ambient ethere)
    pb.add_snapshot(0, "Shimmer", blocks_on=[0, 4], color="cyan")

    # Snap 1 — B : FM4 Synth String + Ganymede ambient
    pb.add_snapshot(1, "FM4Str", blocks_on=[0, 1, 3], color="yellow")

    # Snap 2 — C : String Theory + Ganymede ambient
    pb.add_snapshot(2, "Theory", blocks_on=[0, 2, 3], color="orange")

    # Snap 3 — Combo : String Theory + Shimmer
    pb.add_snapshot(3, "ThSh", blocks_on=[0, 2, 4], color="red")

    return pb


def preset_plug_in_baby():
    """Muse - Plug In Baby (136 BPM) — Matt Bellamy

    Son signature : Z.Vex Fuzz Factory (Industrial Fuzz) pour le riff.
    Fuzz gated et instable, tres agressif. Gate eleve pour effet saccade.

    Chaine : Gate > IndustrialFuzz > Reverb
    Slots  :  0      1                2

    Accordage : standard (E A D G B E). Tonalite : F# (Si mineur harmonique).
    Guitare : Manson DL-1 "Delorean" (aluminium, Fuzz Factory integree, P90 neck,
              Kent Armstrong Motherbucker bridge) — era Origin of Symmetry (2001).
    Ampli : Marshall JCM 2000 DSL 100.

    Industrial Fuzz = Z.Vex Fuzz Factory : fuzz avec instabilite et bruits parasites caracteristiques.
    Compress=0.35 / Gate=0.20 : interaction qui produit les bruits/squeals signature.
    Drive=1.0 (max) / Stability=0.15 : tres bas = instabilite prononcee, oscillations parasites.
    MXR Phase 90 = ScriptModPhase Rate=0.08 (sweep tres lent, presque imperceptible).

    Structure : Riff (intro/transitions/outro) — Chorus — Arpeges (verse, synthé original)
    Pas de solo, pas de tremolo.

    Chaine : Gate > IndustrialFuzz > ScriptModPhase > 70sChorus > Reverb > KinkyBoost
    Slots  :  0       1                  2                3           4         5

    Snap 0 Riff    : Fuzz + Phaser + Reverb + KWB
    Snap 1 Chorus  : Fuzz + Phaser + Reverb (plus ouverte) + KWB
    Snap 2 Arpeges : Phaser + CE-1 Chorus + Reverb longue (son synthé, sans fuzz)
    Snap 3 Clean   : accordage / attente
    """
    pb = PresetBuilder("Plug In Baby", tempo=136.0, styles=["alt_rock", "hard_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.20})

    # Industrial Fuzz = Z.Vex Fuzz Factory
    # Compress=0.35 / Gate=0.20 : interaction produit les bruits/squeals caracteristiques
    # Drive=1.0 (max) / Stability=0.15 : tres bas = instabilite et oscillations parasites
    pb.add_block("HD2_DistIndustrialFuzz", slot=1,
                 overrides={"Compress": 0.50, "Gate": 0.20, "Drive": 1.0,
                            "Stability": 0.08, "Oscillator": False, "Level": 0.76})

    # ScriptModPhase = MXR Phase 90 : sweep tres lent (presque imperceptible en jeu)
    pb.add_block("HD2_PhaserScriptModPhase", slot=2,
                 overrides={"Rate": 0.05, "Mix": 0.50})

    # 70s Chorus (CE-1) : actif uniquement sur Arpeges — texture synthé/pad
    # Mode chorus (pas vibrato) : Mix=0.65 = epaississement clavier sur arpeges claires
    pb.add_block("HD2_Chorus70sChorus", slot=3, enabled_default=False,
                 overrides={"ChorusIntensity": 0.60, "VibratoRate": 0.35,
                            "VibratoDepth": 0.45, "Mix": 0.65, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.15, "Mix": 0.16,
                            "@trails": True})

    # KinkyBoost : compense volume fuzz vs reference clean
    # Actif sur Riff et Chorus, exclu sur Arpeges (clean = reference) et Clean
    pb.add_block("HD2_DistKinkyBoost", slot=5,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 2, 4, 5], color="orange")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 4, 5],
                    params={4: {"Decay": 0.50, "Mix": 0.22}},
                    color="red")

    # Arpeges : sans fuzz, sans KWB — phaser + CE-1 + reverb longue = texture synthé
    pb.add_snapshot(2, "Arpeges", blocks_on=[0, 2, 3, 4],
                    params={4: {"Decay": 0.65, "Mix": 0.40}},
                    color="green")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_radio_song():
    """Superbus - Radio Song (158 BPM) — Patrice Focone

    Accordage : standard (E A D G B E).
    Son : Fender Telecaster → OD legere → pop-rock entrainent.
    Brillant et punchy, delay pour l'espace.

    Chaine : Gate > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :  0      1                  2              3

    Snap 0 Verse  : OD legere (Gain=0.28, Level=0.70) + reverb — reference clean
    Snap 1 Chorus : OD plus presente (Gain=0.38, Level=0.74) + reverb
    Snap 2 Lead   : OD (Gain=0.52, Level=0.85) + delay — palm mutes 12e case
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Radio Song", tempo=158.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # LPHP=True (High Peak) : output plus eleve, uniformisation projet
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.28, "Tone": 0.62, "LPHP": True, "Level": 0.70})

    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.19, "Feedback": 0.10, "Mix": 0.16,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.15, "Mix": 0.16})

    # KinkyBoost : Level=0.70 seul insuffisant — OCD seul (sans stacking) nécessite le boost
    # Actif sur Verse/Chorus/Lead, exclu Clean
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3, 4], color="green")

    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 3, 4],
                    params={1: {"Gain": 0.38, "Level": 0.74}},
                    color="orange")

    # Lead : palm mutes cordes aigues 12e case
    pb.add_snapshot(2, "Lead", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.52, "Level": 0.85}},
                    color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_sex_on_fire():
    """Kings of Leon - Sex on Fire (153 BPM) — Caleb + Matthew Followill

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    2 guitaristes : Caleb (rythmique) + Matthew (lead, bends). Eric joue les deux.
    Guitare : Gibson ES-335 (humbuckers semi-creux). Ampli : Vox AC30 Top Boost (driven).
    OCD = crunch principal. Delay 8eme note (196ms) sur Chorus pour faire crier les bends.

    Volumes calibres sur I Wanna Be Your Slave : OCD Level=0.72 sur Riff = reference clean.

    Chaine : Gate > CompulsiveDrive > SimpleDelay > Reverb > KinkyBoost
    Slots  :  0      1                 2               3         4

    Snap 0 Riff   : OCD crunch leger (Gain=0.42, Level=0.72) + Reverb + KWB
    Snap 1 Chorus : OCD plus chaud (Gain=0.58, Level=0.88) + Delay + Reverb ouverte + KWB
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Sex on Fire", tempo=153.0, styles=["indie_rock", "post_grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Compulsive Drive = Fulltone OCD : crunch AC30 Top Boost
    # Level=0.72 sur Riff = reference clean (calibre a l'oreille, meme methode que IWBYS)
    # LPHP=True (High Peak) : output plus eleve, uniformisation projet
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.42, "Tone": 0.55, "LPHP": True, "Level": 0.72})

    # Simple Delay : 8eme note a 153 BPM = 196ms — epaissit les bends du Chorus
    # Feedback tres bas = 1 repetition, Mix modere = delay present sans noyer
    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.20, "Feedback": 0.08, "Mix": 0.22,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.55, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.28})

    # KinkyBoost : compensation volume supplementaire (OCD + AC30 = son sous reference)
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    pb.add_snapshot(0, "Riff", blocks_on=[0, 1, 3, 4], color="green")

    # Chorus : OCD plus chaud + delay pour les bends + reverb plus ouverte
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.58, "Level": 0.88},
                            3: {"Decay": 0.65, "Mix": 0.35}},
                    color="orange")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_song_2():
    """Blur - Song 2 (130 BPM) — Graham Coxon

    Accordage : standard (E A D G B E). Tonalite : Fa (F).
    Guitare : Fender Telecaster '52 (single-coils). Ampli : Marshall.

    Dynamique signature quiet/loud — explosion clean->RAT distortion.
    Verse = clean direct sur l'ampli (pas d'OD), pas de KinkyBoost = contraste maximal.
    Chorus "Woo-hoo!" = ProCo RAT (Vermin Dist) cranked + KinkyBoost.

    Chaine : Gate > VerminDist > Reverb > KinkyBoost
    Slots  :  0      1            2          3

    Snap 0 Verse  : clean direct + reverb legere (intro/verse/pre-chorus)
    Snap 1 Chorus : RAT (Gain=0.75, Filter=0.55, Level=0.85) + reverb + KWB — explosion
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Song 2", tempo=130.0, styles=["alt_rock", "post_grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # Vermin Dist = ProCo RAT 2 : distorsion signature Coxon, son agressif middy
    # Level=0.85 + KinkyBoost = chorus violemment plus fort que verse (dynamique signature)
    pb.add_block("HD2_DistVerminDist", slot=1, enabled_default=False,
                 overrides={"Gain": 0.75, "Filter": 0.55, "Level": 0.85})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.16})

    # KinkyBoost : EXCLU du Verse = contraste explosif quiet/loud volontaire
    pb.add_block("HD2_DistKinkyBoost", slot=3, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Verse : CLEAN pur — contraste dynamique avec le Chorus (comme Lithium)
    pb.add_snapshot(0, "Verse", blocks_on=[0, 2], color="green")

    # Chorus "Woo-hoo!" : explosion RAT + KWB
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_toxicity():
    """System of a Down - Toxicity (115 BPM) — Daron Malakian

    Accordage : Drop C (C G C F A D).
    Eric est en Drop D physiquement — PolyPitch -2 semitones transpose tout d'un ton vers le bas.
    PolyPitch always-on sur TOUS les snaps (y compris Clean) : l'accordeur voit le Drop C.
    AutoEQ=1.0 : compensation spectrale max du pitch shift (basses en surplus, perte de clarte).

    Guitare : Ibanez Iceman DMM1 (humbuckers haute sortie).
    Ampli : Mesa/Boogie Dual Rectifier + Marshall JMP 2203.
    HM-2 = Swedish Chainsaw. MXR 10-Band EQ = 10 Band Graphic (simule l'EQ rack de Malakian
    + affine la compensation PolyPitch : cut 250Hz mud, boost 2kHz clarte).

    Pas de solo guitare dans Toxicity (pas de snap Solo).

    Chaine : PolyPitch > Gate > SwedishChainsaw > 10BandEQ > Reverb > KinkyBoost
    Slots  :     0          1         2                3           4         5

    2 sons : Verse (clean) et Disto (chorus/riff/break).
    Verse clean : gate souple, reverb plus ouverte — "dirty amp volume rolled back" (simple).
    Disto : Heavy Dist (Boss Metal Zone Legacy) — memes reglages que How You Remind Me,
            valides a l'oreille (Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80).

    Snap 0 Verse : clean, gate souple, reverb ouverte (Mix=0.20)
    Snap 1 Disto : Metal Zone + KWB (chorus/riff/break)
    Snap 2 Clean : accordage Drop C
    Snap 3 Clean : accordage Drop C
    """
    pb = PresetBuilder("Toxicity", tempo=115.0, styles=["nu_metal"])

    # Poly Pitch : Drop D → Drop C (-1 ton = -2 semitones), always-on tous snaps
    # AutoEQ=1.0 : compensation spectrale max du pitch shift
    # Tracking=3 : qualite polyphonique maximale (accords + power chords)
    pb.add_block("L6SPB_PolyPitch", slot=0,
                 overrides={"Interval": -2, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -46.0, "Decay": 0.18})

    # Heavy Dist = Boss Metal Zone (Legacy DM4) : memes reglages que How You Remind Me
    # Valides a l'oreille : massif et tight en Drop C
    # enabled_default=False : uniquement sur Disto
    pb.add_block("HD2_DM4HeavyDistortion", slot=2, enabled_default=False,
                 overrides={"Drive": 0.70, "Bass": 0.80, "Mid": 0.40,
                            "Treble": 0.55, "Output": 0.80})

    # 10 Band Graphic : compensation PolyPitch (250Hz mud -3dB, 2kHz clarte +2dB)
    # + simulation MXR 10-Band EQ de Malakian
    pb.add_block("HD2_EQGraphic10Band", slot=3,
                 overrides={"250Hz": -3.0, "2kHz": 2.0, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.52, "Modulation": 0.10, "Mix": 0.10})

    # KinkyBoost : compensation volume Metal Zone vs reference clean
    pb.add_block("HD2_DistKinkyBoost", slot=5,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Verse : clean basique, gate souple, reverb ouverte
    pb.add_snapshot(0, "Verse", blocks_on=[0, 1, 3, 4],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            4: {"Mix": 0.20}},
                    color="green")

    # Disto : Metal Zone + KWB — chorus, riff, break
    pb.add_snapshot(1, "Disto", blocks_on=[0, 1, 2, 3, 4, 5], color="red")

    pb.add_snapshot(2, "Clean", blocks_on=[0, 1, 3, 4],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            4: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 1, 3, 4],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_travel_the_world():
    """Superbus - Travel The World (120 BPM) — Patrice Focone

    Accordage : standard (E A D G B E). Tonalite : Si mineur (Bm).
    3 sons distincts, tous satures. Pas de clean utilise dans le morceau
    (snap Clean conserve pour accordage uniquement).

    Lick : bends/slides intro + transitions chorus->verse — necessite delay/reverb pour
    la presence lead. Verse et Chorus = meme son rythmique. Bridge = idem un peu plus fort.

    Chaine : Gate > CompulsiveDrive > SimpleDelay > Reverb > KinkyBoost
    Slots  :  0      1                 2               3         4

    Snap 0 Lick   : OCD + Delay 8eme (250ms) + Reverb ouverte + KWB
    Snap 1 Verse  : OCD rythmique (Gain=0.35, Level=0.70) + Reverb + KWB
    Snap 2 Bridge : OCD plus fort (Gain=0.42, Level=0.82) + Reverb + KWB
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Travel The World", tempo=120.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # OCD always-on : son sature de base pour tout le morceau (verse/chorus/bridge/lick)
    # Defaults = settings Verse (Gain=0.35, Level=0.70) — overrides Bridge/Lick par snap
    # LPHP=True (High Peak) : output plus eleve, uniformisation projet
    pb.add_block("HD2_DistCompulsiveDrive", slot=1,
                 overrides={"Gain": 0.35, "Tone": 0.60, "LPHP": True, "Level": 0.70})

    # SimpleDelay : 8eme note a 120 BPM = 250ms — actif uniquement sur le Lick
    pb.add_block("HD2_DelaySimpleDelay", slot=2, enabled_default=False,
                 overrides={"Time": 0.25, "Feedback": 0.10, "Mix": 0.22,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.18, "Mix": 0.18})

    # KinkyBoost : compensation volume OCD (Level=0.70 + KWB = reference clean)
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Lick : OCD + Delay + Reverb ouverte — bends/slides intro et transitions
    pb.add_snapshot(0, "Lick", blocks_on=[0, 1, 2, 3, 4],
                    params={1: {"Gain": 0.42, "Level": 0.78},
                            3: {"Mix": 0.28, "Decay": 0.55}},
                    color="red")

    # Verse : rythmique sature (defaults OCD)
    pb.add_snapshot(1, "Verse", blocks_on=[0, 1, 3, 4], color="orange")

    # Bridge : meme que Verse, OCD plus fort
    pb.add_snapshot(2, "Bridge", blocks_on=[0, 1, 3, 4],
                    params={1: {"Gain": 0.42, "Level": 0.82}},
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


def preset_californication():
    """Red Hot Chili Peppers - Californication (96 BPM) — John Frusciante

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    Studio : Gretsch White Falcon 1957 → Fender Showman (clean) + Marshall JTM-45 (lead)
    splittes en stereo par Boss CE-1 Chorus Ensemble. Live = adaptation mono.

    3 sons : Arpege (intro/verse), Chorus (idem son), Solo (crunch JTM-45).
    Style : arpege/strumming standard (pas funk malgre l'artiste).

    Chaine : Gate > CompulsiveDrive > Chorus70s > Reverb > KinkyBoost
    Slots  :  0      1                 2            3         4

    Snap 0 Arpege : Clean + CE-1 chorus discret + Reverb (arpeges Am-F intro/verse)
    Snap 1 Chorus : meme son que Arpege (chorus joue power chords mais reste clair)
    Snap 2 Solo   : OCD crunch (Plexi/JTM-45) + CE-1 + Reverb + KWB
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("Californication", tempo=96.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Compulsive Drive = OCD simule JTM-45 (Plexi britannique)
    # enabled_default=False : actif uniquement sur Solo (Verse/Chorus = clean)
    # LPHP=True : punch britannique, Gain modere pour crunch leger
    pb.add_block("HD2_DistCompulsiveDrive", slot=1, enabled_default=False,
                 overrides={"Gain": 0.32, "Tone": 0.58, "LPHP": True, "Level": 0.70})

    # 70s Chorus = CE-1 : simule le split stereo studio (Showman/JTM-45)
    # En mono, on garde un Mix discret pour le caractere shimmer
    pb.add_block("HD2_Chorus70sChorus", slot=2,
                 overrides={"ChorusIntensity": 0.40, "VibratoRate": 0.35,
                            "VibratoDepth": 0.35, "Mix": 0.18, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.15, "Mix": 0.16})

    # KinkyBoost : compensation volume OCD sur le snap Solo (regle calibration)
    pb.add_block("HD2_DistKinkyBoost", slot=4, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Arpege : clean + CE-1 + Reverb (intro et verse, arpeges Am-F)
    pb.add_snapshot(0, "Arpege", blocks_on=[0, 2, 3], color="green")

    # Chorus : meme son (power chords mais pas satures)
    pb.add_snapshot(1, "Chorus", blocks_on=[0, 2, 3], color="yellow")

    # Solo : OCD crunch + CE-1 + Reverb + KWB
    pb.add_snapshot(2, "Solo", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


PRESETS = {
    "Are You Gonna Go My Way - Lenny Kravitz": preset_are_you_gonna_go_my_way,
    "Beggin - Maneskin":                       preset_beggin,
    "Be Yourself - Audioslave":                preset_be_yourself,
    "Black Hole Sun - Soundgarden":            preset_black_hole_sun,
    "Californication - Red Hot Chili Peppers": preset_californication,
    "Creep - Radiohead":                       preset_creep,
    "Dani California - Red Hot Chili Peppers": preset_dani_california,
    "Drive - Incubus":                         preset_drive,
    "Even Flow - Pearl Jam":                   preset_even_flow,
    "Figure It Out - Royal Blood":             preset_figure_it_out,
    "Fly Away - Lenny Kravitz":                preset_fly_away,
    "How You Remind Me - Nickelback":          preset_how_you_remind_me,
    "Hysteria - Muse":                         preset_hysteria,
    "I Wanna Be Slave - Maneskin":             preset_i_wanna_be_your_slave,
    "Killing in the Name - RATM":              preset_killing_in_the_name,
    "Le Reste - Clara Luciani":                preset_le_reste,
    "No One Knows - QOTSA":                    preset_no_one_knows,
    "Nue - Clara Luciani":                     preset_nue,
    "Nappes Test":                             preset_nappes_test,
    "Plug In Baby - Muse":                     preset_plug_in_baby,
    "Radio Song - Superbus":                   preset_radio_song,
    "Sex on Fire - Kings of Leon":             preset_sex_on_fire,
    "Song 2 - Blur":                           preset_song_2,
    "Toxicity - System of a Down":             preset_toxicity,
    "Lithium - Nirvana":                        preset_lithium,
    "Travel The World - Superbus":             preset_travel_the_world,
}
