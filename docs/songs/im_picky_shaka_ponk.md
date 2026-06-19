# I'm Picky — Shaka Ponk

## Informations générales
| Champ | Valeur |
|---|---|
| Album | The Geeks and the Jerkin' Socks (2008) |
| BPM | 117.5 (analyse audio, confirme estimation 115) |
| Tonalité | Si majeur / Sol# mineur (capo case 4, formes Em-D-G-D) |
| Accordage | Standard, capo case 4 |
| Style | alt_metal |
| Guitariste | Cyril Roger "CC" |

## Structure du morceau
| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro/Verse | Mesa Rectifier cranked | KWB seul | PIK Riff | Saturation extreme deja sur l'intro (pas de section clean) |
| Bridge | idem Verse | KWB seul | PIK Riff | Memes accords simplifies (Em D C C) |
| Chorus | Rectifier + push | KWB + Scream808 (TS9 stack) | PIK Chorus | Tab : "rythmique doublee" en studio — compense par le stacking TS9 |
| Solo | idem Chorus (meme progression Em D G D) | KWB + Scream808 | PIK Chorus | Pas de solo melodique distinct, instrumental sur la meme grille |
| Outro | idem Chorus, intensite peak | KWB + Scream808 | PIK Chorus | Section la plus longue et la plus forte (RMS peak) |

## Improvisation
Pas de solo melodique au sens lead — section instrumentale sur la meme grille
d'accords (Em D G D, capo 4 -> sonne G#m F# B F#). Gamme : penta mineure G#
ou Si majeur si jeu plus melodique.

## Preset HX Effects
**Fichier :** `output/I'm Picky - Shaka Ponk.hlx`
**Chaine :** `Gate > Scream808 > KWB > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | PIK Riff | KWB seul (Gain=0.78) — Verse/Bridge |
| 1 | PIK Chorus | + Scream808 push (Gain=0.65) — Chorus/Solo/Outro |
| 2 | PIK Clean | Accordage |
| 3 | PIK Clean | Accordage |

Pattern de matching ampli reutilise depuis `docs/pedal_guides/od_dist_fuzz.md`
(Mesa Boogie Dual Rectifier -> KWB + Scream808 stacking).

## Sources
| URL | Contenu |
|---|---|
| [Equipboard - Cyril Roger](https://equipboard.com/pros/cyril-roger) | Pedalboard CC, ampli Mesa Rectifier |
| [Guitaretab - chords](https://www.guitaretab.com/s/shaka-ponk/293552.html) | Accords, capo 4, structure |
| Analyse audio (`audio_analysis/02. I'm Picky_analysis.json`) | BPM 117.5, tonalite Si majeur, saturation extreme toutes sections |
