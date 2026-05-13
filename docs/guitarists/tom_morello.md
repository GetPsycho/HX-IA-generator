# Tom Morello — Audioslave / RATM

## Groupes
- Rage Against the Machine (RATM) — 1991-2000, 2007-2011, 2019-
- Audioslave — 2001-2007 (avec Chris Cornell)

## Guitares principales

| Guitare | Album | Détail |
|---|---|---|
| **Fender Soul Power Strat** | Audioslave (2002), **Out of Exile (2005)** | Trouvée au Guitar Center Hollywood. Modifiée : Seymour Duncan Hot Rails (bridge), Fender Noiseless (neck/mid), killswitch, tremolo Ibanez Edge locking. |
| **Gibson Les Paul Custom Shop "Budweiser"** | **Revelations (2006)** | DiMarzio Super Distortion (bridge) + DiMarzio P.A.F. (neck). |
| Fender Telecaster "Sendero Luminoso" | RATM | Drop-D, usage ponctuel. |

**"Be Yourself" (Out of Exile, 2005) : Soul Power Strat.** Accordage standard E.

Cordes : GHS Boomers 9-46. Médiator : Dunlop Tortex Jazz Purple 1.14mm.

---

## Amplis

| Ampli | Notes |
|---|---|
| **Marshall JCM 800 2205 (50W)** | **Principal depuis 1988.** Canal boost/overdrive uniquement — jamais le canal clean. Cabinet Peavey 4×12 1987 avec Celestion G12K-85. |
| Vox AC30 TB(X) | Introduit pour Revelations. Overdubs et doublages. |

**Réglages JCM800 documentés (photo + déclarations Morello) :**

| Param | Valeur |
|---|---|
| Gain | 9 |
| Bass | 10 |
| Middle | 10 |
| Treble | 6–7 |
| Presence | 1–7 (sources divergent) |
| Master Volume | 6 |
| Reverb | **0** |

Morello n'utilise **que le canal overdrive** — aucune pédale de distorsion ou d'OD.
Toute la saturation vient du préampli du JCM800.

---

## Pédales et chaîne de signal (ère Audioslave)

**Architecture clé : toutes les pédales sont dans la boucle d'effets (FX loop) du JCM800.**
Rien avant l'ampli (pas de boost d'entrée, pas d'OD frontale).

```
Guitare → JCM800 (canal overdrive, Gain 9)
  → FX Send
    → Boss TR-2 Tremolo
    → Dunlop GCB-95 Cry Baby Wah
    → DigiTech WH-1 Whammy (original V1)
    → Boss DD-2 / DD-3 Digital Delay
    → DOD FX40B EQ (boost de solo : EQ flat, Level +)
    → MXR Phase 90
  → FX Return → Cabinet
```

| Pédale | Rôle |
|---|---|
| **Dunlop GCB-95 Cry Baby** | Wah solos expressifs (balayage lent et lyrique) |
| **DigiTech WH-1 Whammy** | Pitch-shift, harmonies (Cochise, Like a Stone) |
| **Boss DD-2/DD-3** | Delay principal (slap-back ou séquences) |
| **DOD FX40B EQ** | **Boost de solo uniquement** — EQ flat, Level au-dessus de l'ampli |
| MXR Phase 90 | Phaser lent (ponctuel) |
| Boss TR-2 Tremolo | Like a Stone, Gasoline |
| DigiTech XP-300 Space Station | Effets spéciaux ponctuels |

---

## Sons par titre

| Titre | Album | Son | Notes |
|---|---|---|---|
| **Be Yourself** | Out of Exile | Crunch très léger intro (vol. guitare roulé) → crunch modéré verse → crunch fort chorus → crunch + DOD boost solo | Pas de delay documenté sur ce titre. Wah = GCB-95 sur solo. |
| Like a Stone | Audioslave | Clean + tremolo (verse), crunch (chorus), Whammy + wah (solo) | |
| Cochise | Audioslave | Overdrive fort + Whammy (riff intro), wah solo | |
| Show Me How to Live | Audioslave | Crunch fort, riff puissant | |
| Gasoline | Audioslave | Clean + tremolo, crunch modéré | |
| Killing in the Name | RATM | Overdrive élevé + Whammy | |

---

## Technique — Sons clairs sans canal clean

Morello n'a pas de canal clean sur le JCM800. Il obtient ses sons quasi-propres en
**roulant le potentiomètre de volume de la guitare** sur le canal overdrive.
Résultat : crunch très léger (pas un clean pur), typique des arpèges de Be Yourself.

Cette technique est cruciale pour les presets : l'OCD ne doit **pas** être bypassée
sur les snaps "intro" — elle doit rester active avec un Gain très bas (~0.08).

---

## Notes pour les presets

- **Be Yourself :** OCD `enabled_default=True` (toujours active, simule le canal gain permanent). Gain variable par snapshot : Intro 0.08, Verse 0.22, Chorus 0.38, Solo 0.55.
- **LPHP switch OCD :** False (LP) sur Intro/Verse = chaleur ; True (HP) sur Chorus/Solo = punch Marshall britannique.
- **KinkyBoost = DOD FX40B** sur Solo uniquement (Drive=0, Boost=True = +6 dB propre).
- **Pas de delay** sur Be Yourself — non documenté sur ce titre.
- **Wah externe** : Cry Baby GCB95 de Morello ≈ Cry Baby MC404 CAE d'Eric.

---

## Sources

- Guitar World — Soul Power Strat (Morello)
- Guitar Gear Finder — Tom Morello Audioslave Rig
- Ground Guitar — Tom Morello Guitars & Gear
- Guitar Chalk — Tom Morello Amp Settings
- Neural DSP — Tom Morello Pedalboard and Amp Settings
- Rig Diagram — Tom Morello Audioslave 2004 (guitar.com)
- Equipboard — Tom Morello
