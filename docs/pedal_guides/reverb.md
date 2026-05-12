# Reverb — Guide des Paramètres

## Rôle de la Reverb Guitare

La reverb simule l'acoustique d'un espace (salle, chambre, hall, plaque...).
Elle ajoute :
- **Sustain** perçu (les notes semblent tenir plus longtemps)
- **Espace** (son tridimensionnel, impression de volume)
- **Cohésion** entre les sons (les notes fortes et douces semblent appartenir au même espace)

**Règle d'or :** La reverb ne devrait pas s'entendre — on devrait entendre son absence.
Si on perçoit clairement la reverb, Mix ou Decay est probablement trop élevé.

---

## Ganymede = Line 6 Original Reverb

**HX Effects model ID :** `HD2_ReverbGanymede`

La Ganymede est la reverb "flagship" de la gamme Line 6. Caractère : espace ambiant
très ouvert, musicalité élevée, modulation intégrée pour éviter un son figé/artificiel.
Basée sur les algorithmes Lexicon (référence studio), mais avec une signature Line 6 propre.

### Paramètres
| Param | Plage | Ce que ça fait vraiment |
|---|---|---|
| **Decay** | 0–1 | Durée de la queue de reverb. 0.3 = courte (studio) ; 0.5 = medium ; 0.7+ = grande salle/hall |
| **Predelay** | 0–0.5 s | Délai avant le début de la reverb. 0.02 = léger (son naturel) ; 0.06+ = sensation de distance |
| **Tone** | 0–1 | Filtre de la reverb en sortie. 0.5 = neutre ; 0.6–0.7 = légèrement brillant (présence) ; < 0.4 = sombre |
| **Modulation** | 0–1 | LFO interne qui module légèrement la reverb. 0.15–0.25 = naturel ; 0 = figé/digital ; 0.5+ = chorus-like |
| **Mix** | 0–1 | Volume de la reverb par rapport au signal sec. 0.08–0.12 = très discrète ; 0.18–0.25 = présente |

---

## Sweet spots Ganymede

| Contexte | Decay | Predelay | Tone | Modulation | Mix | Notes |
|---|---|---|---|---|---|---|
| Clean ambiant discret | 0.10 | 0.01 | 0.60 | 0.20 | 0.10 | Quasi-invisible, juste de l'air |
| Rock/pop standard | 0.42–0.52 | 0.02 | 0.58–0.62 | 0.20 | 0.16–0.22 | Présente sans dominer |
| Intro atmosphérique | 0.62–0.70 | 0.02 | 0.62 | 0.20 | 0.24–0.28 | Grande salle, Intro Drive style |
| Metal serré | 0.30 | 0.01 | 0.55 | 0.10 | 0.08 | Reverb très courte, pas de boue |
| Ambient/shoegaze | 0.80–0.90 | 0.04 | 0.65 | 0.30 | 0.40+ | Wall of reverb, effet de nappe |
| Accordage/attente (snap Clean) | 0.45 | 0.02 | 0.60 | 0.20 | 0.10 | Volume bas, juste présente |

---

## Paramètre Decay — Guide Visuel

```
Decay 0.10 : ████                (studio tight, peu de queue)
Decay 0.30 : ████████████        (rock)
Decay 0.50 : ████████████████████ (medium, la moitié de la plage)
Decay 0.70 : ████████████████████████████ (grande salle)
Decay 0.90 : ████████████████████████████████████ (hall/cathédrale)
```

**Danger du Decay trop élevé :** Les notes se chevauchent → boue, perte de lisibilité.
Sur un accord rythmique, un Decay 0.70+ peut rendre le jeu complètement illisible.

---

## Predelay — Pourquoi 0.02 par défaut

Le **Predelay** est le temps entre le signal sec et le début de la réverbération.

- **Predelay = 0** : reverb commence immédiatement → son "dans" la pièce, peu de distance
- **Predelay = 0.02 (20 ms)** : légère séparation signal/reverb → son naturel, guitare en avant
- **Predelay = 0.06 (60 ms)** : séparation perceptible → son d'"espace" plus grand, distance
- **Predelay > 0.10** : effet de delay avant la reverb → son artificiel/studio

La valeur 0.02 est un équilibre : le signal sec reste lisible, la reverb soutient sans coller.

---

## Modulation — Éviter la Reverb "Digitale"

Une reverb sans modulation sonne souvent artificiellement "figée" (problème des reverbs
numériques first-gen). La modulation interne ajoute une légère variation naturelle.

**0.15–0.25 :** Modulation naturelle, l'oreille ne l'entend pas consciemment.
**0.30–0.40 :** Modulation plus évidente, commence à sonner comme un chorus-reverb.
**0.50+ :** Effet voulu uniquement (shimmer, espace ambient prononcé).

---

## Placement Reverb dans la Chaîne

```
Guitare → Gate → OD → Modulation → Delay → Reverb
```

**Toujours en dernier (ou avant-dernier avec boost/vol en fin) :**
La reverb doit envelopper le son final. Si un OD est après la reverb, la queue de reverb
est saturée → son désordonné et peu musical.

**Exception valide :** KinkyBoost/VolPanGain après la reverb pour ajuster le volume global
du preset sans re-colorer la queue de reverb.

---

## Reverb et Gate — Interaction Critique

**Problème :** Un Gate avec Threshold trop élevé peut couper les queues de reverb.

```
Bonne pratique : Gate avant la reverb dans la chaîne
→ le Gate ne touche pas à la queue de reverb (il coupe le signal ENTRANT)
```

Si le Gate est placé **après** la reverb, les queues sont également gatées → coupures
abruptes sur la fin des notes, son très peu naturel.

**Dans ce projet :** Gate toujours en slot 0 (premier), Reverb en slot 3 ou 4 (après l'OD).
Le Gate voit le signal propre, la reverb voit le signal filtré+saturé.

---

## Interaction Reverb et Mix par Snapshot

La Ganymede est partagée entre tous les snapshots, mais son Mix peut être ajusté
par snapshot via le paramètre `params` dans `add_snapshot()`.

**Cas classique :** Snap "Clean" avec `Mix: 0.10` — reverb réduite pour un son
d'accordage discret, sans la reverb "live" du snap Verse.

```python
pb.add_snapshot(3, "Clean", blocks_on=[0, 3],
                params={3: {"Mix": 0.10}},  # reverb discrète sur snap Clean
                color="blue")
```

---

## Autres Types de Reverb (référence)

Les modèles suivants existent dans HX Effects mais ne sont pas utilisés dans le projet :

| Model | Caractère | Quand l'utiliser |
|---|---|---|
| **Spring Reverb** | Son de printemps de Fender/Marshall | Blues classique, rockabilly |
| **Plate Reverb** | Chaleureux, studio vintage | Solos, sons chantants |
| **Room Reverb** | Court, naturel | Son "live" réaliste |
| **Hall Reverb** | Grand espace, queue longue | Ballades, ambient |
| **Cave Reverb** | Très long, non-linéaire | Expérimental, shoegaze |

La **Ganymede** est le choix polyvalent : pas de "coloration" vintage de la spring,
mais assez musical pour couvrir tous les styles du setlist.

---

## Sources
- Lexicon — Digital Reverb Technology
- Line 6 HX Effects Pilot's Guide
- Guitar World — Understanding Reverb Types
- Sound on Sound — Reverb Placement Techniques
- Expérience projet : tous les presets utilisent la Ganymede, Mix ajusté par snapshot (Clean snap)
