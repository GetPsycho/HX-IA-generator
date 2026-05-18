# John Frusciante — Red Hot Chili Peppers

## Guitares principales (ère Stadium Arcadium, 2006)

| Guitare | Micros | Notes |
|---|---|---|
| **1962 Fender Stratocaster** (sunburst) | Single-coil Fender | Guitare principale Stadium Arcadium. Offerte par Anthony Kiedis en 1998. |
| **1954 Fender Stratocaster** (maple fretboard) | Single-coil Fender | Utilisée en alternance. Dani California (certaines sections). |
| 1961 Fender Stratocaster (olympic white) | Single-coil | Overdubs |
| 1969 Gibson Les Paul Custom | Humbuckers | "Readymade" et overdubs spécifiques |

Cordes D'Addario .010-.046. Picks Dunlop Orange Tortex 0.60mm.

**Dani California :** neck pickup pour les verses clean. Bridge pour les solos distordus.

---

## Amplis (ère Stadium Arcadium, 2006)

| Ampli | Rôle |
|---|---|
| **Marshall Major 200W** (modèle 1967, tubes KT88) | Principal, son chaud et puissant |
| Marshall Silver Jubilee 2550 (100W) | En parallèle avec le Major |
| Fender Blackface Showman | Sons clairs studio |

**Technique :** Les deux canaux du Marshall bridgés simultanément (patch leads).

| Param | Réglage Silver Jubilee |
|---|---|
| Gain | 4 |
| Treble | 8 |
| Mid | 2 |
| Bass | 6 |
| Reverb | 7 |
| Master | 5 |

Enceintes Marshall 4×12 Celestion d'époque. Micros : SM57 proximité + Royer R-121 à 4m (room).

---

## Pédales — ère Stadium Arcadium (2006)

| Pédale | Usage |
|---|---|
| **Boss DS-2 Turbo Distortion** | **Distorsion principale** chorus/solo Dani California |
| **Moog MF-101 Low-Pass Filter** | Filtre live verse Dani California (voir note studio) |
| Moog MF-103 Phaser 12-Stage | Autres titres — **pas sur Dani California** |
| Moog MF-105 MuRF | Verse 2 harmonies + textures solo Dani California |
| **Ibanez WH-10 V1 Wah** | Solo Dani California (fin, run wah rapide). Utilisé souvent "inversé" |
| Boss CE-1 Chorus Ensemble | Chorus sur autres titres |
| EHX Holy Grail Reverb V1 | Reverb ambiance sons clairs |
| EHX POG | Octaver polyphonique (studio) |
| MXR M-133 Micro Amp | Clean boost |
| Delta Labs Effectron II | Delay sur le run wah final (solo Dani California) |
| Doepfer A-100 modular | **Studio seulement** — voir note ci-dessous |

---

## Note studio — Filtre verse Dani California

Le son "wobbly/oscillant" du verse B n'est **pas** une pédale envelope filter classique en studio.
C'est un **synthétiseur modulaire Doepfer A-100** : un générateur ADSR déclenché par les dynamiques de jeu contrôle dynamiquement un filtre passe-bas. Le signal est splitté en stéréo : canal gauche sec, canal droit traité.

**En live :** Frusciante reproduisait cet effet avec le **Moog MF-101 LPF** + Moog CP-251 Control Processor (LFO pour simuler l'ouverture/fermeture). Josh Klinghoffer utilisait un Line 6 FM4 pour le même rôle.

**Conséquence pour le preset :** Le verse A est **clean pur** (pas d'OD). Le filtre n'entre qu'au verse B (snap "Lick").

---

## Chaîne de signal — Dani California (live)

```
Strat 1962 (neck pickup, verse)
  → Moog MF-101 Low-Pass Filter (verse B "Lick" uniquement)
  → Boss DS-2 Turbo Distortion (chorus / solo)
  → Ibanez WH-10 V1 (solo final uniquement)
  → Marshall Major 200W (canaux bridgés)
```

---

## Sons par titre

| Titre | Section | Son | Pédales actives |
|---|---|---|---|
| **Dani California** | Verse A | Clean pur | Aucune (straight into amp) |
| **Dani California** | Verse B (Lick) | Clean + filtre dynamique | MF-101 LPF |
| **Dani California** | Chorus | Distorsion mid-gain | DS-2 Turbo II |
| **Dani California** | Solo | Dist + wah | DS-2 + WH-10 (inversée) + Effectron II |
| **Californication** | Intro / Verse / Chorus | Clean arpeggios + CE-1 chorus | CE-1 split stéréo Showman/JTM-45 |
| **Californication** | Solo | Crunch léger (JTM-45) | OCD style Plexi + KWB en live |
| Can't Stop | Riff | Crunch funky | DS-2 gain modéré |

---

## Équivalents HX Effects

| Pédale originale | Modèle HX Effects | Model ID | Notes |
|---|---|---|---|
| Moog MF-101 LPF | Auto Filter | `HD2_FilterAutoFilter` | Mode BP (1) retenu : Mode LP trop grave en pratique |
| Boss DS-2 Turbo | Deez One Mod (DS-1 Keeley) | `HD2_DistDeezOneMod` | DS-2 non modélisé ; Keeley DS-1 ≈ Turbo mode |
| Ibanez WH-10 Wah | Pédale externe | — | Eric utilise son Cry Baby MC404 CAE |
| Boss CE-1 Chorus | 70s Chorus | `HD2_Chorus70sChorus` | Autres titres |
| EHX Holy Grail | Reverb Ganymede | `HD2_ReverbGanymede` | |

---

## Notes pour les presets

- **Dani California verse :** pas d'OD — le verse est clean direct dans le Marshall.
- **AutoFilter Mode BP :** le MF-101 original est un LPF (Mode 0 sur HX). En pratique, Mode 0 trop sombre/grave sur le HX — Mode BP (1) validé par test utilisateur.
- **DS-2 Turbo II :** Drive 0.65 (légèrement plus que DS-1 standard), Tone neutre (0.52). Solo : Drive 0.72.
- **WH-10 inversée :** Frusciante utilisait souvent la wah heel-down = treble, toe-down = bass. Pas modélisable simplement en live — la Cry Baby externe d'Eric s'en approchera dans l'autre sens.

---

## Sources

- Ground Guitar — Frusciante Stadium Arcadium gear breakdown
- Ground Guitar — Frusciante Breaks Down Dani California
- Ground Guitar — Moog MF-101 Low Pass Filter (Frusciante)
- Guitar FX Depot — Stadium Arcadium Guitar Rig
- Rock Guitar Universe — Frusciante Gear & Tone Guide
- Guitar Lessons London — Frusciante on Recording Dani California
- Equipboard — John Frusciante rig
- Guitar Chalk — Dani California amp settings
