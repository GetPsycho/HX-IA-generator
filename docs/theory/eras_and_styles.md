# Ères et Styles — Sons Guitare par Contexte

## Comment utiliser ce fichier

Ce guide relie un style/ère à une palette de sons typiques.
Utilisation recommandée :
1. Identifier le style et l'ère du morceau
2. Lire la palette attendue → premier filtre avant de chercher la fiche guitariste
3. Vérifier que le preset final est cohérent avec ce contexte

**Priorité :** La fiche guitariste spécifique (docs/guitarists/) est toujours plus fiable.
Ce guide est un point de départ, pas une règle absolue.

---

## Funk / Soul — 70s–80s

**Repères :** Nile Rodgers (Chic, David Bowie, Daft Punk), James Brown, Stevie Wonder.
**Dans le setlist :** Clara Luciani (Sage, style Nile Rodgers)

### Son caractéristique
- **Guitare :** Strat neck pickup ou bridge, cordes légères
- **Ampli :** Clean absolu — pas de saturation ampli
- **Compresseur :** Indispensable (Dyna Comp / Red Squeeze) — le squish est le son
- **Pas de distorsion**
- **Delay :** Absent ou très discret
- **Reverb :** Très courte (son sec, studio)

### Construction du preset
```
Gate → Red Squeeze → [Chorus discret] → Reverb courte
```
- Sensitivity compresseur : 0.55–0.70
- Mix reverb : 0.08–0.15 (quasi-absente)
- Chorus (optionnel) : CE-1, très bas Mix (0.35–0.45)

### Alerte de cohérence
Si le preset a de la distorsion ou une reverb longue → vérifier — très atypique pour ce style.

---

## Hard Rock / Classic Rock — 70s

**Repères :** Led Zeppelin, Jimi Hendrix, Cream, Lenny Kravitz (revivaliste 90s).
**Dans le setlist :** Are You Gonna Go My Way (Kravitz 1993 — son délibérément 70s)

### Son caractéristique
- **Guitare :** Les Paul ou Strat, humbuckers ou single-coil poussés
- **Ampli :** Marshall ou Marshall-like, push du préampli (crunch naturel de l'ampli)
- **Fuzz ou Big Muff** : saturation principale (pas d'OD transparente)
- **Wah** : très présente (Hendrix, Kravitz)
- **Pas de delay numérique** (ou slapback analogique)
- **Reverb** : spring (naturel d'ampli) ou absente
- **Phaser/Flanger** : possibles mais discrets (Flanger sur Bridge uniquement)
- **Pas de chorus** (trop moderne pour ce son)

### Construction du preset
```
Gate → Big Muff → [Flanger ou Wah externe] → [EQ 3Band] → [Delay slapback] → Reverb courte
```
- Big Muff : Sustain 0.75–0.85, Tone 0.45–0.55
- Reverb Mix : 0.15–0.20 (spring-like, courte)
- Delay si présent : slapback uniquement (Feedback=0, Time < 0.12)

### Alerte de cohérence
Chorus ou phaser présent sur tous les snaps → trop "moderne" pour un son 70s authentique.

---

## Grunge / Alt-Rock — 90s (US)

**Repères :** Nirvana, Pearl Jam, Soundgarden, Alice in Chains, Radiohead (debut).
**Dans le setlist :** Even Flow, Black Hole Sun, Creep

### Son caractéristique
- **Guitare :** Strat (Cobain, Greenwood), SG (Thayil), Les Paul (Cantrell)
- **Ampli :** Marshal JCM800, Mesa Boogie, ou solid-state poussé (Fender Eighty-Five)
- **Saturation principale :** Big Muff (Strat vers ampli clean) ou Marshall en crunch
- **Compresseur :** Absent ou très discret (dynamique préservée)
- **OD :** Légère si présente, pour pousser l'ampli (TS808 style)
- **Chorus :** Discret sur les parties clean (Nirvana Verse, Radiohead Verse)
- **Rotary :** Spécifique à Soundgarden (Kim Thayil, Leslie cabinet)
- **Reverb :** Présente mais pas excessive (Decay 0.40–0.55)
- **Phaser :** Rare (quelques titres de RHCP, pas grunge pur)

### Construction du preset (pattern typique grunge)
```
Gate → [Big Muff] → [Dimension D ou Chorus discret] → Reverb
```
- Big Muff Sustain : 0.72–0.85 selon l'intensité
- Chorus/Dimension : uniquement sur Verse clean, bypasse sur Refrain distordu
- Gate : souvent nécessaire (Big Muff = bruit de fond élevé)

### Alerte de cohérence
Compresseur fort (Sensitivity > 0.60) + Big Muff = inhabituel pour le grunge.
Delay long avec feedback = trop "alt-rock atmosphérique", pas grunge.

---

## Alt-Rock / Post-Grunge Atmosphérique — 90s–2000s

**Repères :** Radiohead (OK Computer+), Incubus, Coldplay, The Smashing Pumpkins.
**Dans le setlist :** Drive (Incubus 2001)

### Son caractéristique
- **Guitare :** Strat, 12 cordes possibles, jeu souvent arpégé
- **Ampli :** Clean ou légèrement crunchant
- **Phaser :** Central dans ce son (Incubus = Phase 90 / Boss PH-2)
- **Chorus :** Possible sur les parties clean, enrichit le son d'arpèges
- **OD :** Légère à medium, rarement très haute saturation
- **Delay :** Possible, souvent tempo-synché ou atmosphérique
- **Reverb :** Plus présente que le grunge (Decay 0.50–0.70), espace ouvert

### Construction du preset
```
Gate → [OD légère] → Phaser → [Chorus] → Reverb large
```
- Phaser Rate variable par snapshot (lent sur intro, plus vif sur verse)
- Reverb Decay : 0.50–0.65 (espace)
- OD si présente : Gain très modéré (0.15–0.35)

### Alerte de cohérence
Pas de phaser/chorus = son trop sec pour ce style. Distorsion élevée = atypique.

---

## Funk-Rock / Alt-Rock Groovy — 90s–2000s

**Repères :** Red Hot Chili Peppers (Frusciante), Rage Against The Machine, Audioslave.
**Dans le setlist :** Dani California (RHCP), Be Yourself (Audioslave)

### Son caractéristique RHCP (Frusciante)
- **Guitare :** Strat 54 ou 62, neck pickup pour funk, bridge pour leads
- **Ampli :** Marshall Major ou Fender Dual Showman — son chaud et puissant
- **Envelope filter (Auto Filter) :** Sur les licks funk (Moog MF-101 style)
- **OD** : Légère (crunch de Strat) sur le verse, DS-2 ou équivalent sur le chorus/solo
- **Wah :** External, sur les solos
- **Compresseur :** Discret ou absent (dynamique préservée pour le funk)
- **Reverb :** Présente, naturelle

### Son caractéristique Audioslave (Morello)
- **Guitare :** ESP Telecaster custom, DiMarzio
- **Ampli :** Marshall JCM900, Silvertone vintage
- **OD :** Medium à élevée (crunch rock), pas de fuzz
- **Whammy :** Signature (pas disponible sur HX Effects dans ce projet)
- **Effets spéciaux :** Killswitch (interruptions rythmiques), talk box
- **Reverb :** Discrète

### Construction du preset RHCP
```
Gate → OCD légère → AutoFilter (BP) → [Dist chorus] → Reverb
```
- AutoFilter Mode 1 (BP) : plus funk que Mode 0 (LP trop grave)
- OCD Gain très bas (0.04–0.10) pour le crunch de Strat

### Alerte de cohérence
AutoFilter Mode 0 (LP) sur le lick funk = son trop grave/boueux (leçon Dani California).

---

## Nu-Metal / Alt-Metal — 2000s

**Repères :** System of a Down, Muse, Linkin Park, Rage Against The Machine.
**Dans le setlist :** Toxicity (SOAD), Hysteria (Muse), Plug In Baby (Muse)

### Son caractéristique SOAD (Daron Malakian)
- **Guitare :** Gibson, accordage Drop C ou Drop D
- **Ampli :** Mesa Boogie Dual Rectifier, Marshall JCM2000
- **Dist :** Haute saturation (Boss HM-2 ou équivalent chainsaw)
- **Gate :** Essentiel — noise gate serré pour le palm-muting tight
- **Pas de modulation** (pas de phaser/chorus)
- **Reverb :** Courte (Decay 0.30–0.40)

### Son caractéristique Muse (Bellamy)
- **Guitare :** Gibson Les Paul, Manson custom (circuit intégré)
- **Ampli :** Marshall JMP-1, saturation élevée
- **Fuzz :** Gated fuzz (Fuzz Factory) pour Plug In Baby — gate élevé, Gate saccadé
- **OD :** KWB (Kowloon Walled Bunny) pour Hysteria — haute saturation, basse agressive
- **Octave/Pitch :** Signature Muse (non représenté ici)
- **Reverb :** Discrète

### Construction du preset
```
Gate (serré) → [Fuzz/Dist haute gain] → [EQ mid boost] → Reverb courte
```
- Gate Threshold : -48 à -46 dB (metal/palm-muting)
- Dist Gain : 0.75–0.95 selon le modèle
- Reverb Decay : 0.28–0.40

### Alerte de cohérence
Compresseur avant une dist haute gain = inhabituel pour le metal (compresse ce que la dist va saturer).
Phaser actif sur tous les snaps = atypique pour ce style.

---

## Stoner Rock / Desert Rock — 90s–2000s

**Repères :** Queens of the Stone Age, Fu Manchu, Kyuss.
**Dans le setlist :** No One Knows (QOTSA 2002)

### Son caractéristique
- **Guitare :** Les Paul ou similaire, accordage Standard ou DADGAD
- **Ampli :** Mesa Boogie Mark I (Josh Homme), son mid-heavy vintage
- **OD :** Légère à medium (SD-1 / Stupor OD), jamais très haute distorsion
- **EQ :** Boost des mids (500 Hz–1 kHz) — centrale dans ce son
- **Gate :** Présent pour le silence entre les riffs
- **Reverb :** Très discrète (Decay 0.25–0.35, son sec et direct)
- **Pas de modulation** (pas de phaser/chorus)

### Construction du preset
```
Gate → OD légère → 10-Band EQ (boost 500–2k) → Reverb très courte
```
- EQ : +3 à +5 dB à 1 kHz (présence mid-heavy signature Josh Homme)
- Reverb Mix : 0.08–0.12 (quasi-absente)

---

## Post-Grunge / Rock Alternatif — 2000s

**Repères :** Nickelback, Linkin Park, Puddle of Mudd, Kings of Leon.
**Dans le setlist :** How You Remind Me (Nickelback), Sex on Fire (Kings of Leon)

### Son caractéristique Nickelback (Ryan Peake)
- **Boss HM-2** (Swedish Chainsaw) : tout au maximum = son "chainsaw"
- **Ampli :** Marshall JCM900
- **Gate serré** (palm-muting agressif)
- **Pas de modulation**

### Son caractéristique Kings of Leon (Matthew Followill)
- **Guitare :** Gibson ES-325, Epiphone Casino
- **Son crunchant** mais pas haute saturation
- **Phaser** : Small Stone discret sur certains titres (Bridge de Sex on Fire)
- **Reverb** : Présente (rock indie, son ouvert)

### Construction du preset Nickelback
```
Gate (très serré) → HM-2 (tout à fond) → Reverb courte
```

### Construction du preset Kings of Leon
```
Gate → OCD (crunch léger-medium) → [Phaser discret] → Reverb
```
- Phaser uniquement sur un snap (Bridge), bypasse en Verse/Chorus

---

## Pop-Rock Française — 2020s

**Repères :** Clara Luciani, Pomme, Angèle (guitares discrètes).
**Dans le setlist :** Le Reste, Nue, Radio Song, Travel The World (Sage / Ambroise Willaume)

### Son caractéristique (Sage, style Nile Rodgers)
- **Guitare :** Strat ou Telecaster, cordes légères
- **Son propre absolu** — zéro distorsion
- **Compresseur fort** (Nile Rodgers = Red Squeeze Sensitivity 0.65+)
- **Chorus discret** (CE-1 sur les refrains, Mix 0.35–0.45)
- **Reverb discrète** (Decay 0.40–0.55, Mix 0.15–0.20)
- **Phaser** : absent (trop coloré pour ce style pop)

### Construction du preset
```
Gate discret → Red Squeeze → [Chorus70s sur refrain] → Reverb
```
- Gate Threshold : -54 à -52 dB (très discret pour laisser passer les attaques clean)

### Alerte de cohérence
Toute saturation sur un preset Clara Luciani = erreur (sauf titre spécifique demandé).

---

## Tableau de Référence Rapide

| Style | Ère | Saturation | Compresseur | Modulation | Reverb Mix | Exemple setlist |
|---|---|---|---|---|---|---|
| Funk/Soul | 70–80s | Aucune | Fort (0.60+) | Chorus discret | 0.08–0.12 | Clara Luciani |
| Hard rock | 70s | Fuzz/Big Muff | Absent | Absent | 0.15–0.18 | AYGGMW |
| Grunge | 90s | Big Muff | Discret | Dimension/Chorus clean only | 0.18–0.22 | BHS, Creep, Even Flow |
| Alt-rock atmosphérique | 90–00s | OD légère | Absent | Phaser central | 0.22–0.28 | Drive |
| Funk-rock | 90–00s | OD légère + Dist | Absent | Envelope filter | 0.18–0.22 | Dani California |
| Nu-metal | 00s | Haute gain | Absent | Absent | 0.08–0.15 | Toxicity, Muse |
| Stoner rock | 90–00s | OD medium | Absent | Absent | 0.08–0.12 | No One Knows |
| Post-grunge | 00s | HM-2 ou OCD | Absent | Phaser discret | 0.18–0.28 | Nickelback, KoL |
| Pop-rock fr | 20s | Aucune | Fort (0.65+) | Chorus refrain | 0.15–0.20 | Clara Luciani |

---

## Sources
- Rolling Stone — History of Guitar Tones
- Premier Guitar — Era-Defining Tones
- Guitar World — Decade by Decade Guitar Sounds
- Fiches guitaristes : docs/guitarists/ (référence prioritaire)
- Expérience projet : tous les presets ci-dessus
