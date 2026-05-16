# Toxicity — System of a Down (2001)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Toxicity (2001) |
| BPM | 115 |
| Tonalité | Drop C (C mineur) |
| Accordage | Drop C — C G C F A D |
| Style | Nu-metal |
| Guitariste | Daron Malakian |

---

## Structure du morceau

| Section | Son guitare | Effets actifs | Snap HX | Notes |
|---|---|---|---|---|
| Intro/Riff | HM-2 chainsaw, palm-muting serré | Tous + gate Decay=0.18 | Riff | Riff principal, picking alterné rapide |
| Verse | Idem Riff | Tous + gate Decay=0.18 | Riff | Même son que le riff |
| Chorus | HM-2 full, sustain plus ouvert | Tous + gate Decay=0.26 | Chorus | Power chords plein |
| Bridge/Break | HM-2, gate très serré, riff syncopé | Tous + gate Decay=0.14 | Break | Breakdown caractéristique |

**Pas de solo guitare dans Toxicity.**

---

## Accordage — Drop C via PolyPitch

Eric joue en **Drop D** physiquement (corde grave descendue de Mi à Ré).
Le bloc `PolyPitch` (-2 semitones, always-on) transpose tout d'un ton vers le bas → **Drop C**.

Le PolyPitch est actif sur **tous les snaps** incluant Clean :
l'accordeur de l'HX Effects voit le signal transposé et indique le Drop C.
Eric accorde ses cordes en Drop D — l'HX fait le reste.

---

## Compensation EQ du pitch shift

Descendre d'un ton via pitch shift introduit une coloration sonore :
excès de basses (mud), perte de clarté dans les haut-mids.

**Technique de compensation (documentée dans `eq.md`) :**
1. `AutoEQ=1.0` sur le PolyPitch : correction spectrale automatique (Line 6)
2. `10 Band Graphic` en complément :
   - 250 Hz : -3 dB (couper le mud du down-pitch)
   - 2 kHz : +2 dB (redonner clarté et attaque)

---

## Improvisation

Pas de section d'improvisation — Toxicity est un morceau structuré sans solo.

---

## Preset HX Effects

**Fichier :** `output/Toxicity - System of a Down.hlx`

**Chaîne :**
```
PolyPitch > Gate > SwedishChainsaw > 10BandEQ > Reverb > KinkyBoost
    0          1         2               3           4         5
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Riff | HM-2 + gate serré (Decay=0.18) + EQ + Reverb + KWB |
| 1 | Chorus | HM-2 + gate ouvert (Decay=0.26) + EQ + Reverb + KWB |
| 2 | Break | HM-2 + gate très serré (Decay=0.14) + EQ + Reverb + KWB |
| 3 | Clean | PolyPitch actif → accordage Drop C |

**Particularités :**
- PolyPitch always-on (tous snaps) : Drop D → Drop C
- AutoEQ=1.0 : compensation spectrale automatique du shift
- 10BandEQ : simulation MXR rack Malakian + affinage EQ manuel
- KinkyBoost : compensation volume HM-2 vs référence clean

---

## Sources

| URL | Contenu |
|---|---|
| [Guitar Chalk — Toxicity amp settings](https://www.guitarchalk.com/toxicity-system-of-a-down-amp-settings/) | Gear studio, amp settings Mesa Rectifier, HM-2 |
| [SevenString.org — EQ low tuned](https://sevenstring.org/threads/how-do-you-eq-low-tuned-guitars.224286/) | EQ compensation pour guitares down-tunées |
| [Kemper Forum — drop tuned guitar](https://forum.kemper-amps.com/forum/thread/45788-drop-tuned-guitar-tips/) | Tips EQ + gain pour pitch shift vers le bas |
| [Line 6 — Helix 3.0 Poly Pitch](https://musicplayers.com/2020/11/line-6-introduces-helix-3-0-firmware-major-updates-that-include-polyphonic-pitch-effects/) | AutoEQ param du PolyPitch |
