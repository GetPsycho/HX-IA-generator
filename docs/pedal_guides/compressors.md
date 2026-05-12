# Compresseurs — Guide des Paramètres

## Rôle d'un compresseur guitare
- **Régularise le niveau** entre les notes fortes et faibles
- **Ajoute du sustain** en prolongeant le sustain naturel des notes
- **Sculpte l'attaque** (attack/release pour les compresseurs avancés)
- **Ajoute du "squish"** (caractère compressé) sur certains styles (funk, country)

---

## Red Squeeze = MXR Dyna Comp

**HX Effects model ID :** `HD2_CompressorRedSqueeze`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Sensitivity** | 0–1 | Taux de compression. Bas = compression légère (invisible). Haut = squish fort, funk |
| **Mix** | 0–1 | Dry/Wet. 1.0 = 100% compressé. 0.5 = parallèle (NY compression) |
| **Level** | -60 à +12 dB | Makeup gain. Compense la réduction de volume par la compression |

### Sweet spots
| Contexte | Sensitivity | Level | Mix | Notes |
|---|---|---|---|---|
| Sustain subtil ("invisible") | 0.30–0.40 | +2 dB | 1.0 | On remarque plus sa disparition |
| Rock / pop-rock | 0.50–0.60 | +3 dB | 1.0 | Régularisation sans squish |
| Funk / Nile Rodgers | 0.65–0.75 | +4 dB | 1.0 | Squish fonctionnel, attaque snappy |
| Comp avant OD | 0.45–0.55 | +2 dB | 1.0 | Signal uniforme vers l'OD |
| Country slapback | 0.78–0.85 | +4 dB | 1.0 | Squish agressif + delay court |
| NY Compression (parallèle) | 0.85 | +4 dB | 0.50 | Comp agressive mélangée au signal sec |

**Réglage Nile Rodgers :** Sensitivity 0.65, Level +4 dB.
Donne le squish caractéristique du chucking sur Strat single-coil.

**Piège :** Level en dB — ne pas oublier que +6 dB = très fort. Commencer à +2–3 dB.

### Placement dans la chaîne
| Position | Effet | Quand l'utiliser |
|---|---|---|
| Avant OD | Signal régularisé → OD sonne uniforme | Funk, pop-rock, son "studio" |
| Après OD | Colle le sustain de la disto | Metal, solos, son sustain naturel |
| Seul (pas d'OD) | Sustain + makeup clean | Nile Rodgers, country, clean funk |

---

## LA Studio Comp = Teletronix LA-2A

**HX Effects model ID :** `HD2_CompressorLAStudioComp`

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **PeakReduction** | 0–1 | Taux de compression. Analogue au "Sensitivity" du Dyna Comp mais plus "musical" |
| **Gain** | 0–1 | Makeup gain (interne) |

### Caractère
Le LA-2A est un compresseur optique (tube + cellule optique). Son caractère est :
- **Plus transparent** que le Dyna Comp (moins de squish)
- **Compression progressive** qui s'adapte au signal
- **Attack et release automatiques** (pas de contrôle direct)
- Idéal pour un sustain naturel sans artefacts

### Sweet spots
| Contexte | PeakReduction | Gain | Notes |
|---|---|---|---|
| Clean boost naturel | 0.45–0.55 | 0.60 | Invisible mais efficace |
| Sustain solos | 0.65–0.75 | 0.65 | Solos qui "chantent" |
| Vocals guitar (fingerpicking) | 0.50–0.60 | 0.55 | Douceur et régularité |

**Différence Dyna Comp vs LA-2A :**
- Dyna Comp = squish évident, attaque marquée → Funk, country, son caractérisé
- LA-2A = compression douce, transparente → Rock, pop, son "studio propre"

---

## Noise Gate = Line 6 Original

**HX Effects model ID :** `HD2_GateNoiseGate`

Techniquement un "gate" (portereau) et non un compresseur, mais intimement lié.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Threshold** | -80 à 0 dB | Niveau en dessous duquel le signal est coupé |
| **Decay** | 0–1 | Vitesse de fermeture du gate. Bas = fermeture rapide (metal) ; haut = fermeture douce |

### Sweet spots
| Contexte | Threshold | Decay | Notes |
|---|---|---|---|
| Song clean/douce | -54 à -52 dB | 0.40 | Gate très discret, laisse les queues de reverb |
| Rock standard | -52 à -50 dB | 0.30 | Equilibré |
| Dist medium | -50 à -48 dB | 0.25 | Coupe le bruit entre les riffs |
| Metal / palm-muting serré | -48 à -46 dB | 0.18–0.20 | Gate agressif pour le tight |
| Fuzz | -50 à -48 dB | 0.28 | Plus de bruit résiduel avec fuzz |

**Placement :** Toujours en **premier slot** (slot 0). Le gate doit voir le signal brut
de la guitare, pas un signal déjà coloré ou saturé.

**Piège :** Un gate trop serré (Threshold trop haut) coupe les fins de notes et les queues
de reverb. Sur les sons clean ou avec reverb longue, utiliser un Threshold bas (-52 à -54 dB).

---

## Compression parallèle (NY Compression)

Technique studio adaptable sur HX Effects via le paramètre Mix du Red Squeeze.

**Mix=0.50** sur le Red Squeeze avec Sensitivity élevée (0.80+) :
- 50% signal sec (non compressé) + 50% signal très compressé
- Résultat : le transitoire d'attaque passe (du signal sec) + sustain compressé (du wet)
- Son très naturel avec du punch

Très utilisé en studio pour les guitares rythmiques qui doivent garder de l'attaque
tout en ayant du sustain et de la régularité.

---

## Sources
- MusicRadar — MXR Dyna Comp FX Files
- Traveling Guitarist — MXR Dyna Comp Tutorial
- Guitar Chalk — Nile Rodgers Amp Settings
- Origin Effects — Tech Tips : Compressors
- Expérience projet : Beggin' (Red Squeeze), Clara Luciani (Nile Rodgers style), Creep Stabs
