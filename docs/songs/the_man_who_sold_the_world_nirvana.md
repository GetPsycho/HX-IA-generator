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
Martin D-18E acoustique-électrique + Boss DS-2 (subtil, intro/solo uniquement) —
pas du 100% acoustique malgré le format "Unplugged". Pas de Small Clone audible
à l'écoute sur ce titre (retiré). Pat Smear (2e guitare, ligne de basse mobile
au chorus) non reproduit (guitariste unique).

3 sons distincts (retour écoute Eric) :

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro/Riff | Acoustique + DS-2 subtil | AcousGtrSim + DeezOneMod | TMW Intro | Motif répété 2-3 fois |
| Verse | Folk pur, sans DS-2 | AcousGtrSim seul | TMW Verse | Son clairement différent à l'oreille |
| Solo | Variation de l'intro | AcousGtrSim + DeezOneMod + reverb + | TMW Solo | Plus de reverb/sustain ("qui dure") |

## Improvisation
Solo joué par Cobain sur la même grille (La majeur/mineur selon le passage).
Gamme : penta mineure de La, ou Mixolydien selon la mélodie de Bowie.

## Preset HX Effects
**Fichier :** `output/The Man Who Sold the World - Nirvana.hlx`
**Chaîne :** `PolyPitch > Gate > AcousGtrSim > DeezOneMod > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | TMW Intro | Acoustique + DS-2 subtil + reverb normale |
| 1 | TMW Verse | Acoustique seule (pas de DS-2) |
| 2 | TMW Solo | Acoustique + DS-2 + reverb plus longue/présente |
| 3 | TMW Clean | Accordage |

PolyPitch (Interval=-1, AutoEQ=1.0) simule l'accordage demi-ton bas — pattern
identique à Toxicity (Drop D → Drop C), ici standard → Eb standard.

## Sources
| URL | Contenu |
|---|---|
| [Guitar.com - Unplugged gear](https://guitar.com/features/artist-rigs/the-gear-used-on-nirvana-mtv-unplugged-in-new-york-album/) | DS-2 confirmé sur ce titre |
| [Songsterr](https://www.songsterr.com/a/wsa/nirvana-the-man-who-sold-the-world-mtv-unplugged-tab-s487821) | Accordage Eb, parties Cobain/Smear |
| Analyse audio (`audio_analysis/04 - The Man Who Sold the World_analysis.json`) | Tempo, EQ chaude |
| Écoute directe (Eric) | 3 sons distincts (Intro/Verse/Solo), Small Clone non audible |
