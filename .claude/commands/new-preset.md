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

## 0.5. Analyse audio (si disponible)

**Toujours exécuter cette étape** — que ce soit en mode audit ou en mode création.

Lance :
```bash
python presets/analyze_song.py "<titre du morceau>"
```

Le script cherche, dans cet ordre :
1. Un rapport JSON existant dans `audio_analysis/<...>_analysis.json`
2. Sinon, un fichier audio dans `audio_analysis/sources/` (matching fuzzy par tokens)
   → si trouvé, lance automatiquement la séparation Demucs + l'analyse (~2-3 min)

**Sortie :**
- `REPORT: <chemin>` → un rapport est disponible. **Lis le JSON** et utilise-le comme source primaire.
- `NO_AUDIO` → aucune analyse possible. Continue avec recherche web uniquement.

**Quand un rapport est disponible**, exploite ces données :
- `key` → tonalité confirmée (cross-check avec UG)
- `tempo` → BPM confirmé (attention au double/moitié possible)
- `sections.segments` → structure du morceau avec timestamps
- `sections.notes` → notes interprétatives (riff signature récurrent, transitions, etc.)
- `effects` (global) → saturation/compression/EQ moyens sur la guitare isolée
- `section_effects` → **par section** : `intensity` (quiet/moderate/loud/peak),
  `saturation` (level + score), `eq.balance`, source (`guitar_stem` ou `[MIX]`)

**Distinctions importantes** :
- **Saturation** = caractère sonore (saturé/clean) — reste constant si l'ampli sature toujours
- **Intensity (RMS)** = puissance perçue — varie selon le volume joué (ex: Cornell Be Yourself
  roule le volume → même son saturé mais intensity quiet→loud)
- **Tag `[MIX]`** : Demucs n'a pas pu isoler la guitare sur cette section (typique parties
  clean noyées dans le mix) → analyse faite sur le mix complet, valeur dégradée

**Cross-check avec le preset (mode audit) :**
Si le preset existant a un OCD Gain=0.18 mais l'analyse audio montre saturation=high (0.60+),
c'est probablement que l'original est plus saturé que ce que le preset reproduit. Deux interprétations :
1. **Adaptation gear voulue** : Eric a Super Distortion = haute sortie → moins de gain ajouté nécessaire
2. **Sous-évaluation** : le preset était trop conservateur

→ Présenter l'écart à l'utilisateur pour qu'il tranche.

**Cross-check avec la recherche web (mode création) :**
L'analyse audio donne les chiffres (BPM, tonalité, intensité par section) ;
la recherche web donne le matériel (Marshall JCM800, OCD, etc.) → les deux se complètent.
Le matching gear→pédale HX reste guidé par la recherche.

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

5. **Contexte du groupe d'Eric** : si le morceau original utilise un instrument qu'un autre
   membre du groupe joue déjà (ex : basse, second guitariste), Eric ne simule PAS cet instrument.
   Il joue uniquement la partie qui lui revient dans l'arrangement live du groupe.
   Ex : Royal Blood = basse + guitare-fuzz → bassiste joue la basse, Eric joue le chemin fuzz.
   → Supprimer tout bloc de simulation d'instrument (Boctaver, octave-down, etc.) si redondant.

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

  **Étape préalable obligatoire : déterminer le type de canal de l'ampli.**
  - Ampli **canal clean** (Mesa Boogie clean, Fender Twin, etc.) → la saturation vient
    exclusivement des pédales. Chaque pédale OD/dist est togglée (`enabled_default=False`).
  - Ampli **canal unique saturé / cranked** (Marshall JCM800, Plexi, Vox AC30 poussé…) →
    l'ampli EST la source principale de saturation. Même à Gain modéré sur le knob,
    le son de base est déjà très saturé pour des styles grunge/hard rock.
    → Simuler avec un bloc always-on à **haut gain** (OCD Gain 0.65+, ou pédale équivalente).
  - Ampli **2 canaux** (clean + saturé) → vérifier quel canal est utilisé sur CE titre,
    puis appliquer la règle correspondante.

  **Cas OD + ampli saturé (ex: TS9 → JCM800) :**
  Une OD comme la TS9 dans un ampli déjà cranked n'ajoute pas de saturation principale —
  elle compresse et booste les mids d'un préampli déjà saturé.
  → **Gain stacking** : deux blocs always-on en série.
    - Bloc 1 (OD pédal) : Gain faible (0.35–0.45), Level élevé (0.65–0.75) — rôle de push
    - Bloc 2 (sim ampli) : Gain élevé (0.65–0.82), LPHP selon caractère — rôle de saturation principale
  → Consulte la table de simulation ampli dans `docs/pedal_guides/od_dist_fuzz.md`.
    Si c'est un nouveau matching ampli→pédale, le documenter dans ce fichier.

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

**Calibration OCD (CompulsiveDrive) — règle de départ obligatoire :**
L'expérience live du projet a établi que `Level=0.52` (valeur "naïve") est systématiquement
en dessous de la référence clean. La combinaison validée est **Level=0.70 + KinkyBoost (Boost=True)**.
Ces deux éléments ensemble sont nécessaires pour atteindre la référence clean avec un OCD seul.

→ **Toujours** ajouter un KinkyBoost (Drive=0, Boost=True) sur les snaps OCD.
→ Partir de Level=0.70 sur l'OCD pour le snap le plus faible.
→ Si gain stacking (Klon+OCD, TS9+OCD…), le KinkyBoost peut être omis ou réduit.
→ En audit : absence de KinkyBoost OU OCD Level < 0.65 = signal sous-calibré, à corriger.

---

## 3. Validation utilisateur

Attends l'accord explicite avant de toucher les fichiers.

---

## 4. Écriture des fichiers

### Fiche guitariste
Crée ou met à jour `docs/guitarists/<nom>.md`. Si la recherche révèle des infos
nouvelles sur un titre déjà documenté, mettre à jour la fiche.

### Fiche morceau
Crée ou met à jour `docs/songs/<titre_artiste>.md` (snake_case). Format :

```markdown
# Titre — Artiste (Année)

## Informations générales
| Champ | Valeur |
|---|---|
| Album | ... |
| BPM | ... |
| Tonalité | ... (ex: Mi mineur) |
| Accordage | ... (ex: Standard, Drop D) |
| Style | ... |
| Guitariste(s) | ... |

## Structure du morceau
| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro | ... | ... | ... | ... |
| Verse | ... | ... | ... | ... |
| Chorus | ... | ... | ... | ... |
| Solo | ... | ... | ... | ... |

## Improvisation
| Section | Tonalité | Gammes recommandées | Notes |
|---|---|---|---|
| Solo | ... (module si différente du reste) | Penta mineure, Dorien, Blues... | ... |

## Preset HX Effects
**Fichier :** `output/Titre - Artiste.hlx`
**Chaîne :** `Gate > ... > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | ... | ... |

## Sources
| URL | Contenu |
|---|---|
| [Ultimate Guitar](url) | Accordage, structure, tonalité |
| ... | ... |
```

**Règles pour la fiche morceau :**
- Tonalité : chercher sur Ultimate Guitar (indiquée en en-tête des tabs officielles)
- Section Improvisation : indiquer la tonalité spécifique du solo si elle module,
  et les gammes jouables (mineur, majeur, pentatonique, blues, Dorien, mixolydien…)
- Pas de solo → l'indiquer explicitement

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
