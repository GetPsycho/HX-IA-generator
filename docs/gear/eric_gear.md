# Gear d'Eric — Référence pour les Presets

## Guitare

### Principale : Fender Stratocaster US

Configuration micros mixte :

| Position | Micro | Sortie | Usage |
|---|---|---|---|
| **Chevalet** | DiMarzio Super Distortion | Très haute (~13.7 kΩ) | **Principal** — riffs, accords, rhythm |
| **Milieu** | Original Strat single-coil | Faible | Funk, positions mixtes |
| **Manche** | Original Strat single-coil | Faible | Solos |

**Incidence sur les presets :**
- Le Super Distortion au chevalet pousse les étages de gain plus fort qu'un single-coil.
  À Gain égal, la saturation sera plus importante que chez les guitaristes référence
  (Frusciante, Cobain) qui utilisent des single-coils. Ne pas compenser artificiellement —
  ça contribue à une sonorité propre à Eric.
- Le micro milieu (single-coil d'origine) pour le funk : plus proche des sons Frusciante/Nile
  Rodgers (single-coil neck/mid). Position 4 (milieu + chevalet) possible aussi.
- Le micro manche (single-coil d'origine) pour les solos : sortie plus faible, son plus doux.
  Le KinkyBoost (boost de solo) est d'autant plus utile pour compenser le delta de volume
  entre le chevalet (rhythm) et le manche (solo).

---

### Seconde guitare : Lag Roxanne

| Caractéristique | Valeur |
|---|---|
| Micros | 2 humbuckers Seymour Duncan |
| Accordage | C standard (C F Bb Eb G C) — baritone tuning |
| Usage | Morceaux baritone — ex : No One Knows (QOTSA), micro chevalet |

**Incidence :** Cette guitare est dédiée aux morceaux nécessitant un accordage très bas
(C standard), évitant un pitch shift logiciel qui dégrade le son. Les humbuckers
Seymour Duncan apportent un caractère plus chaud et épais que la Stratocaster pour
les sons stoner/rock baritone.

---

## Ampli

**Mesa Boogie Single Rectifier 50W** — utilisé en **son clair exclusivement**.

| Param | Valeur |
|---|---|
| Canal | Clean uniquement |
| Volume | Adapté à la scène |
| EQ | À calibrer selon la salle |

**Cabinet :** Mesa Boogie 2×12.

**Connexion HX Effects :** entrée guitare de l'ampli (pas en 4CM / FX loop).

```
Guitare → HX Effects → Entrée guitare Mesa Boogie → Cab 2×12
```

**Incidence du Mesa Boogie clean sur les presets :**

Le signal HX Effects passe par le préampli du Mesa avant d'atteindre le cab.
Le Single Rectifier clean channel a un caractère propre :

- **Son articulé et tight** — le Mesa clean a une définition du bas-médium très nette.
  Les OD/dist du HX sonneront plus serrées et moins "spongy" que sur un Marshall.
- **Légèrement brillant** — le Mesa clean peut avoir tendance à accentuer les aigus.
  Surveiller les réglages Tone/Treble des pédales — ne pas aller trop haut.
- **Préampli à fort headroom** — peu de compression naturelle sur le son clean,
  contrairement à un Fender Tweed ou un Vox AC30. Le compresseur dans le HX
  est donc plus important pour densifier les sons clairs.
- **Différence vs Marshall** — les presets qui simulent un Marshall (Be Yourself)
  passeront par un préampli Mesa très différent. Le caractère "Marshall" vient alors
  entièrement de l'OCD dans le HX — le Mesa apporte juste une coloration propre.

---

## Wah

**Dunlop Cry Baby MC404 CAE** — connectée en externe, avant le HX Effects.

```
Guitare → MC404 CAE → HX Effects → Mesa
```

- Pas modélisée dans les presets HX
- Pour les titres avec wah (solos Dani California, Be Yourself, Even Flow) :
  Eric utilise la MC404 physiquement, sans snap dédié dans le HX
- Le sweep de la MC404 est plus large et plus vocal que le GCB-95 standard

---

## Pédales possédées (référence sonore)

**Keeley 1962X** — British Overdrive (lignée Marshall Bluesbreaker, même famille
que l'Analogman Prince of Tone). Eric apprécie particulièrement son grain/épaisseur.

- **Équivalent HX** : Heir Apparent (`HD2_DistHeirApparent`) — déjà utilisé dans le
  projet pour le pattern "Intro arpège + grain léger" (Gain=0.20, léger). Le même
  modèle peut être poussé plus fort (Gain~0.45-0.55) pour un usage "grain + épaisseur"
  plus présent (ex : No Roots — doublage de riff basse).
- Pas connectée en externe comme la wah — c'est une référence de caractère sonore
  à privilégier quand un OD/crunch "British" moyen-pousse convient au morceau.

---

## Implications globales pour la création de presets

1. **Gain** : Ne pas sur-saturer — le Super Distortion au chevalet pousse déjà fort.
   Les Gain suggérés dans les presets sont des points de départ ; tester avec la guitare réelle.

2. **Tone / Treble** : Surveiller les aigus — le Mesa clean peut accentuer.
   Préférer des valeurs Tone légèrement en dessous de la neutralité (0.50–0.58) plutôt qu'élevées.

3. **Solos** : Micro manche (single-coil faible sortie) = delta de volume avec le chevalet.
   Le KinkyBoost de solo est d'autant plus justifié.

4. **Funk pur** : Micro milieu (single-coil d'origine) — sortie faible, son quacky et articulé.
   Compresseur Sensitivity : 0.55–0.70 (sortie faible → plus de compression nécessaire).
   L'AutoFilter (Dani California Lick) sera plus efficace sur ce micro.
   **Funk-rock** : Super Distortion chevalet — sortie haute, chaîne comp → OD.
   Compresseur Sensitivity : 0.45–0.55 (sortie élevée → comprimer moins pour garder le punch).

5. **Pas de 4CM** : Tous les effets (OD, modulation, delay, reverb) passent par le préampli
   du Mesa. Aucune séparation pre/post ampli possible sans reconfiguration du câblage.
