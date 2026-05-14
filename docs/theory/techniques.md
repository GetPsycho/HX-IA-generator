# Techniques Avancées et Astuces

## Gain Stacking — Combos Classiques

### Principe
Empiler deux pédales de saturation produit un son plus complexe que l'une ou l'autre seule.
L'ordre importe : du moins saturé vers le plus saturé.

### Combos incontournables

| Combo | Ordre | Résultat | Artistes |
|---|---|---|---|
| TS9 → Big Muff | OD → Fuzz | TS tightens le bas, la fuzz gagne du punch et de la chaleur | Smashing Pumpkins |
| Klon → OCD | Boost → OD | Klon pousse les mids, l'OCD sature plus harmonieusement | Maneskin, John Mayer |
| Klon → JCM800 | Boost → Amp | Klon pousse le préampli de l'ampli sans l'écraser | Blues-rock classique |
| TS9 → Marshall | OD → Amp | Tightens le bas du Marshall, mid-honk emblématique | Metal moderne, Zakk Wylde |
| EP Booster → OD | Preampli → OD | Plus de sustain harmonique, l'OD "chante" mieux | Rock classique, solos |
| OCD → Dist haute gain | OD → Dist | L'OCD façonne les fréquences avant la dist | Lead heavy |
| Red Squeeze → OD | Comp → OD | Signal régularisé → OD sonne plus uniforme | Funk-rock, Chili Peppers |

### OD + Fuzz : deux philosophies

**OD avant Fuzz :**
- L'OD nourrit la fuzz avec un signal chaud et compressé
- La fuzz sonne plus épaisse, plus tenue, moins chaotique
- Le bas est "tight", le sustain est long
- Exemple : TS9 (Drive bas, Level haut) → Big Muff → ampli clean

**Fuzz avant OD :**
- La fuzz donne tout son chaos, l'OD "nettoie" et structure en sortie
- Plus de volume général, l'OD pousse l'ampli plus fort
- Son différent : plus "sauvage" en entrée, plus structuré en sortie

### Boost avant vs après OD

```
Boost → OD → Ampli    : plus de saturation harmonique, son plus épais
OD → Boost → Ampli    : plus de volume de sortie seulement (solo boost)
```

**Boost avant OD** : le boost élève le niveau qui entre dans l'OD → l'OD répond plus fort
→ plus de saturation, de sustain, d'harmoniques. Change le caractère du son.

**Boost après OD** : augmente juste le volume de sortie, sans changer la saturation.
Idéal pour les solos : même son OD mais plus fort.

---

## Wah + Fuzz — La Question Hendrix

### Wah avant Fuzz (setup classique)
- Wah filtre le signal propre avant la fuzz → son plus "quacky" et vocal
- Mais : problème d'impédance avec les fuzzes germanium !
  - La wah a une haute impédance de sortie
  - La fuzz germanium a une basse impédance d'entrée
  - → Perte de fréquences, sweep réduit, ton mince

### Fuzz avant Wah (Hendrix inversé)
- Fuzz voit directement la guitare (haute impédance) → sonne mieux
- La wah filtre un signal déjà distordu → son plus "gras" et moins quacky
- Moins de problèmes d'impédance
- **Hendrix utilisait cet ordre sur certains titres** (Vox Wah → Fuzz Face)

**Règle pratique :** Essayer les deux. Sur HX Effects, pas d'impédance à gérer
(tout est numérique), donc l'ordre donne deux sons différents mais pas de problème technique.

---

## Compresseur — Techniques Spécifiques

### Toujours actif ("always on")
Un compresseur bien réglé se remarque surtout quand il est **éteint**.
Il maintient un niveau constant, ajoute du sustain, et régularise les attaques.

Réglage "invisible" : Sensitivity basse (0.3–0.4), Level neutre.

### Funk pur — micro milieu single-coil (Nile Rodgers, Frusciante)

Contexte : signal faible sortie → le compresseur travaille plus.

| Param | Valeur | Pourquoi |
|---|---|---|
| **Sensitivity** | 0.55–0.70 | Sortie single-coil faible → compression plus marquée nécessaire |
| **Level** | +2 à +5 dB | Makeup gain pour compenser la perte de volume de la compression |
| **Attack** (si dispo) | Lente–moyenne | Préserve le transitoire de picking — le "click" initial est fondamental en funk |

- Le **"squish"** caractéristique des accords grattés (chucking) vient d'une Sensitivity élevée
  qui écrase les crêtes puis relâche → rebond rythmique perceptible
- En funk, la **compression EST le son** — pas juste un outil de dynamique
- Modèles HX adaptés : **Red Squeeze** (MXR Dyna Comp, squish musical), **Kinky Comp**
  (Xotic SP, plus transparent et naturel)

**Réglage type micro milieu Eric :**
```
Red Squeeze : Sensitivity=0.62, Level=3.0, Mix=1.0
```

### Funk-rock — Super Distortion bridge + OD dans la chaîne

Contexte : signal haute sortie + pédale OD en aval → rôle du compresseur change.

```
Guitare (SD bridge) → Comp → OD → Ampli
```

| Param | Valeur | Pourquoi |
|---|---|---|
| **Sensitivity** | 0.45–0.55 | Sortie élevée → moins de compression pour ne pas tuer le punch |
| **Level** | +1 à +2 dB | Makeup modéré — l'OD en aval remonte le niveau de toute façon |
| **Attack** | Lente | Même logique : laisser passer le transitoire de picking |

Le compresseur ici remplit un rôle de **"tightening"** : il régularise le signal chaud
du Super Distortion **avant** qu'il entre dans l'OD, pour que l'OD réponde de façon
uniforme quelle que soit la force de picking. Sans comp, l'OD est moins prévisible.

**Réglage type Super Distortion bridge Eric + OCD (Beggin' style) :**
```
Red Squeeze : Sensitivity=0.50, Level=2.0, Mix=1.0
```

### Distinction Red Squeeze vs Red Comp vs Kinky Comp

| Modèle HX | Pédale réelle | Caractère | Usage idéal |
|---|---|---|---|
| **Red Squeeze** | MXR Dyna Comp (HD2) | Squish musical, légère coloration | Funk pur, funk-rock comp+OD |
| **Red Comp** *(Legacy)* | MXR Dyna Comp (legacy) | Même circuit, rendu légèrement différent | Alternative à Red Squeeze |
| **Kinky Comp** | Xotic SP Compressor | Plus transparent, attaque plus naturelle | Toujours actif "invisible", country |

### Sortie du micro et Sensitivity : règle générale

Plus la sortie du micro est élevée, **moins** il faut de Sensitivity pour le même effet perçu.
Un humbucker haute sortie (Super Distortion ~13.7 kΩ) compressé à Sensitivity=0.60
sonnera étouffé et sans vie. Un single-coil milieu à Sensitivity=0.60 sonnera naturel.

| Micro | Sensitivity cible (funk) |
|---|---|
| Single-coil milieu/manche (Strat standard) | 0.55–0.70 |
| Humbucker standard (PAF, ~8 kΩ) | 0.50–0.60 |
| Humbucker haute sortie (Super Distortion, ~13.7 kΩ) | 0.45–0.55 |

### Compresseur avant OD
- Signal régularisé → l'OD reçoit un signal plus uniforme
- Les notes fortes et faibles saturent pareil → son plus "studio"
- Moins de dynamique de jeu (peut être perçu comme négatif ou positif)

### Compresseur après OD
- Contrôle le volume de sortie de la disto
- Ajoute du sustain à la fin de la chaîne de gain
- Risque : amplifie aussi le bruit de fond de la disto

### Slapback + Comp (Country)
Comp agressive (Sensitivity 0.8) + Slapback 80–140 ms (Feedback=0) + treble boost
= son "twang" country caractéristique (Albert Lee, Brad Paisley).

---

## Delay — Techniques

### Slapback (60–120 ms, Feedback=0)
Une seule répétition courte. Effet de présence et d'épaisseur sans écho distinct.
- Donne de la "colle" au son sans le noyer
- Très utilisé en rockabilly, country, rock'n'roll
- Sur HX : Time=0.08–0.12, Feedback=0.0, Mix=0.15–0.25

### Dotted 8th (The Edge — U2)
Delay réglé à 3/4 de la durée d'une noire (= dotted 8th note).
En jouant des noires régulières, les répétitions tombent sur les contretemps.
Crée une illusion de densité rythmique complexe.

**Calcul :**
```
dotted 8th (ms) = (60000 / BPM) × 0.75
Exemple : 120 BPM → 60000/120 × 0.75 = 375 ms
```

### Delay avant Reverb
Ordre canonique : Delay → Reverb.
Les répétitions du delay entrent dans l'espace de la reverb → son naturel.

Delay **après** Reverb : la reverb complète se répète → chaos, effet très particulier
(peut être artistiquement valide mais difficile à contrôler).

### Delay "pseudo-reverb"
Un delay court (100–200 ms, Feedback=0.3–0.5, Mix=0.3) peut remplacer
une reverb subtile avec plus de définition rythmique.

---

## Fuzz — Techniques Spécifiques

### Clean-up au volume guitare
Les fuzzes à transistors (germanium / silicon) réagissent au niveau d'entrée.
- Volume guitare à 10 → fuzz maximale, saturée
- Volume guitare à 6–7 → overdrive épais mais contrôlé
- Volume guitare à 3–4 → son quasiment propre mais avec du corps

C'est une technique de jeu essentielle pour la polyvalence sans changer de preset.

### Fuzz Factory — Gate pour le "gated fuzz"
Le paramètre `Gate` du Fuzz Factory (Industrial Fuzz sur HX) crée un effet
de coupure nette entre les notes. Gate élevé (0.6–0.75) = son saccadé caractéristique
(Plug In Baby de Muse, certains sons Queens of the Stone Age).
Gate bas = fuzz conventionnelle avec sustain naturel.

---

## Modulation — Placements Créatifs

### Phaser avant OD (Hendrix / Robin Trower)
- Le phaser sweape un signal propre → l'OD sature le signal phasé
- Résultat : le phaser est "intégré" dans le son distordu, moins évident
- Caractère plus "chaud" et organique

### Phaser après OD (placement standard)
- Le phaser sweape un signal déjà distordu
- Plus de "swoosh" évident, effet plus prononcé

### Tremolo avant Reverb
- Les coupures du tremolo sont nettes, la reverb vient après
- Entre deux "coups" de tremolo, silence relatif

### Tremolo après Reverb
- Les coupures interrompent la reverb → queue de reverb s'entend entre les coups
- Effet plus "spatial", moins sec

### Chorus + Reverb : shimmer
Chorus **après** Reverb : la queue de reverb est chorussée → shimmer ambiant.
Chorus **avant** Reverb : le chorus est "dans l'espace" de la reverb → plus naturel.

---

## Volume en Live — Compensation Clean vs Saturé

Un son clean aligné au VU avec un son distordu sonnera **2 à 4 dB plus faible**
à volume de scène. Le RMS du clean est intrinsèquement plus bas (crête ≠ sonie perçue)
et la distorsion génère des harmoniques dans la zone 2–5 kHz où l'oreille est la plus
sensible (Fletcher-Munson). Voir aussi `docs/theory/gain_staging.md`.

### Technique 1 — Kinky Boost après la reverb (recommandée)

```
Gate → OD → Reverb → KinkyBoost (Drive=0, Boost=True)
```

- Placement **après** la reverb : +6 dB de volume pur, sans modifier le son
- `enabled_default=False` : activé uniquement sur les snaps clean
- Drive=0 = pas de coloration / Boost=True = +6 dB interne
- **Règle absolue :** boost **après** l'OD = volume uniquement.
  Boost **avant** l'OD = change le taux de saturation.

### Technique 2 — Compresseur sur le snap clean

```
Gate → Compresseur → OD (off) → Reverb
```

- Red Squeeze : Sensitivity 0.45–0.55, Level +3 à +5 dB, Mix 1.0
- Remonte le RMS (niveau moyen) en réduisant les transitoires
- Résultat : le clean "tient" mieux dans un mix avec batterie/basse
- Attack lente recommandée : laisse passer le transitoire de picking (naturel)

### Technique 3 — EQ mid boost en complément

Un boost de médiums (1–2 kHz, +2–3 dB) améliore la **présence** dans le mix
sans augmenter le volume brut. À combiner avec le KinkyBoost ou le compresseur.

### Méthode de calibration pratique (ingés FoH)

1. Aligner les presets au VU en jouant rythmiquement (palm mute)
2. Ajouter **+2 à +4 dB supplémentaires** sur les snaps clean au-delà de l'égalité VU
3. Valider **en répétition avec le groupe complet** — jamais au casque seul
4. Écart acceptable entre presets : ±3 dB. Au-delà de 5 dB → corriger obligatoirement

### Quand NE PAS compenser

Le contraste clean/distordu est parfois voulu : **Lithium (Nirvana)**, philosophie
quiet/loud — le verse clean DOIT être plus faible. Ne pas compenser : la différence
de volume est le message musical.

Critère : si le delta de volume gêne le public ou noie la guitare dans le mix
→ compenser. Si le delta fait partie de l'arrangement → ne pas compenser.

---

## Sources
- MusicRadar — Gain Stacking, Pedal Order
- Premier Guitar — Overdrives, Distortions and Boosts
- Guitar World — Signal Chain, Dotted 8th technique
- BOSS Articles — Pedal Partners (Phaser, Distortion)
- Origin Effects — Compressor Placement Tech Tips
- Sound on Sound — Roger Mayer sur Hendrix
- Expérience projet : Creep (stabs + compresseur), Be Yourself (boost clean), Dani California (AutoFilter placement)
