---
name: shared-pedal-configs
description: Pointeur vers docs/theory/shared_configs.md — source de verite des configs de pedales partagees entre presets (rationalisation v2)
metadata: 
  node_type: memory
  type: reference
  originSessionId: f40a25e5-d184-42ae-8de8-c7cc690b0677
---

# Configs partagees entre presets

**Source de verite** : `docs/theory/shared_configs.md` dans le projet.

Ce fichier liste les patterns sonores recurrents (ex: "intro arpege grain leger",
"grunge bien pousse", "solo standard TS push") et les configs canoniques associees,
avec la table des presets/snaps qui partagent chaque pattern.

## Why

Eric refond progressivement les presets pour que chaque pedale ait une CONFIG FIXE,
et reutilise les memes settings sur plusieurs morceaux quand le caractere convient.
But principal : **propagation coordonnee**. Un ajustement valide en repet
(ex: "le son intro arpege est trop faible") doit pouvoir etre applique d'un coup
sur tous les presets qui partagent ce pattern.

## How to apply

1. Avant de creer/modifier une config de pedale, **lire `docs/theory/shared_configs.md`**
   pour verifier si un pattern existant correspond
2. Si Eric mentionne "comme sur X" / "config de Y" → c'est l'un de ces partages,
   reutiliser tel quel
3. Si Eric demande un ajustement sur un pattern → l'appliquer a TOUS les presets
   listes sous ce pattern, pas juste celui mentionne
4. Apres modification d'une config canonique : mettre a jour la table dans
   `docs/theory/shared_configs.md` et regenerer tous les presets impactes

## Lien

`docs/theory/shared_configs.md` est cite depuis les docstrings des presets refondus
(Dani California notamment) pour donner du contexte au lecteur du code.
