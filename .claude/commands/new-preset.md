Crée un nouveau preset HX Effects pour : $ARGUMENTS

Suis ces étapes dans l'ordre, sans en sauter.

---

## 1. Fiche guitariste

Vérifie si une fiche existe dans `docs/guitarists/` pour le guitariste concerné.

- **Si elle existe** : lis-la pour t'imprégner du son, du matos, des réglages ampli, et des sons spécifiques au morceau demandé.
- **Si elle n'existe pas** : fais une recherche web (equipboard, guitargearfinder, groundguitar, guitarchalk, musicstrive, neuraldsp) et crée le fichier `docs/guitarists/<nom>.md` avec :
  - Guitares principales (modèle, micros)
  - Amplis + réglages de référence
  - Pédales (ère du morceau)
  - Chaîne de signal
  - Sons par titre (tableau)
  - Sources consultées
- **Si elle est incomplète pour ce morceau** : complète-la avec les infos manquantes.

Confirme toujours : BPM, tonalité, sections du morceau (intro/couplet/refrain/solo/bridge), son par section.

---

## 2. Choix des blocs HX Effects

Consulte `docs/pedal_mapping.md` pour trouver les model IDs correspondant aux pédales réelles du guitariste.

Règles de sélection :
- Privilégier le modèle HX qui correspond à la pédale réelle utilisée sur le titre
- Préférer les modèles non-legacy sauf si le son legacy est significativement plus proche
- Vérifier que le model ID existe dans `data/catalog/models_catalog.json` avant de l'utiliser
- Pour les effets non utilisés sur un snapshot : `enabled_default=False`

---

## 3. Structure des snapshots

Détermine les snapshots nécessaires (max 4 sur HX Effects) selon les sections du morceau.
Chaque snapshot doit avoir un rôle clair (ex: Riff, Bridge, Solo, Clean).

---

## 4. Cohérence des volumes

Consulte les presets existants dans `presets/songs.py` pour calibrer les niveaux.
Référence actuelle : Level ~0.45–0.55 sur la sortie de l'OD/distortion en snapshot principal.
Les snapshots clean ou boost doivent être compensés pour ne pas créer de saut de volume.

---

## 5. Écriture du preset

Ajoute une fonction `preset_<nom_snake_case>()` dans `presets/songs.py` :
- Docstring : artiste, tempo, description de la chaîne, rôle de chaque snapshot
- `add_block()` pour chaque effet, dans l'ordre de la chaîne signal
- `add_snapshot()` pour chaque snapshot avec `blocks_on`, `params` si des paramètres varient, et `color`
- Ajouter l'entrée dans le dict `PRESETS` en bas du fichier

---

## 6. Génération et vérification

Lance `python presets/generate_presets.py` et vérifie qu'aucune erreur ou WARNING n'apparaît.

---

## 7. Mise à jour des sources

Si tu as consulté des URLs pour ce preset, ajoute-les dans `docs/sources_research.md` sous une section dédiée au morceau.

---

## 8. Commit

Crée un commit avec un message clair incluant l'artiste, le titre et le BPM.
