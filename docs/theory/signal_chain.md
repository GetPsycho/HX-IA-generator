# Ordre des effets et chaîne de signal

## Ordre canonique

```
Guitare
  → [1] Accordeur (Tuner)
  → [2] Wah / Filtre dynamique
  → [3] Compresseur
  → [4] Boost propre (EP Booster, Micro Amp)
  → [5] Overdrive léger (OD)
  → [6] Distorsion / Fuzz
  → [7] EQ (correcteur tonique)
  → [8] Modulation (Phaser, Flanger, Chorus, Tremolo, Rotary)
  → [9] Delay
  → [10] Reverb
  → Ampli
```

Cet ordre est une convention, pas une loi. Chaque dérogation produit un son différent.

---

## Pourquoi l'ordre compte

### Impédance d'entrée
Chaque pédale a une impédance d'entrée et de sortie. Un mauvais enchaînement
peut "charger" le circuit précédent et altérer le timbre — surtout avec les fuzzes
à transistors germanium, très sensibles à l'impédance en amont.

- **Fuzz germanium → Wah** : la fuzz sonne mieux si elle voit directement la guitare
  (haute impédance). Un buffer ou une wah avant la fuzz peut lui faire perdre son caractère.
- **Buffer anywhere else** : après la fuzz, un buffer est bénéfique pour conserver
  le signal sur des longues longueurs de câble.

### Saturation en aval vs en amont
Ce qui arrive **avant** la disto définit ce qui va être saturé.
Ce qui arrive **après** façonne le son saturé.

- Compresseur → OD : signal régularisé entre les notes → sonne plus "smooth"
- OD → Compresseur : la dynamique de la disto est compressée après coup → sustain
- Phaser → OD : le phaser sature avec les harmoniques, résultat "gras" et dense
- OD → Phaser : le phaser sweape un signal déjà distordu → plus classique, plus "propre"

### Le filtre reçoit ce qui vient avant
Une wah ou un AutoFilter réagit au **contenu fréquentiel** du signal qu'il reçoit.
- Wah après OD : la wah sweape le signal distordu → son "thick", moins quacky
- Wah avant OD : la wah sweape le signal propre → plus authentique et vocal
- AutoFilter après OD : l'envelope follower réagit à l'OD → ouverture plus dramatique

---

## Règles par catégorie

### Accordeur
Toujours en **premier**. Signal non-altéré = accord juste.

### Wah / Filtres dynamiques
**Conventionnellement avant** la disto. Exception notable : Jimi Hendrix mettait
sa Fuzz Face **avant** la Cry Baby — ce qui donne un son plus "chantant" et musical
mais moins quacky. Essayer les deux.

### Compresseur
Deux positions valables :
| Position | Effet |
|---|---|
| **Avant OD** | Signal régularisé → l'OD sonne plus uniforme, moins dynamique |
| **Après OD** | La compression "colle" le sustain de la disto, makeup gain possible |

Pour le son funk/pop (Nile Rodgers) : **compresseur seul**, très en amont.
Pour le metal serré : **gate avant disto**, parfois compresseur après pour le sustain.

### Boost (EP Booster, Micro Amp, Klon en mode boost)
- **Avant OD** : fait "chanter" l'OD différemment — plus de saturation harmonique,
  l'OD réagit à un signal plus fort. Résultat : ton plus épais, sustain augmenté.
- **Après OD** : augmente juste le volume de sortie. Pratique pour les solos (boost de solo).

### OD → Dist → Fuzz
Si on empile :
- L'ordre **OD puis Dist** est le plus commun (OD chauffe la Dist)
- **Dist puis OD** donne un son différent, plus "serré" en sortie
- **OD puis Fuzz** : l'OD nourrit la fuzz, plus de sustain et warmth
- **Fuzz puis OD** : l'OD "nettoie" et structure la fuzz, moins de chaos

### EQ
- **Avant OD** : l'EQ sculpte les fréquences qui vont être saturées (boost de mids → mid-crunch)
- **Après OD** : l'EQ corrige le son distordu (couper les basses d'une big muff qui noie le mix)
- Les deux positions sont valides selon l'objectif.

### Modulation (Phaser, Chorus, Flanger, Tremolo, Rotary)
**Après la disto** dans la grande majorité des cas.
Exceptions :
- Phaser avant OD : son plus "chaud", type Hendrix/Trower
- Tremolo avant reverb : les coupures sont nettes (pas de queue dans le reverb)
- Tremolo après reverb : les coupures laissent la queue réverbérer

### Delay
**Avant la reverb**. Le delay dans la reverb = plus naturel, comme un vrai espace.
La reverb dans le delay = le delay "répète" la reverb → chaos incontrôlé.

Exception créative : parfois le delay après la reverb donne un effet "shimmer" particulier.

### Reverb
**Dernier effet** dans la chaîne. La reverb représente l'espace acoustique dans lequel
tout le reste existe. Rien ne devrait venir après (sauf un volume de sortie ou un DI).

---

## Sur le HX Effects

**Les slots sont la chaîne de signal** — slot 0 = premier effet physiquement traversé.

```
block0 → block1 → block2 → ... → block8 → join → output
```

- Gate en slot 0 : toujours en premier pour couper le bruit dès l'entrée
- Reverb en dernier slot utilisé : respecte l'ordre canonique
- Si on veut Comp avant OD : Comp en slot N, OD en slot N+1

### Enabled_default et snapshot 0
Le bloc `@enabled` au chargement doit correspondre à l'état du snapshot 0.
Le fix dans `preset_builder.py` synchronise automatiquement cet état.

---

## Sources
- HX Effects Owner's Manual v3.80 (docs/pedal_mapping.md)
- Premier Guitar — Effects Signal Chain 101
- That Pedal Show — "Does Order Matter ?"
- Expérience accumulée sur ce projet (sessions de preset)
