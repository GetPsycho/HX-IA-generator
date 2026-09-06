---
name: project-new-songs-batch
description: "Lot de 9 nouveaux morceaux ajoute (juin 2026) — termine, tag v3.3.0 cree"
metadata: 
  node_type: memory
  type: project
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

Eric a ajoute 9 nouveaux morceaux au repertoire (juin 2026), via le skill
`/new-preset` avec le pipeline audio_analysis v3.2.5 (sections + effets par
section) sur des FLAC deposes dans `audio_analysis/sources/`. **Lot termine
et tagge v3.3.0.**

Liste finale :
1. I'm Picky - Shaka Ponk — Mesa Rectifier -> KWB + Scream808 stacking
2. Just a Girl - No Doubt — patterns existants reutilises
3. Lithium - Nirvana — deja existant, audite conforme, rien a faire
4. Locked Out of Heaven - Bruno Mars — clean + chorus leger, style reggae_rock_pop
5. No Roots - Alice Merton — Keeley 1962X reelle d'Eric -> Heir Apparent
6. Not an Addict - K's Choice — un seul son, pattern grunge pousse
7. Special K - Placebo — 2 patterns existants combines
8. Take Me Out - Franz Ferdinand — nouvelle config funk+overdrive
9. The Man Who Sold the World - Nirvana (Unplugged) — PolyPitch + AcousGtrSim,
   corrige en 3 sons apres retour d'ecoute Eric (voir [[feedback_audio_analysis_vs_ecoute]])
10. Time Is Running Out - Muse — 4 sons structure crescendo (retour ecoute direct)

**Tag v3.3.0 cree** (commit e9ac65a et suivants) — voir `[[git_tagging_convention]]`
pour le format. Couvre rationalisation v2 "config partagee" + renommage
snapshots 3 lettres + ce lot complet de 10 presets.

## Why
Eric teste chaque preset en repet avant de valider definitivement — le lot
a ete traite un morceau a la fois via le skill new-preset (recherche ->
validation -> ecriture -> commit individuel), avec corrections post-ecoute
sur au moins un titre.

## How to apply
Ce lot est clos. Pour un futur lot similaire, reprendre le meme workflow
(skill new-preset + audio_analysis), et proposer un nouveau tag SemVer
(v3.4.0 ou v4.0.0 selon nature des changements) une fois le lot complet,
sauf indication contraire d'Eric.
