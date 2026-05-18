# Killing in the Name — Rage Against The Machine (1992)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Rage Against The Machine (1992) |
| BPM | 85 |
| Tonalité | Mi mineur (Em) — Drop D |
| Accordage | **Drop D** — D A D G B E |
| Style | Alt-metal, Funk-rock |
| Guitariste | Tom Morello |

---

## Structure du morceau

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro/Riff | JCM800 cranked | OCD + Reverb + KWB | Riff | Riff signature D power chord avec bend |
| Verse | Idem (palm-muting) | OCD + Reverb + KWB | Riff | Pattern rythmique syncopé |
| Chorus "Killing in the name of..." | Idem riff | OCD + Reverb + KWB | Riff | Power chords D, F, G, A |
| Bridge calme ("Some of those that work forces") | Idem | OCD + Reverb + KWB | Riff | Plus dynamique, gain identique |
| Solo (1:33–2:20) | JCM800 + Whammy +2oct + delay | OCD + PitchWham + Delay + Reverb + KWB | Solo | "DJ scratching" caractéristique |
| Outro "Fuck you, I won't do what you tell me" | Idem riff, montée intense | OCD + Reverb + KWB | Riff | Buildup explosif |

---

## Pédale d'expression — Whammy

**Pédale physique** : Mission Engineering EP1-L6-BK connectée au port EXP 1 du HX Effects.

**Configuration HX :**
- Pitch Wham, slot 2, actif uniquement sur snap Solo
- `Heel = 0` (unisson, pas d'effet)
- `Toe = +24` (= +2 octaves)
- `Pedal` bindé EXP 1
- Mix = 1.0 (100% wet)

**Utilisation live :** sur le solo, balancer la pédale d'avant en arrière au rythme pour créer l'effet "scratching DJ" (pitch up/down rapide).

---

## Improvisation

| Section | Tonalité | Gammes recommandées | Notes |
|---|---|---|---|
| Solo | Mi mineur (Em) | Pentatonique Em, blues Em | Tremolo picking + Whammy = phrases courtes répétées |

---

## Preset HX Effects

**Fichier :** `output/Killing in the Name - RATM.hlx`

**Chaîne :**
```
Gate > CompulsiveDrive > PitchWham > SimpleDelay > Reverb > KinkyBoost
  0         1                2            3            4         5
                            ↑
                        EXP 1 (Pedal)
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Riff | OCD (Gain=0.72, LPHP=True, Level=0.70) + Reverb minimal + KWB |
| 1 | Solo | OCD + Whammy +2oct (EXP 1) + Delay 350ms + Reverb + KWB |
| 2 | Clean | Accordage / attente |
| 3 | Clean | Accordage / attente |

**Particularités :**
- OCD always-on : JCM800 canal overdrive permanent (Morello n'a pas de canal clean)
- LPHP=True : punch britannique du JCM800
- Reverb très basse (Mix=0.08) : original studio est très sec ("no reverb")
- Drop D : Eric descend physiquement le Mi grave en Ré (pas de pitch shift logiciel)
- KinkyBoost actif sur Riff et Solo (règle calibration OCD)
- **Pitch Wham `Pedal` bindé à EXP 1** — premier preset du projet à utiliser ce binding

---

## Sources

| URL | Contenu |
|---|---|
| [Roland — Killing in the Name tone breakdown](https://rolandcorp.com.au/blog/rage-against-the-machines-killing-in-the-name-guitar-tone-dissected) | Telecaster + JCM800 + Whammy +2oct |
| [Guitar Gear Finder — Tom Morello rig](https://guitargearfinder.com/guides/tom-morello-guitar-gear-rig-rage-against-the-machine/) | Gear complet RATM |
| [Ultimate Guitar — KITN](https://www.ultimate-guitar.com/news/tab_spotlight/killing-in-the-name-is-easy-to-learn-hard-to-play-right-the-gap-lives-in-tom-morellos-right-hand) | Drop D, structure, technique |
