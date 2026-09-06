---
name: feedback-audio-analysis-vs-ecoute
description: "L'oreille d'Eric prime sur les metriques de saturation de l'analyse audio quand il y a conflit"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

Quand l'analyse audio (pipeline `audio_analysis`) indique une saturation
"high"/"extreme" sur une section qu'Eric identifie a l'oreille comme clean/folk,
**faire confiance a l'ecoute d'Eric**, pas a la metrique automatique.

## Why
Cas concret : The Man Who Sold the World (Nirvana, MTV Unplugged). L'analyse
audio donnait une saturation constante 0.69-0.85 ("high"/"extreme") sur tout
le morceau, ce qui a conduit a proposer un preset avec un seul son actif
(DS-2 + Small Clone always-on). Eric a corrige : il y a en realite 3 sons
distincts — Intro/Solo avec DS-2 subtil, et un **Verse purement acoustique
sans DS-2** que l'algo ne distinguait pas. Le metrique `harmonic_ratio`-based
de saturation peut lire un fort harmonic_ratio sur du fingerstyle/strumming
acoustique resonant comme "saturation elevee" sans qu'il y ait de pedale de
distorsion impliquee — ce n'est pas fiable pour distinguer clean vs distordu
sur des passages acoustiques/folk.

Idem pour la modulation/chorus : Eric a retire un Small Clone que l'analyse
(et la doc gear generale de Cobain/Unplugged) suggerait, simplement parce
qu'il ne l'entend pas sur ce titre precis.

## How to apply
- Presenter l'analyse audio comme une **hypothese de depart**, pas une
  verite a appliquer aveuglement, surtout sur des morceaux acoustiques/folk
  ou la metrique de saturation est connue pour etre moins fiable.
- Quand Eric donne un retour d'ecoute direct contredisant l'analyse
  (structure en plus de sons, effet absent, etc.), corriger immediatement
  et documenter la correction dans la fiche morceau / docstring (mentionner
  "confirme a l'ecoute" plutot que de s'appuyer uniquement sur le JSON).
- Voir `[[project_new_songs_batch]]` pour le contexte du lot de presets en cours.
