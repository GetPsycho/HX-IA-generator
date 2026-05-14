# HX Effects — Référence des modèles (v3.80)

Équivalences entre les noms HX et les pédales réelles.

**Sources :**
- ✅ Manuel officiel HX Effects 3.80 (pages 19-20 dist, pages suivantes modulation/delay/reverb)
- 📚 Documentation Line 6 officielle / sources reconnues
- ⚠️ Non confirmé — à vérifier dans le manuel

---

## Distorsion / OD / Fuzz — Modèles HD2 (standard)

| Nom HX | Model ID | Pédale réelle | Source |
|---|---|---|---|
| **Alpaca Rouge** | `HD2_DistAlpacaRouge` | ? | ⚠️ |
| **Ampeg Scrambler** | `HD2_DistAmpegScramblerOD` | Ampeg Scrambler OD | 📚 |
| **Arbitrator Fuzz** | `HD2_DistArbitratorFuzz` | Arbiter Fuzz Face (germanium) | 📚 |
| **Ballistic Fuzz** | `HD2_DistBallisticFuzz` | ? | ⚠️ |
| **Bighorn Fuzz** | `HD2_DistRamsHead` | EHX Big Muff Pi Ram's Head '73 | ✅ |
| **Bitcrusher** | `HD2_DistBitcrusher` | Effet numérique (original Line 6) | 📚 |
| **Clawthorn Drive** | `HD2_DistClawthornDrive` | ? | ⚠️ |
| **Compulsive Drive** | `HD2_DistCompulsiveDrive` | Fulltone OCD v1.4 | ✅ |
| **Dark Dove Fuzz** | `HD2_DistDarkDoveFuzz` | ? | ⚠️ |
| **Deez One Mod** | `HD2_DistDeezOneMod` | Boss DS-1 (version modifiée) | 📚 |
| **Deez One Vintage** | `HD2_DistDeezOneVintage` | Boss DS-1 (version vintage) | 📚 |
| **Deranged Master** | `HD2_DistDerangedMaster` | Dallas Rangemaster Treble Booster | 📚 |
| **Dhyana Drive** | `HD2_DistDhyanaDrive` | Hermida Audio Zendrive | ✅ |
| **Hedgehog D9** | `HD2_DistHedgehogD9` | ? (probablement Boss DS-1 ou MXR M104) | ⚠️ |
| **Heir Apparent** | `HD2_DistHeirApparent` | Analogman Prince of Tone | ✅ |
| **Horizon Drive** | `HD2_DistHorizonDrive` | ? | ⚠️ |
| **Industrial Fuzz** | `HD2_DistIndustrialFuzz` | Z.Vex Fuzz Factory | ✅ |
| **Kinky Boost** | `HD2_DistKinkyBoost` | ? (boost pur, original Line 6) | ⚠️ |
| **KWB** | `HD2_DistKWB` | Benadrian Kowloon Walled Bunny | ✅ |
| **Legendary Drive** | `HD2_DistLegendaryDrive` | ? | ⚠️ |
| **Megaphone** | `HD2_DistMegaphone` | Effet mégaphone (original Line 6) | 📚 |
| **Minotaur** | `HD2_DistMinotaur` | Klon Centaur | ✅ |
| **Obsidian 7000** | `HD2_DistObsidian7000` | ? | ⚠️ |
| **Pillars** | `HD2_DistPillars` | ? | ⚠️ |
| **Pocket Fuzz** | `HD2_DistPocketFuzz` | Jordan Boss Tone | ✅ |
| **Prize Drive** | `HD2_DistPrizeDrive` | ? | ⚠️ |
| **Ratatouille Dist** | `HD2_DistRatatouilleDist` | Pro Co RAT (opamp LM308 NPN, vintage) | ✅ |
| **Regal Bass DI** | `HD2_DistRegalBassDI` | ? (DI basse) | ⚠️ |
| **Scream 808** | `HD2_DistScream808` | Ibanez TS808 Tube Screamer | ✅ |
| **Stupor OD** | `HD2_DistStuporOD` | ? | ⚠️ |
| **Swedish Chainsaw** | `HD2_DistSwedishChainsaw` | Boss HM-2 Heavy Metal | ✅ |
| **Teemah!** | `HD2_DistTeemah` | Paul Cochrane Timmy OD | 📚 |
| **Thrifter Fuzz** | `HD2_DistThrifterFuzz` | ? | ⚠️ |
| **Tone Sovereign** | `HD2_DistToneSovereign` | Analogman King of Tone | ✅ |
| **Top Secret OD** | `HD2_DistTopSecretOD` | DOD Overdrive Preamp 250 (?) | ⚠️ |
| **Triangle Fuzz** | `HD2_DistTriangleFuzz` | EHX Big Muff Pi Triangle v1 (1969) | 📚 |
| **Tycoctavia Fuzz** | `HD2_DistTycoctaviaFuzz` | Tycobrahe Octavia | 📚 |
| **Valve Driver** | `HD2_DistValveDriver` | Chandler Tube Driver | ✅ |
| **Vermin Dist** | `HD2_DistVerminDist` | Pro Co RAT (opamp standard) | ✅ |
| **Vital Boost** | `HD2_DistVitalBoost` | ? | ⚠️ |
| **Vital Dist** | `HD2_DistVitalDist` | ? | ⚠️ |
| **Wringer Fuzz** | `HD2_DistWringerFuzz` | ? | ⚠️ |
| **Xenomorph Fuzz** | `HD2_DistXenomorphFuzz` | ? | ⚠️ |
| **ZeroAmp Bass DI** | `HD2_DistZeroAmpBassDI` | ? (DI basse) | ⚠️ |

### Notes distorsion HD2

- **Ratatouille vs Vermin** : deux versions du RAT. Ratatouille = LM308 NPN (vintage, plus chaud,
  plus de sustain) ; Vermin = opamp standard. Pour Jonny Greenwood (Creep), le RAT était
  une version LM308 → Ratatouille Dist est le choix le plus fidèle.
- **Bighorn vs Triangle Fuzz** : deux Big Muff Pi différents. Bighorn = Ram's Head '73
  (légèrement plus de mids, meilleure lisibilité en groupe) ; Triangle = v1 1969
  (plus dark, moins de mids). Pour grunge/stoner → Bighorn.
- **Heir Apparent + Tone Sovereign** : deux facettes de la même pédale (Prince of Tone =
  côté gauche du King of Tone). Tone Sovereign = full King of Tone (deux canaux).
- **Valve Driver + Tube Drive (legacy)** : même circuit Chandler Tube Driver, deux modélisations.

---

## Distorsion / OD / Fuzz — Modèles DM4 Legacy

Les modèles DM4 sont hérités de la pédale Line 6 DM4 (2001).
Model IDs préfixés `HD2_DM4`.

| Nom HX | Model ID | Pédale réelle | Source |
|---|---|---|---|
| **Bronze Master** | `Line6BronzeMaster` | ? | ⚠️ |
| **Buzz Saw** | `HD2_DM4BuzzSaw` | ? | ⚠️ |
| **Classic Dist** | `HD2_DM4ClassicDistortion` | ? (MXR Distortion+ ?) | ⚠️ |
| **Colordrive** | `HD2_DM4ColorDrive` | Colorsound Overdrive | 📚 |
| **Facial Fuzz** | `HD2_DM4FacialFuzz` | Arbiter Fuzz Face (silicon) | 📚 |
| **Fuzz Pi** | `HD2_DM4FuzzPi` | EHX Big Muff Pi (standard) | 📚 |
| **Heavy Dist** | `HD2_DM4HeavyDistortion` | ? | ⚠️ |
| **Jet Fuzz** | `HD2_DM4JetFuzz` | ? | ⚠️ |
| **Jumbo Fuzz** | `HD2_DM4JumboFuzz` | ? | ⚠️ |
| **Killer Z** | `KillerZ` | ? | ⚠️ |
| **L6 Distortion** | `HD2_DM4Line6Distortion` | Original Line 6 | 📚 |
| **L6 Drive** | `HD2_DM4Line6Drive` | Original Line 6 | 📚 |
| **Octave Fuzz** | `HD2_DM4OctaveFuzz` | Tycobrahe Octavia | 📚 |
| **Overdrive** | `HD2_DM4Overdrive` | ? (TS9 ?) | ⚠️ |
| **Screamer** | `HD2_DM4Screamer` | Ibanez TS9 Tube Screamer | 📚 |
| **Sub Oct Fuzz** | `HD2_DM4SubOctFuzz` | ? | ⚠️ |
| **Tube Drive** | `HD2_DM4TubeDrive` | Chandler Tube Driver | ✅ |

---

## Modulation — Modèles clés

| Nom HX | Model ID | Équivalent réel | Source |
|---|---|---|---|
| **70s Chorus** | `HD2_Chorus70sChorus` | Boss CE-1/CE-2 Chorus Ensemble | 📚 |
| **80A Flanger** | `HD2_M1380AFlanger` | MXR M-117R Flanger (ancienne version) | 📚 |
| **AC Flanger** | `HD2_M13ACFlanger` | MXR Micro Flanger ou Script Flanger | ⚠️ |
| **Analog Chorus** | `HD2_MM4AnalogChorus` | Boss CE-2 | 📚 |
| **Analog Flanger** | `HD2_MM4AnalogFlanger` | MXR M117R Flanger | 📚 |
| **Bias Tremolo** | `HD2_MM4BiasTremolo` | Tremolo bias tube (style Vox, Fender) | 📚 |
| **Dimension** | `HD2_MM4Dimension` | Roland Dimension D / Boss DC-2 | 📚 |
| **Gray Flanger** | `HD2_FlangerGrayFlanger` | MXR M117R Flanger | 📚 |
| **Jet Flanger** | `HD2_MM4JetFlanger` | Boss BF-2 Flanger | 📚 |
| **Optical Trem** | `HD2_TremoloOpticalTrem` | Tremolo optique (style Fender) | 📚 |
| **Opto Tremolo** | `HD2_MM4OptoTremolo` | Tremolo opto (style Magnatone) | 📚 |
| **Ring Modulator** | `HD2_MM4RingModulator` | Ring modulator (original) | 📚 |
| **Script Mod Phase** | `HD2_PhaserScriptModPhase` | MXR Phase 90 (modded, pas de R47) | 📚 |
| **Script Phase** | `HD2_MM4ScriptPhase` | MXR Phase 90 (version script, vintage) | 📚 |
| **Tri Chorus** | `HD2_MM4TriChorus` | ? (tri-chorus original) | ⚠️ |
| **U-Vibe** | `HD2_MM4UVibe` | Univox Uni-Vibe | 📚 |

---

## Wah

| Nom HX | Model ID | Équivalent réel | Source |
|---|---|---|---|
| **Chrome** | `HD2_WahChrome` | Dunlop GCB95 Cry Baby | 📚 |
| **Chrome Custom** | `HD2_WahChromeCustom` | Dunlop Custom Cry Baby | 📚 |
| **Colorful** | `HD2_WahColorful` | ? | ⚠️ |
| **Conductor** | `HD2_WahConductor` | ? | ⚠️ |
| **Fassel** | `HD2_WahFassel` | Colorsound Wah / Arbiter Wah vintage | ⚠️ |
| **Teardrop 310** | `HD2_WahTeardrop310` | Jen Cry Baby (forme teardrop) | ⚠️ |
| **Teardrop Bass Q** | `HD2_WahTeardropBassQ` | Wah basse (teardrop) | ⚠️ |
| **Throaty** | `HD2_WahThroaty` | ? | ⚠️ |
| **UK Wah 846** | `HD2_WahUKWah846` | Vox V846 Wah | 📚 |
| **Vetta Wah** | `HD2_WahVettaWah` | Original Line 6 Vetta | 📚 |
| **Weeper** | `HD2_WahWeeper` | ? (wah vintage britannique) | ⚠️ |

---

## Delay — Modèles clés

| Nom HX | Model ID | Équivalent réel | Source |
|---|---|---|---|
| **Bucket Brigade** | `HD2_DelayBucketBrigade` | BBD delay (Electro-Harmonix, Boss DM-2 style) | 📚 |
| **Cosmos Echo** | `HD2_DelayCosmosEcho` | Roland RE-201 Space Echo | 📚 |
| **Elephant Man** | `HD2_DelayElephantMan` | Electro-Harmonix Deluxe Memory Man | 📚 |
| **Tape Echo** | `HD2_DL4TapeEchoStereo` | Maestro Echoplex EP-3 | 📚 |
| **Transistor Tape** | `HD2_DelayTransistorTape` | ? (tape + transistor hybrid) | ⚠️ |
| **Tube Echo** | `HD2_DL4TubeEchoStereo` | Maestro Echoplex EP-1 (tube) | 📚 |
| **Vintage Digital** | `HD2_DelayVintageDigital` | Lexicon Prime Time ou TC 2290 | 📚 |

---

## Reverb

| Nom HX | Model ID | Caractère | Source |
|---|---|---|---|
| **Double Tank** | `HD2_ReverbDoubleTank` | Spring reverb (deux tanks) | 📚 |
| **Ganymede** | `HD2_ReverbGanymede` | Algorithmic hall/room, très naturel | 📚 |
| **Glitz** | `HD2_ReverbGlitz` | Plate / shimmer hybride | 📚 |
| **Hot Springs** | `HD2_ReverbHxSpring` | Spring reverb | 📚 |
| **Nonlinear** | `HD2_ReverbNonLinear` | Reverb non-linéaire (gate reverb style) | 📚 |
| **Plateaux** | `HD2_ReverbPlateaux` | Plate reverb | 📚 |
| **Searchlights** | `HD2_ReverbSearchlights` | ? (reverb atmosphérique) | ⚠️ |

---

## Compresseurs — Modèles clés

| Nom HX | Model ID | Équivalent réel | Source |
|---|---|---|---|
| **Ampeg Opto Comp** | `HD2_CompressorOptoComp` | Ampeg Opto Comp | 📚 |
| **Blue Comp** | `HD2_DM4BlueComp` | Boss CS-3 Compression Sustainer | 📚 |
| **Blue Comp Treb** | `HD2_DM4BlueCompTreb` | Boss CS-3 (treble variant) | 📚 |
| **Deluxe Comp** | `HD2_CompressorDeluxeComp` | ? | ⚠️ |
| **Kinky Comp** | `HD2_CompressorKinkyComp` | ? | ⚠️ |
| **LA Studio Comp** | `HD2_CompressorLAStudioComp` | Urei LA-2A (optique) | 📚 |
| **Red Comp** | `HD2_DM4RedComp` | MXR Dyna Comp | 📚 |
| **Rochester Comp** | `HD2_CompressorRochesterComp` | ? | ⚠️ |

---

## À compléter avec le manuel

Les entrées marquées ⚠️ sont à vérifier dans le manuel officiel HX Effects 3.80,
pages 19+ (section "Models Reference"). Le manuel liste les équivalences officielles
pour chaque modèle.

**PDF à stocker :** `docs/HX_Effects_380_Owners_Manual.pdf` (à fournir).
