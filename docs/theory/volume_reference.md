# Référence de volume — Convention du projet

## Référence absolue

**Le snap "Clean" de "Are You Gonna Go My Way - Lenny Kravitz" est la référence "0 dB" du projet.**

C'est le point d'ancrage absolu pour caler le master de l'ampli/HX en répétition :
1. Eric charge AYGGMW
2. Sélectionne le snap Clean
3. Joue quelques notes ou accords
4. Règle le master du HX et/ou de l'ampli pour atteindre le volume de répétition cible
5. Une fois ce volume calé, **ne plus toucher le master** — tout le reste de la setlist se cale par rapport à ce point

## Pourquoi AYGGMW ?

- C'est l'un des premiers presets validés en répétition réelle
- Le snap Clean (Gate + Reverb Mix=0.10 seule) représente le signal direct guitare passant par le Mesa Boogie clean = la "couleur naturelle" du rig d'Eric
- C'est un morceau central de la setlist (souvent joué)

## Convention propagée à tous les presets

**Tous les Clean snaps de tous les presets doivent être configurés identiquement** :

```python
pb.add_block("HD2_ReverbGanymede", slot=N,
             overrides={... "Mix": 0.16})  # le default sur les autres snaps

pb.add_snapshot(idx, "Clean", blocks_on=[0, N],
                params={N: {"Mix": 0.10}},  # forcé à 0.10 sur le snap Clean
                color="blue")
```

C'est-à-dire :
- Seulement le **Gate** et la **Reverb Ganymede** actifs
- Reverb Mix override à **0.10** sur le snap Clean
- Aucun bloc de saturation (Dist/OD/Fuzz/KinkyBoost)
- Aucun bloc de modulation/delay

**Conséquence** : tous les Clean snaps sortent le même volume réel → ils sont tous équivalents au Clean d'AYGGMW → tous équivalents à la référence 0 dB.

## Exceptions tolérées

- **PolyPitch always-on** sur certains presets (Toxicity drop C) : le PolyPitch passe le signal sans changer son niveau, donc le Clean reste à la référence ✓
- **Blocs always-on neutres** (compresseur très peu poussé, EQ flat, etc.) : à éviter de préférence sur le Clean snap, mais si présents et neutres en volume, OK

## Workflow de calibration

### En répétition

1. Charge AYGGMW sur le HX
2. Snap Clean → règle le master ampli/HX au volume cible
3. **Pour chaque autre preset/snap** : joue, écoute, juge ("trop fort", "trop bas", "ok")
4. **Si à corriger** : ajuste directement sur l'appareil (Level des blocs concernés)
5. Sauvegarde le preset modifié sur l'appareil

### En import des corrections

1. Exporte les .hlx modifiés via HX Edit dans `output/modified/`
2. Lance `python presets/update_from_hlx.py --all`
3. Lis le diff : il liste les changements de Level (et autres params) par snap
4. Demande à Claude d'appliquer les modifications validées sur le code Python source
5. Régénère + commit

## Calibration inter-snap au sein d'un preset

Pour un preset donné, la cohérence inter-snap suit ces principes :

| Snap | Volume cible vs Clean (= ref 0 dB) |
|---|---|
| Clean | 0 dB (référence) |
| Verse / Intro / quasi-clean | 0 à +1 dB (légèrement au-dessus, pour confort de jeu) |
| Chorus / Refrain | 0 à +2 dB (au niveau ou un peu plus fort que verse) |
| Solo / Lead | +2 à +4 dB (sustain + présence renforcés) |
| Outro | identique à chorus ou verse selon le morceau |

## Règles de calibration OCD (rappel)

Pour atteindre la référence Clean avec un OCD seul :
- **LPHP = True** (High Peak) — **obligatoire** sur tous les presets pour cohérence
- **Level = 0.70 minimum** + **KinkyBoost (Drive=0, Boost=True) always-on**

Sans KinkyBoost et Level < 0.70, le snap dist est systématiquement sous la référence Clean.

### LPHP=True : convention projet (obligatoire)

Le paramètre `LPHP` (Low Peak / High Peak switch) de la pédale OCD réelle a un
impact direct sur l'output :
- **LPHP=False (Low Peak)** : son plus comprimé, smooth — mais **output significativement plus bas**
- **LPHP=True (High Peak)** : son plus ouvert, dynamique, punchy — **output élevé**

Découvert en répétition : un preset avec LPHP=False sort ~3-5 dB plus bas qu'un
preset équivalent en LPHP=True, à mêmes paramètres Gain/Level/Tone. Cet écart
casse la cohérence inter-preset.

**Règle projet : tous les blocs `HD2_DistCompulsiveDrive` doivent avoir
`LPHP=True` dans les overrides, sans exception**. Cela inclut :
- Le block default (`pb.add_block("HD2_DistCompulsiveDrive", ..., overrides={..., "LPHP": True, ...})`)
- Tous les overrides snap qui spécifient LPHP doivent être à True (et ne PAS l'overrider à False)

Si on veut un caractère plus chaud/smooth (raison d'être historique de LPHP=False),
compenser via le **Tone** baissé plutôt que LPHP=False (qui sacrifie le volume).

**Vérification** : `python -c "from songs import PRESETS; ..."` peut auditer tous
les presets pour s'assurer qu'aucun OCD n'est en LPHP=False.

### Calibration OCD step-by-step

1. `add_block("HD2_DistCompulsiveDrive", ..., overrides={"LPHP": True, "Level": 0.70+, ...})`
2. Ajouter un KinkyBoost always-on (sauf si gain stacking déjà présent)
3. Ne PAS override LPHP=False dans les snap params
4. Tester contre le snap Clean d'AYGGMW = référence

Voir aussi la règle d'architecture de l'ampli (clean canal vs cranked single channel) dans le skill `new-preset.md`.

## Cas d'usage : ajustement d'un preset

Exemple : tu trouves que le Verse de "X morceau" est 2 dB en dessous de son Chorus.

Tu as 3 leviers :
1. **Monter le Level de la dist sur ce snap** (le plus direct, fait pour ça)
2. **Ajouter un KinkyBoost sur ce snap** (si pas déjà présent) — c'est +6 dB d'un coup, gros bump
3. **Modifier la chaîne** (ajouter un boost, gain stacking) — pour des cas où le delta est récurrent

Le diff workflow capte automatiquement quelle approche tu as choisie via HX Edit.
