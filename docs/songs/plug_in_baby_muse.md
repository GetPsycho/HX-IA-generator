# Plug In Baby — Muse (2001)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Origin of Symmetry (2001) |
| BPM | 136 |
| Tonalité | F# (Si mineur harmonique) |
| Accordage | Standard — E A D G B E |
| Style | Alt-rock / Hard rock |
| Guitariste | Matt Bellamy |

---

## Structure du morceau

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro / Riff | Fuzz Factory ouverte (Phase 90 retiré du preset, retour répét 2026-09) | Fuzz + Reverb + Gain | Riff | Le riff signature — revient en transitions et outro |
| Chorus | Même son que le Riff | Fuzz + Reverb + Gain | Chorus | Power chords, reverb légèrement plus ouverte |
| Verse (arpeges) | Son léger (synthé sur l'original) | Phaser + CE-1 Chorus + Reverb longue + Gain | Arpeges | Eric joue à la guitare, sons d'arpeges clairs avec texture synthé |

**Pas de solo, pas de tremolo (contrairement à certaines sources).**

---

## Improvisation

Pas de section d'improvisation — morceau structuré avec riff signature.

---

## Preset HX Effects

**Fichier :** `output/Plug In Baby - Muse.hlx`

**Chaîne :**
```
Gate > IndustrialFuzz > ScriptModPhase > 70sChorus > Reverb > KinkyBoost > Gain
  0         1                2               3           4         5          6
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Riff | Fuzz (ouverte) + Reverb + KinkyBoost + Gain (sans phaser) |
| 1 | Chorus | Idem Riff, reverb légèrement plus ouverte (+ Gain) |
| 2 | Arpeges | Phaser + CE-1 Chorus (Mix=0.65) + Reverb longue (Decay=0.65) + Gain — texture synthé |
| 3 | Clean | Accordage / attente |

**Particularités :**
- Fuzz Factory = fuzz **ouverte** (pas gated) : Compress=0.10, Gate=0.10, Drive=1.0, Stability=0.25
- Phase 90 : retiré du snap Riff (retour répét 2026-09), conservé uniquement sur Arpeges (l'original l'utilise tout au long du morceau, mais Eric ne le veut pas sur le riff)
- Volume monté (retour répét 2026-09) : bloc Gain pur (HD2_VolPanGain) +4 dB en fin de chaîne, actif sur Riff/Chorus/Arpeges ; snap Clean laissé à la référence
- CE-1 Chorus sur Arpeges uniquement : simule la texture clavier/synthé de l'original
- KinkyBoost exclu des Arpeges (clean = référence, pas besoin de compensation)

---

## Sources

| URL | Contenu |
|---|---|
| [The Pedal Lab — Plug In Bellamy](https://thepedallab.wordpress.com/2011/06/02/plug-in-bellamy/) | Settings Fuzz Factory détaillés (Gate/Comp/Drive/Stab par position horaire) |
| [guitar.com — Genius of Origin of Symmetry](https://guitar.com/reviews/album/the-genius-of-origin-of-symmetry-by-muse/) | Guitare Manson DL-1 "Delorean" confirmée, Fuzz Factory intégrée |
| [Guitar Chalk — Plug In Baby tone](https://www.guitarchalk.com/amp-settings-plug-in-baby-muse/) | Réglages amp, Diezel VH4 Ch3, delay pour solos |
| [guitarguitar.co.uk — Sound like Matt Bellamy](https://www.guitarguitar.co.uk/news/142426/) | Phase 90 slow sweep confirmé, Whammy usage |
| [MuseWiki — Plug In Baby tablature](https://www.musewiki.org/Plug_In_Baby_(tablature)) | Structure, accordage standard, tonalité F# |
