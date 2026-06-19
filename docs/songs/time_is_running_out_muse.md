# Time Is Running Out — Muse (2003)

## Informations générales
| Champ | Valeur |
|---|---|
| Album | Absolution (2003) |
| BPM | 117.5 (analyse audio, proche de l'estimation 120) |
| Tonalité | La mineur (A) |
| Accordage | Standard (E A D G B E) |
| Style | alt_rock |
| Guitariste | Matt Bellamy |

## Structure du morceau
Le riff funky "wah" emblématique du verse vient de la **basse** (Chris
Wolstenholme, Bass Synth Wah/envelope filter) — pas de la guitare, donc rien
à reproduire côté guitare là-dessus. Structure jouée par Eric (arrangement
interprété, pas le gear studio exact) :

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro | Petites notes, crescendo | Clean + 70s Chorus | TRO Intro | Modulation légère |
| Verse | Accords étouffés | OCD léger (Gain~0.30) | TRO Verse | Crunch discret, pas de modulation |
| Chorus | "Gros son", gardé jusqu'à la fin | OCD "grunge bien poussé" | TRO Chorus | Saturation principale du morceau |
| Bridge | Arpèges + tremolo | OCD + Opto Tremolo | TRO Bridge | Saturation + modulation combinées |

Pas de snap Clean dédié — les 4 emplacements sont utilisés pour les 4 sons
réels du morceau (à valider en test physique). Accordage de référence via
un autre preset du set si besoin.

## Improvisation
Pas de solo lead identifié — le pont en arpèges est la section la plus
"lead" du morceau. Gamme : La mineur naturel/penta mineure.

## Preset HX Effects
**Fichier :** `output/Time Is Running Out - Muse.hlx`
**Chaîne :** `Gate > CompulsiveDrive > 70sChorus > OptoTremolo > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | TRO Intro | Chorus seul (OCD off) |
| 1 | TRO Verse | OCD léger (Gain=0.30) |
| 2 | TRO Chorus | OCD grunge bien poussé (Gain=0.65, Tone=0.40, Level=0.80) |
| 3 | TRO Bridge | OCD + Opto Tremolo |

Réutilise le pattern canonique "Grunge bien poussé" (cf.
`docs/theory/shared_configs.md`) pour le Chorus/Bridge — pas de nouvelle
config nécessaire.

## Sources
| URL | Contenu |
|---|---|
| [Guitar Chalk - amp settings](https://www.guitarchalk.com/amp-settings-time-is-running-out-muse/) | Ton punchy/overdrive, EQ |
| [Wikipedia](https://en.wikipedia.org/wiki/Time_Is_Running_Out_(Muse_song)) | Contexte, influence Billie Jean |
| Retour direct Eric | Structure jouée (crescendo/étouffé/gros son/pont) — à confirmer en test physique |
| Analyse audio (`audio_analysis/03 - Time Is Running Out_analysis.json`) | Tempo, tonalité, intensité par section |
