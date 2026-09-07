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
| Intro | Drums seuls puis clean | Gate + Reverb | Verse | Power chords clean |
| Verse 1 | Clean (drums + bass lead) | Gate + Reverb | Verse | Soft, juste rythmique |
| Pre-chorus | Clean qui monte | Gate + Reverb | Verse | Build-up |
| **Chorus "Woo-hoo!"** | **RAT cranked — explosion** | Gate + RAT + Reverb + KWB | Chorus | Distortion violente |
| Verse 2 | Retour clean | Gate + Reverb | Verse | Idem verse 1 |
| Chorus 2 | RAT explosion | Gate + RAT + Reverb + KWB | Chorus | |
| Outro | RAT | Gate + RAT + Reverb + KWB | Chorus | Fin sur le riff distordu |

**2 sons distincts** : Clean (Verse/Intro/Pre-chorus) + Distortion (Chorus/Outro). Dynamique signature quiet/loud — c'est l'identité du morceau.

---

## Improvisation

Pas de solo. Le contenu mélodique tient dans le riff signature du chorus.

---

## Preset HX Effects

**Fichier :** `output/Song 2 - Blur.hlx`

**Chaîne :**
```
Gate > VerminDist > Reverb > KinkyBoost
  0       1            2         3
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Verse | Clean direct (Gate + Reverb légère Mix=0.16) — **pas de KinkyBoost** |
| 1 | Chorus | ProCo RAT (Gain=0.75, Filter=0.55, Level=0.52) + Reverb + KWB |
| 2 | Clean | Accordage / attente |
| 3 | Clean | Accordage / attente |

**Particularités :**
- **Pas de KinkyBoost sur le Verse** : contraste dynamique volontaire (comme Lithium). Le Chorus doit exploser au-dessus du Verse.
- RAT (Vermin Dist) Level=0.52 (sweet spot documenté "Rock british" pour Gain=0.75, cf. `docs/pedal_guides/od_dist_fuzz.md`) + KinkyBoost = chorus plus fort que le verse clean
- **Audit 2026-09-07** : Level était à 0.85, très au-dessus de toute fourchette documentée pour cette pédale (max 0.52 même en config "Heavy") — corrigé (option A) pour rester cohérent avec la règle "+0.20 Gain → -0.05/-0.08 Level" et la fourchette Chorus "0 à +2 dB au-dessus du Verse" (`docs/theory/volume_reference.md`)
- Reverb modérée — pas d'ambiance shoegaze, juste un peu d'espace
- ProCo RAT = pédale signature Coxon (parfois 2 sur son board live)

---

## Sources

| URL | Contenu |
|---|---|
| [Guitar Chalk — Graham Coxon](https://www.guitarchalk.com/graham-coxon-amp-settings/) | Gear et tone Coxon |
| [Reverb — How to Sound Like Blur](https://reverb.com/news/potent-pairings-how-to-sound-like-blur) | DOD FX76 Punkifier sur Song 2 |
| [Ultimate Guitar — Song 2 tab](https://tabs.ultimate-guitar.com/tab/blur/song-2-tabs-99059) | Accordage standard, power chords F |
