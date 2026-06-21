# OD / Distorsion / Fuzz — Guide des Paramètres

## Vocabulaire commun

| Terme | Signification |
|---|---|
| **Gain / Drive / Sustain** | Quantité de saturation du circuit |
| **Level / Volume / Output** | Volume de sortie de la pédale |
| **Tone / Filter / Treble** | Equalisation en sortie |
| **Soft clipping** | Écrêtage progressif, doux → OD |
| **Hard clipping** | Écrêtage brutal → Dist/Fuzz |
| **Gain monte → Level à baisser** | La saturation ajoute des harmoniques qui sonnent plus fort |

---

## Compulsive Drive = Fulltone OCD

**HX Effects model ID :** `HD2_DistCompulsiveDrive`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Saturation. 0.1–0.2 = crunch léger ; 0.4–0.5 = OD medium ; 0.7+ = saturation élevée |
| **Tone** | 0–1 | Treble. 0.4 = chaud/sombre ; 0.55 = neutre ; 0.7+ = brillant/mordant |
| **LPHP** | False/True | **LP (False)** = son plus chaud, plus "spongy", garde le bas ; **HP (True)** = plus de punch, caractère britannique |
| **Level** | 0–1 | Volume de sortie. Indépendant du Gain. |
| **Version** | False/True | V1 vs V2 du circuit (subtil) |

### Sweet spots
| Contexte | Gain | Tone | LPHP | Level | Notes |
|---|---|---|---|---|---|
| Clean boost | 0.04–0.06 | 0.55 | False | 0.52 | Grain imperceptible, juste du corps |
| Crunch léger | 0.15–0.22 | 0.55 | False | 0.52 | Pop-rock, funk-rock |
| OD medium | 0.30–0.40 | 0.58 | True | 0.50 | Rock classique |
| Crunch chaud | 0.38–0.45 | 0.52 | False | 0.50 | Blues, semi-hollowbody |
| Lead rock | 0.55–0.65 | 0.60 | True | 0.45 | Compenser : Gain monte, Level baisse |

**Piège :** LPHP=True donne plus de volume perçu → baisser Level de 0.03–0.05 par rapport à LP.

---

## Vermin Dist = Pro Co RAT

**HX Effects model ID :** `HD2_DistVerminDist`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Saturation. Le RAT couvre de l'OD au fuzz selon la valeur |
| **Filter** | 0–1 | **SENS INVERSÉ** : tourner vers 1 = MOINS de treble (filtre passe-bas) ; vers 0 = plus de brillance |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Gain | Filter | Level | Notes |
|---|---|---|---|---|
| OD medium | 0.45–0.55 | 0.50 | 0.52 | Son polyvalent |
| Rock british | 0.70–0.78 | 0.38 | 0.52 | Filter bas = mids prononcés (Marshall ShredMaster style) |
| Heavy | 0.85–0.95 | 0.55 | 0.48 | Quasi-fuzz, compenser Level |
| Rhythm serré | 0.60–0.70 | 0.62 | 0.50 | Plus de clarté grave, moins de basse |

**Piège critique :** Le Filter est **inversé**. Filter=0.38 ne veut pas dire "peu de filtre"
mais "filtre fortement coupé" → beaucoup moins de treble → plus de mids.
C'est précisément le réglage du son "Marshall ShredMaster" de Jonny Greenwood sur Creep.

---

## Scream 808 = Ibanez TS808 Tube Screamer

**HX Effects model ID :** `HD2_DistScream808`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Saturation. La TS a moins de gain max que la RAT ou l'OCD |
| **Tone** | 0–1 | Treble via filtre passe-bas 723 Hz. 0.5 = neutre ; plus haut = plus brillant |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Gain | Tone | Level | Notes |
|---|---|---|---|---|
| Clean boost (classique) | 0.08–0.12 | 0.65 | 0.75+ | Gain min, Level max : pousse l'ampli |
| Crunch blues | 0.40–0.50 | 0.60 | 0.55 | Mid-hump naturel de la TS |
| Solo rock | 0.55–0.65 | 0.62 | 0.52 | Sustain avec présence |
| Boost metal | 0.10–0.15 | 0.70 | 0.80 | Devant un amp high-gain : tight |

**Caractéristique :** La TS a un **mid-hump naturel à 723 Hz**. Elle sonne automatiquement
avec une présence mid que l'OCD ou la RAT n'ont pas. Très efficace pour couper dans un mix.

**Réglage "clean boost" :** Gain très bas, Level élevé = pousse le préampli de l'ampli
sans vraiment distordre. Technique classique pour solos (Even Flow style Mike McCready).

---

## Swedish Chainsaw = Boss HM-2 Heavy Metal

**HX Effects model ID :** `HD2_DistSwedishChainsaw`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Drive** | 0–1 | Gain/saturation. 0.9–1.0 = son chainsaw total |
| **Bass** | 0–1 | Graves. 0.9–1.0 = basses très poussées |
| **Treble** | 0–1 | Agit sur **mids + treble** ensemble (câblés ensemble dans le circuit) |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Drive | Bass | Treble | Level | Notes |
|---|---|---|---|---|---|
| Swedish death metal | 1.0 | 1.0 | 1.0 | 0.50 | Tout à fond = son chainsaw légendaire |
| Metal équilibré | 0.90 | 0.75 | 0.75 | 0.50 | Plus de clarté que "tout dimed" |
| Drop C (SOAD) | 0.90 | 0.75 | 0.75 | 0.50 | Légèrement moins de bas pour Drop C |
| Heavy crunch | 0.80 | 0.60 | 0.62 | 0.52 | Lisibilité preservée |

**Particularité :** Bass et Treble en opposition (Bass 3h, Treble 9h) = mid-scoop classique.
Le Treble booste simultanément les mids et l'aigu — pas un simple EQ treble.

---

## Heavy Dist = Boss Metal Zone (Legacy DM4)

**HX Effects model ID :** `HD2_DM4HeavyDistortion`

Circuit semi-conducteur high-gain avec EQ active 3 bandes. Très saturé même à Drive modéré.
Différent du Metal Zone MT-2 (qui a un EQ semi-paramétrique en plus).

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Drive** | 0–1 | Gain. 0.5 = déjà très saturé ; 0.7–0.9 = territoire metal massif |
| **Bass** | 0–1 | Graves. 0.7–0.8 = basses lourdes ; 0.5 = neutre |
| **Mid** | 0–1 | Mids. **0.3–0.4 = scoop metal** ; 0.5 = neutre ; 0.6+ = son plus présent |
| **Treble** | 0–1 | Aigus. 0.5–0.6 = présence sans agressivité |
| **Output** | 0–1 | Volume de sortie. Default haut (0.73) — souvent suffisant |

### Sweet spots
| Contexte | Drive | Bass | Mid | Treble | Output | Notes |
|---|---|---|---|---|---|---|
| Post-grunge / Nickelback | 0.70 | 0.80 | 0.40 | 0.55 | 0.80 | Validé sur How You Remind Me — Ryan Peake |
| Nu-metal tight | 0.80 | 0.70 | 0.35 | 0.58 | 0.73 | Mid scoop prononcé, palm mutes définis |
| Modern metal | 0.85 | 0.72 | 0.38 | 0.60 | 0.70 | Plus agressif, scoop léger |
| Death metal sombre | 0.90 | 0.85 | 0.30 | 0.45 | 0.65 | Très grave, mid scoopé |

**Particularité :** Le Mid à 0.30–0.40 crée le "V-shape" typique metal (basses + aigus, mids creusés).
Monter le Mid à 0.50+ donne plus de présence dans le mix mais perd le caractère "metal".

**Piège :** Drive élevé + Bass élevé + Mid bas = palm mutes qui bavent.
Solution : baisser Bass (0.70 → 0.60) ou Gate plus serré.

---

## Industrial Fuzz = Z.Vex Fuzz Factory

**HX Effects model ID :** `HD2_DistIndustrialFuzz`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Compress** | 0–1 | Varie l'impédance d'entrée. Haut = signal écrasé/compressé, attaque "plaquée" |
| **Gate** | 0–1 | Rebias le transistor : haut = coupure nette entre notes (gated fuzz) ; bas = sustain naturel |
| **Drive** | 0–1 | Gain de distorsion. 0.9–1.0 pour usage classique |
| **Stability** | 0–1 | Ouvre les paramètres d'oscillation. **Garder > 0.5 pour un son stable** |
| **Oscillator** | False/True | Active l'oscillation automatique (squeals) — expérimental |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Compress | Gate | Drive | Stability | Level | Notes |
|---|---|---|---|---|---|---|
| Fuzz normale | 0.55 | 0.30 | 0.90 | 0.70 | 0.52 | Stable et musicale |
| Gated fuzz (Plug In Baby) | 0.72 | 0.68 | 0.90 | 0.58 | 0.52 | Coupure nette = son saccadé |
| Fuzz smooth | 0.45 | 0.20 | 0.85 | 0.75 | 0.50 | Sustain long, moins agressif |
| Expérimental | 0.60 | 0.35 | 1.0 | 0.25 | 0.48 | Oscillations et instabilité |

**Piège :** Stability en dessous de 0.4 = comportements imprévisibles (squeals, oscillations).
Ne descendre en dessous que volontairement pour des effets expérimentaux.

---

## Bighorn Fuzz = EHX Big Muff Pi (Ram's Head)

**HX Effects model ID :** `HD2_DistRamsHead`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Sustain** | 0–1 | Gain. La Big Muff a moins de contrôle sur la dynamique que l'OCD |
| **Tone** | 0–1 | Filtre actif : 0.5 = scoop de mids à 1 kHz (signature). 0.2 = très sombre. 0.8 = brillant |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Sustain | Tone | Level | Notes |
|---|---|---|---|---|
| Grunge / stoner | 0.75–0.85 | 0.45–0.50 | 0.50 | Mids scoped, wall of sound |
| Solo lead | 0.82–0.90 | 0.55 | 0.48 | Plus de présence mid |
| Rock lourd | 0.70–0.80 | 0.45 | 0.52 | Equilibré |
| Fuzz légère | 0.50–0.60 | 0.55 | 0.55 | Moins de chaos |

**Caractéristique :** Le Tone à 0.5 crée un scoop de mids à 1 kHz = le son "mur" caractéristique.
Le Ram's Head a légèrement plus de mids que les autres versions (meilleure lisibilité en groupe).

---

## Minotaur = Klon Centaur

**HX Effects model ID :** `HD2_DistMinotaur`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Mélange signal clean/distordu. 0 = 100% clean (boost pur) ; 1 = 100% saturé |
| **Tone** | 0–1 | Filtre treble passif. Très puissant même à faibles valeurs |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Gain | Tone | Level | Notes |
|---|---|---|---|---|
| Boost transparent (pur) | 0.0 | 0.55 | 0.75 | 100% clean, lift de l'ampli |
| Boost coloré | 0.15–0.20 | 0.58 | 0.70 | Grain imperceptible, corps ajouté |
| OD léger | 0.40–0.50 | 0.60 | 0.55 | Crunch doux, transparent |
| OD medium | 0.65–0.75 | 0.62 | 0.50 | Sustain et présence |
| Avant OD/Dist | 0.10–0.20 | 0.60 | 0.70 | Boost pour pousser la pédale suivante |

**Particularité unique :** Le Gain est un **mélangeur** clean/saturé, pas juste un contrôle de gain.
À faible Gain, la pédale agit comme un boost transparent — c'est sa grande force.
La résistance aux diodes germanium n'est significative qu'à haut Gain.

---

## KWB = Benadrian Kowloon Walled Bunny

**HX Effects model ID :** `HD2_DistKWB`

**Correction (retour Eric) :** malgré la plage Gain 0–1, ce n'est PAS une pédale
haut-gain façon Mesa Rectifier — le caractère est plutôt celui d'une **OD légère,
type Tube Screamer un peu poussé**. Ne pas l'utiliser pour simuler un ampli
high-gain ; la réserver à des rôles d'OD légère/medium (boost, push, crunch doux).

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | OD légère type TS poussé — pas un haut-gain malgré la plage |
| **Bass** | -12 à +12 dB | EQ basses fréquences. Valeurs en dB |
| **Treble** | -12 à +12 dB | EQ aigus. Valeurs en dB |
| **Level** | 0–1 | Volume de sortie |
| **PushDiode** | 0–3 | Type de diode en push (timbre de la disto) |
| **PullDiode** | 0–3 | Type de diode en pull (timbre de la disto) |
| **Asym** | 0–1 | Asymétrie du clipping (0 = symétrique, 1 = asymétrique) |

### Sweet spots
| Contexte | Gain | Bass | Treble | Level | Notes |
|---|---|---|---|---|---|
| OD légère (TS-like) | 0.35 | 0.0 | 1.0 | 0.65 | Crunch doux, transparent |
| OD medium poussée | 0.50 | 0.0 | 1.5 | 0.60 | Plus de présence, reste OD pas dist |

Bass et Treble en **dB** (pas 0-1) — attention à la valeur absolue.

---

## Valve Driver = Chandler Tube Driver

**HX Effects model ID :** `HD2_DistValveDriver`

Circuit à tubes (réel, pas à semi-conducteurs) → saturation chaude, compressée, très dynamique.
Utilisé par David Gilmour, Billy Corgan, Trent Reznor. Son organiquement "tube".

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Saturation. Répond très bien à la dynamique de jeu — attaque légère = clean-up naturel |
| **Bass** | 0–1 | Graves. 0.5 = neutre ; > 0.6 = chaleur/lourdeur ; < 0.4 = serré |
| **Treble** | 0–1 | Aigus. 0.5 = neutre ; > 0.6 = présence/mordant ; < 0.4 = chaud/sombre |
| **Level** | 0–1 | Volume de sortie |

### Sweet spots
| Contexte | Gain | Bass | Treble | Level | Notes |
|---|---|---|---|---|---|
| Simulation ampli tube chaud | 0.65–0.72 | 0.52 | 0.48 | 0.55 | Gibson Skylark style : chaleur, compression naturelle |
| OD transparente | 0.40–0.50 | 0.50 | 0.50 | 0.55 | Neutre, laisse le caractère de l'ampli |
| Lead expressif | 0.75–0.82 | 0.48 | 0.55 | 0.50 | Présence lead, dynamique conservée |

**Caractéristique clé :** Contrairement aux OD à semi-conducteurs, le Valve Driver nettoie
naturellement quand on joue piano — comportement identique à un vrai ampli tube saturé.
Idéal pour simuler des petits combos tube (Skylark, Champ, Princeton) poussés à fond.

---

## Gain Stacking Metal — Principes et Approches

Le gain stacking = deux pédales de saturation en série. Résultat plus musical qu'une seule pédale
à saturation maximale : plus dynamique, moins compressé, meilleure définition des palm mutes.

### Règle générale : ordre des pédales

```
Guitare → [Tightener/Boost] → [Saturation principale] → Ampli
```

- **1ère pédale** (avant la dist) : tighten + boost d'entrée → plus d'attaque, graves resserrés
- **2ème pédale** (saturation principale) : caractère du son, clip principal

### Approches validées

| Combo | 1ère pédale | 2ème pédale | Caractère | Usage |
|---|---|---|---|---|
| **TS9 → amp hi-gain** | Scream808 Gain=0.10–0.15, Level=0.80 | Ampli saturé ou pédale high-gain | Tight, attaque percussive, palm mutes définis | Thrash, metalcore, modern metal |
| **TS9 → Metal Zone** | Scream808 Gain=0.20, Level=0.70 | Heavy Dist Drive=0.70–0.85 | Massif et lourd avec présence | Post-grunge, nu-metal |
| **TS9 → HM-2** | Scream808 Gain=0.15, Level=0.70 | SwedishChainsaw Drive=0.90+ | Ultra-saturé, bass très lourde | Death metal suédois |
| **OCD → amp hi-gain** | CompulsiveDrive Gain=0.10, Level=0.80 | KWB ou Heavy Dist | Attaque tight, mid-focus | Modern metal, djent-adjacent |

### TS9 en boost "clean" — technique classique thrash/metal

Réglage spécifique (confirmé SevenString.org / Wampler) :
- TS9 : **Gain=0 (min), Tone=1.0 (max), Level=1.0 (max)**
- Rôle : sculpteur de ton, pas de saturation — serre les graves et ajoute de la cohérence
- Résultat : amp hi-gain + TS9 = palm mutes beaucoup plus définis et percussifs

### EQ et distorsion metal — position et rôles

Deux positions d'EQ, deux fonctions distinctes :

**Avant la distorsion — nettoyer l'entrée**
Un grave non filtré entrant dans un high-gain = boue garantie.
Le signal distordé amplifie toutes les fréquences, y compris les indésirables.

| Fréquence | Action | Effet |
|---|---|---|
| < 80–100 Hz | High-pass (couper) | Supprime le sub-bass qui gonfle la dist inutilement |
| 200–300 Hz | Légère coupe (-2 à -4 dB) | Réduit la boue pré-dist, particulièrement sur humbucker |

→ Modèle HX recommandé : `HD2_EQGraphic10Band` (10 Band Graphic EQ)

**Après la distorsion — sculpter le son final**

| Fréquence | Action | Effet |
|---|---|---|
| 200–400 Hz | Coupe (-3 à -6 dB) | Zone "boueuse / cartonneuse" — première à attaquer |
| 2–4 kHz | Boost léger (+2 à +3 dB) | Présence et articulation, palm mutes coupent mieux |
| 6–8 kHz | Coupe si besoin | Réduit l'agressivité / stridences |

**Note spécifique au rig d'Eric :** le Super Distortion bridge a une sortie élevée qui sature
davantage l'entrée des pédales. Un high-pass à 80–100 Hz **avant** la dist est particulièrement
utile pour des palm mutes définis — plus encore que sur une Strat simple bobinage.

---

### Palm mutes baveux — diagnostic et remèdes

| Symptôme | Cause probable | Remède |
|---|---|---|
| Palm mutes indéfinis, gras | Bass trop élevé sur la dist | Baisser Bass de 0.1–0.15 |
| Palm mutes flottants, mous | Level de sortie trop élevé | Baisser Level, augmenter Gate |
| Palm mutes qui disparaissent | Trop de compression | Baisser Sensitivity compresseur |
| Palm mutes qui bavent en sustain | Gate trop doux | Augmenter Threshold du Noise Gate |

---

## Styles Metal — EQ typique par genre

| Style | Drive | Bass | Mid | Treble | Caractère ampli | Exemples setlist |
|---|---|---|---|---|---|---|
| Thrash | 0.75–0.85 | 0.65 | 0.50 | 0.65 | JCM800 / Marshall | — |
| Post-grunge | 0.65–0.75 | 0.78 | 0.40 | 0.55 | Mesa Dual Rec | How You Remind Me |
| Nu-metal | 0.80–0.90 | 0.70 | 0.35 | 0.60 | 5150 / Mesa | Hysteria, Toxicity |
| Death metal | 0.90–1.0 | 0.85 | 0.30 | 0.50 | HM-2 + amp | — |
| Doom/Stoner | 0.70–0.80 | 0.85 | 0.45 | 0.40 | Big Muff + ampli chaud | — |

**Note HX Effects vs Helix :** Helix et HX Stomp ont des **modèles d'ampli dédiés** (Cali Rectifire = Mesa Dual Rec, PV Panama = Peavey 5150/6505). Ces modèles ne sont **pas disponibles** dans HX Effects (pédales uniquement). L'approche HX Effects = simuler le canal d'ampli avec une pédale de distorsion haute-gain (voir table de matching ci-dessous).

---

## Simulation d'ampli — Table de matching

Quand un guitariste n'utilise pas de pédale OD externe et que toute la saturation
vient du canal gain de l'ampli, un bloc HX doit simuler ce canal de façon permanente
(`enabled_default=True`, Gain variable par snapshot selon l'intensité voulue).

Le choix de la pédale HX doit correspondre au **caractère sonore de l'ampli** :
timbre, réponse aux transitoires, compression naturelle.

| Ampli réel | Pédale HX recommandée | Model ID | Caractère | Source |
|---|---|---|---|---|
| **Marshall JCM800** (canal overdrive, Gain 7–9) | Compulsive Drive (OCD) | `HD2_DistCompulsiveDrive` | Crunch dynamique, LPHP=True pour le punch britannique | Be Yourself — Tom Morello |
| **Gibson Skylark** (petit combo tube ~4W, saturé à fond) | Arbitrator Fuzz | `HD2_DistArbitratorFuzz` | Fuzz Face germanium à gain modéré → "fuzz sur les bords" d'un petit tube saturé. Fuzz 0.62. Plus fidèle que le Valve Driver (trop lisse). | Are You Gonna Go My Way — Craig Ross |
| **Marshall JCM 2000 DSL** (canal Lead, gain bas + volume fort) | Compulsive Drive (OCD) | `HD2_DistCompulsiveDrive` | Même lignée que JCM800 (britannique). LPHP=True, Gain=0.65–0.70. Saturation de power amp naturelle — pas de préamp extrême. | Hysteria — Matt Bellamy |
| **Mesa Boogie Dual Rectifier / Metal Zone style** (canal Modern, Gain 7+) | Heavy Dist (Boss Metal Zone) | `HD2_DM4HeavyDistortion` | Saturation metal massive, palm-muting tight. Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80 (cf. pattern partagé "Heavy Dist Boss Metal Zone" dans shared_configs.md). **KWB n'est PAS adapté ici** : malgré sa plage Gain 0-1, c'est une OD légère type TS poussé, pas un haut-gain (corrigé apres retour Eric). | How You Remind Me — Ryan Peake / Toxicity |
| **ADA MP-1** (préampli rack, gain saturé articulé, pas de modèle dédié HX) | Compulsive Drive (OCD) | `HD2_DistCompulsiveDrive` | Plus poussé que le canal JCM800/DSL : Gain=0.75, Tone=0.38, LPHP=True, Level=0.80. Précédé d'un RAT (Ratatouille Dist) toujours actif en push (Gain=0.40, Filter=0.60, Level=0.70) — gain stacking, le RAT filtre/compresse plus qu'il ne sature. | He-Man Woman Hater — Nuno Bettencourt |

**À compléter au fil des presets.** Quand un nouveau cas de simulation d'ampli est
rencontré, ajouter une ligne à ce tableau avec l'ampli, la pédale choisie, le
caractère, et le titre/guitariste source.

**Réglages OCD pour simulation JCM800 :**

| Section | Gain | LPHP | Caractère |
|---|---|---|---|
| Intro / son quasi-propre | 0.05–0.10 | False (LP) | Très léger crunch, chaleur |
| Verse / crunch discret | 0.18–0.25 | False (LP) | Crunch modéré, rond |
| Chorus / crunch présent | 0.32–0.42 | True (HP) | Punch Marshall, mordant |
| Solo / crunch poussé | 0.50–0.60 | True (HP) | Gain élevé, présence lead |

---

## Résumé : Compensation Gain → Level

Pour chaque pédale, quand le Gain monte de 0.20 :

| Pédale | Compensation Level approximative |
|---|---|
| OCD (CompulsiveDrive) | -0.05 à -0.08 |
| RAT (VerminDist) | -0.05 à -0.07 |
| TS808 (Scream808) | -0.04 à -0.06 |
| HM-2 (SwedishChainsaw) | -0.05 à -0.08 |
| Big Muff (Bighorn) | -0.04 à -0.06 |
| Klon (Minotaur) | -0.05 (mais le Gain est un mélangeur) |

**Règle générale :** +0.20 Gain → -0.05 à -0.08 Level pour maintenir le même volume perçu.
Toujours vérifier à l'oreille.

---

## Sources
- ElectroSmash — Fulltone OCD, Pro Co RAT, TS808, Big Muff, Klon Centaur analyses
- Guitar Chalk — OCD, RAT, TS808, Phase 90, Fuzz Factory settings
- BOSS Articles — HM-2 Swedish Death Metal
- Premier Guitar — Overdrives and Distortions guide
- Z.Vex — Fuzz Factory documentation
- Wikipedia — Pro Co RAT, Boss HM-2, Klon Centaur
- Line 6 Community — Metal tones HX Effects (https://line6.com/support/topic/63310)
- SevenString.org — HX Stomp thrash/modern metal settings
- Wampler Pedals — Gain stacking 101 (https://www.wamplerpedals.com/blog/music/2020/05/gain-stacking-101/)
- JHS Pedals — How to stack pedals (https://jhspedals.info/blogs/news/how-to-stack-pedals)
- Line 6 Blog — Gainful Deployment: Stacking Overdrives (https://blog.line6.com/2020/04/27/gainful-deployment-stacking-overdrives/)
- MusicRadar — Pedal gain stacking guide (https://www.musicradar.com/how-to/pedal-gain-stacking-order-and-more-explained)
- Metal Guitarist Forums — Stoner/Doom tone discussion
- RiffHard — Doom metal tone guide
