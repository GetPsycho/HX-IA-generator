---
name: feedback-polypitch-dsp-budget
description: "PolyPitch consomme jusqu'a 50% du budget DSP HX Effects - limite le nombre de blocs combinables, bloc Gain pur comme contournement"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

**Poly Pitch (`L6SPB_PolyPitch`) consomme jusqu'a 50% du budget DSP** d'un
preset HX Effects, confirme par le manuel Line 6 et par test live (juin 2026).

## Why
Eric a teste Lithium (7 blocs avec PolyPitch) et Drive (8 blocs avec PolyPitch) :
les deux s'importaient comme des presets "vides" (aucun bloc visible dans la
chaine), sans erreur explicite. Le JSON genere etait structurellement valide
(verifie en profondeur, decodeur du projet, diff position par position avec
des presets fonctionnels) — ce n'etait pas un bug de code, mais une vraie
contrainte materielle. Eric a trouve la cause exacte dans le manuel HX et
confirme via l'interface HX Edit (les blocs deviennent grises/non-ajoutables
quand le budget est sature).

**Seuil empirique** : avec PolyPitch present, le preset tient a ~5-6 blocs
au total (Poly Pitch inclus) si les autres blocs sont des pedales modelisees
(KinkyBoost, Big Muff, etc.). Special K (5 blocs) marche. Lithium/Drive a
7-8 blocs avec un bloc modelise supplementaire ne marchaient pas.

**Solution validee** : remplacer un bloc modelise non-essentiel par
`HD2_VolPanGain` ("Gain", categorie volumepan, un seul parametre Gain en dB) —
un simple utilitaire volume sans modelisation de circuit, donc quasi nul en
cout DSP. En testant ce remplacement, Lithium (7 blocs, Gain au lieu de
KinkyBoost) ET Drive (8 blocs, Gain au lieu de KinkyBoost) fonctionnent avec
PolyPitch actif. Compromis : on perd la coloration harmonique de la pedale
(ex: KinkyBoost "Color clean Verse" = harmoniques chaudes), on garde juste
le bump de volume.

## How to apply
- Avant d'ajouter Poly Pitch a un preset existant : compter le nombre total
  de blocs (Poly Pitch inclus). Si ≥6-7, ne pas ajouter sans verifier d'abord,
  ou retirer/alleger un autre bloc.
- Si un preset avec PolyPitch a besoin d'un boost de volume mais que le
  budget DSP est tendu : utiliser `HD2_VolPanGain` (bloc "Gain" pur) plutot
  qu'une pedale modelisee (KinkyBoost, OCD, etc.) pour ce role precis.
- Toujours regenerer ET faire tester en live avant de considerer un ajout
  PolyPitch comme acquis — le bug ne se voit pas dans le JSON, seulement
  a l'import reel sur l'appareil/HX Edit.
- Documentation complete dans `docs/pedal_guides/hx_models_reference.md`
  (section "Poly Pitch — limite DSP critique").
- Voir aussi `[[project_new_songs_batch]]` pour le contexte (lot ou PolyPitch
  a ete ajoute a plusieurs presets via un footswitch utilitaire).
