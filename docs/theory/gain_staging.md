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

#### Pourquoi le clean paraît plus faible (physique)

**RMS vs crête.** Un son clean a une grande plage dynamique : les pics d'attaque sont bien
au-dessus du niveau moyen (RMS). La distorsion écrête ces pics → le RMS se rapproche
du niveau de crête. À SPL de crête égal, le son distordu a un RMS 6 à 12 dB plus élevé.
C'est le RMS que l'oreille perçoit comme sonie, pas les pics.

**Fletcher-Munson.** La distorsion génère des harmoniques dans la zone 2–5 kHz, là où
l'oreille est la plus sensible. Le son clean, riche en fondamentales graves, active moins
cette zone → il paraît plus faible à niveau mesuré identique.

**Conséquence pratique :** un clean aligné au VU avec un preset distordu sonnera encore
**2 à 4 dB plus faible** à volume de scène avec batterie et basse. La correction doit
dépasser la simple égalité mesurée.

#### Solutions par ordre de pertinence

| Technique | Mécanisme | Cas d'usage |
|---|---|---|
| **Compresseur (Red Squeeze)** | Remonte le RMS en réduisant les transitoires | Snaps clean avec jeu dynamique (funk, arpèges) |
| **Kinky Boost après reverb** | +6 dB volume pur (Drive=0, Boost=True) | Snaps clean simples, rapide à câbler |
| **EQ mid boost (1–2 kHz, +2–3 dB)** | Améliore la présence dans le mix sans volume brut | En complément d'un boost de volume |
| **volume_offset_db** | Décale tout le preset en sortie | Compensation inter-presets (pas intra-snapshots) |

#### Règle empirique validée en live (ingés FoH)

- Écart acceptable entre deux presets : **±1 à 2 dB**
- Seuil de correction obligatoire : **au-delà de 3 dB**
- Lift intentionnel pour solo lead : **+1 à +3 dB** (voulu)
- Boost clean pour compenser gain élevé : **+6 à +12 dB**
- **+2 à +4 dB supplémentaires** au-delà de l'égalité VU sur les snaps clean — à valider
  en répétition avec le groupe, pas au casque seul

#### Quand NE PAS compenser

Le contraste dynamique clean/distordu est parfois le **langage musical du morceau**.
Lithium (Nirvana) = philosophie quiet/loud Pixies — le verse clean DOIT être plus faible.
Ne pas compenser dans ce cas : la différence de volume est le message.

**Dans ce projet** : `volume_offset_db` du `PresetBuilder` pour l'égalisation inter-presets.
Kinky Boost ou compresseur pour l'égalisation intra-snapshot (Verse vs Chorus).

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
