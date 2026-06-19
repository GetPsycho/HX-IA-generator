# Special K — Placebo (2000)

## Informations générales
| Champ | Valeur |
|---|---|
| Album | Black Market Music (2000) |
| BPM | 160 (audio detecte 80.7, alternative x2 = 161.5 proche de l'estimation) |
| Tonalité | Do# majeur (C#) — confirmé Wikipédia |
| Accordage | Standard, capo case 1 (decision Eric) |
| Style | alt_rock |
| Guitariste | Brian Molko |

## Structure du morceau
| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro/Verse | OD légère, brillante | Heir Apparent | SPK Verse | Saturation moderee (audio: 0.28-0.43) |
| Chorus/Outro | Saturation plus poussée | Compulsive Drive (grunge bien poussé) | SPK Chorus | Audio : pic saturation outro (0.64) |

## Improvisation
Pas de solo guitare identifié.

## Preset HX Effects
**Fichier :** `output/Special K - Placebo.hlx`
**Chaîne :** `Gate > HeirApparent > CompulsiveDrive > Reverb`

| Snap | Nom | Son |
|---|---|---|
| 0 | SPK Verse | Heir Apparent (Gain=0.20, Tone=0.50, Level=0.85) — pattern "Intro arpège" |
| 1 | SPK Chorus | OCD (Gain=0.65, Tone=0.40, LPHP=True, Level=0.80) — pattern "Grunge bien poussé" |
| 2 | SPK Clean | Accordage |
| 3 | SPK Clean | Accordage |

Deux patterns canoniques existants réutilisés (cf. `docs/theory/shared_configs.md`)
plutôt qu'une config dédiée — l'analyse audio montre un son "bright" globalement
moderement saturé qui correspond bien à ces deux paliers déjà documentés.

## Sources
| URL | Contenu |
|---|---|
| [Wikipedia - Special K (song)](https://en.wikipedia.org/wiki/Special_K_(song)) | Tonalité Do# majeur |
| Analyse audio (`audio_analysis/Placebo - Black Market Music - 03 - Special K_analysis.json`) | Tempo, EQ bright, saturation par section |
