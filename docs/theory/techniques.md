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

### Funk / Nile Rodgers (Dyna Comp)
- Sensitivity : 0.6–0.75 (compression bien présente mais pas excessive)
- Level : +3 à +6 dB de makeup
- Le "squish" caractéristique des accords grattés (chucking) vient de là
- Couplé à une Strat neck pickup → son clean funk articulé

### Compresseur avant OD
- Signal régularisé → l'OD reçoit un signal plus uniforme
- Les notes fortes et faibles saturationnent pareil → son plus "studio"
- Moins de dynamique de jeu (peut être perçu comme négatif ou positif)

### Compresseur après OD
- Contrôle le volume de sortie de la disto
- Ajoute du sustain à la fin de la chaîne de gain
- Le sustain de la disto est "collé" et prolongé
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

Un signal propre est intrinsèquement moins présent qu'un signal distordu
(la disto ajoute des harmoniques = énergie perçue accrue).

Solutions pour compenser un snapshot clean face à un snapshot distordu :
1. **Red Squeeze** (Dyna Comp) : compression + makeup gain = snapshot clean présent
2. **Kinky Boost** (EP Booster) : preampli chaud, ajoute corps et harmoniques
3. **volume_offset_db** du PresetBuilder : décale tout le preset de N dB en sortie
4. **VolPanGain** : boost dB pur — efficace mais sans couleur

---

## Sources
- MusicRadar — Gain Stacking, Pedal Order
- Premier Guitar — Overdrives, Distortions and Boosts
- Guitar World — Signal Chain, Dotted 8th technique
- BOSS Articles — Pedal Partners (Phaser, Distortion)
- Origin Effects — Compressor Placement Tech Tips
- Sound on Sound — Roger Mayer sur Hendrix
- Expérience projet : Creep (stabs + compresseur), Be Yourself (boost clean), Dani California (AutoFilter placement)
