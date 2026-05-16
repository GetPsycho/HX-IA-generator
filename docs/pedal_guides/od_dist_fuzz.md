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

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Gain** | 0–1 | Saturation haute-gain. 0.6+ = territoire très saturé |
| **Bass** | -12 à +12 dB | EQ basses fréquences. Valeurs en dB |
| **Treble** | -12 à +12 dB | EQ aigus. Valeurs en dB |
| **Level** | 0–1 | Volume de sortie |
| **PushDiode** | 0–3 | Type de diode en push (timbre de la disto) |
| **PullDiode** | 0–3 | Type de diode en pull (timbre de la disto) |
| **Asym** | 0–1 | Asymétrie du clipping (0 = symétrique, 1 = asymétrique) |

### Sweet spots
| Contexte | Gain | Bass | Treble | Level | Notes |
|---|---|---|---|---|---|
| High gain chaud | 0.72 | 2.0 | 1.0 | 0.52 | Muse Hysteria style |
| Metal serré | 0.80 | 0.0 | 0.0 | 0.50 | Neutre, laisser l'ampli sculpter |
| Lead saturé | 0.85 | 1.5 | 2.0 | 0.45 | Compenser Level |

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
| **Mesa Boogie Dual Rectifier** (canal Modern, Gain 7+) | KWB | `HD2_DistKWB` | Saturation haute-gain très serrée, caractère métal moderne. EQ neutre (Bass=0.0, Treble=0.0). Gain=0.78. Gain stacking : Scream808 (TS9, Gain=0.65) en amont resserre les palm mutes via mid hump 723 Hz. | How You Remind Me — Ryan Peake |

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
