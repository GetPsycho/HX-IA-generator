# Gain Staging et Compensation de Volume

## Principe fondamental : Gain ≠ Volume

Le **Gain** contrôle la quantité de saturation/distorsion du circuit.
Le **Level** (ou Output/Volume) contrôle la quantité de signal qui sort de la pédale.

Ces deux paramètres sont **indépendants mais liés** :

> Quand on monte le Gain, on monte aussi implicitement le niveau perçu
> (la saturation ajoute des harmoniques qui sonnent "plus fort").
> Il faut donc baisser le Level pour compenser.

### Exemple concret — OCD entre deux snapshots

```
Chorus : Gain=0.32, Level=0.55  → niveau perçu OK
Solo   : Gain=0.62, Level=0.55  → TROP FORT (le gain +30% a dopé le volume perçu)
Solo   : Gain=0.62, Level=0.48  → niveau perçu cohérent avec le Chorus
```

**Règle de base :** Si tu montes le Gain de 0.2–0.3, baisse le Level de 0.05–0.10
pour compenser. Toujours vérifier à l'oreille.

---

## Gain Stacking

Empiler plusieurs étages de gain pour obtenir un son qu'aucune pédale seule
ne peut donner. L'ordre **compte énormément**.

### Principe

```
Signal → OD légère → Dist haute → Ampli
```

Chaque étage reçoit un signal déjà coloré/compressé par le précédent.
Le résultat est plus riche qu'une seule pédale à gain élevé.

### Ordre recommandé : du moins au plus saturé

```
Clean Boost → OD légère → OD/Dist medium → Dist haute → Fuzz
```

**Pourquoi ?** La pédale la plus saturée réagit au signal qu'elle reçoit.
Une OD légère avant une fuzz "nourrit" la fuzz avec un signal chaud et compressé
→ la fuzz sonne plus épaisse et tenue.

L'inverse (Fuzz → OD) est possible mais donne un son différent :
l'OD "nettoie" et structure la fuzz, moins de chaos.

### Combos classiques

| Combo | Effet | Contexte |
|---|---|---|
| Klon → OCD | Klon booste les mids avant l'OCD → crunch plus épais | Rock, Maneskin |
| TS9 → Big Muff | TS tightens le bas, la fuzz gagne du punch | Grunge, stoner |
| EP Booster → OD | Preampli qui "nourrit" l'OD, plus de sustain | Solos, rock classique |
| OD léger → Dist haute gain | OD façonne les fréquences avant la dist | Metal, punk |
| TS9 → Marshall JCM800 | Tube Screamer pousse le préampli de l'ampli | Blues-rock classique |
| Fuzz → Wah | Wah filtre un signal déjà saturé, son plus "gras" | Hendrix inversé |
| Wah → Fuzz | Wah quacky + fuzz derrière, son plus conventionnel | Hendrix standard |

### Boost avant vs après OD

| Position | Résultat |
|---|---|
| **Boost avant OD** | Pousse l'OD plus fort → plus de saturation, de sustain, d'harmoniques |
| **Boost après OD** | Augmente juste le volume de sortie → idéal pour les solos (level boost) |

Pour un "solo boost" : mettre le boost **après** l'OD en mode level +6 à +10 dB.
Pour changer le caractère de l'OD : mettre le boost **avant**.

---

## La Fuzz et le Volume Guitare

Particularité unique des fuzzes à transistors : elles répondent au volume de la guitare.

- **Volume guitare à 10** : fuzz maximale, saturée et chaotique
- **Volume guitare à 6–7** : overdrive épais mais contrôlé
- **Volume guitare à 3–4** : son propre mais avec du corps

C'est le "clean-up" naturel de la fuzz. Cela permet une grande expressivité
sans changer de preset — simplement en roulant le volume de la guitare.

**Sur HX Effects** : ce comportement est reproduit sur les modèles Fuzz (Industrial Fuzz,
Bighorn, Triangle Fuzz, etc.). Le signal entrant dans le bloc fuzz simule ce comportement.

---

## Compensation de Level entre Snapshots

Problème courant : un snapshot "Solo" est plus fort qu'un snapshot "Chorus" parce qu'on
a monté le Gain sans baisser le Level.

### Méthode de calibration

1. **Snap de référence** : le snapshot le plus joué (souvent Chorus/Verse)
2. Fixer son Level en premier
3. Pour chaque autre snap, ajuster Level pour **matcher le volume perçu**
4. Le Solo peut être légèrement plus fort (+1 à +2 dB perçu) — c'est voulu
5. Le Clean doit être compensé si pas de disto (voir Kinky Boost / Red Squeeze)

### Compensation du son clean

Un signal propre est intrinsèquement moins "présent" qu'un signal distordu
(la disto ajoute des harmoniques = énergie perçue). Solutions :

- **Compresseur** : nourrit le signal clean avec plus d'attaque et sustain (Red Squeeze)
- **Kinky Boost (EP Booster)** : preampli qui ajoute corps et chaleur (+harmonic richness)
- **VolPanGain** : boost dB pur (moins coloré) — attention au bug footswitch si mal géré

**Dans ce projet** : on utilise le `volume_offset_db` du `PresetBuilder` pour l'égalisation
globale entre presets, et les Level des effets pour l'égalisation interne par snapshot.

---

## Règles résumées

1. **Gain monte → Level baisse** (compenser ~0.05–0.10 par +0.20 de gain)
2. **Gain stacking** : toujours du moins saturé vers le plus saturé
3. **Boost avant OD** = change le caractère / **Boost après OD** = change le volume
4. **Son clean + compresseur** = meilleure alternative que boost pur pour la cohérence live
5. **OD avant Fuzz** = fuzz plus tenue / **Fuzz avant OD** = fuzz structurée
6. **Fuzz + volume guitare** = technique de clean-up essentielle
7. Toujours calibrer les levels **à l'oreille** après les avoir estimés par calcul

---

## Sources
- MusicRadar — Gain Stacking Order and More Explained
- Premier Guitar — Tone Tips : Overdrives, Distortions and Boosts
- Premier Guitar — ABCs of Compression
- Expérience projet : calibration Be Yourself, Black Hole Sun, Creep
