# audio_analysis/

Dossier des rapports d'analyse audio generes par `presets/analyze_audio.py`.

## Workflow

1. Deposer le fichier audio quelque part (peu importe le chemin)
2. Lancer :
   ```bash
   python presets/analyze_audio.py "chemin/vers/le/fichier.mp3"
   ```
3. Le rapport JSON est ecrit dans ce dossier : `<nom_fichier>_analysis.json`
4. Le skill `/new-preset` lira automatiquement ce rapport s'il existe pour
   le morceau en cours (matching par nom).

## Versions du pipeline

| Version | Detecteurs |
|---|---|
| **v3.0** | Tonalite (Krumhansl-Schmuckler), Tempo (librosa beat_track) |
| v3.1 (a venir) | Sections (intro/verse/chorus/bridge/outro avec timestamps) |
| v3.2 (a venir) | Effets (saturation, reverb, modulation, delay, EQ) |

## Format JSON

Le rapport contient au minimum :
```json
{
  "pipeline_version": "3.0",
  "file":             "chemin/audio.mp3",
  "filename":         "audio.mp3",
  "duration_s":       218.4,
  "sample_rate":      22050,
  "key": {
    "tonic":      "A",
    "tonic_fr":   "La",
    "mode":       "minor",
    "name":       "A minor",
    "name_fr":    "La mineur",
    "confidence": 0.42,
    "score":      0.87
  },
  "tempo": {
    "bpm":     132.5,
    "bpm_int": 132,
    "n_beats": 287
  }
}
```

## Conventions

- **Fichiers audio NON commites** (gitignore) — trop lourds, source perso
- **Rapports JSON commites** — donnees derivees utiles cross-sessions
- **Qualite audio recommandee** : FLAC ou MP3 320 kbps pour la fiabilite
  des analyses d'effets (v3.2). Pour key/tempo, MP3 192+ suffit.

## Fiabilite des analyses

| Analyse | Sensibilite qualite | YouTube via yt-dlp OK ? |
|---|---|---|
| Tonalite | Tres faible | Oui largement |
| Tempo | Tres faible | Oui |
| Sections | Faible | Oui |
| Effets (v3.2) | Moyenne-Haute | Marginal, lossless preferable |
