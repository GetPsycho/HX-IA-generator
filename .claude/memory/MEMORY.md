# Mémoire du projet hx-setlist-generator

- [Gear d'Eric](user_gear.md) — Stratocaster US, Super Distortion bridge, micro milieu funk pur / bridge funk-rock, Mesa Boogie clean, wah MC404 CAE externe
- [Cohérence des volumes](feedback_volumes.md) — règles dans new-preset.md + hx_models_reference.md (Arbitrator Fuzz déficit output)
- [Justifications avec sources](feedback_justification_sources.md) — toujours inclure les URLs quand on justifie un choix de preset
- [Accordage : source Ultimate Guitar](feedback_tuning_source.md) — utiliser UG en priorité pour confirmer l'accordage
- [Configs pédales partagées](shared_pedal_configs.md) — pointeur vers `docs/theory/shared_configs.md` (source de vérité projet, patterns sonores réutilisés inter-presets)
- [Convention de tags git](git_tagging_convention.md) — jalons annotés (v0/v1/v2/v3.2.5), SemVer depuis v3.2.5, toujours demander avant de tagger
- [Lot 9 nouveaux morceaux](project_new_songs_batch.md) — terminé, tag v3.3.0 créé (22 juin 2026)
- [Écoute > analyse audio](feedback_audio_analysis_vs_ecoute.md) — en cas de conflit, faire confiance à l'oreille d'Eric (saturation acoustique = faux positifs algo)
- [Limite DSP PolyPitch](feedback_polypitch_dsp_budget.md) — PolyPitch = jusqu'à 50% du budget DSP, max ~5-6 blocs ; utiliser HD2_VolPanGain au lieu d'une pédale modélisée si budget tendu
- [Footswitch Auto Color](feedback_footswitch_auto_color.md) — Auto Color ne se recalcule qu'à l'ouverture manuelle d'un bloc ; couleur pilotée par @fs_customcolor selon catégorie (mapping confirmé)
- [Convention EXP1 = Volume](feedback_exp1_volume_convention.md) — injection automatique (PresetBuilder.build()) d'un bloc Volume sur EXP1 partout sauf conflit (Whammy) ou 8 blocs déjà atteints ; ne pas l'ajouter manuellement dans preset_*()
- [Sauvegarde memory dans le repo](feedback_memory_backup_habit.md) — recopier systématiquement vers .claude/memory/ + commit à chaque changement de mémoire ; pousser régulièrement sur origin
