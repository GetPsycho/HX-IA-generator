# The Man Who Sold the World — Nirvana (1994, MTV Unplugged, cover David Bowie)

## Informations générales
| Champ | Valeur |
|---|---|
| Album | MTV Unplugged in New York (1994) |
| BPM | 117.5 (analyse audio, proche de l'estimation 118) |
| Tonalité | La (A) — accordage demi-ton bas (Eb standard) |
| Accordage | Demi-ton plus bas (Eb Ab Db Gb Bb Eb), simulé via PolyPitch (-1 semitone) |
| Style | grunge |
| Guitariste | Kurt Cobain |

## Structure du morceau
Martin D-18E acoustique-électrique + Boss DS-2 (subtil) + Small Clone chorus —
pas du 100% acoustique malgré le format "Unplugged". Pat Smear (2e guitare,
ligne de basse mobile au chorus) non reproduit (guitariste unique).
Un seul son actif tout le morceau (analyse audio : saturation constamment
haute, pas de vraie rupture clean/distordu).

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Tout le morceau (+ solo) | Acoustique + grain DS-2 + chorus | AcousGtrSim + DeezOneMod + 70sChorus | TMW Riff | PolyPitch -1 semitone always-on |

## Improvisation
Solo joué par Cobain sur la même grille (La majeur/mineur selon le passage).
Gamme : penta mineure de La, ou Mixolydien selon la mélodie de Bowie.

## Preset HX Effects
**Fichier :** `output/The Man Who Sold the World - Nirvana.hlx`
**Chaîne :** `PolyPitch > Gate > AcousGtrSim > DeezOneMod > 70sChorus > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | TMW Riff | Acoustique + DS-2 subtil + Small Clone — seul son actif |
| 1 | TMW Clean | Accordage |
| 2 | TMW Clean | Accordage |
| 3 | TMW Clean | Accordage |

PolyPitch (Interval=-1, AutoEQ=1.0) simule l'accordage demi-ton bas — pattern
identique à Toxicity (Drop D → Drop C), ici standard → Eb standard.

## Sources
| URL | Contenu |
|---|---|
| [Guitar.com - Unplugged gear](https://guitar.com/features/artist-rigs/the-gear-used-on-nirvana-mtv-unplugged-in-new-york-album/) | DS-2 + Small Clone confirmés sur ce titre |
| [Songsterr](https://www.songsterr.com/a/wsa/nirvana-the-man-who-sold-the-world-mtv-unplugged-tab-s487821) | Accordage Eb, parties Cobain/Smear |
| Analyse audio (`audio_analysis/04 - The Man Who Sold the World_analysis.json`) | Tempo, saturation constante, EQ chaude |
