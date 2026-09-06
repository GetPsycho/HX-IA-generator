---
name: git-tagging-convention
description: "Convention de tags git du projet (v0/v1/v2/v3.2.5) — jalons annotes avec changelog detaille, SemVer depuis v3.2.5"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

Le projet utilise des tags git annotes (`git tag -a`) comme jalons majeurs,
pas a chaque commit. Tags existants : v0, v1, v2, v3.2.5.

**Convention de message** : "vX.Y.Z - <resume court>" en premiere ligne,
puis un corps detaille "Etat depuis [tag precedent]" structure par categories
(ex: PRESETS, NOUVELLES FONCTIONNALITES TECHNIQUES, DOCUMENTATION, PROCESS),
avec Co-Authored-By: Claude Sonnet 4.6 si Claude a contribue.

**SemVer adopte a partir de v3.2.5** (v0/v1/v2 etaient MAJOR-only, pre-SemVer).
Regle annoncee dans le message du tag v3.2.5 lui-meme :
- patch (v3.2.x) : petites ameliorations/corrections
- minor (v3.x.0) : nouvelle fonctionnalite non-breaking
- major (vX.0.0) : breaking change

Tagger : "Tyler D. <get.psycho@gmail.com>" (meme identite que les commits).

## Why
Eric veut pouvoir reperer rapidement les jalons importants dans l'historique
sans avoir a parcourir des dizaines de petits commits. Les tags servent de
points de repere "etat stable / fonctionnalite complete", pas de release
au sens deploiement.

## How to apply
Ne PAS proposer de tag a chaque commit. Le proposer quand un ensemble
coherent de changements est termine (nouvelle fonctionnalite, gros lot de
presets, refonte de process). Toujours demander confirmation avant de creer
le tag (action visible/durable) et proposer un numero de version coherent
avec le SemVer. Voir `[[project_new_songs_batch]]` pour un cas concret recent
ou Eric a prefere attendre la fin d'un lot de travail avant de tagger.
