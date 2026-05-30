# audio_analysis/sources/

Dossier de depot pour les fichiers audio a analyser.

## Usage

Deposer les FLAC/MP3 ici puis lancer :
```bash
python presets/analyze_audio.py audio_analysis/sources/Hysteria.flac
```

Les fichiers audio ne sont pas commites (gitignore).
Les rapports JSON generes (parents de ce dossier) le sont.
Les stems separes par Demucs vont dans `cache/` (gitignore aussi).

## Bonne pratique

- Nommer les fichiers simplement (`Hysteria.flac`, `Killing_in_the_Name.flac`)
  pour faciliter le matching avec les fiches docs/songs/
- Privilegier FLAC ou MP3 320 kbps minimum pour fiabilite analyse effets
