# Are You Gonna Go My Way — Lenny Kravitz (1993)

## Informations générales

| Champ | Valeur |
|---|---|
| Album | Are You Gonna Go My Way (1993) |
| BPM | 130 (confirmé analyse audio : 129.2) |
| Tonalité | **Mi mineur (Em)** — confirmé analyse audio v3.2 |
| Accordage | Standard — E A D G B E |
| Style | Hard rock, Funk-rock |
| Guitariste | Craig Ross (joue toutes les parties en une prise) |

---

## Structure du morceau

D'après l'analyse audio (8 sections détectées sur stem guitare isolé) :

| Temps | Section | Cluster | Intensité | Saturation | Snap HX |
|---|---|---|---|---|---|
| 00:00 → 00:17 | Intro | A | moderate (0.64) | moderate (0.39) | Riff |
| 00:17 → 00:30 | Verse 1 | D | moderate (0.68) | moderate (0.42) | Riff |
| 00:30 → 00:39 | Transition / pre-chorus | C | quiet (0.51) | moderate (0.37) | Riff |
| 00:39 → 01:21 | Chorus 1 + riff reprise | A | moderate (0.56) | moderate (0.46) | Riff |
| 01:21 → 02:33 | Verse 2 + Chorus 2 (gros bloc) | A | moderate (0.62) | low (0.25) | Riff |
| 02:33 → 02:42 | **Solo (debut)** | A | **peak (1.00)** | moderate (0.38) | **Solo** |
| 02:42 → 02:50 | **Solo (fin) / Bridge** | B | **peak (0.99)** | low (0.24) | **Bridge** ou **Solo** |
| 02:50 → 03:31 | Chorus outro | A | moderate (0.73) | moderate (0.32) | Riff |

**Notes clés :**
- **Le solo est court (~16s)** — confirmé par les deux sections à intensity=peak.
- **Bridge avec flanger** : le tape flanging Henry Hirsch est plus prononcé sur le bridge (section [B] à 2:42).
- **Tonalité** : Em confirmée par l'analyse audio (confidence 0.26 sur Krumhansl).

---

## Improvisation

| Section | Tonalité | Gammes recommandées | Notes |
|---|---|---|---|
| Solo | Mi mineur (Em) | Pentatonique Em, Em blues, Em naturelle | Style bluesy Hendrix/Page, ~16s, peu de notes mais beaucoup de feeling |

---

## Preset HX Effects

**Fichier :** `output/Are You Gonna Go My Way - Lenny Kravitz.hlx`

**Chaîne :**
```
Gate > Minotaur (Klon) > CompulsiveDrive (OCD) > GrayFlanger > Reverb
  0       1                  2                       3            4
```

| Snap | Nom | Son |
|---|---|---|
| 0 | Riff | Klon (Gain=0.40, Level=0.86) + OCD (Gain=0.65, Tone=0.35, LPHP=False, Level=0.80) + Reverb |
| 1 | Bridge | Idem Riff + Gray Flanger (Mix=0.48) |
| 2 | Solo | OCD Gain=0.78, Level=0.82 (push) + Reverb |
| 3 | Clean | Accordage / attente |

**Particularités :**
- **Gain stacking Klon + OCD** : remplace l'Arbitrator Fuzz initialement testé. Le Klon en front pousse l'OCD pour saturation perçue plus forte sans augmenter le volume.
- **OCD LPHP=False** : caractère chaleureux/chimey (pas le punch britannique JCM800)
- **Tone des deux dist baissés** (Klon 0.45, OCD 0.35) : compensation du caractère brillant du Super Distortion d'Eric
- **KinkyBoost retiré** : le gain stacking le remplace selon règle calibration projet

---

## Validation par analyse audio v3.2

L'analyse du stem guitare isolé (Demucs htdemucs_6s) confirme :
- ✅ Saturation moderate (0.41) globale — cohérent avec Skylark cranked
- ✅ Pas de delay, pas de reverb perceptible (cohérent avec mix sec)
- ✅ Pas de modulation détectable en global (le flanger n'est sur le bridge que ~8s)
- ✅ EQ bright sur les sections principales → preset compense avec Tone bas

Le preset adapte le son original pour le gear d'Eric (Super Distortion chevalet, Mesa Boogie clean). L'écart entre l'analyse de l'original et les paramètres du preset est **intentionnel** et cohérent avec la règle "audio = original, preset = adaptation gear".

---

## Sources

| URL | Contenu |
|---|---|
| [Guitar World — Craig Ross on AYGGMW](https://www.guitarworld.com/) | Craig Ross interview, une seule prise, Skylark |
| [Premier Guitar — Shred with Shifty Craig Ross](https://www.premierguitar.com/) | Détails techniques solo |
| [guitar.com — That whole thing was just one take](https://guitar.com/) | Confirmation solo une prise |
| Analyse audio v3.2 (`audio_analysis/01 - Are You Gonna Go My Way_analysis.json`) | Tonalité Em, BPM 129, structure 8 sections |
