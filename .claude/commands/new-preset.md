Crée un nouveau preset HX Effects pour : $ARGUMENTS

Suis ces étapes dans l'ordre strict. Ne modifie aucun fichier avant l'étape 4.

---

## 0. Preset déjà existant ? → Mode audit

Avant toute chose, cherche le titre dans `presets/songs.py` (dict `PRESETS` et fonctions `preset_*`).

**Si le preset existe déjà**, bascule en **mode audit** — ne pas recréer from scratch :

1. Lis le code de la fonction `preset_*` correspondante.
2. Audite-le contre **toutes les règles actuelles** du skill :
   - **Spécificités du morceau** : type d'instrument par section (acoustique/électrique ?) correct ?
     Accordage alternatif documenté ? Partie jouée identifiée ? Adaptation live/studio explicite ?
   - Volume : KinkyBoost présent sur les snaps distorsion si fuzz ? Cas connu Arbitrator Fuzz + Big Muff ?
   - Architecture signal : pédale togglée vs canal ampli permanent, `enabled_default` correct ?
   - Snaps Clean inutilisés remplis avec le son accordage (Gate + Reverb, Mix=0.10) ?
   - Styles conformes à `docs/theory/eras_and_styles.md` ?
   - Docstring à jour (rôle de chaque snap, justifications, accordage si alternatif) ?
   - Sources dans `docs/sources_research.md` ?
3. Présente les écarts constatés avec les corrections proposées. **Attends la validation.**
4. Applique les corrections validées, génère, commite.

**Si le preset n'existe pas**, continue avec l'étape 1 ci-dessous.

---

## 1. Recherche

### Spécificités du morceau — à déterminer en priorité absolue

Avant de regarder les effets, établir ces 4 points factuels pour CE titre :

1. **Type d'instrument par section** : acoustique / électrique / les deux — et pour quelle(s) section(s).
   Si acoustique présent → prévoir `L6SPB_AcousGtrSim` et recommander micro manche.

2. **Accordage alternatif** : standard / Drop D / Eb / Open / autre.
   À documenter dans la fiche guitariste et mentionner dans la docstring.

3. **Quelle partie guitare on reproduit** : quand il y a plusieurs pistes (rythmique + lead,
   deux guitares, overdubs), préciser laquelle Eric joue seul en live.

4. **Adaptation live vs studio** : si le son studio n'est pas reproductible en live (triple-tracking,
   instruments impossibles à répliquer), documenter l'adaptation retenue et pourquoi.

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

Présente et justifie les 5 points suivants. **Attends la validation avant de passer à l'étape 3.**
Justifie chaque choix par rapport à ce que la recherche a révélé.

### Spécificités du morceau
Rappelle les 4 points établis en étape 1 (instrument, accordage, partie jouée, adaptation live/studio).
C'est le premier point présenté — il conditionne tout le reste.

### Parties guitare et snapshots
- Liste les sections du morceau et le son par section
- Détermine le nombre de snapshots (max 4) et le rôle de chacun

### Sélection des pédales
- Identifie les pédales réelles du guitariste sur ce titre
- Trouve les model IDs HX les plus proches (consulte `data/catalog/models_catalog.json`)
  - Les modèles sont en deux sous-catégories : **Mono/Stereo** (HD2, modèles modernes)
    et **Legacy** (DM4, MM4, DL4, FM4 — IDs contenant `_DM4`, `_MM4`, `_DL4`, `_FM4`).
    Considérer les deux : certains sons classiques n'existent qu'en Legacy.
- Consulte `docs/pedal_guides/` pour les paramètres de référence :
  - `hx_models_reference.md` : pédale réelle → Model ID (lookup inversé inclus)
  - `od_dist_fuzz.md` : sweet spots OD/dist/fuzz + table simulation ampli
  - `compressors.md`, `modulation.md`, `delay.md`, `reverb.md`, `filters.md`, `eq.md`
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
La **référence de niveau** est le signal guitare propre passant par le Mesa Boogie
(aucun bloc de saturation actif). C'est le "0 dB" du rig d'Eric, commun à tous les presets.

**Quand un preset a un snap Clean** (Gate + Reverb seule) : il sert de référence
auto-contenue — les snaps distorsion s'alignent sur lui.

**Quand un preset n'a pas de snap Clean** : calibrer les snaps distorsion par oreille
par rapport aux presets adjacents dans la setlist, ou par rapport au snap Clean
de n'importe quel autre morceau chargé sur l'appareil.

**Si une pédale de saturation baisse le volume sous la référence clean :**
→ Ajouter un KinkyBoost always-on (Drive=0, Boost=True) après la reverb,
  actif sur tous les snaps distorsion, **exclu du snap Clean si présent**.

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

**Règles techniques HX Effects :**
- **Slots** : 9 blocs disponibles, indices **0 à 8**. Ne pas hésiter à utiliser 6, 7, 8.
- **Échelle paramètres** : les valeurs lues sur l'appareil ou dans HX Edit sont sur
  une échelle ×10. Valeur interne = valeur affichée ÷ 10.
  Ex : l'utilisateur dit "level à 8" → écrire `"Level": 0.8` dans le preset.

---

## 5. Génération et vérification

Lance `python presets/generate_presets.py` et vérifie l'absence d'erreur ou WARNING.

---

## 6. Mise à jour sources_research.md

Ajouter ou compléter l'entrée dans `docs/sources_research.md` :

```markdown
## Artiste - Titre (année)

### Informations confirmées
- BPM, tonalité, guitare, ampli, pédales, sons par section

### Sources consultées
| URL | Contenu |
|-----|---------|
| ... | ... |
```

---

## 7. Commit

Message : `Titre - Artiste : preset + fiche <guitariste>`
Inclure les changements clés (chaîne, snaps, matching ampli si nouveau).
