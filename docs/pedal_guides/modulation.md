# Modulation — Guide des Paramètres

## Vue d'ensemble — Ordre et Placement

Les effets de modulation (phaser, chorus, flanger, rotary) se placent généralement
**après les pédales de gain** et **avant le delay et la reverb**.

| Placement | Effet | Exemple |
|---|---|---|
| **Avant OD** | Modulation intégrée à la saturation, son chaud/organique | Hendrix (phaser→fuzz) |
| **Après OD** | Modulation claire sur le signal distordu, effet plus évident | Placement standard |
| **Avant Delay** | Les répétitions du delay sont non-modulées | Son propre |
| **Après Delay** | Les répétitions sont modulées = chaos/ambient | Effet spécial |

---

## Phaser — Principes communs

Un phaser divise le signal en deux, déphasage une copie via un filtre à tout-passe,
puis recombine les deux. Les fréquences qui s'annulent créent le "swoosh" caractéristique.

**Stages :** nombre d'étages de déphasage. Plus = plus de notches (trous spectraux).
- 2 stages = son léger, transparent
- 4 stages = standard (Phase 90, Small Stone)
- 6 stages = plus riche
- 8 stages = très prononcé (Phase 90 "Script" 8-stage)

**Rate :** vitesse d'oscillation du LFO. Lent = ambiant/atmosphérique. Rapide = woozy/psyché.

---

## Deluxe Phaser = Boss PH-2 Super Phaser

**HX Effects model ID :** `HD2_PhaserDeluxePhaser`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Rate** | 0–10 Hz | Vitesse d'oscillation. 0.2–0.5 = lent/atmosphérique ; 0.8–2.0 = vivant ; 4+ = rapide/psyché |
| **Depth** | 0–1 | Amplitude du sweep. Haut = sweep plus large (plus de "wow") |
| **Feedback** | 0–1 | Résonance/réinjection. Haut = son plus prononcé, pics plus marqués |
| **Stages** | 2, 4, 6, 8 | Nombre d'étages (notches). 4 = standard Boss PH-2 |
| **Mix** | 0–1 | Dry/Wet. 0.5 = mix standard pour que l'effet soit perceptible sans dominer |
| **Level** | 0.0 (0 dB) | Volume de sortie. 0.0 = neutre |

### Sweet spots
| Contexte | Rate | Depth | Feedback | Stages | Mix | Notes |
|---|---|---|---|---|---|---|
| Intro atmosphérique (Drive) | 0.3 | 0.85 | 0.28 | 4 | 0.50 | Phaser lent, grand espace |
| Verse standard (Drive) | 0.8 | 0.80 | 0.28 | 4 | 0.50 | Phaser modéré, vivant |
| Solo funk | 1.5 | 0.75 | 0.20 | 4 | 0.45 | Plus rapide, sans excès de résonance |
| Ambient/shoegaze | 0.15 | 0.90 | 0.35 | 8 | 0.55 | Très lent, 8 stages = riche |

**Usage projet :** Drive (Incubus) — Rate différent selon snapshot (Intro=0.3, Verse=0.8).

---

## Script Mod Phase = MXR Phase 90 "Script"

**HX Effects model ID :** `HD2_PhaserScriptModPhase`

Modèle du MXR Phase 90 version "Script" (années 70, sans le switch R28).
Son plus doux et vintage que la version moderne.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Rate** | 0–10 | Vitesse du sweep. 0.2 = très lent (solo expressif) ; 2+ = rapide |
| **Mix** | 0–1 | Dry/Wet |
| **Level** | 0.0 | Volume de sortie |

Peu de paramètres = caractère simple et vintage, difficile d'avoir un son "mauvais".

### Sweet spots
| Contexte | Rate | Mix | Notes |
|---|---|---|---|
| Solo lent (Even Flow) | 0.22 | 0.45 | Sweep très lent, expressif sous la wah |
| Rhythm funkylent | 0.60 | 0.40 | Groove, pas agressif |
| Classic rock standard | 1.20 | 0.50 | Phase 90 réglage "medium" classique |

**Usage projet :** Even Flow (Pearl Jam) — Rate=0.22 pour le solo uniquement.

---

## Pebble Phaser = EHX Small Stone

**HX Effects model ID :** `HD2_PhaserPebblePhaser`

Modèle du EHX Small Stone Phase Shifter (EHX "Bad Stone" sur certaines listes).
Son plus épais et organique que le Phase 90.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Rate** | 0–10 | Vitesse du sweep |
| **Color** | False/True | **False** = son ouvert, plus doux ; **True** = plus résonant/prononcé |
| **Level** | 0.0 | Volume de sortie |

### Sweet spots
| Contexte | Rate | Color | Notes |
|---|---|---|---|
| Rock classique (Sex on Fire) | 0.30 | False | Phaser discret, juste le mouvement |
| Funk expressif | 0.80 | True | Plus de résonance, caractère |
| Psychédélique | 0.50 | True | Milieu de chemin |

**Usage projet :** Sex on Fire (Kings of Leon) — Rate=0.30, Color=False, uniquement sur Bridge.

---

## 70s Chorus = Boss CE-1 / CE-2

**HX Effects model ID :** `HD2_Chorus70sChorus`

Modèle du Boss CE-1 Chorus Ensemble (1976, premier chorus Boss).
Le CE-2 est une version directe du CE-1 en format pédale compact.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **ChorusIntensity** | 0–1 | Profondeur/intensité du chorus. Haut = vibrato/chorus prononcé |
| **VibratoRate** | 0–1 | Vitesse du LFO (vitesse d'oscillation) |
| **VibratoDepth** | 0–1 | Amplitude du vibrato (profondeur de la modulation de pitch) |
| **Mix** | 0–1 | Dry/Wet |
| **Level** | 1.0 | Volume de sortie |

**Différence Chorus vs Vibrato sur le CE-1 :**
- En mode Chorus : signal sec + signal modulé (effet d'épaississement)
- En mode Vibrato : 100% signal modulé (pitch fluctue, vibrato réel)

### Sweet spots
| Contexte | ChorusIntensity | VibratoRate | VibratoDepth | Mix | Notes |
|---|---|---|---|---|---|
| Shimmer clean (Nue/Radio Song) | 0.45–0.50 | 0.35–0.40 | 0.35–0.40 | 0.40–0.45 | Chorus discret, juste de l'air |
| Chorus prononcé (Intro Drive) | 0.55–0.65 | 0.45 | 0.45 | 0.50 | Plus de mouvement |
| Vibrato Andy Summers | 0.70 | 0.30 | 0.60 | 0.70 | Police style, vibrato evident |

**Usage projet :** Drive (Intro + Refrain), Nue, Radio Song, Travel The World.
Toujours en `enabled_default=False` — activé uniquement sur les snaps concernés.

---

## Gray Flanger = MXR M117R Flanger

**HX Effects model ID :** `HD2_FlangerGrayFlanger`

Modèle du MXR M117R Flanger (1976, version "Gray Box" vintage).
Son de flanging classique années 70, moins agressif que les flangers modernes.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Rate** | 0–1 | Vitesse du LFO. Bas = flanging lent/atmosphérique |
| **Width** | 0–1 | Amplitude du sweep. Haut = flanging plus profond |
| **Regen** | 0–1 | Réinjection (feedback). Haut = son très métallique/jet-like |
| **Mix** | 0–1 | Dry/Wet |

### Sweet spots
| Contexte | Rate | Width | Regen | Mix | Notes |
|---|---|---|---|---|---|
| Hard rock années 70 (AYGGMW Bridge) | 0.12 | 0.70 | 0.45 | 0.40 | Flanging lent et profond |
| Flanging rapide | 0.40 | 0.60 | 0.30 | 0.35 | Plus de mouvement |
| Jet flanger | 0.20 | 0.85 | 0.70 | 0.50 | Regen élevé = son "avion" |
| Chorus-like (subtil) | 0.10 | 0.40 | 0.15 | 0.30 | Mix bas = épaississement discret |

**Piège :** Regen élevé (0.70+) = son très prononcé qui peut sonner cheap.
Garder Regen 0.30–0.55 pour un flanging musical.

**Usage projet :** Are You Gonna Go My Way (Lenny Kravitz) — Bridge uniquement.

---

## Rotary Drum/Horn = Leslie 145 (via MM4)

**HX Effects model ID :** `HD2_MM4RotaryDrumHorn`

Modèle du Leslie 145 via le MM4 de Line 6. Simule le son du haut-parleur rotatif
(baffle rotatif bass = "Drum" + corne rotative treble = "Horn").

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Speed** | False/True | **False** = lent (slow, son swirling épais) ; **True** = rapide (fast, Doppler prononcé) |
| **Depth** | 0–1 | Profondeur de la modulation du Drum (baffe basses) |
| **Horn Depth** | 0–1 | Profondeur de la modulation du Horn (corne aigus) |
| **Drive** | 0–1 | Saturation interne du Leslie (simulation du préampli tube du Leslie) |
| **Mix** | 0–1 | Dry/Wet. 0.85 = très présent (Kim Thayil style) |
| **Level** | -60 à +6 dB | Volume de sortie. En dB |

### Sweet spots
| Contexte | Speed | Depth | Horn Depth | Drive | Mix | Level | Notes |
|---|---|---|---|---|---|---|---|
| Kim Thayil / BHS Verse | True | 0.82 | 0.88 | 0.5 | 0.85 | +4 dB | Swirl rapide, très présent, léger drive |
| Slow ambient | False | 0.75 | 0.80 | 0.0 | 0.65 | 0 dB | Effet rotatif lent, atmosphérique |
| Drive léger (Vibe style) | True | 0.60 | 0.65 | 0.0 | 0.45 | 0 dB | Plus subtil, Uni-Vibe like |

**Note Drive :** La valeur Drive pour le rotary est en échelle 0–1, mais le HX Edit
affiche par exemple "5" pour une valeur interne de 0.5 (même règle ÷10 que les autres).

**Usage projet :** Black Hole Sun (STP) — Verse uniquement (Speed=True, Drive=0.5, Level=+4 dB).
Toujours `enabled_default=False` — l'erreur de ne pas le faire active le rotary sur tous les snaps.

---

## Dimension = Roland Dimension D (via MM4)

**HX Effects model ID :** `HD2_MM4Dimension`

Modèle du Roland SDD-320 Dimension D via le MM4. C'est un chorus très discret
et transparent — pas de LFO évident, juste de l'"espace" et de la dimension.

**4 modes SW (switchs exclusifs — un seul actif à la fois) :**
| Switch | Intensité | Caractère |
|---|---|---|
| **SW1=True** | Mode 1 — le plus subtil | Très transparent, quasi-invisible |
| **SW2=True** | Mode 2 | Légèrement plus présent |
| **SW3=True** | Mode 3 | Chorus modéré, commence à s'entendre |
| **SW4=True** | Mode 4 — le plus spacieux | Effet le plus large, signature son Radiohead |

### Paramètres
| Param | Valeur | Ce que ça fait vraiment |
|---|---|---|
| **SW1** | False | Sélecteur mode 1 |
| **SW2** | False | Sélecteur mode 2 |
| **SW3** | False | Sélecteur mode 3 |
| **SW4** | True | Sélecteur mode 4 (le plus utilisé) |
| **Mix** | 1.0 | Dry/Wet — généralement à 1.0 (plein effet) |
| **Level** | 0.0 | Volume de sortie (0 = neutre) |

**Usage projet :** Creep (Radiohead) — Verse uniquement, SW4=True. Simule le son propre
et spatial de Jonny Greenwood sur les couplets de Creep.

**Piège :** Ne jamais activer deux SW simultanément — un seul à la fois pour que le modèle
fonctionne correctement.

---

## Placement Modulation dans la Chaîne

```
Guitare → Gate → [Comp] → OD/Dist → [Phaser/Chorus/Flanger] → [Rotary] → Delay → Reverb
```

**Règles pratiques :**
- Phaser **avant** OD = caractère "intégré", organique (Hendrix, Robin Trower)
- Phaser **après** OD = swoosh évident sur le signal distordu (standard)
- Chorus + Reverb : Chorus **avant** Reverb (plus naturel) ou **après** (shimmer)
- Rotary : toujours en dernier avant Delay/Reverb — simule l'espace du cabinet

---

## Sources
- Boss CE-1 Service Manual & Tech Corner
- MXR Phase 90 History — Analogman, JHS Pedals
- Roland SDD-320 Dimension D Manual
- Guitar.com — Leslie 145 vs 122
- Premier Guitar — Modulation Effects Guide
- Expérience projet : Drive (phaser rate par snapshot), Black Hole Sun (rotary enabled_default), Creep (Dimension D SW4)
