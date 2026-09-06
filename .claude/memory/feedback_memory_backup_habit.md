---
name: feedback-memory-backup-habit
description: "Recopier les fichiers memory vers .claude/memory/ du repo et committer, systematiquement"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fca108e8-2cd8-416e-8724-e65c548d4fcd
  modified: 2026-09-06T20:38:32.993Z
---

Chaque fois qu'un fichier memory est cree ou modifie dans
`~/.claude/projects/c--Users-ericf-repository-hx-setlist-generator/memory/`,
le recopier vers `.claude/memory/` dans le repo du projet et committer
(pas besoin de demander a chaque fois — habitude systematique).

## Why
La memoire auto de Claude Code est stockee localement uniquement, sans
synchro cloud (confirme via doc officielle). Une reinstallation, un
changement de PC, ou un formatage ferait perdre tout l'historique de
memoire (gear, conventions, feedback accumule) si rien n'est versionne.
Le repo git est deja pousse sur GitHub (`origin/master`), donc y copier
la memoire la met a l'abri.

## How to apply
- Apres toute ecriture/mise a jour d'un fichier dans le dossier memory
  (nouveau fichier ou edition d'un existant), copier ce fichier vers
  `.claude/memory/<meme nom>.md` dans le repo, `git add`, et committer
  avec un message court (ex: "Sauvegarde memory : <sujet>").
- Ne pas grouper artificiellement — un commit par mise a jour de memoire
  est acceptable, ou grouper si plusieurs fichiers memory changent dans
  la meme session.
- Si le repo n'a pas ete pousse depuis un moment (verifier `git log
  origin/master -1` vs `git log -1`), le signaler et pousser — Eric a
  confirme vouloir un push regulier plutot que de laisser trainer des
  commits locaux non pousses (episode du 2026-09-06 : 203 commits de
  retard sur origin, remonte a mai).
