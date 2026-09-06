---
name: feedback-footswitch-auto-color
description: "Couleur des footswitches HX Effects en mode pedale — Auto Color ne se recalcule qu'a l'ouverture manuelle d'un bloc ; solution = Custom Color par categorie, mapping confirme"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

En mode pédale (stomp mode) sur le HX Effects, la couleur de la LED de
chaque footswitch peut être en **"Auto Color"** (calculée par categorie de
bloc) ou en **"Custom Color"** (`@fs_customcolor`, valeur fixe choisie).
Réglage visible dans HX Edit : Bypass/Controller Assign > bloc > Switch LED.

## Découverte clé : Auto Color ne se recalcule qu'à l'ouverture manuelle
Sur un **import frais** d'un preset (jamais ouvert dans HX Edit), le switch
en Auto Color reste bloqué sur la dernière valeur `@fs_ledcolor` écrite dans
le fichier JSON — la vraie couleur par catégorie ne se calcule/affiche
qu'**après avoir ouvert le panneau de réglages du bloc au moins une fois**
dans HX Edit. Conséquence pratique : nos presets générés et importés
directement (jamais "réveillés" bloc par bloc) affichaient tous la même
couleur (notre placeholder `@fs_ledcolor`), pas la vraie Auto Color —
inutilisable pour un usage live où les presets sont importés et joués
directement.

**Solution adoptée** : ne plus utiliser Auto Color. Écrire directement la
**vraie couleur Auto Color de chaque catégorie** en Custom Color
(`@fs_customcolor`), pour qu'elle soit correcte dès l'import, sans aucune
manipulation. Implémenté dans `_build_footswitch()` (`src/preset_builder.py`)
via `FS_CATEGORY_COLOR` (catégorie catalogue → nom couleur) et
`FS_CUSTOMCOLOR_INDEX` (nom → index).

## Mapping @fs_customcolor (index de la liste déroulante "Switch LED")
Confirmé par tests successifs sur l'appareil (Red=2, Blue=8 sur le même bloc) :

```
0=Auto Color, 1=White, 2=Red, 3=Dark Orange, 4=Light Orange, 5=Yellow,
6=Green, 7=Turquoise, 8=Blue, 9=Violet, 10=Pink, 11=Off
```

## Mapping catégorie catalogue → couleur Auto Color réelle
Relevé directement sur l'appareil (juin 2026), catégorie par catégorie,
après ouverture du panneau de chaque bloc pour forcer le calcul Auto Color :

| Catégorie catalogue | Couleur réelle |
|---|---|
| gate | Yellow |
| compressor | Yellow |
| eq | Yellow |
| distortion | Light Orange |
| reverb | Dark Orange |
| volumepan | Turquoise |
| pitch-synth | Violet |
| filter | Violet |
| delay | Green |
| modulation | Blue |

Catégories non testées (rares/absentes des presets actuels) : wah, preamp,
sendreturn, io, fixed — pas de couleur assignée, retombent en Auto Color
classique (même limitation "ouverture manuelle requise" si jamais utilisées).

## Particularité Custom Color
Une couleur Custom **persiste mais dimme** quand le bloc est bypassé (ex :
rouge vif actif → rouge terne inactif) — pas de changement de teinte
possible entre actif/inactif avec une seule valeur `@fs_customcolor`. C'est
pour ça que le mapping est par **catégorie de pédale**, pas par état
actif/inactif (cette idée initiale a été abandonnée — pas réalisable).

## How to apply
- Ne plus toucher à `@fs_ledcolor` pour piloter la couleur visible — c'est
  `@fs_customcolor` qui contrôle tout désormais. `@fs_ledcolor` reste écrit
  comme valeur cosmétique/inerte (`FS_COLOR_PLACEHOLDER`), sans effet réel.
  **Ne jamais mettre `@fs_ledcolor=0`** (= sélection littérale "Off",
  switch éteint) — toujours une valeur non nulle.
- Si un nouveau modèle de pédale utilise une catégorie catalogue absente de
  `FS_CATEGORY_COLOR`, demander à Eric de relever sa vraie couleur Auto
  Color sur l'appareil (ouvrir le panneau du bloc dans HX Edit) avant de
  l'ajouter au mapping — ne pas deviner.
- Les couleurs de **snapshots** (`@ledcolor` au niveau snapshot, mécanisme
  séparé, fixé à bleu standard sur demande Eric) ne sont pas concernées par
  cette limitation Auto Color — non remis en question.
- Voir aussi `[[feedback_polypitch_dsp_budget]]` et
  `[[feedback_exp1_volume_convention]]` pour d'autres cas où le JSON était
  structurellement valide mais où le comportement réel sur l'appareil ne
  correspondait pas aux attentes — toujours tester en live avant de
  considérer un changement de comportement comme acquis.
