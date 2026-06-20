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
            presets utilisant l'OCD), Gain=0.65, Level=0.80
            INCHANGE sur tous les snaps (Riff/Bridge/Solo) — caractere preserve.

    Solo : boost via Scream 808 (TS808) PLACE ENTRE Klon ET OCD (push classique
           TS->ampli). Le TS pousse l'OCD plus fort avec son EQ bosse haut-mids
           (~2-4 kHz) -> le lead ressort sans modifier les reglages OCD eux-memes.
           Drive=0.25 (push leger), Tone=0.55, Level=0.92.
           Approche "rationalisation volume" : on ne touche pas l'OCD, on
           ajoute un boost TS dedie au lead.

    Flanger uniquement sur Bridge (absent du morceau original sur Riff/Solo).

    Pas de delay : pas adapte au style de ce morceau (hard rock direct, riff sec).

    Chaine : Gate > Minotaur > Scream808 > CompulsiveDrive > GrayFlanger > Reverb
    Slots  :  0      1          2            3                  4             5

    Snap 0 Riff   : Klon + OCD + reverb (pas de flanger, TS off)
    Snap 1 Bridge : Klon + OCD + flanger (Mix=0.48) + reverb (TS off)
    Snap 2 Solo   : Klon + Scream808 (push) + OCD (inchange) + reverb
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

    # Scream 808 (Ibanez TS808) = boost solo place ENTRE Klon et OCD
    # (push TS classique vers l'ampli/dist suivante).
    # Gain=0.25 : push leger, peu de saturation propre ajoutee
    # Tone=0.55 : bosse mediums signature TS808 (~2-4 kHz, fait ressortir le lead)
    # Level=0.92 : pousse fort le signal qui rentre dans l'OCD = OCD reagit
    #              plus fort (saturation et volume perçus +) sans modifier
    #              les reglages OCD eux-memes
    # Active uniquement sur snap Solo (lead boost) — preserve la philosophie
    # "rationalisation" : OCD inchange sur tous les snaps.
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = simulation Gibson Skylark cranked
    # LPHP=True (High Peak) : output plus eleve, cohere avec autres presets OCD
    #   (LPHP=False sortait trop bas par rapport au Clean de reference)
    # Tone=0.35 : adouci pour donner du coffre et reduire les aigus agressifs
    # Gain=0.65 + push Klon = saturation prononcee qui "deborde" aux limites
    pb.add_block("HD2_DistCompulsiveDrive", slot=3,
                 overrides={"Gain": 0.65, "Tone": 0.35, "LPHP": True, "Level": 0.80})

    # Gray Flanger = approximation du tape flanging studio (Henry Hirsch)
    # Mix variable par snapshot : Riff=0.28 discret, Bridge=0.48 prononce (via params)
    pb.add_block("HD2_FlangerGrayFlanger", slot=4, enabled_default=False,
                 overrides={"Rate": 0.12, "Width": 0.70, "Regen": 0.45, "Mix": 0.28})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.16})

    # Riff : pas de flanger, pas de TS (Klon + OCD only)
    pb.add_snapshot(0, "AYG Riff", blocks_on=[0, 1, 3, 5], color="yellow")

    # Bridge : flanger active (Mix prononce), pas de TS
    pb.add_snapshot(1, "AYG Bridge", blocks_on=[0, 1, 3, 4, 5],
                    params={4: {"Mix": 0.48}},
                    color="blue")

    # Solo : Klon + Scream808 (push entre Klon et OCD) + OCD INCHANGE
    # Choix rationalisation : on n'augmente pas Gain/Level de l'OCD,
    # le TS pousse l'OCD pour faire ressortir le lead.
    pb.add_snapshot(2, "AYG Solo", blocks_on=[0, 1, 2, 3, 5],
                    color="red")

    pb.add_snapshot(3, "AYG Clean", blocks_on=[0, 5],
                    params={5: {"Mix": 0.10}},
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

    Snap 0 Verse  : OCD Gain=0.05 (presque clean, juste coloration tone OCD)
    Snap 1 Refrain: OCD Gain=0.15 (crunch tres leger)

    Note : iteration 3 sur la saturation Beggin' apres feedback live.
    Sur stem isole : verse=low(0.22), refrain=moderate.
    Historique : 0.18/0.24 (initial) -> 0.30/0.40 (trop sature)
                 -> 0.18/0.28 (encore trop) -> 0.05/0.15 (cette version).
    OCD Level=0.82 reste eleve pour preserver le volume (Gain bas
    n'altere pas le volume final, le Level commande le mix wet/dry).
    """
    pb = PresetBuilder("Beggin'", tempo=134.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.40})

    # Red Squeeze = Ross Compressor : squish funky, regularise l'attaque
    # Sensitivity 0.50 : compense la sortie elevee du Super Distortion d'Eric
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.50, "Mix": 1.0, "Level": 2.0})

    # OCD always-on : coloration tone OCD essentiellement (Gain tres bas)
    # LPHP=True (HP) : attaque percussive et seche, colle avec le Mesa Boogie tight
    # Gain=0.05 verse (default block), 0.15 refrain (override snap)
    # Level=0.88 : bump volume apres validation saturation (volume etait un peu bas)
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.05, "Tone": 0.60, "LPHP": True, "Level": 0.88})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.15})

    pb.add_snapshot(0, "BGN Verse", blocks_on=[0, 1, 2, 3], color="green")

    pb.add_snapshot(1, "BGN Refrain", blocks_on=[0, 1, 2, 3],
                    params={2: {"Gain": 0.15}},
                    color="orange")

    pb.add_snapshot(2, "BGN Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "BGN Clean", blocks_on=[0, 3],
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

    REFONTE rationalisation v2 : chaque pedale a une CONFIG FIXE,
    les snaps activent/desactivent les blocs (pas d'override Gain/Level).

    - Intro : Heir Apparent (Prince of Tone, Analogman = Bluesbreaker modded)
              Caractere British crunch leger = "JCM800 rolled back" (volume
              guitare baisse sur ampli sature en permanence). Pas l'OCD :
              caractere different demande pedale dediee.
    - Verse / Chorus / Solo : OCD avec config FIXE (= ex-config Verse).
              JCM800 cranked en regime nominal. Aucun override snap.
    - Solo : ajout Scream 808 (TS) entre... non, ici sans Klon en front,
              le TS est juste avant l'OCD. Meme principe qu'AYGGMW :
              TS pousse l'OCD pour faire ressortir le lead sans modifier OCD.

    Delay subtil sur Verse : "presque un delay leger en fond" entendu sur
    le stem guitare isole (early reflections studio probablement). Mix tres
    bas pour rester discret. Delay PLACE AVANT la Reverb (ordre standard :
    delay genere les echos, reverb enveloppe l'ensemble).

    Chaine : Gate > HeirApparent > Scream808 > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :  0      1              2            3                  4             5

    Snap 0 Intro  : Gate + Heir Apparent + Reverb (Mix=0.32, Decay=0.58 = ambiance large)
    Snap 1 Verse  : Gate + OCD + Delay subtle + Reverb
    Snap 2 Chorus : Gate + OCD + Reverb (= Verse sans delay)
    Snap 3 Solo   : Gate + TS (push) + OCD + Reverb (wah = pedale externe MC404)

    Configs fixes :
    - Heir Apparent : Gain=0.20, Tone=0.50, Level=0.85 (crunch leger British)
    - Scream 808   : Gain=0.25, Tone=0.55, Level=0.92 (meme qu'AYGGMW)
    - OCD          : Gain=0.22, Tone=0.55, LPHP=True, Level=0.80 (ex-Verse)
    """
    pb = PresetBuilder("Be Yourself", tempo=117.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.32})

    # Heir Apparent (Analogman Prince of Tone = Bluesbreaker modded)
    # Caractere British crunch leger = JCM800 rolled back de Morello en intro
    # Gain=0.20 : grain leger sans saturation prononcee
    # Tone=0.50 : neutre, laisse passer le caractere Bluesbreaker
    # Level=0.85 : compense pour atteindre la reference volume
    # Active uniquement sur snap Intro.
    pb.add_block("HD2_DistHeirApparent", slot=1, enabled_default=False,
                 overrides={"Gain": 0.20, "Tone": 0.50, "Level": 0.85})

    # Scream 808 (Ibanez TS808) = boost solo place avant l'OCD
    # MEME CONFIG qu'AYGGMW : push leger + bosse haut-mids = lead ressort
    # Active uniquement sur snap Solo.
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = simulation canal overdrive JCM800 en regime nominal
    # CONFIG FIXE = ex-config Verse (etait le centre de gravite du morceau)
    # Plus aucun override Gain/Level/Tone sur les snaps : le caractere
    # reste identique sur Verse/Chorus/Solo, c'est l'ajout du TS qui fait
    # le bump Solo.
    pb.add_block("HD2_DistCompulsiveDrive", slot=3, enabled_default=False,
                 overrides={"Gain": 0.22, "Tone": 0.55, "LPHP": True, "Level": 0.80})

    # Simple Delay : actif uniquement sur Verse (slap subtil "en fond")
    # 8eme note a 117 BPM = 256ms, Mix tres bas (0.12) pour rester subtle
    pb.add_block("HD2_DelaySimpleDelay", slot=4, enabled_default=False,
                 overrides={"Time": 0.26, "Feedback": 0.10, "Mix": 0.12,
                            "TempoSync1": False})

    # Reverb : default Mix=0.22 (Verse/Chorus/Solo), override Mix=0.32
    # + Decay=0.58 sur Intro pour ambiance large.
    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.25, "Mix": 0.22})

    # Intro : Heir Apparent (grain leger British) + Reverb large
    pb.add_snapshot(0, "BYS Intro", blocks_on=[0, 1, 5],
                    params={5: {"Mix": 0.32, "Decay": 0.58}},
                    color="green")

    # Verse : OCD (config fixe) + delay subtle
    pb.add_snapshot(1, "BYS Verse", blocks_on=[0, 3, 4, 5],
                    color="yellow")

    # Chorus : OCD seul (= Verse sans le delay)
    pb.add_snapshot(2, "BYS Chorus", blocks_on=[0, 3, 5],
                    color="orange")

    # Solo : TS pousse l'OCD (config OCD inchangee, lead ressort via le TS)
    # Wah = pedale externe (Cry Baby MC404 CAE d'Eric)
    pb.add_snapshot(3, "BYS Solo", blocks_on=[0, 2, 3, 5],
                    color="red")

    return pb


def preset_black_hole_sun():
    """Soundgarden - Black Hole Sun (105 BPM) — Kim Thayil

    Son signature : H&K Rotosphere emule le Leslie Model 16 de l'enregistrement.
    Rotary FAST sur le verse clean (Refrain : Rotary retire en live, trop present).
    Intro : arpeges clean Cornell. Slapback 80ms differencie le solo.

    REFONTE rationalisation v2 : chaque pedale a une CONFIG FIXE.

    - Intro : Heir Apparent (= Be Yourself Intro, meme config) — arpeges avec
              grain leger, Bluesbreaker modded. Remplace l'ancien OCD a Gain=0.06.
    - Verse : Rotary FAST + KinkyBoost (color, Drive=0.35) + Reverb. Clean colore.
    - Refrain : Big Muff seul (config fixe, Level monte pour autosuffisance).
                KinkyBoost retire du Refrain (etait un patch compensation output,
                resolu en montant directement le Level du Big Muff).
    - Solo : Big Muff (config fixe identique Refrain) + Scream 808 push +
             Slapback. Le TS pousse le Big Muff = lead ressort, meme principe
             qu'AYGGMW/Be Yourself.

    Chaine : Gate > HeirApparent > Scream808 > BigMuff > Rotary > KinkyBoost > Slapback > Reverb
    Slots  :  0      1              2           3         4        5             6          7

    Snap 0 Intro  : Gate + Heir Apparent + Reverb
    Snap 1 Verse  : Gate + Rotary FAST + KinkyBoost (color) + Reverb
    Snap 2 Refrain: Gate + Big Muff + Reverb
    Snap 3 Solo   : Gate + Scream808 (push) + Big Muff + Slapback + Reverb

    Configs fixes :
    - Heir Apparent : Gain=0.20, Tone=0.50, Level=0.85 (identique Be Yourself Intro)
    - Scream 808   : Gain=0.25, Tone=0.55, Level=0.92 (identique pattern projet)
    - Big Muff     : Sustain=0.80, Tone=0.55, Level=0.85 (Sustain repris de
                     Lithium ; Tone+Level remontes apres test live refrain BHS)
    - KinkyBoost   : Drive=0.35, Boost=True (color + bump volume Verse clean)
    """
    pb = PresetBuilder("Black Hole Sun", tempo=105.0, styles=["grunge"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Heir Apparent (Analogman Prince of Tone = Bluesbreaker modded)
    # Meme config que Be Yourself Intro — meme principe : arpeges + grain leger
    # Active uniquement sur snap Intro.
    pb.add_block("HD2_DistHeirApparent", slot=1, enabled_default=False,
                 overrides={"Gain": 0.20, "Tone": 0.50, "Level": 0.85})

    # Scream 808 (Ibanez TS808) = boost solo place avant le Big Muff
    # Pousse le Big Muff pour faire ressortir le lead, meme principe qu'AYGGMW.
    # Active uniquement sur snap Solo.
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # Bighorn Fuzz = Ram's Head Big Muff : distorsion epaisse pour refrain/solo
    # CONFIG FIXE : meme reglages sur Refrain et Solo. Le boost Solo passe par
    # le Scream 808 en push, pas par modification du Big Muff lui-meme.
    # Sustain=0.80 (repris de Lithium, valide en repet).
    # Tone=0.55 + Level=0.85 (test live BHS : refrain pas assez clair/fort
    # avec 0.45/0.78 — Tone remonte pour ouvrir le son, Level pour porter).
    pb.add_block("HD2_DistRamsHead", slot=3, enabled_default=False,
                 overrides={"Sustain": 0.80, "Tone": 0.55, "Level": 0.85})

    # Rotary Drum/Horn = Leslie 145 : simule le H&K Rotosphere de Kim Thayil
    # Speed=True (fast), Mix=0.85 — utilise uniquement sur Verse
    pb.add_block("HD2_MM4RotaryDrumHorn", slot=4, enabled_default=False,
                 overrides={"Speed": True, "Depth": 0.82, "Horn Depth": 0.88,
                            "Drive": 0.5, "Mix": 0.85, "Level": 4.0})

    # Kinky Boost = Xotic EP Booster : color + bump volume sur Verse clean
    # Drive=0.35 : harmoniques chaudes (rôle "color" — epaissit le clean)
    # Boost=True : +6 dB pour compenser le volume Verse (sans saturation)
    # Active uniquement sur snap Verse.
    pb.add_block("HD2_DistKinkyBoost", slot=5, enabled_default=False,
                 overrides={"Drive": 0.35, "Boost": True, "Bright": False})

    # Slapback 80ms : differencie le Solo du Refrain
    # Active uniquement sur Solo. Place avant la Reverb (ordre delay->reverb).
    pb.add_block("HD2_DelaySimpleDelay", slot=6, enabled_default=False,
                 overrides={"Time": 0.08, "Feedback": 0.0, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=7,
                 overrides={"Decay": 0.50, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.20, "Mix": 0.22})

    # Intro : arpeges Cornell, Heir Apparent grain leger + Reverb
    pb.add_snapshot(0, "BHS Intro", blocks_on=[0, 1, 7], color="yellow")

    # Verse : Rotary FAST + KinkyBoost (color Drive=0.35) + Reverb
    pb.add_snapshot(1, "BHS Verse", blocks_on=[0, 4, 5, 7], color="green")

    # Refrain : Big Muff seul (config fixe, Level autosuffisant)
    pb.add_snapshot(2, "BHS Refrain", blocks_on=[0, 3, 7], color="orange")

    # Solo : Scream 808 pousse Big Muff (config inchangee) + Slapback
    pb.add_snapshot(3, "BHS Solo", blocks_on=[0, 2, 3, 6, 7], color="red")

    return pb


def preset_creep():
    """Radiohead - Creep (93 BPM) — Jonny Greenwood

    Son : Fender Telecaster Plus → Marshall ShredMaster
    → Fender Eighty-Five clean (solid-state, tres scoop : Bass 11, Mid 1, Treble 11).
    Verse : tremolo lent et doux (style Voodoo Lab Tremolo, opto-style).
    Stabs : "gros coup" pousse, fort et sec (Klon push devant OCD).

    REFONTE rationalisation v2 : chaque pedale a une CONFIG FIXE.

    - Verse : Optical Trem (lent et doux) + KinkyBoost (color) + Reverb.
    - Stabs : Klon Minotaur (gros push) + OCD (config fixe). PAS de reverb = sec.
    - Chorus: OCD seul + Reverb.
    - Solo  : Scream 808 (push) + OCD + Reverb (formule standard projet, sans delay).

    OCD Gain=0.65 ici (= AYGGMW) car pas de boost always-on pour pousser :
    le Gain doit etre suffisant pour le caractere "grunge pousse" sur
    Chorus et Solo. Sur les Stabs c'est le Top Secret OD (active uniquement
    la) qui pousse l'OCD pour le "gros coup fort".

    Chaine : Gate > TopSecretOD > Scream808 > OCD > OptoTremolo > KinkyBoost > Reverb
    Slots  :  0      1             2           3     4             5             6

    Snap 0 Verse  : Gate + Opto Tremolo + KinkyBoost (color) + Reverb
    Snap 1 Stabs  : Gate (Th -40) + Top Secret OD (push) + OCD + KinkyBoost (+6 dB sortie)
                    sec (pas de reverb)
    Snap 2 Chorus : Gate + OCD + Reverb
    Snap 3 Solo   : Gate + Scream808 (push) + OCD + Reverb (pas de delay)

    Configs fixes :
    - Top Secret OD : Gain=0.80, Level=1.0 (DOD 250, OP-amp brut, gros push Stabs)
    - Scream 808    : Gain=0.25, Tone=0.55, Level=0.92 (identique pattern projet)
    - OCD           : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge pousse,
                      Tone baisse pour moins d'aigu, Level baisse vs 0.85 prec.)
    - Opto Tremolo  : Speed=4.4 Hz, Depth=0.65, VolSens=0.10, Mix=1.0 (valide repet)
    - KinkyBoost    : Drive=0.35, Boost=True (color Verse, idem BHS)
    """
    pb = PresetBuilder("Creep", tempo=93.0, styles=["grunge", "alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Top Secret OD = DOD Preamp/Overdrive 250 : OP-amp brut, agressif
    # = gros boost pour les Stabs (caractere "gros coup pousse fort").
    # Gain=0.80 : pousse fort l'OCD (saturation marquee + perception forte volume)
    # Level=1.0  : sortie max pour gros son live (test live : 0.92 trop faible)
    # Active uniquement sur Stabs.
    pb.add_block("HD2_DistTopSecretOD", slot=1, enabled_default=False,
                 overrides={"Gain": 0.80, "Level": 1.0})

    # Scream 808 (Ibanez TS808) = boost solo place avant l'OCD
    # Pousse l'OCD pour faire ressortir le lead — meme principe qu'AYGGMW/BHS.
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = simule canal sature pousse Marshall ShredMaster + scoop Eighty-Five
    # Gain=0.65 = "grunge bien pousse" (= AYGGMW).
    # Tone=0.40 : adouci (moins d'aigu — test live a montre que 0.50 trop brillant)
    # Level=0.80 : baisse vs 0.85 (test live = un poil trop fort vs ref AYGGMW)
    pb.add_block("HD2_DistCompulsiveDrive", slot=3, enabled_default=False,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Opto Tremolo (Legacy MM4) = approche Voodoo Lab Tremolo
    # Reglages valides en repet : Speed=4.4 Hz, Depth=65%, VolSens=10%
    pb.add_block("HD2_MM4OptoTremolo", slot=4, enabled_default=False,
                 overrides={"Speed": 4.4, "Depth": 0.65, "Shape": 0.0,
                            "VolSens": 0.10, "Mix": 1.0, "Level": 0.0})

    # KinkyBoost = Xotic EP Booster : config "color Verse" (idem BHS Verse)
    # Drive=0.35 (harmoniques chaudes) + Boost=True (+6 dB volume Verse clean)
    pb.add_block("HD2_DistKinkyBoost", slot=5, enabled_default=False,
                 overrides={"Drive": 0.35, "Boost": True, "Bright": False})

    pb.add_block("HD2_ReverbGanymede", slot=6,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.16})

    # Verse : Optical Trem (lent doux) + KinkyBoost (color) + Reverb
    pb.add_snapshot(0, "CRP Verse", blocks_on=[0, 4, 5, 6], color="green")

    # Stabs : Top Secret OD pousse OCD + KinkyBoost en sortie (+6 dB boost)
    # = "gros coup pousse" fort et sec
    # PAS de reverb : sec, attaque "mute" tres marquee
    # Gate Threshold override -40 dB : OCD + TopSecretOD pousse genere du bruit
    # de fond avec Threshold=-50 (calibre Verse clean). -40 dB coupe le bruit.
    pb.add_snapshot(1, "CRP Stabs", blocks_on=[0, 1, 3, 5],
                    params={0: {"Threshold": -40.0}},
                    color="orange")

    # Chorus : OCD seul + Reverb (sustain large)
    pb.add_snapshot(2, "CRP Chorus", blocks_on=[0, 3, 6], color="red")

    # Solo : Scream 808 pousse OCD + Reverb (formule standard projet)
    pb.add_snapshot(3, "CRP Solo", blocks_on=[0, 2, 3, 6], color="blue")

    return pb


def preset_dani_california():
    """RHCP - Dani California (97 BPM) — John Frusciante

    Son original : Fender Strat → Moog MF-101 LPF (verse lick) → Boss DS-2 Turbo
    (chorus/solo) → Marshall Major 200W bridge. Wah (solo) : pedale externe MC404 CAE.

    REFONTE rationalisation v2 : abandon du DS-2 (Deez One Mod) au profit de
    configs canoniques reutilisees dans d'autres presets.

    - Verse : son d'intro de Be Yourself = Heir Apparent (Bluesbreaker modded)
              = arpege + grain leger. Caractere different du clean pur historique
              mais plus de corps en live.
    - Lick  : meme son que Verse + AutoFilter (MF-101) toujours utilise.
    - Chorus: OCD config Creep (= grunge bien pousse, Gain=0.65, Tone=0.40, Level=0.80).
              Frusciante sur Dani Cal pousse fort le Marshall Major — l'OCD a ce
              caractere mieux que le DS-2 en repet.
    - Solo  : OCD identique + Scream 808 push (formule standard projet) + reverb.
              Wah externe MC404 (pas dans la chaine).

    Chaine : Gate > AutoFilter > HeirApparent > Scream808 > OCD > Reverb
    Slots  :  0      1            2              3            4     5

    Snap 0 Verse  : Gate + Heir Apparent + Reverb
    Snap 1 Lick   : Gate + AutoFilter + Heir Apparent + Reverb
    Snap 2 Chorus : Gate + OCD + Reverb
    Snap 3 Solo   : Gate + Scream808 (push) + OCD + Reverb (wah externe)

    Configs partagees (cf. shared_pedal_configs.md) :
    - Heir Apparent : Gain=0.20, Tone=0.50, Level=0.85 (idem Be Yourself Intro / BHS Intro)
    - OCD           : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (idem Creep)
    - Scream 808    : Gain=0.25, Tone=0.55, Level=0.92 (formule Solo standard)
    """
    pb = PresetBuilder("Dani California", tempo=97.0, styles=["funk_rock", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # Auto Filter = Moog MF-101 LPF (approximation live du Doepfer A-100 studio)
    # Mode BP (1) : valide par test (LP trop grave sur le lick)
    # Place devant les sat : voit le signal clean (envelope plus reactive)
    # Sens=0.475 (entre 0.55 trop ouvert et 0.40 teste trop ferme, retour live) :
    # milieu entre les deux pour doser le "wah" du lick
    pb.add_block("HD2_FilterAutoFilter", slot=1, enabled_default=False,
                 overrides={"Mode": 1, "FilterGain": 14.0, "FilterQ": 6.0,
                            "Sens": 0.475, "Attack": 0.01, "Decay": 0.30,
                            "Frequency": 200.0, "FreqDepth": 4500.0,
                            "Direction": True, "Mix": 1.0, "Level": 0.0})

    # Heir Apparent (Analogman Prince of Tone = Bluesbreaker modded)
    # CONFIG CANONIQUE "arpege + grain leger" — partagee avec Be Yourself
    # Intro et BHS Intro.
    pb.add_block("HD2_DistHeirApparent", slot=2, enabled_default=False,
                 overrides={"Gain": 0.20, "Tone": 0.50, "Level": 0.85})

    # Scream 808 (Ibanez TS808) = formule Solo standard
    # Pousse l'OCD pour faire ressortir le lead, meme principe qu'AYGGMW/BHS/Creep.
    pb.add_block("HD2_DistScream808", slot=3, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = simule canal sature pousse (Marshall Major bridge en live)
    # CONFIG CANONIQUE "grunge bien pousse" — partagee avec Creep Chorus/Solo.
    pb.add_block("HD2_DistCompulsiveDrive", slot=4, enabled_default=False,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.16})

    # Verse : Heir Apparent + Reverb (son d'intro Be Yourself)
    pb.add_snapshot(0, "DAN Verse", blocks_on=[0, 2, 5], color="green")

    # Lick : AutoFilter dynamique + Heir Apparent + Reverb
    pb.add_snapshot(1, "DAN Lick", blocks_on=[0, 1, 2, 5], color="yellow")

    # Chorus : OCD + Reverb (grunge pousse)
    pb.add_snapshot(2, "DAN Chorus", blocks_on=[0, 4, 5], color="orange")

    # Solo : Scream 808 pousse OCD + Reverb (wah externe MC404 CAE)
    pb.add_snapshot(3, "DAN Solo", blocks_on=[0, 3, 4, 5], color="red")

    return pb


def preset_drive():
    """Incubus - Drive (91 BPM) — Mike Einziger

    Morceau majoritairement acoustique : Intro/Verse/Chorus joues a la guitare acoustique.
    Solo : guitare electrique (PRS McCarty) avec H&K Tube Rotosphere MkII (Leslie simulator),
    Boss PH-2 Super Phaser, overdrive leger germanium-style, delay sparse.

    Micro manche recommande pour le snap Acoustique (plus chaud, meilleur rendu sim).

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale). KinkyBoost remplace par un bloc "Gain" pur (HD2_VolPanGain) :
    le KinkyBoost (pedale modelisee) faisait depasser le budget DSP avec
    PolyPitch actif (cf. docs/pedal_guides/hx_models_reference.md section
    Poly Pitch) — le bloc Gain est un simple utilitaire volume, beaucoup
    plus leger, pour le meme role (gonfler le solo).

    Chaine : PolyPitch > Gate > AcousSim > Phaser > Rotosphere > Gain > Delay > Reverb
    Slots  :     0          1       2         3         4           5       6       7

    Snap 0 Acoustique : simulation acoustique + reverb ambiante (Intro/Verse/Chorus)
    Snap 1 Solo       : Phaser + Rotosphere FAST + Gain (+boost) + delay + reverb
    Snap 2 Clean      : accordage / attente
    Snap 3 Clean      : accordage / attente
    """
    pb = PresetBuilder("Drive", tempo=91.0, styles=["alt_rock"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Acoustic Sim : simulation caisse de resonance sur guitare electrique
    # Mode=1 (Medium body), micro manche recommande pour maximiser l'effet
    # Level en dB (range -60/+6) : 0.0 = unite
    pb.add_block("L6SPB_AcousGtrSim", slot=2, enabled_default=False,
                 overrides={"Mode": 1, "Body": 0.65, "Top": 0.55,
                            "Shimmer": 0.25, "Level": 0.0})

    # Deluxe Phaser = Boss PH-2 Super Phaser : sweep organique sur le solo
    # Mix=0.75 : bien present, contribue au caractere avec le Rotosphere
    pb.add_block("HD2_PhaserDeluxePhaser", slot=3, enabled_default=False,
                 overrides={"Rate": 0.6, "Depth": 0.82, "Feedback": 0.28,
                            "Stages": 4, "Mix": 0.75, "Level": 0.0})

    # Rotary Drum/Horn = H&K Tube Rotosphere MkII : signature du solo de Drive
    # Speed=True (fast) : rotation rapide, swirl present
    # Mix=0.88 : effet dominant
    pb.add_block("HD2_MM4RotaryDrumHorn", slot=4, enabled_default=False,
                 overrides={"Speed": True, "Depth": 0.85, "Horn Depth": 0.90,
                            "Drive": 0.3, "Mix": 0.88, "Level": 4.0})

    # Gain pur (utilitaire volume, pas une pedale modelisee) : gonfle le solo
    # +11 dB (remonte depuis 6 dB, retour test live)
    pb.add_block("HD2_VolPanGain", slot=5, enabled_default=False,
                 overrides={"Gain": 11.0})

    # Delay sparse : eco unique, profondeur sans surcharger le Rotosphere
    pb.add_block("HD2_DelaySimpleDelay", slot=6, enabled_default=False,
                 overrides={"Time": 0.40, "Feedback": 0.15, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=7,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.22})

    pb.add_snapshot(0, "DRV Acoustique", blocks_on=[1, 2, 7], color="green")

    # Solo : Phaser + Rotosphere (FAST) + Gain + delay + reverb
    pb.add_snapshot(1, "DRV Solo", blocks_on=[1, 3, 4, 5, 6, 7], color="red")

    pb.add_snapshot(2, "DRV Clean", blocks_on=[1, 7],
                    params={7: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "DRV Clean", blocks_on=[1, 7],
                    params={7: {"Mix": 0.10}},
                    color="white")

    return pb


def preset_even_flow():
    """Pearl Jam - Even Flow (103 BPM) — Mike McCready / Stone Gossard

    Accordage : Drop D (D A D G B E). Enregistrement un quart de ton plus bas.
    Son original : Fender Strat 1958 + Ibanez TS9 → Marshall JCM800 cranked.
    Le son ne change pas entre Verse/Chorus/Bridge — un seul snap principal.
    Wah (licks et solo) : pedale externe (MC404 CAE d'Eric).

    REFONTE rationalisation v2 : application du pattern canonique "Rock direct"
    (= AYGGMW) = Klon + OCD always-on en gain stacking.
    Iteration 2 : la version OCD seule "grunge bien pousse" manquait de corps,
    on rajoute le Klon en front pour gain stacking (mid-bump 700-800 Hz =
    chaleur sans aigus parasites, contrairement au TS9 d'origine).

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale) pour transposer rapidement si besoin en live.

    Chaine : PolyPitch > Gate > Minotaur > Scream808 > CompulsiveDrive > Reverb
    Slots  :     0          1       2          3            4              5

    Snap 0 Principal : Klon + OCD + reverb (Intro/Verse/Chorus/Bridge/Licks)
    Snap 1 Solo      : + Scream 808 push (formule Solo standard, identique AYGGMW)
    Snap 2 Clean     : accordage / attente
    Snap 3 Clean     : accordage / attente

    Note : Phase 90 + DD-3 (signature McCready) retires — Solo aligne sur la
    formule standard AYGGMW (Klon + TS push + OCD + reverb, rien d'autre).
    Wah externe MC404 CAE garde son role differenciant sur le snap Solo.

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Minotaur    : Gain=0.40, Tone=0.45, Level=0.86 (Klon push pattern "Rock direct")
    - OCD         : Gain=0.65, Tone=0.35, LPHP=True, Level=0.80 (pattern "Rock direct"
                    idem AYGGMW — Tone=0.35 plus adouci car Klon pousse en front)
    - Scream 808  : Gain=0.25, Tone=0.55, Level=0.92 (formule Solo standard)
    """
    pb = PresetBuilder("Even Flow", tempo=103.0, styles=["grunge"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -50.0, "Decay": 0.32})

    # Klon Minotaur always-on = front push pour gain stacking permanent
    # Mid-bump 700-800 Hz = corps + chaleur (pas d'aigus parasites comme TS9).
    # CONFIG CANONIQUE "Rock direct" partagee avec AYGGMW.
    pb.add_block("HD2_DistMinotaur", slot=2,
                 overrides={"Gain": 0.40, "Tone": 0.45, "Level": 0.86})

    # Scream 808 (Ibanez TS808) = formule Solo standard
    # Pousse l'OCD + Klon pour faire ressortir le lead.
    pb.add_block("HD2_DistScream808", slot=3, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Rock direct" — partagee avec AYGGMW
    # Tone=0.35 (vs 0.40 du grunge seul) : Klon pousse en front, on peut adoucir
    pb.add_block("HD2_DistCompulsiveDrive", slot=4,
                 overrides={"Gain": 0.65, "Tone": 0.35, "LPHP": True, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.20, "Mix": 0.18})

    # Principal : Klon + OCD always-on + Reverb (= Riff/Bridge AYGGMW)
    pb.add_snapshot(0, "EVF Principal", blocks_on=[1, 2, 4, 5], color="orange")

    # Solo : + Scream 808 push (= Solo AYGGMW, wah externe MC404 CAE)
    pb.add_snapshot(1, "EVF Solo", blocks_on=[1, 2, 3, 4, 5], color="red")

    pb.add_snapshot(2, "EVF Clean", blocks_on=[1, 5],
                    params={5: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "EVF Clean", blocks_on=[1, 5],
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

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale) pour transposer rapidement si besoin en live.

    Chaine : PolyPitch > Gate > HeavyDist > Chorus70s > Reverb > KinkyBoost
    Slots  :     0          1       2           3           4         5

    Snap 0 Verse  : clean brillant + KinkyBoost (Bright=True) + reverb (intro/verse/bridge)
    Snap 1 Chorus : Metal Zone — saturation metal massive
    Snap 2 Arpeges: clean + CE-1 vibrato + KinkyBoost + reverb
    Snap 3 Clean  : accordage / attente
    """
    pb = PresetBuilder("How You Remind Me", tempo=86.0, styles=["post_grunge"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Heavy Dist = CONFIG CANONIQUE "Heavy Dist Boss Metal Zone" — partagee Toxicity
    # enabled_default=False : uniquement sur Chorus
    pb.add_block("HD2_DM4HeavyDistortion", slot=2, enabled_default=False,
                 overrides={"Drive": 0.70, "Bass": 0.80, "Mid": 0.40,
                            "Treble": 0.55, "Output": 0.80})

    # 70s Chorus (CE-1) en mode Vibrato : ChorusIntensity=0 = vibrato pur (pas de chorus)
    # VibratoRate=0.60 (6), VibratoDepth=0.50 (5), Mix=0.50 (5)
    # enabled_default=False : uniquement sur Arpeges
    pb.add_block("HD2_Chorus70sChorus", slot=3, enabled_default=False,
                 overrides={"ChorusIntensity": 0.0, "VibratoRate": 0.60,
                            "VibratoDepth": 0.50, "Mix": 0.50, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.12})

    # KinkyBoost Bright=True : simule le caractere scintillant du Fender Super 60 rack
    # enabled_default=False : actif sur Verse + Arpeges, exclu Chorus et Clean
    pb.add_block("HD2_DistKinkyBoost", slot=5, enabled_default=False,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": True})

    # Verse/Intro : clean brillant + KinkyBoost (Bright=True) + reverb ouverte
    pb.add_snapshot(0, "HOW Verse", blocks_on=[1, 4, 5],
                    params={4: {"Mix": 0.20}},
                    color="green")

    # Chorus : Metal Zone seule = saturation metal massive
    pb.add_snapshot(1, "HOW Chorus", blocks_on=[1, 2, 4], color="red")

    # Arpeges : clean + CE-1 vibrato + reverb ouverte + KinkyBoost
    pb.add_snapshot(2, "HOW Arpeges", blocks_on=[1, 3, 4, 5],
                    params={4: {"Mix": 0.20}},
                    color="yellow")

    pb.add_snapshot(3, "HOW Clean", blocks_on=[1, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_hysteria():
    """Muse - Hysteria (93 BPM) — Matt Bellamy

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    Guitare studio : Gibson SG Standard (rouge, Absolution 2003).
    Ampli : Marshall JCM 2000 DSL 100 — Bellamy : "gain really low, volume on full"
    = saturation de power amp naturelle, caractere Marshall britannique.

    Hysteria est principalement une chanson de basse (Chris Wolstenholme).
    La guitare joue en soutien — le bassiste du groupe d'Eric couvre la ligne de basse.

    REFONTE rationalisation v2 : OCD aligne sur pattern canonique "Grunge bien
    pousse" (= Creep / Dani California / Even Flow), Solo via Scream 808 push
    (formule standard projet). KinkyBoost retire (pas dans le pattern).

    Chaine : Gate > Scream808 > CompulsiveDrive > DuckedDelay > Reverb
    Slots  :  0      1            2                 3             4

    Snap 0 Riff   : OCD + reverb
    Snap 1 Chorus : OCD + DuckedDelay subtle + reverb
    Snap 2 Solo   : Scream 808 push + OCD + DuckedDelay (ambiance lead) + reverb ample
    Snap 3 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD         : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808  : Gain=0.25, Tone=0.55, Level=0.92 (formule Solo standard)

    Notes :
    - On perd un peu la brillance "Marshall JCM2000 ouvert" (Tone=0.58 avant)
      au profit de la coherence inter-preset (Tone=0.40 grunge). A revoir si
      en repetition le caractere Muse n'est plus assez present.
    - DuckedDelay et Reverb gardent leurs overrides snap (ambiance space-rock
      lead) — ce sont des effets, pas des boost/sat (legitime).
    """
    pb = PresetBuilder("Hysteria", tempo=93.0, styles=["alt_rock", "hard_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.25})

    # Scream 808 (Ibanez TS808) = formule Solo standard
    # Pousse l'OCD pour faire ressortir le lead sans modifier OCD.
    pb.add_block("HD2_DistScream808", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/EvenFlow
    # JCM 2000 DSL canal Lead, gain bas + vol fort = ce caractere s'approche
    # du grunge pousse meme si historiquement Tone=0.58 (plus brillant).
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Ducked Delay : duck quand on joue (note seche et presente), remonte entre les phrases
    # LowCut=150Hz / HighCut=6000Hz : repeats plus chauds et moins envahissants
    # Defaults orientés Chorus (subtle) — overrides Solo ci-dessous
    # enabled_default=False : actif uniquement sur Chorus et Solo
    pb.add_block("HD2_DelayDuckedDelay", slot=3, enabled_default=False,
                 overrides={"Time": 0.16, "Feedback": 0.06, "LowCut": 150.0,
                            "HighCut": 6000.0, "Mix": 0.25, "Threshold": 0.45,
                            "Ducking": 0.75, "DynAttack": 0.02, "DynRel": 0.30,
                            "TempoSync1": False, "@trails": True})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.15, "Mix": 0.14,
                            "@trails": True})

    pb.add_snapshot(0, "HYS Riff", blocks_on=[0, 2, 4], color="orange")

    pb.add_snapshot(1, "HYS Chorus", blocks_on=[0, 2, 3, 4], color="red")

    # Solo : Scream 808 push + OCD (config fixe) + DuckedDelay long + Reverb ample
    pb.add_snapshot(2, "HYS Solo", blocks_on=[0, 1, 2, 3, 4],
                    params={3: {"Time": 0.32, "Feedback": 0.04, "Mix": 0.55},
                            4: {"Decay": 0.55, "Predelay": 0.05, "Mix": 0.28}},
                    color="yellow")

    pb.add_snapshot(3, "HYS Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_i_wanna_be_your_slave():
    """Maneskin - I Wanna Be Your Slave (131 BPM) — Thomas Raggi

    Accordage : standard (E A D G B E). Tonalite : Do# mineur (C#m).
    Guitare : Fender Telecaster / Stratocaster (single-coils). Ampli : Marshall 1987X Plexi.

    REFONTE rationalisation v2 : abandon du Klon always-on + OCD low-gain
    au profit du pattern canonique "grunge bien pousse" (= Creep/DaniCal/Hysteria).
    Chorus pousse via Scream 808 + Simple Delay (formule "TS push moment fort"
    appliquee a un Chorus dynamique, idem Solo standard).
    KinkyBoost retire (pas dans le pattern).

    Chaine : Gate > Scream808 > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :  0      1            2                 3             4

    Snap 0 Verse  : OCD + reverb (grunge bien pousse)
    Snap 1 Chorus : + Scream 808 push + Simple Delay subtle
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD         : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808  : Gain=0.25, Tone=0.55, Level=0.92 (formule push standard,
                    ici sur Chorus au lieu du Solo — meme principe "moment fort")
    """
    pb = PresetBuilder("I Wanna Be Slave", tempo=131.0, styles=["rock", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Scream 808 (Ibanez TS808) = formule "TS push moment fort"
    # Applique ici au Chorus (le moment dynamique du morceau) au lieu d'un Solo.
    # Meme principe et meme config qu'AYGGMW/Hysteria Solo.
    pb.add_block("HD2_DistScream808", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/Hysteria
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Simple Delay subtle pour le Chorus : ambiance, peu de feedback
    # Time=0.23s = croche a 131 BPM
    pb.add_block("HD2_DelaySimpleDelay", slot=3, enabled_default=False,
                 overrides={"Time": 0.23, "Feedback": 0.18, "Mix": 0.18,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.38, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.18, "Mix": 0.14})

    # Verse : OCD + Reverb (= Hysteria Riff)
    pb.add_snapshot(0, "IWB Verse", blocks_on=[0, 2, 4], color="yellow")

    # Chorus : + Scream 808 push + Simple Delay subtle
    pb.add_snapshot(1, "IWB Chorus", blocks_on=[0, 1, 2, 3, 4], color="orange")

    pb.add_snapshot(2, "IWB Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "IWB Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_killing_in_the_name():
    """RATM - Killing in the Name (85 BPM) — Tom Morello

    Accordage : Drop D (D A D G B E). Eric descend le Mi grave en Re physiquement.
    Studio : Fender Telecaster (neck pickup) → Marshall JCM800 50W canal overdrive.

    REFONTE rationalisation v2 : OCD aligne sur pattern canonique "Grunge bien
    pousse" (= Creep/DaniCal/Hysteria/IWBYS). Delay Solo retire.
    Reverb tres minimale : l'enregistrement studio est tres sec.

    Solo : Whammy +1 octave bindee a EXP 1 (Mission EP1-L6-BK port externe).
    Talon = unisson (0 semitone), pointe = +12 semitones (1 octave up).
    Effet "DJ scratching" caracteristique du solo de Morello.
    + Scream 808 push (formule "TS push moment fort" pour faire ressortir le lead).

    Chaine : Gate > Scream808 > CompulsiveDrive > PitchWham > Reverb
    Slots  :  0      1            2                 3            4

    Snap 0 Riff   : OCD + Reverb minimal
    Snap 1 Solo   : Scream 808 push + OCD + Whammy +1oct (EXP 1) + Reverb
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente

    KinkyBoost retire (pas dans le pattern "Grunge bien pousse").

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD         : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808  : Gain=0.25, Tone=0.55, Level=0.92 (TS push moment fort)
    """
    pb = PresetBuilder("Killing in the Name", tempo=85.0,
                       styles=["alt_metal", "funk_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Scream 808 (Ibanez TS808) = formule "TS push moment fort"
    # Pousse l'OCD pour faire ressortir le lead, en complement de la Whammy.
    pb.add_block("HD2_DistScream808", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/Hysteria/IWBYS
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Pitch Wham : Heel=0 (unisson), Toe=+12 (+1 octave) — solo seulement
    # Le param "Pedal" est bindee a EXP 1 (cf. bind_exp_pedal ci-dessous)
    pb.add_block("HD2_PitchPitchWham", slot=3, enabled_default=False,
                 overrides={"Heel": 0, "Toe": 12, "Mix": 1.0, "Level": 0.0})

    # Reverb minimale : "no reverb" sur l'enregistrement studio
    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.55, "Modulation": 0.10, "Mix": 0.08})

    # Bind du param "Pedal" du Pitch Wham (slot 3) a EXP 1
    # Valeur snapshot par defaut = 0.0 (talon = unisson, pas d'effet pitch)
    pb.bind_exp_pedal(slot=3, param_name="Pedal", exp_id=1, value=0.0)

    pb.add_snapshot(0, "KIN Riff", blocks_on=[0, 2, 4], color="orange")

    # Solo : Scream 808 push + Whammy +1 oct sur EXP 1 (signature Morello)
    pb.add_snapshot(1, "KIN Solo", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(2, "KIN Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "KIN Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_le_reste():
    """Clara Luciani - Le Reste (113 BPM) — Sage (Ambroise Willaume)

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    Micro recommande : micro milieu (single-coil) — plus proche du son Nile Rodgers.

    Son : Strat clean compressee, inspiration Nile Rodgers ("riffs de guitare funky a la Nile Rodgers").
    Red Squeeze (Dyna Comp) = compression snappy, attaque articulee.
    KinkyBoost Drive=1 : epaisseur harmonique chaude (EP Booster pousse) sur Verse funk.
    Pas de distorsion. Reverb discrete (guide Funk : Mix 0.08-0.15, adapte live).

    Chaine : Gate > RedSqueeze > KinkyBoost > Reverb
    Slots  :  0      1            2              3

    Snap 0 Verse : Strat compressee + KinkyBoost + reverb discrete (Mix=0.14)
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente
    """
    pb = PresetBuilder("Le Reste", tempo=113.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -54.0, "Decay": 0.40})

    # Red Squeeze = MXR Dyna Comp : compression Nile Rodgers
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.62, "Mix": 1.0, "Level": 8.5})

    # KinkyBoost = Xotic EP Booster : Drive=0.1 pour harmoniques chaudes + volume funk
    pb.add_block("HD2_DistKinkyBoost", slot=2,
                 overrides={"Drive": 0.1, "Boost": True, "Bright": False})

    # Reverb remontee (0.14 -> 0.22, retour test live) — aligne sur Nue (meme artiste/son)
    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.52, "Predelay": 0.02,
                            "Tone": 0.68, "Modulation": 0.12, "Mix": 0.22})

    pb.add_snapshot(0, "LER Verse", blocks_on=[0, 1, 2, 3], color="green")

    pb.add_snapshot(1, "LER Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "LER Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "LER Clean", blocks_on=[0, 3],
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

    pb.add_snapshot(0, "NOK Principal", blocks_on=[0, 1, 2, 3, 4], color="orange")

    # Solo : Drive monte + Level un peu plus haut, EQ conserve (caractere Josh Homme)
    pb.add_snapshot(1, "NOK Solo", blocks_on=[0, 1, 2, 3, 4],
                    params={1: {"Drive": 0.78, "Level": 0.80}},
                    color="red")

    pb.add_snapshot(2, "NOK Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "NOK Clean", blocks_on=[0, 3],
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
    pb.add_snapshot(0, "NUE Lick", blocks_on=[0, 1, 2, 3], color="yellow")

    pb.add_snapshot(1, "NUE Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "NUE Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "NUE Clean", blocks_on=[0, 3],
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
    pb.add_snapshot(0, "NAP Shimmer", blocks_on=[0, 4], color="cyan")

    # Snap 1 — B : FM4 Synth String + Ganymede ambient
    pb.add_snapshot(1, "NAP FM4Str", blocks_on=[0, 1, 3], color="yellow")

    # Snap 2 — C : String Theory + Ganymede ambient
    pb.add_snapshot(2, "NAP Theory", blocks_on=[0, 2, 3], color="orange")

    # Snap 3 — Combo : String Theory + Shimmer
    pb.add_snapshot(3, "NAP ThSh", blocks_on=[0, 2, 4], color="red")

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

    pb.add_snapshot(0, "PIB Riff", blocks_on=[0, 1, 2, 4, 5], color="orange")

    pb.add_snapshot(1, "PIB Chorus", blocks_on=[0, 1, 4, 5],
                    params={4: {"Decay": 0.50, "Mix": 0.22}},
                    color="red")

    # Arpeges : sans fuzz, sans KWB — phaser + CE-1 + reverb longue = texture synthé
    pb.add_snapshot(2, "PIB Arpeges", blocks_on=[0, 2, 3, 4],
                    params={4: {"Decay": 0.65, "Mix": 0.40}},
                    color="green")

    pb.add_snapshot(3, "PIB Clean", blocks_on=[0, 4],
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

    pb.add_snapshot(0, "RAD Verse", blocks_on=[0, 1, 3, 4], color="green")

    pb.add_snapshot(1, "RAD Chorus", blocks_on=[0, 1, 3, 4],
                    params={1: {"Gain": 0.38, "Level": 0.74}},
                    color="orange")

    # Lead : palm mutes cordes aigues 12e case
    pb.add_snapshot(2, "RAD Lead", blocks_on=[0, 1, 2, 3],
                    params={1: {"Gain": 0.52, "Level": 0.85}},
                    color="red")

    pb.add_snapshot(3, "RAD Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_sex_on_fire():
    """Kings of Leon - Sex on Fire (153 BPM) — Caleb + Matthew Followill

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am).
    2 guitaristes : Caleb (rythmique) + Matthew (lead, bends). Eric joue les deux.
    Guitare : Gibson ES-335 (humbuckers semi-creux). Ampli : Vox AC30 Top Boost (driven).

    REFONTE rationalisation v2 : OCD aligne sur pattern canonique "Grunge bien
    pousse" (= Creep/DaniCal/Hysteria/IWBYS/KITN). Chorus pousse via Scream 808
    (formule "TS push moment fort"). KinkyBoost retire (Regle 2).
    Reverb Mix corrige : 0.28 etait trop fort vs reference projet (0.14-0.16).

    Delay 8eme note (196ms) sur Chorus : epaissit les bends de Matthew Followill.

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale) pour transposer rapidement si besoin en live.

    Chaine : PolyPitch > Gate > Scream808 > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :     0          1       2            3                4              5

    Snap 0 Riff   : OCD + Reverb
    Snap 1 Chorus : Scream808 push + OCD + Delay bends + Reverb ouverte
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD        : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808 : Gain=0.25, Tone=0.55, Level=0.92 (TS push moment fort)
    """
    pb = PresetBuilder("Sex on Fire", tempo=153.0, styles=["indie_rock", "post_grunge"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Scream 808 = formule "TS push moment fort" : pousse l'OCD sur le Chorus
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/Hysteria/IWBYS/KITN
    pb.add_block("HD2_DistCompulsiveDrive", slot=3,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Simple Delay : 8eme note a 153 BPM = 196ms — epaissit les bends du Chorus
    pb.add_block("HD2_DelaySimpleDelay", slot=4, enabled_default=False,
                 overrides={"Time": 0.20, "Feedback": 0.08, "Mix": 0.22,
                            "TempoSync1": False})

    # Reverb Mix=0.16 (corrige depuis 0.28 — trop fort vs reference projet)
    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.55, "Predelay": 0.02,
                            "Tone": 0.65, "Modulation": 0.20, "Mix": 0.16})

    pb.add_snapshot(0, "SEX Riff", blocks_on=[1, 3, 5], color="green")

    # Chorus : TS push + OCD + delay bends + reverb ouverte
    pb.add_snapshot(1, "SEX Chorus", blocks_on=[1, 2, 3, 4, 5],
                    params={5: {"Decay": 0.65, "Mix": 0.28}},
                    color="orange")

    pb.add_snapshot(2, "SEX Clean", blocks_on=[1, 5],
                    params={5: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "SEX Clean", blocks_on=[1, 5],
                    params={5: {"Mix": 0.10}},
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
    pb.add_snapshot(0, "SG2 Verse", blocks_on=[0, 2], color="green")

    # Chorus "Woo-hoo!" : explosion RAT + KWB
    pb.add_snapshot(1, "SG2 Chorus", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(2, "SG2 Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "SG2 Clean", blocks_on=[0, 2],
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

    REFONTE : alignement complet sur How You Remind Me — seule la Heavy Dist
    assure la saturation, memes reglages exacts. EQ10Band et KinkyBoost retires
    (simplification + libere du budget DSP pour PolyPitch, cf.
    docs/pedal_guides/hx_models_reference.md section Poly Pitch).

    Pas de solo guitare dans Toxicity (pas de snap Solo).

    Chaine : PolyPitch > Gate > HeavyDist > Reverb
    Slots  :     0          1       2          3

    2 sons : Verse (clean) et Disto (chorus/riff/break).
    Verse clean : gate souple, reverb plus ouverte — "dirty amp volume rolled back" (simple).
    Disto : Heavy Dist (Boss Metal Zone Legacy) — memes reglages que How You Remind Me,
            valides a l'oreille (Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80).

    Snap 0 Verse : clean, gate souple, reverb ouverte (Mix=0.20)
    Snap 1 Disto : Metal Zone seule (chorus/riff/break)
    Snap 2 Clean : accordage Drop C
    Snap 3 Clean : accordage Drop C

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Heavy Dist : Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80
      (Heavy Dist Boss Metal Zone, identique How You Remind Me)
    """
    pb = PresetBuilder("Toxicity", tempo=115.0, styles=["nu_metal"])

    # Poly Pitch : Drop D → Drop C (-1 ton = -2 semitones), always-on tous snaps
    # AutoEQ=1.0 : compensation spectrale max du pitch shift
    # Tracking=3 : qualite polyphonique maximale (accords + power chords)
    pb.add_block("L6SPB_PolyPitch", slot=0,
                 overrides={"Interval": -2, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    # Footswitch 6 (constant entre presets) pour desactiver facilement en mode pedale
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -46.0, "Decay": 0.18})

    # Heavy Dist = CONFIG CANONIQUE "Heavy Dist Boss Metal Zone" — partagee How You Remind Me
    # Valide a l'oreille : massif et tight en Drop C
    # enabled_default=False : uniquement sur Disto
    pb.add_block("HD2_DM4HeavyDistortion", slot=2, enabled_default=False,
                 overrides={"Drive": 0.70, "Bass": 0.80, "Mid": 0.40,
                            "Treble": 0.55, "Output": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.30, "Predelay": 0.01,
                            "Tone": 0.52, "Modulation": 0.10, "Mix": 0.10})

    # Verse : clean basique, gate souple, reverb ouverte
    pb.add_snapshot(0, "TOX Verse", blocks_on=[0, 1, 3],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            3: {"Mix": 0.20}},
                    color="green")

    # Disto : Metal Zone seule — chorus, riff, break
    pb.add_snapshot(1, "TOX Disto", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(2, "TOX Clean", blocks_on=[0, 1, 3],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            3: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "TOX Clean", blocks_on=[0, 1, 3],
                    params={1: {"Threshold": -55.0, "Decay": 0.50},
                            3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_travel_the_world():
    """Superbus - Travel The World (120 BPM) — Patrice Focone

    Accordage : standard (E A D G B E). Tonalite : Si mineur (Bm).
    3 sons distincts, tous satures. Pas de clean utilise dans le morceau
    (snap Clean conserve pour accordage uniquement).

    REFONTE rationalisation v2 : OCD aligne sur pattern canonique "Grunge bien
    pousse" (= Creep/DaniCal/Hysteria/IWBYS/KITN/SEX). Lick et Bridge pousses
    via Scream 808 (formule "TS push moment fort") au lieu de monter le Gain/Level
    de l'OCD. KinkyBoost retire (Regle 2 — pas dans le pattern).

    Lick : bends/slides intro + transitions chorus->verse — TS push + delay/reverb
    pour la presence lead. Verse = son rythmique de base. Bridge = TS push (sans delay).

    Chaine : Gate > Scream808 > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :  0      1            2                 3              4

    Snap 0 Lick   : Scream808 push + OCD + Delay 8eme (250ms) + Reverb ouverte
    Snap 1 Verse  : OCD + Reverb
    Snap 2 Bridge : Scream808 push + OCD + Reverb
    Snap 3 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD        : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808 : Gain=0.25, Tone=0.55, Level=0.92 (TS push moment fort)
    """
    pb = PresetBuilder("Travel The World", tempo=120.0, styles=["pop_rock_fr", "funk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Scream 808 = formule "TS push moment fort" : pousse l'OCD sur Lick et Bridge
    pb.add_block("HD2_DistScream808", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/Hysteria/IWBYS/KITN/SEX
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # SimpleDelay : 8eme note a 120 BPM = 250ms — actif uniquement sur le Lick
    pb.add_block("HD2_DelaySimpleDelay", slot=3, enabled_default=False,
                 overrides={"Time": 0.25, "Feedback": 0.10, "Mix": 0.22,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.62, "Modulation": 0.18, "Mix": 0.18})

    # Lick : TS push + OCD + Delay + Reverb standard (alignee sur le reste du
    # morceau — pas de reverb "ouverte", ca reste un morceau rock direct)
    pb.add_snapshot(0, "TTW Lick", blocks_on=[0, 1, 2, 3, 4], color="red")

    # Verse : OCD seul (config fixe)
    pb.add_snapshot(1, "TTW Verse", blocks_on=[0, 2, 4], color="orange")

    # Bridge : TS push + OCD (sans delay)
    pb.add_snapshot(2, "TTW Bridge", blocks_on=[0, 1, 2, 4], color="yellow")

    pb.add_snapshot(3, "TTW Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_lithium():
    """Nirvana - Lithium (124 BPM) — Kurt Cobain

    Son : Fender Mustang 1969 → EHX Big Muff Pi → Fender Bassman (Butch Vig, Nevermind).
    Verse : quasi-clean + EHX Small Clone discret + compresseur (articulation des
    notes, "comme sur le CD"). Chorus : Big Muff plein, pas de modulation —
    explosion dynamique quiet/loud.

    Accordage : 1 ton plus bas que standard (comme l'enregistrement original),
    simule via PolyPitch (Interval=-2, AutoEQ=1.0) — meme pattern que Toxicity
    et The Man Who Sold the World. Always-on tous snaps (y compris Clean).

    Big Muff aligne sur la CONFIG CANONIQUE "Mur fuzz sombre Big Muff" (identique
    Black Hole Sun, y compris le Level) — l'objectif du projet est un minimum
    de variation de volume entre presets, donc plus de "variante Lithium"
    separee. Le contraste quiet/loud du morceau reste volontaire (pas de
    compensation de volume entre Verse et Chorus), mais le Chorus lui-meme
    sort desormais au meme niveau que les autres usages du pattern.

    Verse : boost via un bloc "Gain" pur (HD2_VolPanGain, +11 dB, ajuste en test
    live) au lieu d'un KinkyBoost — KinkyBoost (pedale modelisee) faisait
    depasser le budget DSP avec PolyPitch actif (cf.
    docs/pedal_guides/hx_models_reference.md section Poly Pitch). Confirme en
    test live : Gain leger + PolyPitch fonctionnent ensemble. Le bloc Gain est
    un simple utilitaire volume (pas de modelisation de circuit) — compromis :
    on garde le bump de volume mais pas les harmoniques chaudes de l'EP Booster.

    Chaine : PolyPitch > Gate > RedSqueeze > RamsHead > Chorus70s > Gain > Reverb
    Slots  :     0          1        2           3          4         5       6

    Snap 0 Verse  : quasi-clean + compresseur + Small Clone discret + Gain (+6dB) + reverb
    Snap 1 Chorus : Big Muff (config BHS) + reverb (drop distorsion)
    Snap 2 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Big Muff : Sustain=0.80, Tone=0.55, Level=0.85 (mur fuzz sombre Big Muff,
      identique Black Hole Sun — plus de variante separee pour Lithium)
    """
    pb = PresetBuilder("Lithium", tempo=124.0, styles=["grunge"])

    # Poly Pitch : 1 ton plus bas (-2 semitones), comme l'enregistrement original
    pb.add_block("L6SPB_PolyPitch", slot=0,
                 overrides={"Interval": -2, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    # Footswitch 6 (constant entre presets) pour desactiver facilement en mode pedale
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -50.0, "Decay": 0.30})

    # Red Squeeze : articulation des notes clean du Verse ("comme sur le CD")
    # enabled_default=False : uniquement sur Verse
    pb.add_block("HD2_CompressorRedSqueeze", slot=2, enabled_default=False,
                 overrides={"Sensitivity": 0.50, "Mix": 1.0, "Level": 2.0})

    # Bighorn Fuzz = EHX Big Muff Pi : confirme par Butch Vig pour Lithium
    # CONFIG CANONIQUE "Mur fuzz sombre Big Muff" — identique Black Hole Sun
    # (plus de variante separee : objectif minimum de variation de volume)
    # enabled_default=False : verse quasi-clean par defaut
    pb.add_block("HD2_DistRamsHead", slot=3, enabled_default=False,
                 overrides={"Sustain": 0.80, "Tone": 0.55, "Level": 0.85})

    # 70s Chorus = approx. EHX Small Clone : Mix remonte a 0.40 (retour test live)
    # enabled_default=False : uniquement sur Verse, bypasse sur Chorus distordu
    pb.add_block("HD2_Chorus70sChorus", slot=4, enabled_default=False,
                 overrides={"ChorusIntensity": 0.30, "VibratoRate": 0.35,
                            "VibratoDepth": 0.25, "Mix": 0.40, "Level": 1.0})

    # Gain pur (utilitaire volume, pas une pedale modelisee) : +11 dB sur le Verse
    # (remonte depuis 6 dB, retour test live)
    # enabled_default=False : uniquement sur Verse
    pb.add_block("HD2_VolPanGain", slot=5, enabled_default=False,
                 overrides={"Gain": 11.0})

    # Reverb reduite (Mix 0.20 -> 0.14, retour test live)
    pb.add_block("HD2_ReverbGanymede", slot=6,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.14})

    # Verse : quasi-clean + compresseur + Small Clone discret + Gain + reverb
    # Contraste volontaire avec le chorus — ne pas compenser le delta de volume
    pb.add_snapshot(0, "LIT Verse", blocks_on=[0, 1, 2, 4, 5, 6], color="green")

    # Chorus : Big Muff plein (config BHS) — drop dynamique quiet/loud
    pb.add_snapshot(1, "LIT Chorus", blocks_on=[0, 1, 3, 6], color="red")

    pb.add_snapshot(2, "LIT Clean", blocks_on=[0, 1, 6],
                    params={6: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "LIT Clean", blocks_on=[0, 1, 6],
                    params={6: {"Mix": 0.10}},
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

    pb.add_snapshot(0, "FIG Riff", blocks_on=[0, 1, 2, 3], color="red")

    pb.add_snapshot(1, "FIG Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(2, "FIG Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "FIG Clean", blocks_on=[0, 2],
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

    pb.add_snapshot(0, "FLY Riff", blocks_on=[0, 1, 2], color="orange")

    pb.add_snapshot(1, "FLY Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(2, "FLY Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="white")

    pb.add_snapshot(3, "FLY Clean", blocks_on=[0, 2],
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
    pb.add_snapshot(0, "CAL Arpege", blocks_on=[0, 2, 3], color="green")

    # Chorus : meme son (power chords mais pas satures)
    pb.add_snapshot(1, "CAL Chorus", blocks_on=[0, 2, 3], color="yellow")

    # Solo : OCD crunch + CE-1 + Reverb + KWB
    pb.add_snapshot(2, "CAL Solo", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(3, "CAL Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_im_picky():
    """Shaka Ponk - I'm Picky (117.5 BPM) — Cyril Roger "CC"

    Accordage : standard, capo case 4. Formes Em-D-G-D/C -> sonne Sol# mineur /
    Si majeur (confirme par analyse audio, confidence basse mais coherent).

    REFONTE : abandon du matching Mesa Rectifier/KWB au profit des patterns
    canoniques deja etablis (cf. docs/theory/shared_configs.md) — reutilisation
    directe du pattern "Rock direct" (AYGGMW) plutot qu'une config dediee.

    Snap renomme "Solo" (ex-"Chorus") : la tab notait "la rythmique est
    doublee" en studio sur Chorus/Solo/Outro — un seul guitariste en live ne
    peut pas reproduire ce doublage, on epaissit via le meme TS push qu'AYGGMW
    Solo.

    Chaine : Gate > Minotaur > Scream808 > CompulsiveDrive > Reverb
    Slots  :  0      1          2            3                 4

    Snap 0 Riff  : Klon + OCD (= AYGGMW Riff)
    Snap 1 Solo  : Klon + Scream808 push + OCD (= AYGGMW Solo)
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Minotaur    : Gain=0.40, Tone=0.45, Level=0.86 (Klon push pattern "Rock direct")
    - OCD         : Gain=0.65, Tone=0.35, LPHP=True, Level=0.80 (pattern "Rock direct")
    - Scream 808  : Gain=0.25, Tone=0.55, Level=0.92 (TS push moment fort)
    """
    pb = PresetBuilder("I'm Picky", tempo=117.5, styles=["alt_metal"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -48.0, "Decay": 0.22})

    # Klon Minotaur = CONFIG CANONIQUE "Rock direct" — partagee AYGGMW/Even Flow
    pb.add_block("HD2_DistMinotaur", slot=1,
                 overrides={"Gain": 0.40, "Tone": 0.45, "Level": 0.86})

    # Scream 808 = formule "TS push moment fort" : pousse l'OCD sur le Solo
    pb.add_block("HD2_DistScream808", slot=2, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Rock direct" — partagee AYGGMW/Even Flow
    pb.add_block("HD2_DistCompulsiveDrive", slot=3,
                 overrides={"Gain": 0.65, "Tone": 0.35, "LPHP": True, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.32, "Predelay": 0.02,
                            "Tone": 0.52, "Modulation": 0.10, "Mix": 0.10})

    # Riff : Klon + OCD always-on (= AYGGMW Riff)
    pb.add_snapshot(0, "PIK Riff", blocks_on=[0, 1, 3, 4], color="orange")

    # Solo : + Scream 808 push (= AYGGMW Solo)
    pb.add_snapshot(1, "PIK Solo", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(2, "PIK Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "PIK Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_just_a_girl():
    """No Doubt - Just a Girl (107.7 BPM) — Tom Dumont

    Accordage : standard (E A D G B E). Tonalite : Re majeur (D) — confirme
    Ultimate Guitar + analyse audio (score 0.89).

    Ampli : Divided By 13 RSA31 / Soldano SLO-100 (boutique high-headroom,
    crunch permanent, pas de canal clean). Analyse audio : saturation
    constante mais moderee ("high" 0.53-0.74) sur tout le morceau — la
    dynamique Verse/Chorus vient du jeu (palm mute vs strumming plein),
    pas d'un changement de pedale. Un seul son de base suffit donc pour
    tout le morceau hors solo.

    OCD aligne sur le pattern canonique "Grunge bien pousse" (le niveau de
    saturation mesure correspond a cette config existante, cf.
    docs/theory/shared_configs.md) — pas de nouveau pattern necessaire.

    Solo : formule "TS push moment fort" (Scream808) + Pebble Phaser
    (EHX Small Stone, specifique a ce titre selon la recherche gear)
    pour faire ressortir le solo du reste du morceau.

    Chaine : Gate > Scream808 > CompulsiveDrive > PebblePhaser > Reverb
    Slots  :  0      1            2                 3              4

    Snap 0 Riff  : OCD seul (grunge bien pousse) — couvre Intro/Verse/Chorus/Bridge
    Snap 1 Solo  : Scream808 push + OCD + Pebble Phaser
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD        : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    - Scream 808 : Gain=0.25, Tone=0.55, Level=0.92 (TS push moment fort)
    """
    pb = PresetBuilder("Just a Girl", tempo=107.7, styles=["ska_punk"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Scream 808 = formule "TS push moment fort" : pousse l'OCD sur le Solo
    pb.add_block("HD2_DistScream808", slot=1, enabled_default=False,
                 overrides={"Gain": 0.25, "Tone": 0.55, "Level": 0.92})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — niveau de saturation mesure
    # par l'analyse audio (0.53-0.74) correspond a ce pattern existant
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Pebble Phaser = EHX Small Stone : specifique au Solo (gear recherche pour ce titre)
    pb.add_block("HD2_PhaserPebblePhaser", slot=3, enabled_default=False,
                 overrides={"Rate": 0.30, "Color": False, "Spread": 0.0, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.14})

    # Riff : OCD seul — couvre tout le morceau hors solo (dynamique par le jeu)
    pb.add_snapshot(0, "JAG Riff", blocks_on=[0, 2, 4], color="orange")

    # Solo : TS push + OCD + Phaser
    pb.add_snapshot(1, "JAG Solo", blocks_on=[0, 1, 2, 3, 4], color="red")

    pb.add_snapshot(2, "JAG Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "JAG Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_no_roots():
    """Alice Merton - No Roots (117.5 BPM)

    Accordage : standard (E A D G B E). Tonalite : La mineur (Am, Dm, F, G).

    Le riff signature studio est une guitare octave-down (sonne comme une basse) —
    pas la partie qu'Eric reproduit ici. Dans l'arrangement du groupe d'Eric, le
    bassiste joue ce riff et Eric le double a la guitare, a hauteur normale, avec
    un son OD a grain/epaisseur. Variation de jeu : mini-strumming (8 allers-retours
    rapides) a intervalles reguliers — meme son, technique differente uniquement.
    Un seul snap actif, fidele a cette description (pas de changement de pedale).

    Pedale : Heir Apparent (Analogman Prince of Tone) = meme lignee Bluesbreaker
    que la Keeley 1962X reelle d'Eric (cf. docs/gear/eric_gear.md). Gain plus
    pousse que le pattern "Intro arpege + grain leger" existant (Gain=0.20) pour
    un caractere plus present adapte au doublage de riff.

    Chaine : Gate > HeirApparent > Reverb > KinkyBoost
    Slots  :  0      1              2         3

    Snap 0 Riff  : Heir Apparent — seul son actif, couvre tout le morceau
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente
    """
    pb = PresetBuilder("No Roots", tempo=117.5, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Heir Apparent (Analogman Prince of Tone = Keeley 1962X reelle d'Eric)
    # Gain plus pousse que le pattern "Intro arpege" pour du grain/epaisseur
    pb.add_block("HD2_DistHeirApparent", slot=1,
                 overrides={"Gain": 0.50, "Tone": 0.45, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=2,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.14})

    # KinkyBoost : calibration volume standard sur snap OD
    pb.add_block("HD2_DistKinkyBoost", slot=3,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": False})

    # Riff : seul son actif — couvre tout le morceau (riff doublé + mini-strumming)
    pb.add_snapshot(0, "NTR Riff", blocks_on=[0, 1, 2, 3], color="orange")

    pb.add_snapshot(1, "NTR Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "NTR Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "NTR Clean", blocks_on=[0, 2],
                    params={2: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_not_an_addict():
    """K's Choice - Not an Addict (86.1 BPM) — Sam & Gert Bettens

    Accordage : standard (E A D G B E). Tonalite : Mi majeur (E) — accords
    intro A-C#m-B-B (IV-vi-V-V) et chorus E-F#sus2-Asus2 (I-II-IV), diatoniques
    a Mi majeur.

    Piege tempo : analyse audio detecte 172.3 BPM mais le tempo reel est la
    moitie (86.1 BPM, alternative donnee par le pipeline) — confirme par
    l'estimation utilisateur (84).

    Pas de partie acoustique reproduite en live (decision Eric) — un seul son
    de guitare electrique sur tout le morceau. OCD aligne sur le pattern
    canonique "Grunge bien pousse" (cf. docs/theory/shared_configs.md).

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale) pour transposer rapidement si besoin en live.

    Chaine : PolyPitch > Gate > CompulsiveDrive > Reverb
    Slots  :     0          1       2               3

    Snap 0 Riff  : OCD — seul son actif, couvre tout le morceau
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    """
    pb = PresetBuilder("Not an Addict", tempo=86.1, styles=["alt_rock"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse"
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.14})

    # Riff : seul son actif — couvre tout le morceau
    pb.add_snapshot(0, "NAA Riff", blocks_on=[1, 2, 3], color="orange")

    pb.add_snapshot(1, "NAA Clean", blocks_on=[1, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "NAA Clean", blocks_on=[1, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "NAA Clean", blocks_on=[1, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_special_k():
    """Placebo - Special K (160 BPM) — Brian Molko

    Accordage : standard, capo case 1 (decision Eric — pas de retune complet
    ni de simulation PolyPitch). Tonalite : Do# majeur (C#) — confirme Wikipedia.

    Piege tempo : analyse audio detecte 80.7 BPM, alternative x2 = 161.5 BPM
    proche de l'estimation utilisateur (160) — tempo reel retenu = 160.

    Deux patterns canoniques existants reutilises (cf. docs/theory/shared_configs.md)
    plutot qu'une config dediee — l'analyse audio montre un son "bright"
    (high-mid boost, bas/bas-mids coupes) globalement modere (saturation
    0.28-0.43 sur la majorite du morceau, pic a 0.64 sur l'outro) qui
    correspond bien a ces deux paliers deja documentes :
    - Verse/Riff   : OD legere = pattern "Intro arpege + grain leger" (Heir Apparent)
    - Chorus/Outro : saturation plus poussee = pattern "Grunge bien pousse" (OCD)

    Poly Pitch utilitaire : -1/2 ton, desactive par defaut, footswitch 6
    (mode pedale) pour transposer rapidement si besoin en live — independant
    du capo case 1 (decision Eric pour l'accordage de base, pas de retune).

    Chaine : PolyPitch > Gate > HeirApparent > CompulsiveDrive > Reverb
    Slots  :     0          1       2              3                4

    Snap 0 Verse  : Heir Apparent (OD legere)
    Snap 1 Chorus : OCD (grunge bien pousse)
    Snap 2 Clean  : accordage / attente
    Snap 3 Clean  : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Heir Apparent : Gain=0.20, Tone=0.50, Level=0.85 (intro arpege + grain leger)
    - OCD           : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    """
    pb = PresetBuilder("Special K", tempo=160.0, styles=["alt_rock"])

    # Poly Pitch utilitaire : -1/2 ton, desactive par defaut (footswitch 6 en mode pedale)
    pb.add_block("L6SPB_PolyPitch", slot=0, enabled_default=False,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Heir Apparent = CONFIG CANONIQUE "Intro arpege + grain leger"
    pb.add_block("HD2_DistHeirApparent", slot=2, enabled_default=False,
                 overrides={"Gain": 0.20, "Tone": 0.50, "Level": 0.85})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse"
    pb.add_block("HD2_DistCompulsiveDrive", slot=3, enabled_default=False,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.40, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.15, "Mix": 0.14})

    pb.add_snapshot(0, "SPK Verse", blocks_on=[1, 2, 4], color="green")

    pb.add_snapshot(1, "SPK Chorus", blocks_on=[1, 3, 4], color="red")

    pb.add_snapshot(2, "SPK Clean", blocks_on=[1, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "SPK Clean", blocks_on=[1, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_take_me_out():
    """Franz Ferdinand - Take Me Out (104 BPM) — Alex Kapranos & Nick McCarthy

    Accordage : standard (E A D G B E). Tonalite : Mi mineur (E) — confirme
    sheet music officielle.

    2 guitares imbriquees a l'origine (Kapranos + McCarthy, "lean snarling
    dual guitar parts") — un seul guitariste dans le groupe d'Eric, fusion
    en une seule rythmique jouant le riff signature.

    Style de jeu funky (attaque percussive/syncopee, cf. retour Eric :
    "funk avec de l'overdrive par-dessus") + overdrive ("Overdriven Guitar"
    credite sur Songsterr). Analyse audio : pas de vraie rupture de
    saturation entre les sections (0.42-0.68 partout) -> un seul son actif.

    OCD aligne sur la CONFIG CANONIQUE "Grunge bien pousse" (au lieu d'une
    config dediee Tone brillant) — cf. docs/theory/shared_configs.md.

    Chaine : Gate > RedSqueeze > CompulsiveDrive > EQ10Band > Reverb
    Slots  :  0      1            2                  3            4

    Snap 0 Riff  : RedSqueeze (attaque funky) + OCD (grunge bien pousse) + EQ cut bas
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - OCD : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    """
    pb = PresetBuilder("Take Me Out", tempo=104.0, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Red Squeeze = attaque funky/percussive avant l'OD
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.50, "Mix": 1.0, "Level": 2.0})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — partagee Creep/DaniCal/etc.
    pb.add_block("HD2_DistCompulsiveDrive", slot=2,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # 10 Band Graphic : cut bas pour le caractere tight/mid-forward (vs analyse audio)
    pb.add_block("HD2_EQGraphic10Band", slot=3,
                 overrides={"250Hz": -4.0, "500Hz": -2.0, "2kHz": 1.5, "Level": 0.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.32, "Predelay": 0.02,
                            "Tone": 0.55, "Modulation": 0.12, "Mix": 0.12})

    # Riff : seul son actif — couvre tout le morceau
    pb.add_snapshot(0, "TMO Riff", blocks_on=[0, 1, 2, 3, 4], color="orange")

    pb.add_snapshot(1, "TMO Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "TMO Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "TMO Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_the_man_who_sold_the_world():
    """Nirvana - The Man Who Sold the World (117.5 BPM) — Kurt Cobain (cover Bowie)

    MTV Unplugged in New York (1994). Martin D-18E acoustique-electrique +
    Boss DS-2 (subtil sur l'intro/solo uniquement, pas le verse). Accordage
    demi-ton plus bas (Eb standard), tonalite reelle La (A). Pas de Small
    Clone : non audible sur ce titre a l'ecoute (retire malgre la mention
    generale Cobain/Unplugged dans la doc gear).

    3 sons distincts (retour ecoute Eric) :
    - Intro/Riff : motif repete 2-3 fois, acoustique + OCD "grunge bien pousse"
    - Verse : acoustique seule (config "Drive Acoustique", memes reglages)
    - Solo  : intro + delay (variation avec plus de sustain/mouvement)

    Pat Smear (2e guitare Unplugged, ligne de basse mobile au chorus) non
    reproduit — guitariste unique dans le groupe d'Eric, on joue uniquement
    la partie de Cobain (melodie + solo).

    Accordage simule via PolyPitch (Interval=-1 semitone, AutoEQ=1.0) —
    meme pattern que Toxicity (Drop D -> Drop C), ici standard -> Eb standard.

    Chaine : PolyPitch > Gate > AcousGtrSim > CompulsiveDrive > SimpleDelay > Reverb
    Slots  :     0          1        2              3               4           5

    Snap 0 Intro : Acoustique + OCD (grunge bien pousse) + reverb
    Snap 1 Verse : Acoustique seule (config "Drive Acoustique") — son folk pur
    Snap 2 Solo  : Intro + Delay (sustain/mouvement)
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - AcousGtrSim : Mode=1, Body=0.65, Top=0.55, Shimmer=0.25, Level=0.0
      (identique Drive — snap Acoustique)
    - OCD         : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    """
    pb = PresetBuilder("The Man Who Sold the World", tempo=117.5, styles=["grunge"])

    # Poly Pitch : standard -> Eb standard (-1 semitone), always-on tous snaps
    pb.add_block("L6SPB_PolyPitch", slot=0,
                 overrides={"Interval": -1, "Cents": 0.0, "AutoEQ": 1.0,
                            "Tracking": 3, "Mix": 1.0})
    # Footswitch 6 (constant entre presets) pour desactiver facilement en mode pedale
    pb.assign_footswitch(0, 6)

    pb.add_block("HD2_GateNoiseGate", slot=1,
                 overrides={"Threshold": -52.0, "Decay": 0.35})

    # Acoustic Sim : CONFIG CANONIQUE "Drive Acoustique" — partagee Drive
    pb.add_block("L6SPB_AcousGtrSim", slot=2,
                 overrides={"Mode": 1, "Body": 0.65, "Top": 0.55,
                            "Shimmer": 0.25, "Level": 0.0})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — actif Intro/Solo, absent du Verse
    pb.add_block("HD2_DistCompulsiveDrive", slot=3, enabled_default=False,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # Simple Delay : 8eme note a 117.5 BPM ~ 255ms — actif uniquement sur le Solo
    pb.add_block("HD2_DelaySimpleDelay", slot=4, enabled_default=False,
                 overrides={"Time": 0.25, "Feedback": 0.15, "Mix": 0.20,
                            "TempoSync1": False})

    pb.add_block("HD2_ReverbGanymede", slot=5,
                 overrides={"Decay": 0.45, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.20, "Mix": 0.18})

    # Intro/Riff : acoustique + OCD grunge bien pousse
    pb.add_snapshot(0, "TMW Intro", blocks_on=[0, 1, 2, 3, 5], color="orange")

    # Verse : acoustique seule (config "Drive Acoustique")
    pb.add_snapshot(1, "TMW Verse", blocks_on=[0, 1, 2, 5], color="green")

    # Solo : Intro + Delay (sustain/mouvement)
    pb.add_snapshot(2, "TMW Solo", blocks_on=[0, 1, 2, 3, 4, 5], color="red")

    pb.add_snapshot(3, "TMW Clean", blocks_on=[0, 1, 5],
                    params={5: {"Mix": 0.10}},
                    color="blue")

    return pb


def preset_time_is_running_out():
    """Muse - Time Is Running Out (117.5 BPM) — Matt Bellamy

    Accordage : standard (E A D G B E). Tonalite : La mineur (A).

    Le riff funky "wah" emblematique du verse vient de la BASSE (Chris
    Wolstenholme, Bass Synth Wah/envelope filter) — pas de la guitare, donc
    rien a reproduire cote guitare la-dessus (contexte groupe : le bassiste
    couvre deja ce hook).

    Structure jouee par Eric (arrangement interprete, ajustee apres test) :
    intro arpegee (grain leger + chorus) -> gros son sature garde jusqu'a la
    fin (chorus) -> pont en arpeges avec chorus (tremolo retire, pas necessaire).

    Pas de snap Verse distinct (retire — pas necessaire). Snap Clean ajoute
    a la place pour l'accordage.

    Chaine : Gate > HeirApparent > CompulsiveDrive > 70sChorus > Reverb
    Slots  :  0      1              2                  3            4

    Snap 0 Intro  : Heir Apparent (grain leger) + Chorus — crescendo
    Snap 1 Clean  : accordage / attente
    Snap 2 Chorus : OCD "grunge bien pousse" — gros son garde jusqu'a la fin
    Snap 3 Bridge : OCD + Chorus (meme effet que l'Intro) — arpeges

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - Heir Apparent : Gain=0.20, Tone=0.50, Level=0.85 (intro arpege + grain leger)
    - OCD           : Gain=0.65, Tone=0.40, LPHP=True, Level=0.80 (grunge bien pousse)
    """
    pb = PresetBuilder("Time Is Running Out", tempo=117.5, styles=["alt_rock"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -50.0, "Decay": 0.28})

    # Heir Apparent = CONFIG CANONIQUE "Intro arpege + grain leger" — actif Intro seulement
    pb.add_block("HD2_DistHeirApparent", slot=1, enabled_default=False,
                 overrides={"Gain": 0.20, "Tone": 0.50, "Level": 0.85})

    # OCD = CONFIG CANONIQUE "Grunge bien pousse" — actif Chorus/Bridge
    pb.add_block("HD2_DistCompulsiveDrive", slot=2, enabled_default=False,
                 overrides={"Gain": 0.65, "Tone": 0.40, "LPHP": True, "Level": 0.80})

    # 70s Chorus : Mix remonte (0.35 -> 0.50, "un peu plus de chorus") — Intro et Bridge
    pb.add_block("HD2_Chorus70sChorus", slot=3, enabled_default=False,
                 overrides={"ChorusIntensity": 0.40, "VibratoRate": 0.35,
                            "VibratoDepth": 0.30, "Mix": 0.50, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=4,
                 overrides={"Decay": 0.42, "Predelay": 0.02,
                            "Tone": 0.58, "Modulation": 0.18, "Mix": 0.16})

    # Intro : Heir Apparent (grain leger) + Chorus — crescendo
    pb.add_snapshot(0, "TRO Intro", blocks_on=[0, 1, 3, 4], color="green")

    pb.add_snapshot(1, "TRO Clean", blocks_on=[0, 4],
                    params={4: {"Mix": 0.10}},
                    color="blue")

    # Chorus : OCD grunge bien pousse (defaults) — gros son garde jusqu'a la fin
    pb.add_snapshot(2, "TRO Chorus", blocks_on=[0, 2, 4], color="orange")

    # Bridge : OCD + Chorus (meme effet que l'Intro, tremolo retire) — arpeges
    pb.add_snapshot(3, "TRO Bridge", blocks_on=[0, 2, 3, 4], color="red")

    return pb


def preset_locked_out_of_heaven():
    """Bruno Mars - Locked Out of Heaven (143.6 BPM)

    Accordage : standard (E A D G B E). Tonalite : Fa majeur (F).
    Capo 5 propose sur certaines tabs UG mais pas necessaire, jouable
    directement en Fa majeur.

    Guitare : Bruno Mars lui-meme (Fender Stratocaster), son clean. Influence
    explicite The Police ("You try to write a Police song!") — "skank" reggae
    (coups courts sur le contretemps) + chorus leger type Andy Summers,
    confirme par analyse audio (rate 0.6 Hz, depth 0.45, confiance forte).

    Saturation tres faible (0.18-0.20) sur la quasi-totalite du morceau
    (intro+chorus = 188s sur 233s) -> un seul son actif, pas de distorsion.

    KinkyBoost = CONFIG CANONIQUE "Clean brillant strumming" (identique How
    You Remind Me) : clean colore et scintillant, coherent avec le clean
    Stratocaster de Bruno Mars.

    Chaine : Gate > RedSqueeze > 70sChorus > Reverb > KinkyBoost
    Slots  :  0      1            2            3         4

    Snap 0 Riff  : RedSqueeze (comp skank) + 70s Chorus (leger) + KinkyBoost — seul son actif
    Snap 1 Clean : accordage / attente
    Snap 2 Clean : accordage / attente
    Snap 3 Clean : accordage / attente

    Configs partagees (cf. docs/theory/shared_configs.md) :
    - KinkyBoost : Drive=0.0, Boost=True, Bright=True (clean brillant strumming)
    """
    pb = PresetBuilder("Locked Out of Heaven", tempo=143.6, styles=["reggae_rock_pop"])

    pb.add_block("HD2_GateNoiseGate", slot=0,
                 overrides={"Threshold": -52.0, "Decay": 0.30})

    # Red Squeeze : compression pour l'attaque skank reggae
    # Level remonte 4.0 -> 8.5 (= Le Reste) : bridait le volume (retour test live)
    pb.add_block("HD2_CompressorRedSqueeze", slot=1,
                 overrides={"Sensitivity": 0.55, "Mix": 1.0, "Level": 8.5})

    # 70s Chorus : leger, confirme par analyse audio (rate 0.6 Hz, depth 0.45)
    pb.add_block("HD2_Chorus70sChorus", slot=2,
                 overrides={"ChorusIntensity": 0.45, "VibratoRate": 0.40,
                            "VibratoDepth": 0.30, "Mix": 0.35, "Level": 1.0})

    pb.add_block("HD2_ReverbGanymede", slot=3,
                 overrides={"Decay": 0.35, "Predelay": 0.02,
                            "Tone": 0.60, "Modulation": 0.12, "Mix": 0.12})

    # KinkyBoost = CONFIG CANONIQUE "Clean brillant strumming" — partagee How You Remind Me
    pb.add_block("HD2_DistKinkyBoost", slot=4,
                 overrides={"Drive": 0.0, "Boost": True, "Bright": True})

    # Riff : seul son actif — couvre tout le morceau
    pb.add_snapshot(0, "LOH Riff", blocks_on=[0, 1, 2, 3, 4], color="orange")

    pb.add_snapshot(1, "LOH Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(2, "LOH Clean", blocks_on=[0, 3],
                    params={3: {"Mix": 0.10}},
                    color="blue")

    pb.add_snapshot(3, "LOH Clean", blocks_on=[0, 3],
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
    "I'm Picky - Shaka Ponk":                  preset_im_picky,
    "Just a Girl - No Doubt":                  preset_just_a_girl,
    "No Roots - Alice Merton":                 preset_no_roots,
    "Not an Addict - K's Choice":               preset_not_an_addict,
    "Special K - Placebo":                      preset_special_k,
    "Take Me Out - Franz Ferdinand":             preset_take_me_out,
    "The Man Who Sold the World - Nirvana":      preset_the_man_who_sold_the_world,
    "Time Is Running Out - Muse":                preset_time_is_running_out,
    "Locked Out of Heaven - Bruno Mars":          preset_locked_out_of_heaven,
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
