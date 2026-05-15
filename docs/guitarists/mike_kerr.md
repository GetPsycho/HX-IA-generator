# Mike Kerr — Royal Blood

## Instrument

**Basse court-scale** (Fender Jaguar Bass signature, 30"). Royal Blood est un duo basse/batterie sans guitare.

---

## Rig — Split signal (signature Royal Blood)

Le son "guitare" de Royal Blood vient d'un signal de basse splitté en deux chemins :

```
Fender Jaguar Bass
  → Boss LS-2 Line Selector (split)
    ├── Chemin A : ampli basse (Fender Bassman) → bas du spectre, son clean
    └── Chemin B : EHX POG2 (+1 oct) → Fuzz → ampli guitare (Fender Supersonic) → son "guitare"
```

Le POG2 transpose la basse **une octave AU-DESSUS** pour la mettre dans le registre guitare, puis le fuzz crée le mur de son caractéristique.

---

## Pédales principales

| Pédale | Usage |
|---|---|
| **EHX POG2** (×2) | Octave +1 (met la basse en registre guitare) |
| **ZVex Mastotron Fuzz** | Fuzz principal, son très chargé |
| **EHX Germanium 4 Big Muff Pi** | Fuzz alternatif, son plus chaud |
| **Tech 21 Red Ripper** | Dist basse, maintient le sub-bass sur le chemin A |
| Boss LS-2 | Split du signal |
| Boss PS-6 Pitch Shifter | Effets dive-bomb, solos |

---

## Accordage

Standard basse : E-B-G-D. Pas d'accordage alternatif.

---

## Sons par titre

| Titre | Section | Son | Notes |
|---|---|---|---|
| **Figure It Out** | Riff/Chorus | Basse fuzzée plein registre | POG2 +1 oct + Mastotron/Big Muff, fort Oct1 |
| **Figure It Out** | Verse | Légèrement plus aéré | Même chaîne, octave moins prononcée |

---

## Adaptation HX Effects (guitare → simulation basse)

Logique **inversée** par rapport au rig original :
- Kerr : basse → POG2 **+1 oct** → registre guitare
- Eric (guitare) : guitare → Boctaver **-1 oct** → registre basse

| Élément original | Adaptation Eric | Model ID |
|---|---|---|
| POG2 (+1 oct sur basse) | Boctaver (-1 oct sur guitare) | `VIC_PitchBoctaver` |
| EHX Bass Big Muff Pi | Industrial Fuzz (EHX Bass Big Muff) | `HD2_DistIndustrialFuzz` |

**Note tracking Boctaver** : le Boss OC-2 (Boctaver) fonctionne mieux sur **notes simples** — les riffs Royal Blood sont mélodiques, pas en accords → tracking optimal.

---

## Sources

- https://www.guitarworld.com/features/royal-blood-mike-kerr-gear
- https://blog.andertons.co.uk/sound-like/sound-like-royal-blood
- https://deplike.com/blog/rig-detective-royal-blood/
- https://equipboard.com/pros/mike-kerr
- https://www.cogeffects.co.uk/royal-blood.php
