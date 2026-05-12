# EQ — Guide des Paramètres

## Rôle de l'EQ Guitare

L'EQ (égaliseur) coupe ou booste des fréquences spécifiques pour :
- **Sculpter le timbre** (plus chaud, plus brillant, plus présent)
- **Corriger un défaut** d'ampli ou de guitare
- **Couper dans un mix** (boost des mids pour ressortir)
- **Imiter un caractère** de tonalité spécifique (scoop de mids HM-2, mid-hump TS808)

---

## Fréquences Guitare — Référence

| Bande | Fréquence | Caractère |
|---|---|---|
| Sub-basse | < 80 Hz | Fréquences inutiles pour la guitare — couper ou ignorer |
| Basse | 80–200 Hz | Corps/chaleur de la guitare ; trop = son boueux |
| Bas-mids | 200–500 Hz | Chaleur et rondeur ; trop = son "en carton" |
| Mids | 500 Hz–2 kHz | Présence et lisibilité dans le mix ; les mids = capacité à "couper" |
| Haut-mids | 2–5 kHz | Attaque, pick, mordant |
| Aigus | 5–10 kHz | Brillance, air ; trop = son sifflant |
| Présence | > 10 kHz | Air et brillance extrême |

**Règle des mids :** En live, il vaut mieux avoir trop de mids que pas assez.
Les fréquences de 500 Hz–2 kHz sont celles qui permettent à la guitare de s'entendre
dans un mix avec basse, batterie et voix. Couper les mids = son hi-fi seul mais inaudible en groupe.

---

## Simple 3-Band = Line 6 Original

**HX Effects model ID :** `HD2_EQSimple3Band`

EQ à 3 bandes simples (bas, mids, aigus). Pratique pour des corrections rapides
sans DSP élevé. Les fréquences de coupure ne sont pas précisées (bandes fixes).

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **LowGain** | -12 à +12 dB | Boost/cut des basses |
| **MidFreq** | ~100–5000 Hz | Fréquence centrale de la bande mid (paramétrique) |
| **MidGain** | -12 à +12 dB | Boost/cut des mids à la fréquence MidFreq |
| **HighGain** | -12 à +12 dB | Boost/cut des aigus |

### Sweet spots
| Contexte | LowGain | MidFreq | MidGain | HighGain | Notes |
|---|---|---|---|---|---|
| Correction neutre | 0 | 800 | 0 | 0 | Aucune modification |
| Bridge/solo (AYGGMW) | 0 | 800.0 | -2.0 | -3.0 | Réduit les mids/aigus pour le son de bridge |
| Boost mids présence | 0 | 1000 | +3 | 0 | Guitare qui coupe dans le mix |
| Coupure basse (tight) | -3 | 200 | 0 | 0 | Moins de basse = son plus serré |
| Brillance clean | 0 | 3000 | +2 | +2 | Plus d'air et d'attaque sur son clean |

**Usage projet :** Are You Gonna Go My Way (Bridge) — `MidFreq: 800.0, MidGain: -2.0, HighGain: -3.0`.

---

## 10-Band Graphic = MXR 10-Band EQ

**HX Effects model ID :** `HD2_EQGraphic10Band`

Modèle du MXR M108S 10-Band Graphic EQ. 10 bandes de boost/cut fixées, très précis.

### Paramètres
| Param | Fréquence | Caractère |
|---|---|---|
| **31Hz** | 31 Hz | Sub-basse (inutile pour guitare) |
| **63Hz** | 63 Hz | Basse profonde |
| **125Hz** | 125 Hz | Corps de la guitare |
| **250Hz** | 250 Hz | Chaleur et rondeur |
| **500Hz** | 500 Hz | Bas-mids, chaleur |
| **1kHz** | 1 kHz | Zone critique de présence |
| **2kHz** | 2 kHz | Attaque et mordant |
| **4kHz** | 4 kHz | Haut-mids, pick |
| **8kHz** | 8 kHz | Brillance |
| **16kHz** | 16 kHz | Air (souvent inaudible en live) |
| **Level** | dB | Gain de sortie global de l'EQ |

Toutes les bandes : plage **-12 à +12 dB**.

### Sweet spots
| Contexte | 500Hz | 1kHz | 2kHz | Level | Notes |
|---|---|---|---|---|---|
| Boost mids Josh Homme (QOTSA) | +3 | +4 | +2 | 0 | No One Knows : mid-hump agressif |
| Mid-scoop Marshall | -3 | -4 | -3 | 0 | V-shape classique, graves+aigus |
| Présence solo | 0 | +2 | +3 | 0 | Attaque et mordant pour ressortir |
| Tone correction grave | +2 | 0 | 0 | -2 | Compense le manque de basse de la guitare |

**Usage projet :** No One Knows (QOTSA) — `500Hz: 3.0, 1kHz: 4.0, 2kHz: 2.0, Level: 0.0`.
Josh Homme utilise une grosse coupe de mids basse mais un fort boost 500Hz–2kHz pour la présence.

---

## Kinky Boost = Xotic EP Booster (bonus EQ)

**HX Effects model ID :** `HD2_DistKinkyBoost`

Techniquement classé comme "Dist" dans HX, mais c'est un préampli/boost propre.
Il ajoute de la couleur tonale sans distorsion notable si Drive est bas.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Drive** | 0–1 | Gain du préampli. 0.0 = boost neutre ; 0.5+ = coloration prononcée |
| **Boost** | False/True | **True** = +6 dB de boost supplémentaire (switch interne du EP Booster) |
| **Bright** | False/True | **True** = boost des aigus (présence) ; False = neutre |

**Caractère tonale du Kinky Boost (Drive > 0) :**
- Légère couleur "vintage" chaude
- Harmoniques paires ajoutées (son plus "tube")
- Mid-hump discret autour de 1–2 kHz

**Usage projet :** Be Yourself (boost verse/chorus), Black Hole Sun (intro et verse).
Drive=0.0 + Boost=True = boost de volume pur (+6 dB) sans coloration.

---

## EQ — Placement dans la Chaîne

```
Guitare → Gate → [EQ correction] → OD/Dist → [EQ sculptage] → Reverb
```

**EQ avant OD :** Sculpte les fréquences qui entrent dans la saturation.
Couper les basses avant l'OD = saturation plus "tight" (moins de basse saturée = son plus serré).

**EQ après OD :** Corrige le timbre du signal distordu.
Plus courant : on entend l'OD, puis on sculpte sa couleur finale.

**EQ en fin de chaîne :** Correction globale du preset pour qu'il s'intègre dans le mix.

---

## EQ vs Tone des Pédales

La plupart des pédales ont leur propre EQ interne (Tone, Filter, Bass/Treble).
Un bloc EQ dédié est utile quand :
- Le Tone de la pédale ne permet pas assez de précision
- On veut agir sur plusieurs bandes simultanément
- On imite un ampli ou un EQ racket spécifique

**Alternative :** Ajuster le Tone de l'OD suffit souvent dans un preset standard.
Le bloc EQ consomme un slot — ne l'utiliser que si nécessaire.

---

## Sources
- MXR 10-Band EQ Manual
- Guitar Chalk — EQ Settings for Guitar
- Premier Guitar — EQ Fundamentals
- ElectroSmash — MXR Phase 90, 10-Band EQ
- Expérience projet : Are You Gonna Go My Way (Simple3Band), No One Knows (Graphic10Band Josh Homme style)
