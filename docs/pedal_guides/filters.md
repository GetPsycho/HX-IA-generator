# Filtres et Wah — Guide des Paramètres

## Types de filtres

| Type | Caractère | Utilisation |
|---|---|---|
| **LP (Low-Pass)** | Laisse passer les graves, coupe les aigus. Plus le cutoff est bas = plus sombre | Moog MF-101 style, son wobbly grave/mid |
| **BP (Band-Pass)** | Laisse passer une bande de fréquences. Plus "quacky", moins de graves | Wah-like, funk, moins bass-heavy |
| **HP (High-Pass)** | Laisse passer les aigus, coupe les graves. Plus brillant et fin | Rare en guitare, effets spéciaux |

**Leçon apprise sur Dani California :** Mode LP (0) trop grave pour le lick funk.
Passer en BP (1) = sweep dans les mids → beaucoup plus funk et expressif.

---

## Auto Filter = Line 6 Original (inspiré Moog MF-101)

**HX Effects model ID :** `HD2_FilterAutoFilter`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Mode** | 0, 1, 2 | **0=LP** (sombre/grave), **1=BP** (mid/quacky), **2=HP** (brillant/fin) |
| **FilterGain** | 0–36 dB | Résonance au point de coupure. Haut = pic prononcé (sifflement) |
| **FilterQ** | 1–10 | Q (sélectivité). Haut = pic étroit et marqué. Bas = filtre large |
| **Sens** | 0–1 | Sensibilité de l'envelope follower. Haut = le filtre réagit à moindre dynamique |
| **Attack** | 0.005–2.0 s | Vitesse d'ouverture du filtre. Bas = très rapide (funk percussif) |
| **Decay** | 0.005–3.0 s | Vitesse de fermeture. Haut = le filtre reste ouvert longtemps |
| **Frequency** | 20–1000 Hz | Fréquence de départ (position du filtre au repos) |
| **FreqDepth** | 0–10000 Hz | Amplitude du sweep. Haut = le filtre s'ouvre très loin en fréquence |
| **Direction** | True/False | True = filtre s'ouvre en montant (attack), False = s'ouvre en descendant |
| **Mix** | 0–1 | Dry/Wet |
| **Level** | -60 à 0 dB | Volume de sortie |

### Sweet spots

**Mode BP (1) — Funk / Wah dynamique (Dani California style)**
```
Mode: 1, FilterGain: 14.0, FilterQ: 6.0
Sens: 0.55, Attack: 0.01, Decay: 0.30
Frequency: 200.0, FreqDepth: 4500.0
Direction: True
```
Le filtre sweape une bande de mids → son funk/quacky expressif, pas trop grave.

**Mode LP (0) — Filtre grave/basseux (Moog LPF pur)**
```
Mode: 0, FilterGain: 12.0, FilterQ: 5.0
Sens: 0.55, Attack: 0.01, Decay: 0.35
Frequency: 80.0, FreqDepth: 4000.0
Direction: True
```
Le filtre laisse passer les graves → son wobbly très bass-heavy (peut noyer le mix).

**Réglages slow/expressif (ambient)**
```
Sens: 0.35, Attack: 0.05, Decay: 0.80
Frequency: 100.0, FreqDepth: 3000.0
```
Le filtre réagit lentement, reste ouvert longtemps = effet plus doux, moins agressif.

### Piège
**FilterQ trop élevé** (8+) = sifflement prononcé au point de résonance.
Garder entre 5 et 7 pour un son musical.

**Mode LP avec fréquence de départ basse** = début trop grave.
Remonter Frequency à 150–300 Hz pour démarrer dans les mids.

---

## Mutant Filter = Musitronics Mu-Tron III

**HX Effects model ID :** `HD2_FilterMutantFilter`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Mode** | 0, 1, 2 | 0=LP, 1=BP, 2=HP |
| **Peak** | 0–1 | Résonance au cutoff. Équivalent du FilterQ. Garder < 0.85 |
| **Gain** | 0–1 | Sensibilité de l'envelope follower (équivalent Sens) |
| **Range** | False/True | Étendue de la plage de sweep. True = plus large |
| **Drive** | True/False | Active le clipping interne du Mu-Tron |
| **Mix** | 0–1 | Dry/Wet |
| **Level** | -60 à 0 dB | Volume de sortie |

Moins de contrôle précis que l'Auto Filter mais character plus authentique Mu-Tron.

### Sweet spots
| Contexte | Mode | Peak | Gain | Range | Notes |
|---|---|---|---|---|---|
| Funk standard | 1 (BP) | 0.65 | 0.45 | False | Quacky, mid-heavy |
| Funk expressif | 1 (BP) | 0.75 | 0.55 | True | Plus de sweep, plus dramatique |
| Wah lent | 0 (LP) | 0.60 | 0.35 | False | Filtre LPF doux |

---

## Wah — Principes généraux

Les wah du HX Effects (Fassel, UK Wah 846, Teardrop 310, etc.) fonctionnent
avec le paramètre `Pedal` qui simule la position de la pédale wah physique.

**Sur HX Effects sans expression pedal :** La wah est statique (position fixe).
Pour une wah dynamique, il faudrait une expression pedal assignée au `Pedal` du bloc wah.

**Alternative :** L'Auto Filter en Mode BP avec Direction=True et Sens élevée
simule une wah automatique qui réagit au jeu.

### Placement Wah dans la chaîne
| Position | Son | Artistes |
|---|---|---|
| Avant OD | Son quacky classique, dynamique | Clapton, SRV |
| Après OD | Son plus "gras", sweep dans le distordu | Hendrix (certains titres) |
| Avant Fuzz | Problème impédance avec fuzzes germanium | À éviter sur HX (pas de problème) |
| Après Fuzz | Son plus stable, sweep du signal fuzz | Hendrix setup préféré |

---

## Sources
- Moog MF-101S Official Manual
- Guitar Chalk — Wah Pedal Settings
- BOSS — Filter Effects Guide
- Expérience projet : Dani California AutoFilter Mode LP → BP (leçon apprise)
