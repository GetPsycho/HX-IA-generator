---
name: feedback-exp1-volume-convention
description: "EXP 1 est maintenant reservee par defaut a une pedale de volume sur tous les presets, injectee automatiquement par PresetBuilder.build()"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

Eric a une seule pédale d'expression physique branchée sur le HX Effects.
Convention établie (juin 2026) : **EXP 1 = pédale de volume par défaut**
sur tous les presets, sauf ceux où EXP 1 est déjà utilisée pour autre
chose (Whammy/Pitch Wham sur Killing in the Name et He-Man Woman Hater).

## Why
Eric veut pouvoir ajuster le volume en live "si besoin" sur n'importe
quel morceau sans avoir à modifier chaque preset un par un. Plutôt que
de toucher les ~33 fonctions `preset_*()` une par une (risque d'erreurs
mécaniques répétées), la solution adoptée est **au niveau du framework** :
`PresetBuilder._maybe_add_exp_volume()` (appelée en tout début de
`build()`) injecte automatiquement un bloc en fin de chaîne, toujours
actif sur tous les snapshots, bindé à EXP 1.

**Itération 2** (suite retour Eric) : un bloc Volume classique
(`HD2_VolPanVol`, param "Pedal" 0-1) ne peut qu'**atténuer** (talon=plein,
pointe=silence) — pas de boost possible au-dessus du volume par défaut.
Eric voulait l'inverse : pouvoir **monter** le volume au-dessus du
défaut. Remplacé par `HD2_VolPanGain` (param "Gain", plage catalogue
-120/+12 dB), avec la pédale EXP restreinte à une **plage custom 0 à
+6 dB** (`EXP_VOLUME_BOOST_DB = 6.0`) via le nouveau paramètre
`range_min`/`range_max` de `bind_exp_pedal()` — talon = 0 dB (neutre,
aucun changement), pointe = +6 dB (boost). Sans cette restriction, balayer
toute la plage catalogue (-120 à +12) aurait fait du talon un quasi-mute,
pas une position neutre.

La méthode skip automatiquement si :
- EXP 1 est déjà bindée à un autre paramètre dans le preset (whammy, etc.)
- Le preset est déjà à 8 blocs (`MAX_BLOCKS`), le maximum HX Effects

34 presets sur 36 ont reçu le bloc. Seuls 2 exclus, pour conflit EXP1
(Killing in the Name, He-Man Woman Hater).

**Correction MAX_BLOCKS** : `MAX_BLOCKS` était fixé à 8 dans
`preset_builder.py`, alors que le HX Effects supporte réellement **9
blocs** (slots 0-8, cf. `new-preset.md` : "Slots : 9 blocs disponibles,
indices 0 à 8"). Bug corrigé (Eric a posé la question "mais c'est pas 9
blocs le max ?").

**Mais 9 blocs reste instable pour certaines combinaisons** : après le
fix, Drive et Black Hole Sun (8 blocs avant, 9 après ajout du volume) se
sont avérés instables à l'import en test live (même symptôme que le
budget DSP PolyPitch — preset qui ne charge pas correctement). Solution :
nouvelle méthode `PresetBuilder.disable_exp_volume()`, appelée
explicitement dans `preset_drive()` et `preset_black_hole_sun()` pour les
exclure de l'injection auto et les ramener à 8 blocs. Donc le plafond
hardware théorique (9) ne garantit pas qu'un preset à 9 blocs fonctionne
toujours — dépend de la combinaison de modèles (DSP réel), pas juste du
compte de slots.

## How to apply
- **Ne pas ajouter manuellement** de bloc Volume + `bind_exp_pedal` dans
  une fonction `preset_*()` — c'est géré automatiquement par le framework.
- Si un nouveau preset doit utiliser EXP 1 pour un effet pitch/whammy
  (comme Killing in the Name), le binding explicite dans la fonction
  `preset_*()` prend le pas et désactive l'injection automatique du
  volume pour ce preset — c'est le comportement voulu, pas un bug.
- Si un preset à 8-9 blocs devient instable après ajout du volume (preset
  vide/non chargé à l'import — toujours vérifier en test live, jamais
  visible dans le JSON), appeler `pb.disable_exp_volume()` dans sa
  fonction `preset_*()` plutôt que de retirer un bloc existant sans
  validation Eric (cas Drive/Black Hole Sun).
- Voir aussi `[[feedback_polypitch_dsp_budget]]` pour la contrainte DSP
  distincte (budget PolyPitch) qui limite differemment le nombre de blocs
  utilisables — les deux contraintes (PolyPitch et "9 blocs instable")
  se ressemblent (preset qui ne charge pas) mais ont des causes separees.
