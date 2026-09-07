# Song 2 — Blur (1997)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Blur (1997) |
| BPM | 130 |
| Tonalité | Fa (F) |
| Accordage | Standard — E A D G B E |
| Style | Alt-rock, Post-grunge |
| Guitariste | Graham Coxon |

---

## Structure du morceau

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro | Drums seuls puis clean/grain léger | Gate + Heir Apparent + Reverb | Verse | Power chords, léger grain |
| Verse 1 | OD légère (grain léger) | Gate + Heir Apparent + Reverb | Verse | Soft, juste rythmique |
| Pre-chorus | OD légère qui monte | Gate + Heir Apparent + Reverb | Verse | Build-up |
| **Chorus "Woo-hoo!"** | **OCD — grunge bien poussé** | Gate + OCD + Reverb | Chorus | Distortion soutenue |
| Verse 2 | Retour OD légère | Gate + Heir Apparent + Reverb | Verse | Idem verse 1 |
| Chorus 2 | OCD grunge poussé | Gate + OCD + Reverb | Chorus | |
| Outro | OCD | Gate + OCD + Reverb | Chorus | Fin sur le riff distordu |

**2 sons distincts** : Heir Apparent (Verse/Intro/Pre-chorus) + OCD (Chorus/Outro). Dynamique signature quiet/loud — c'est l'identité du morceau.

**Refonte 2026-09-07** : le RAT (Vermin Dist) d'origine ne convenait pas à l'oreille
en répétition (même après correction du Level à 0.52). Remplacé par les deux
patterns canoniques de Dani California (cf. `docs/theory/shared_configs.md`) :
Heir Apparent ("Intro arpège + grain léger") pour le Verse, OCD ("Grunge bien
poussé") pour le Chorus — le contraste vient désormais de l'écart de gain entre
les deux pédales plutôt que d'un Level de RAT hors fourchette documentée.

---

## Improvisation

Pas de solo. Le contenu mélodique tient dans le riff signature du chorus.

---

## Preset HX Effects

**Fichier :** `output/Song 2 - Blur.hlx`

**Chaîne :**
```
Gate > HeirApparent > CompulsiveDrive > Reverb
  0        1                2              3
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Verse | Heir Apparent (Gain=0.20, Tone=0.50, Level=0.85) — pattern "Intro arpège" |
| 1 | Chorus | OCD (Gain=0.65, Tone=0.40, LPHP=True, Level=0.80) — pattern "Grunge bien poussé" |
| 2 | Clean | Accordage / attente |
| 3 | Clean | Accordage / attente |

**Particularités :**
- Deux patterns canoniques déjà validés (Dani California Verse/Chorus, cf. `docs/theory/shared_configs.md`), réutilisés tels quels plutôt qu'une config RAT dédiée
- Le contraste quiet/loud signature du morceau vient de l'écart Heir Apparent (Gain=0.20) → OCD (Gain=0.65)
- Reverb modérée — pas d'ambiance shoegaze, juste un peu d'espace
- ProCo RAT (pédale signature Coxon en réalité) abandonné : ne convenait pas à l'oreille en répétition

---

## Sources

| URL | Contenu |
|---|---|
| [Guitar Chalk — Graham Coxon](https://www.guitarchalk.com/graham-coxon-amp-settings/) | Gear et tone Coxon |
| [Reverb — How to Sound Like Blur](https://reverb.com/news/potent-pairings-how-to-sound-like-blur) | DOD FX76 Punkifier sur Song 2 |
| [Ultimate Guitar — Song 2 tab](https://tabs.ultimate-guitar.com/tab/blur/song-2-tabs-99059) | Accordage standard, power chords F |
