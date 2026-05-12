# Delay — Guide des Paramètres

## Rôle du Delay Guitare
- **Épaississement** (répétitions très courtes, < 50 ms) — slapback, pseudo-double-tracking
- **Rythme** (répétitions synchro au tempo) — The Edge style, groove
- **Espace** (répétitions longues, feedback élevé) — son ambient, post-rock
- **Sustain** (pseudo-reverb) — delay court avec feedback modéré

---

## Simple Delay = Line 6 Original

**HX Effects model ID :** `HD2_DelaySimpleDelay`

Le Simple Delay est le delay de base du HX Effects — pas de "coloration" vintage,
répétitions propres et fidèles. Idéal quand on veut de la fonctionnalité sans caractère.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Time** | 0–2 s (ou en divisions si TempoSync) | Temps entre les répétitions. Valeur en secondes si TempoSync=False |
| **Feedback** | 0–1 | Nombre de répétitions. 0 = une seule répétition ; 0.5 = plusieurs répétitions qui diminuent ; 0.9+ = quasi-infini (attention aux feedbacks incontrôlés) |
| **Mix** | 0–1 | Volume des répétitions par rapport au signal sec |
| **TempoSync1** | True/False | **True** = Time s'exprime en fraction du tempo ; **False** = Time en secondes absolues |

### Quand utiliser TempoSync=False
Sur tous les presets du projet, `TempoSync1: False` est utilisé pour contrôler
le temps précisément en secondes — indépendamment du tempo du preset.
Si TempoSync=True, le delay change de caractère si le tempo change.

---

## Slapback — Technique Fondamentale

Un délai très court (50–150 ms) avec **Feedback=0** (une seule répétition).
Son effet : épaississement, présence, sensation de "double-tracking" naturel.

```
Time: 0.08 à 0.12 s (80–120 ms)
Feedback: 0.0 (une seule répétition)
Mix: 0.15–0.25
```

**Usages :**
- Rockabilly / Country : slapback 80–120 ms, Mix 0.20
- Rock 50s/60s : Elvis, Eddie Cochran, Gene Vincent
- Solos rock : donne de la "colle" sans noyer le son dans les répétitions
- **Black Hole Sun Solo** : slapback 80 ms pour distinguer le Solo du Refrain

**Calcul du slapback :**
```
Perçu naturel   : 60–100 ms (presque imperceptible)
Perçu distinct  : 100–150 ms (echo discret)
Ambiant/doubleur: 180–250 ms
```

---

## Sweet spots par Contexte

| Contexte | Time | Feedback | Mix | TempoSync | Notes |
|---|---|---|---|---|---|
| Slapback (BHS Solo) | 0.08 | 0.0 | 0.18 | False | Une répétition = son plus large que reverb |
| Slapback rockabilly | 0.10 | 0.0 | 0.22 | False | Plus distinct |
| Delay court (AYGGMW Solo) | 0.12 | 0.0 | 0.22 | False | Slapback légèrement plus long |
| Delay medium (Even Flow Solo) | 0.29 | 0.12 | 0.18 | False | Quelques répétitions, très discret |
| Delay Verse moyen | 0.35 | 0.25 | 0.20 | False | Delay discret, sustain prolongé |
| Delay The Edge style | 0.375 | 0.45 | 0.28 | False | 375 ms = dotted 8th à 120 BPM |

---

## Technique : Dotted 8th Note Delay (The Edge — U2)

Delay syncopé : les répétitions tombent sur les contretemps.
En jouant des noires régulières, les répétitions créent une rythmique complexe.

**Calcul :**
```
dotted 8th (ms) = (60000 / BPM) × 0.75

Exemples :
80 BPM  → 562 ms
100 BPM → 450 ms
120 BPM → 375 ms
140 BPM → 321 ms
```

**Réglage sur Simple Delay :**
```
Time: [valeur calculée en secondes]  ex. 0.375 pour 120 BPM
Feedback: 0.40–0.55
Mix: 0.25–0.35
TempoSync1: False
```

---

## Placement Delay dans la Chaîne

```
Guitare → Gate → OD/Dist → Modulation → Delay → Reverb
```

**Delay avant Reverb (standard) :** Les répétitions du delay entrent dans l'espace
de la reverb → son naturel, les répétitions ont de la queue.

**Delay après Reverb (rare) :** La reverb complète (avec sa queue) est répétée →
résultat très dense, difficile à contrôler — effet expérimental.

**Delay avant Modulation :** La modulation affecte les répétitions → effet inhabituellement
espacé. Possible mais rare.

---

## Interaction Delay et Gain Stacking

**Delay après une OD :** les répétitions sont "propres" (pas re-saturées).
Le signal sec est distordu, les répétitions sont nettes → contraste.

**Delay avant OD (rarissime) :** les répétitions repassent dans l'OD → coloration
progressive des répétitions. Son très instable, éviter sauf effet voulu.

---

## Bucket Brigade = analog delay (legacy DL4)

**HX Effects model ID :** (DL4 models — ex. `HD2_DL4BucketBrigade`)

Non utilisé dans le projet actuellement. Caractère : répétitions plus chaudes/dégradées
que le Simple Delay, avec un léger filtrage des hautes fréquences sur chaque répétition
(comportement des chips BBD analogiques). Plus "vintage", répétitions qui s'effacent
naturellement. Idéal quand on veut un delay avec caractère de couleur.

---

## Sources
- Guitar World — Delay Settings and Techniques
- Premier Guitar — The Edge U2 Delay
- TC Electronic — Understanding Delay Types
- Expérience projet : Black Hole Sun (slapback Solo), Even Flow (delay Solo), Are You Gonna Go My Way (slapback Solo)
