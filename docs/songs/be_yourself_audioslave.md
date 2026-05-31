# Be Yourself — Audioslave (2005)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Out of Exile (2005) |
| BPM | 117 (confirmé analyse audio) |
| Tonalité sonnante | **Si mineur (Bm)** — confirmé analyse audio v3.2 (confidence 0.36, score 0.94) |
| Accordage | Standard — E A D G B E |
| **Capo** | **Case 2** — Eric joue avec capo (shapes Am sonnent en Bm) |
| Style | Alt-rock |
| Guitariste | Tom Morello |

---

## Philosophie sonore Morello (à connaître)

Tom Morello **n'utilise QUE le canal overdrive** de son Marshall JCM800 — pas de canal clean. Il obtient ses sons quasi-propres en **roulant le potentiomètre de volume guitare** sur le canal saturé. Résultat : crunch très léger sur l'intro, sat. complète sur le chorus, sans toucher l'ampli.

**Conséquence pour le preset :** l'OCD reste **always-on** avec Gain variable par snap (simulation du volume guitare qui pousse plus ou moins l'ampli déjà saturé). L'analyse audio confirme cette logique : **saturation reste high/extreme partout**, c'est l'**intensity (RMS) qui varie quiet → peak**.

---

## Structure du morceau (22 sections détectées sur le stem guitare)

| Temps | Section | Cluster | Intensité | Saturation | Snap HX |
|---|---|---|---|---|---|
| 00:00 → 00:35 | Intro arpèges | B | quiet (0.40) | extreme (0.80) | **Intro** |
| 00:35 → 00:52 | Build-up (bridges B) | B | quiet (0.42-0.45) | extreme | Intro |
| 00:52 → 01:00 | Chorus_1 (entry) | A | quiet (0.40) | extreme | Chorus |
| 01:00 → 01:21 | Chorus_2 + build | A/B | quiet → moderate | high | Chorus |
| 01:21 → 01:30 | Verse 1 | E | moderate (0.64) | high | **Verse** |
| 01:30 → 02:04 | Choruses 2-5 | A | moderate (0.58-0.61) | high/extreme | Chorus |
| 02:04 → 02:40 | Verses 2-5 | E | moderate (0.57-0.64) | high | Verse |
| **02:40 → 03:12** | **SOLO (32s)** | **C** | **PEAK (1.00)** | moderate (0.52) | **Solo** |
| 03:12 → 03:47 | Post-solo / breakdowns | C/D | moderate (0.67-0.76) | high | Chorus |
| 03:47 → 03:56 | Verse 6 (calm) | E | quiet (0.53) | high | Verse |
| 03:56 → 04:33 | **Outro chorus (37s)** | A | **loud (0.85)** | moderate | Chorus |
| 04:33 → 04:39 | Fade-out | B | very_quiet (0.05) | extreme | (Clean) |

**Insights clés :**
- **Solo identifié : 02:40 → 03:12 (~32 secondes)** à intensity=PEAK, c'est le moment lead avec Cry Baby Wah
- **Outro chorus très puissant** (3:56-4:33, 37s, loud) — pic de l'instrumental final
- Saturation reste constamment élevée — c'est l'intensité (volume joué) qui crée la dynamique

---

## Improvisation

| Section | Tonalité | Gammes recommandées | Notes |
|---|---|---|---|
| Solo | Si mineur (Bm) | Pentatonique Bm, Bm blues | Style expressif Morello, wah pour le caractère, ~32s |

---

## Preset HX Effects

**Fichier :** `output/Be Yourself - Audioslave.hlx`

**Chaîne :**
```
Gate > CompulsiveDrive (OCD) > SimpleDelay > Ganymede
  0       1                       2             3
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Intro | OCD Gain=**0.01** (quasi-clean), Level=0.92 + Reverb large (Mix=0.32) |
| 1 | Verse | OCD Gain=0.22, Level=0.85 + **Delay subtle** (Time=256ms, Mix=0.12) + Reverb |
| 2 | Chorus | OCD Gain=0.38, Level=0.80, LPHP=True (crunch présent) + Reverb |
| 3 | Solo | OCD Gain=0.55, Level=0.80, LPHP=True (lead) + Reverb (**wah = Cry Baby externe**) |

**Particularités :**
- **OCD always-on** : simule le canal overdrive permanent du JCM800. Pas de bypass clean.
- **Gain variable** : simule le potentiomètre de volume guitare qui pousse plus ou moins l'ampli.
- **LPHP=False sur Intro/Verse** : caractère chaleureux (volume roulé = ton chaud).
- **LPHP=True sur Chorus/Solo** : punch britannique JCM800 quand l'ampli est pleinement poussé.
- **Delay subtle sur Verse** : "presque un delay léger en fond" perçu sur le stem isolé.
- **Wah Cry Baby externe** : Eric utilise sa MC404 CAE physique pour le solo.

---

## Sources

| URL | Contenu |
|---|---|
| [Tom Morello fiche guitariste](../guitarists/tom_morello.md) | Philosophy volume rolled back, JCM800 cranked only |
| Analyse audio v3.2 (`audio_analysis/Audioslave_Out of Exile_03_Be Yourself_analysis.json`) | Bm, 117 BPM, 22 sections, solo confirmé 32s |
| Premier Guitar / Guitar World — interviews Morello | Setup classique JCM800 + Strat Soul Power |
