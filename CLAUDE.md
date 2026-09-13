# Contexte projet — pour reprendre une session à tout moment

Ce fichier est auto-chargé par Claude Code au démarrage d'une session dans
ce repo. Il permet de reprendre le fil même si l'historique de conversation
a disparu. Il est versionné dans git, donc disponible sur n'importe quelle
machine. Complément : `.claude/memory/` contient une copie brute et
systématique de la mémoire Claude Code (sauvegarde anti-perte, pas
auto-chargée — voir [feedback_memory_backup_habit.md](.claude/memory/feedback_memory_backup_habit.md)).

## Qui est l'utilisateur

Eric — guitariste. Gear complet dans `docs/gear/eric_gear.md` :
Stratocaster US (Super Distortion au chevalet, usage principal), Mesa
Boogie Single Rectifier 50W (son clair exclusivement), pas de 4CM, wah
Cry Baby MC404 CAE externe (avant le HX Effects, hors presets).

## Le projet en une phrase

Génère des presets HX Effects (Line 6) pour un répertoire de reprises, à
partir d'une analyse audio des morceaux originaux + du gear réel d'Eric.
Le skill `/new-preset` (`.claude/commands/new-preset.md`) pilote tout le
workflow : recherche → analyse audio → validation → écriture → commit.

## État au dernier commit (voir `git log` pour le détail exact)

Tag le plus récent : **v3.3.0** (lot de 9 nouveaux morceaux, juin 2026).
Depuis, ajouts ponctuels au coup par coup (pas encore taggés) : pédale de
volume EXP1 automatique sur les presets, fix couleurs de footswitch, et
plusieurs nouveaux presets (This Picture, Blur, He-Man Woman Hater...).
Se fier au code et aux fichiers `docs/` pour l'état exact des paramètres
(ex. la plage de boost EXP1 a été ajustée plusieurs fois — vérifier
`src/preset_builder.py` plutôt qu'une valeur figée ici).

## Conventions clés (détail dans `.claude/memory/`)

- **Sources dans les justifications** : toujours citer les URLs quand on
  justifie un choix de preset.
- **Accordage** : Ultimate Guitar en priorité.
- **Écoute > analyse audio** : en cas de conflit, faire confiance à
  l'oreille d'Eric (l'algo de saturation donne des faux positifs sur
  l'acoustique/folk résonant).
- **Configs partagées** : vérifier `docs/theory/shared_configs.md` avant
  de créer une nouvelle config de pédale ; propager les ajustements
  validés à tous les presets qui partagent le pattern.
- **Budget DSP PolyPitch** : jusqu'à 50% du budget DSP — max ~5-6 blocs
  au total si PolyPitch est présent ; utiliser `HD2_VolPanGain` (bloc
  Gain pur) plutôt qu'une pédale modélisée si le budget est tendu.
- **Footswitch en mode pédale** : ne jamais piloter la couleur via
  `@fs_ledcolor` (cosmétique, ne se recalcule qu'à l'ouverture manuelle
  du bloc) — utiliser `@fs_customcolor` avec le mapping catégorie→couleur
  confirmé sur l'appareil.
- **EXP1 = volume par défaut** : injecté automatiquement par
  `PresetBuilder.build()`, pas à la main dans `preset_*()`. Désactivé
  explicitement via `disable_exp_volume()` si instable (9 blocs) ou déjà
  utilisé pour un autre effet (whammy).
- **Tags git** : jalons majeurs seulement (pas à chaque commit), SemVer
  depuis v3.2.5, toujours demander confirmation avant de tagger.

## Maintenance de ce fichier et de la mémoire

- Chaque fois qu'un fichier est créé/modifié dans la mémoire locale Claude
  Code de ce projet (`~/.claude/projects/.../memory/`), le recopier vers
  `.claude/memory/` dans ce repo et committer — pas besoin de redemander,
  c'est une habitude systématique (détail dans
  [.claude/memory/feedback_memory_backup_habit.md](.claude/memory/feedback_memory_backup_habit.md)).
  Sinon `.claude/memory/` se désynchronise silencieusement et la
  sauvegarde perd son intérêt.
- Mettre à jour ce `CLAUDE.md` (section "État", "Conventions clés") quand
  quelque chose de notable change — pas à chaque micro-commit.
- Pousser sur `origin` régulièrement plutôt que de laisser traîner des
  commits locaux non poussés.

## Après une réinstallation / nouvelle machine

Cloner ce repo suffit à récupérer ce fichier (auto-chargé) mais **pas** la
vraie mémoire locale de Claude Code (`~/.claude/projects/.../memory/`,
hors repo, vidée par une réinstallation). Si cette session constate que
sa mémoire locale sur ce projet est vide/absente alors que
`.claude/memory/` contient des fichiers : proposer de les recopier vers
le dossier memory local pour restaurer le détail fin (au-delà du résumé
ci-dessus).

Ne reviennent pas non plus automatiquement (`.claude/settings.local.json`
est gitignoré) : les permissions auto-approuvées, à réaccorder une fois.

## Préférences de travail sur ce projet

- Bash/PowerShell/WebSearch/WebFetch : exécuter directement sans demander
  confirmation (`.claude/settings.json`).
