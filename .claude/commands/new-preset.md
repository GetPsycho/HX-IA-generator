Crée un nouveau preset HX Effects pour : $ARGUMENTS

Suis ces étapes dans l'ordre strict. Ne modifie aucun fichier avant l'étape 4.

---

## 1. Recherche

### Fiche guitariste
Vérifie si une fiche existe dans `docs/guitarists/` pour le guitariste concerné.
- **Si elle existe** : lis-la pour t'imprégner du son, du matos et des sons par titre.
- **Dans tous les cas** : fais une recherche web ciblée sur **ce titre spécifiquement**
  (pas seulement le guitariste en général). Sources : equipboard, guitargearfinder,
  groundguitar, guitarchalk, musicstrive, neuraldsp, Premier Guitar, Guitar World.
  Cherche : guitare utilisée sur CE titre, pédales actives par section, ampli,
  structure du morceau côté guitare (intro/verse/chorus/solo), sons par section.
- **Si la fiche est absente ou incomplète pour ce titre** : crée/complète
  `docs/guitarists/<nom>.md` (guitares, amplis + réglages, pédales, chaîne signal,
  sons par titre, sources).

---

## 2. Analyse — à exposer à l'utilisateur AVANT tout

Présente et justifie les 4 points suivants. **Attends la validation avant de passer à l'étape 3.**
Justifie chaque choix par rapport à ce que la recherche a révélé.

### Parties guitare et snapshots
- Liste les sections du morceau et le son par section
- Détermine le nombre de snapshots (max 4) et le rôle de chacun

### Sélection des pédales
- Identifie les pédales réelles du guitariste sur ce titre
- Trouve les model IDs HX les plus proches (consulte `data/catalog/models_catalog.json`)
- Consulte `docs/pedal_guides/` pour les paramètres de référence
- **Consulte `docs/gear/eric_gear.md`** pour les incidences du matériel d'Eric sur le son
  (Super Distortion chevalet = haute sortie, Mesa Boogie clean = tight/brillant,
  micro manche single-coil pour solos, micro milieu pour funk)
- **Règle d'architecture — répliquer le flux signal original :**
  - Saturation venant d'une pédale togglée → `enabled_default=False`
  - Saturation venant d'un canal d'ampli permanent (pas de canal clean, pas de pédale OD) →
    bloc toujours actif, Gain variable par snapshot. Choisir la pédale HX dont le
    caractère correspond le mieux à cet ampli (consulte la table de simulation ampli
    dans `docs/pedal_guides/od_dist_fuzz.md`). Si c'est un nouveau matching ampli→pédale,
    le documenter dans ce fichier.

### Style
- Assigne les styles depuis `docs/theory/eras_and_styles.md`
- Si un style utilisé n'existe pas encore dans ce fichier → l'ajouter

### Techniques utilisées
- Volume compensation clean vs saturé : consulte `docs/theory/techniques.md`
  (section "Volume en Live"). Ajouter KinkyBoost (Drive=0, Boost=True) sur les snaps
  clean/quasi-clean, sauf si le contraste dynamique est intentionnel (ex: Lithium).

### Référence de volume — règle absolue
Le snap **Clean** (Gate + Reverb seule, utilisé pour l'accordage) est la **référence
de niveau 0 dB** du rig d'Eric. Tous les snaps distorsion/overdrive doivent s'aligner
sur ce niveau. C'est la référence commune à **tous les presets**.

**Si une pédale de saturation baisse le volume sous le snap Clean :**
→ Ajouter un KinkyBoost always-on (Drive=0, Boost=True) après la reverb,
  actif sur tous les snaps distorsion, **exclu du snap Clean**.

**Cas connu — Arbitrator Fuzz (`HD2_DistArbitratorFuzz`)** :
Déficit d'output structurel — même au Level=1.0 (max), le signal reste sous
le niveau clean. Fix validé : Level=0.90 + KinkyBoost always-on.
Voir `docs/pedal_guides/hx_models_reference.md` (section Notes Arbitrator Fuzz).

---

## 3. Validation utilisateur

Attends l'accord explicite avant de toucher les fichiers.

---

## 4. Écriture des fichiers

### Fiche guitariste
Crée ou met à jour `docs/guitarists/<nom>.md`. Si la recherche révèle des infos
nouvelles sur un titre déjà documenté, mettre à jour la fiche.

### Preset
Ajoute `preset_<nom_snake_case>()` dans `presets/songs.py` :
- Docstring : artiste, tempo, description chaîne signal, rôle de chaque snapshot,
  justifications clés (ex: "OCD always-on = canal gain JCM800 permanent")
- `PresetBuilder(name, tempo, styles=[...])` avec les styles identifiés
- `add_block()` pour chaque effet dans l'ordre de la chaîne signal
- `add_snapshot()` avec `blocks_on`, `params` si variation par snap, `color`
- Entrée dans le dict `PRESETS` au format `"Titre - Artiste"`

---

## 5. Génération et vérification

Lance `python presets/generate_presets.py` et vérifie l'absence d'erreur ou WARNING.

---

## 6. Commit

Message : `Titre - Artiste : preset + fiche <guitariste>`
Inclure les changements clés (chaîne, snaps, matching ampli si nouveau).
