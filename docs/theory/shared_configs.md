# Configs de pédales partagées entre presets

## Objectif

Identifier des **patterns sonores** récurrents entre morceaux et **réutiliser la même config** de pédale partout où le pattern apparaît.

**Avantages** :
1. Un ajustement validé en répétition se propage à tous les morceaux qui partagent le pattern
2. Cohérence sonore inter-presets (le son "intro arpège grain léger" sonne pareil partout)
3. Moins de surface à calibrer (1 config par rôle au lieu de N copies divergentes)

**Règle 1** : avant de créer une nouvelle config pour une pédale, vérifier si un pattern existant correspond. Si oui, réutiliser tel quel. Sinon, créer un nouveau pattern et le documenter ici.

**Règle 2 — purisme du pattern** : quand on applique un pattern à un snap, on **retire les autres pédales de saturation/boost qui ne font PAS partie du pattern** (fuzz, OD, dist, boost). Le pattern définit ce qui doit être là, le reste sort. Exemple : si un preset utilise le pattern "Grunge bien poussé" (= OCD seul) et qu'il avait un KinkyBoost en sortie, le KinkyBoost dégage.

Les effets non-saturation (delay, reverb, modulation, filtre) peuvent rester librement — la règle vise uniquement les **fuzz / OD / dist / boost**.

Exceptions justifiables (à documenter dans la docstring du preset) : compensation volume très spécifique en répétition validée, caractère sonore particulier impossible à reproduire autrement.

---

## Patterns sonores et configs canoniques

### Pattern : "Intro arpège + grain léger"
*Strumming/arpèges sur son clair avec un peu de grain (style Bluesbreaker rolled back).*

**Pédale** : Heir Apparent (Analogman Prince of Tone)
**Config** : `Gain=0.20, Tone=0.50, Level=0.85`

| Preset | Snap |
|---|---|
| Be Yourself | Intro |
| Black Hole Sun | Intro |
| Dani California | Verse + Lick |
| Special K | Verse |

---

### Pattern : "Grunge bien poussé" (OCD seule)
*Saturation Marshall-like soutenue sans push externe permanent. Pour Chorus/Solo grunge ou alt-rock.*

**Pédale** : OCD (Compulsive Drive)
**Config** : `Gain=0.65, Tone=0.40, LPHP=True, Level=0.80`

| Preset | Snap |
|---|---|
| Creep | Stabs / Chorus / Solo |
| Dani California | Chorus / Solo |
| Hysteria | Riff / Chorus / Solo |
| I Wanna Be Your Slave | Verse / Chorus |
| Killing in the Name | Riff / Solo |
| Sex on Fire | Riff / Chorus |
| Travel The World | Verse / Bridge |
| Just a Girl | Riff (couvre Intro/Verse/Chorus/Bridge) |
| Not an Addict | Riff (seul son actif, tout le morceau) |
| Special K | Chorus |
| Time Is Running Out | Chorus / Bridge |
| Take Me Out | Riff |

---

### Pattern : "Rock direct" (OCD + Klon always-on en push)
*Rock direct avec gain stacking permanent (Klon en front pousse l'OCD).*

**Pédale** : OCD (Compulsive Drive)
**Config** : `Gain=0.65, Tone=0.35, LPHP=True, Level=0.80`

Différence vs "grunge bien poussé" : Tone=0.35 (encore plus adouci pour compenser le Super Distortion brillant + Klon mid-bump en push).

**Klon associé** : `Gain=0.40, Tone=0.45, Level=0.86`

| Preset | Snap |
|---|---|
| AYGGMW | Riff / Bridge / Solo |
| Even Flow | Principal / Solo |
| I'm Picky | Riff / Solo |

---

### Pattern : "TS push moment fort" (ex-"Solo standard")
*Faire ressortir un moment fort (Solo OU Chorus dynamique) sans modifier la dist principale. TS placé AVANT la dist principale.*

**Pédale** : Scream 808 (Ibanez TS808)
**Config** : `Gain=0.25, Tone=0.55, Level=0.92`

| Preset | Snap |
|---|---|
| AYGGMW | Solo |
| Be Yourself | Solo |
| Black Hole Sun | Solo |
| Creep | Solo |
| Dani California | Solo |
| Even Flow | Solo |
| Hysteria | Solo |
| I Wanna Be Your Slave | Chorus (1er cas hors Solo) |
| Killing in the Name | Solo (combiné avec Whammy +1 oct) |
| Sex on Fire | Chorus |
| Travel The World | Lick / Bridge |
| Just a Girl | Solo (combiné avec Pebble Phaser) |
| I'm Picky | Solo |

**Généralisation** : initialement nommé "Solo standard", ce pattern fonctionne pour tout snap qu'on veut "faire ressortir" — le Chorus dynamique d'IWBYS en est le 1er exemple. Le principe reste : TS push fait monter présence + volume sans toucher au caractère de la dist principale.

---

### Pattern : "Color clean Verse"
*Épaissir un clean coloré (harmoniques chaudes EP Booster) + +6 dB volume.*

**Pédale** : KinkyBoost (Xotic EP Booster)
**Config** : `Drive=0.35, Boost=True, Bright=False`

| Preset | Snap |
|---|---|
| Black Hole Sun | Verse |
| Creep | Verse |

---

### Pattern : "Clean brillant strumming"
*Son clair en strumming/arpèges avec caractère brillant (style Fender Super 60 rack, scintillant). +6 dB volume + boost aigus pour la définition.*

**Pédale** : KinkyBoost (Xotic EP Booster)
**Config** : `Drive=0.0, Boost=True, Bright=True`

| Preset | Snap |
|---|---|
| How You Remind Me | Verse / Arpèges |
| Locked Out of Heaven | Riff |

**Différence vs "Color clean Verse"** : pas de Drive (donc pas d'harmoniques chaudes), mais Bright=True ajoute des aigus = caractère "scintillant" plutôt que "épais".

---

### Pattern : "Heavy Dist Boss Metal Zone"
*Saturation metal massive, palm-muting tight (style Boss Metal Zone Legacy).*

**Pédale** : Heavy Dist (Boss Metal Zone, Legacy DM4)
**Config** : `Drive=0.70, Bass=0.80, Mid=0.40, Treble=0.55, Output=0.80`

| Preset | Snap |
|---|---|
| How You Remind Me | Chorus |
| Toxicity | Disto |

---

### Pattern : "Mur fuzz sombre Big Muff"
*Big Muff Ram's Head pour Chorus/Refrain grunge épais.*

**Pédale** : Bighorn Fuzz
**Config canonique** : `Sustain=0.80, Tone=0.55, Level=0.85`

| Preset | Snap |
|---|---|
| Black Hole Sun | Refrain / Solo |
| Lithium | Chorus |

**Historique** : Lithium avait une "variante" separee (Tone=0.45, Level=0.50,
plus sombre/moins fort), retiree au profit de la config canonique identique —
l'objectif du projet est un minimum de variation de volume entre presets.

---

## Patterns structurels (chaîne)

### Pattern "Solo standard"
TS (Scream 808) placé AVANT la dist principale + cette dist active (config fixe) + Reverb.
**Pas de delay** sauf cas spécifiques (tremolo picking Greenwood exclu après test).

### Pattern "Stabs grunge"
Boost OD agressif (Top Secret OD) placé AVANT la dist principale + KinkyBoost en sortie (+6 dB)
+ Gate Threshold override (-40 dB vs -50 default) pour couper le bruit de fond saturé.
**Pas de reverb** (sec).

### Ordre chaîne canonique
```
Gate > [boosts pre-dist] > [dist principale] > [modulation] > [color/boost post] > [delay] > Reverb
```

**Delay AVANT reverb** = ordre standard (delay génère les échos, reverb enveloppe l'ensemble).

---

## Workflow d'ajustement coordonné

Quand un test live révèle qu'un pattern n'est pas optimal (ex: "le son d'intro arpège est trop faible") :

1. Identifier le pattern concerné dans ce fichier
2. Ajuster la config canonique
3. Appliquer la nouvelle config **à TOUS les presets listés sous ce pattern**
4. Régénérer (`python presets/generate_presets.py`)
5. Mettre à jour la valeur dans ce fichier
6. Mentionner dans le commit que l'ajustement vient de la table partagée

C'est l'avantage principal de ce système : un ajustement = N presets cohérents.
