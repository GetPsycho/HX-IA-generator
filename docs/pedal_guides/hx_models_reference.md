# HX Effects — Référence des modèles (v3.80)

Source officielle : HX Effects 3.80 Owner's Manual (40-00-0399 Rev D).
PDF : `docs/HX Effects 3.80 Owner's Manual - English .pdf`

Toutes les entrées de ce fichier sont ✅ confirmées par le manuel officiel.

---

## Distorsion / OD / Fuzz — Modèles HD2 (standard)

| Nom HX | Model ID | Pédale réelle (source officielle) |
|---|---|---|
| **Kinky Boost** | `HD2_DistKinkyBoost` | Xotic EP Booster |
| **Deranged Master** | `HD2_DistDerangedMaster` | Dallas Rangemaster Treble Booster |
| **Minotaur** | `HD2_DistMinotaur` | Klon Centaur |
| **Teemah!** | `HD2_DistTeemah` | Paul Cochrane Timmy Overdrive |
| **Heir Apparent** | `HD2_DistHeirApparent` | Analogman Prince of Tone (= Keeley 1962X possédée par Eric, même lignée Bluesbreaker) |
| **Tone Sovereign** | `HD2_DistToneSovereign` | Analogman King of Tone |
| **Alpaca Rouge** | `HD2_DistAlpacaRouge` | Way Huge Red Llama (modded) |
| **Compulsive Drive** | `HD2_DistCompulsiveDrive` | Fulltone OCD |
| **Dhyana Drive** | `HD2_DistDhyanaDrive` | Hermida Audio Zendrive |
| **Horizon Drive** | `HD2_DistHorizonDrive` | Horizon Precision Drive |
| **Valve Driver** | `HD2_DistValveDriver` | Chandler Tube Driver |
| **Top Secret OD** | `HD2_DistTopSecretOD` | DOD OD-250 |
| **Prize Drive** | `HD2_DistPrizeDrive` | Nobels ODR-1(bc) |
| **Scream 808** | `HD2_DistScream808` | Ibanez TS808 Tube Screamer |
| **Pillars** | `HD2_DistPillars` | Earthquaker Devices Plumes |
| **Hedgehog D9** | `HD2_DistHedgehogD9` | MAXON SD9 Sonic Distortion |
| **Stupor OD** | `HD2_DistStuporOD` | BOSS SD-1 Overdrive |
| **Deez One Vintage** | `HD2_DistDeezOneVintage` | BOSS DS-1 Distortion (Made-in-Japan) |
| **Deez One Mod** | `HD2_DistDeezOneMod` | BOSS DS-1 Distortion (Keeley modded) |
| **Ratatouille Dist** | `HD2_DistRatatouilleDist` | Pro Co RAT (opamp LM308 NPN, vintage) |
| **Vermin Dist** | `HD2_DistVerminDist` | Pro Co RAT (opamp standard) |
| **Vital Dist** | `HD2_DistVitalDist` | Earthquaker Devices Life — circuit distorsion/octave |
| **Vital Boost** | `HD2_DistVitalBoost` | Earthquaker Devices Life — circuit boost |
| **KWB** | `HD2_DistKWB` | Benadrian Kowloon Walled Bunny Distortion — caractere reel : OD legere type TS poussé, pas un haut-gain (voir od_dist_fuzz.md) |
| **Legendary Drive** | `HD2_DistLegendaryDrive` | Carvin VLD1 Legacy Drive (canal high gain) |
| **Swedish Chainsaw** | `HD2_DistSwedishChainsaw` | BOSS HM-2 Heavy Metal Distortion (MIJ) |
| **Arbitrator Fuzz** | `HD2_DistArbitratorFuzz` | Arbiter Fuzz Face |
| **Pocket Fuzz** | `HD2_DistPocketFuzz` | Jordan Boss Tone Fuzz |
| **Bighorn Fuzz** | `HD2_DistRamsHead` | '73 Electro-Harmonix Ram's Head Big Muff Pi |
| **Triangle Fuzz** | `HD2_DistTriangleFuzz` | Electro-Harmonix Big Muff Pi (Triangle) |
| **Dark Dove Fuzz** | `HD2_DistDarkDoveFuzz` | Electro-Harmonix Russian Big Muff Pi |
| **Ballistic Fuzz** | `HD2_DistBallisticFuzz` | Euthymia ICBM Fuzz |
| **Industrial Fuzz** | `HD2_DistIndustrialFuzz` | Z.Vex Fuzz Factory |
| **Tycoctavia Fuzz** | `HD2_DistTycoctaviaFuzz` | Tycobrahe Octavia |
| **Wringer Fuzz** | `HD2_DistWringerFuzz` | BOSS FZ-2 (modifié par Garbage) |
| **Thrifter Fuzz** | `HD2_DistThrifterFuzz` | Original Line 6 |
| **Xenomorph Fuzz** | `HD2_DistXenomorphFuzz` | Subdecay Harmonic Antagonizer |
| **Megaphone** | `HD2_DistMegaphone` | Mégaphone (effet de type téléphone) |
| **Bitcrusher** | `HD2_DistBitcrusher` | Original Line 6 |
| **Ampeg Scrambler** | `HD2_DistAmpegScramblerOD` | Ampeg Scrambler Bass Overdrive |
| **ZeroAmp Bass DI** | `HD2_DistZeroAmpBassDI` | Tech 21 SansAmp Bass Driver DI V1 |
| **Regal Bass DI** | `HD2_DistRegalBassDI` | Noble Preamp Bass DI |
| **Obsidian 7000** | `HD2_DistObsidian7000` | Darkglass Electronics Microtubes B7K Ultra |
| **Clawthorn Drive** | `HD2_DistClawthornDrive` | Wounded Paw Battering Ram |

### Notes distorsion HD2 — comportements spécifiques

- **Arbitrator Fuzz (`HD2_DistArbitratorFuzz`) — déficit d'output structurel** :
  Même au Level=1.0 (max, affiché "10" dans HX Edit), le signal reste en dessous
  du niveau clean. Fix : Level=0.90 + KinkyBoost always-on (Drive=0, Boost=True)
  sur les snaps distorsion, exclu du snap Clean (référence niveau). Validé sur AYGGMW.

- **Ratatouille vs Vermin** : deux versions du RAT. Ratatouille = LM308 NPN (vintage, plus
  chaud, plus de sustain) ; Vermin = opamp standard. Pour Jonny Greenwood sur Creep,
  le RAT d'époque utilisait le LM308 → **Ratatouille Dist** est le choix le plus fidèle.
- **Bighorn vs Triangle Fuzz vs Dark Dove** : trois Big Muff Pi différents.
  Bighorn = Ram's Head '73 (plus de mids, lisibilité groupe) ;
  Triangle = v1 1969 (plus dark) ; Dark Dove = Russian Muff (plus agressif).
- **Heir Apparent + Tone Sovereign** : Prince of Tone (un côté) et King of Tone (complet,
  deux canaux). Tone Sovereign inclut les deux modes du King of Tone.
- **Valve Driver + Tube Drive (legacy)** : même circuit Chandler Tube Driver, deux
  modélisations distinctes. Valve Driver = HD2, Tube Drive = DM4 Legacy.
- **Wringer Fuzz** : version modifiée par Butch Vig (producteur/batteur de Garbage) du
  Boss FZ-2 Hyper Fuzz — utilisé sur plusieurs albums de Garbage.
- **Kinky Boost** : Xotic EP Booster = boost époxy transparent, idéal pour push d'ampli
  ou solo. Utilisé dans nos presets avec Drive=0, Boost=True.

---

## Distorsion / OD / Fuzz — Modèles DM4 Legacy

Hérités de la pédale Line 6 DM4 (2001). Sous-catégorie "Legacy" dans l'appareil.

| Nom HX | Model ID | Pédale réelle (source officielle) |
|---|---|---|
| **Tube Drive** | `HD2_DM4TubeDrive` | Chandler Tube Driver |
| **Screamer** | `HD2_DM4Screamer` | Ibanez Tube Screamer |
| **Overdrive** | `HD2_DM4Overdrive` | DOD Overdrive/Preamp 250 |
| **Classic Dist** | `HD2_DM4ClassicDistortion` | Pro Co RAT |
| **Heavy Dist** | `HD2_DM4HeavyDistortion` | BOSS Metal Zone |
| **Colordrive** | `HD2_DM4ColorDrive` | Colorsound Overdriver |
| **Buzz Saw** | `HD2_DM4BuzzSaw` | Maestro Fuzz Tone |
| **Facial Fuzz** | `HD2_DM4FacialFuzz` | Arbiter Fuzz Face |
| **Jumbo Fuzz** | `HD2_DM4JumboFuzz` | Vox Tone Bender |
| **Fuzz Pi** | `HD2_DM4FuzzPi` | Electro-Harmonix Big Muff Pi |
| **Jet Fuzz** | `HD2_DM4JetFuzz` | Roland Jet Phaser |
| **L6 Drive** | `HD2_DM4Line6Drive` | Colorsound Overdriver (modded) |
| **L6 Distortion** | `HD2_DM4Line6Distortion` | Original Line 6 |
| **Sub Oct Fuzz** | `HD2_DM4SubOctFuzz` | PAiA Roctave Divider |
| **Octave Fuzz** | `HD2_DM4OctaveFuzz` | Tycobrahe Octavia |
| **Bronze Master** | `Line6BronzeMaster` | Maestro Bass Brassmaster |
| **Killer Z** | `KillerZ` | BOSS Metal Zone MT-2 |

---

## Dynamiques / Compresseurs

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **Deluxe Comp** | `HD2_CompressorDeluxeComp` | Original Line 6 |
| **Red Squeeze** | `HD2_CompressorRedSqueeze` | MXR Dyna Comp |
| **Kinky Comp** | `HD2_CompressorKinkyComp` | Xotic SP Compressor |
| **Ampeg Opto Comp** | `HD2_CompressorOptoComp` | Ampeg Opto Comp |
| **Rochester Comp** | `HD2_CompressorRochesterComp` | Ashly CLX-52 (avec Billy Sheehan) |
| **LA Studio Comp** | `HD2_CompressorLAStudioComp` | Teletronix LA-2A |
| **3-Band Comp** | `HD2_Compressor3BandComp` | Original Line 6 |
| **Noise Gate** | `HD2_GateNoiseGate` | Original Line 6 |
| **Hard Gate** | `HD2_GateHardGate` | Original Line 6 |
| **Horizon Gate** | `HD2_GateHorizonGate` | Horizon Precision Drive — circuit gate |
| **Tube Comp** *(Legacy)* | `HD2_DM4TubeComp` | Teletronix LA-2A |
| **Red Comp** *(Legacy)* | `HD2_DM4RedComp` | MXR Dyna Comp |
| **Blue Comp** *(Legacy)* | `HD2_DM4BlueComp` | BOSS CS-1 |
| **Blue Comp Treb** *(Legacy)* | `HD2_DM4BlueCompTreb` | BOSS CS-1 (Treble switch actif) |
| **Boost Comp** *(Legacy)* | `HD2_DM4BoostComp` | MXR Micro Amp |

---

## Modulation — Modèles principaux

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **Optical Trem** | `HD2_TremoloOpticalTrem` | Circuit tremolo optique Fender |
| **60s Bias Trem** | `HD2_Tremolo60sBiasTrem` | Vox AC-15 Tremolo |
| **Bleat Chop Trem** | `HD2_TremoloPattern` | Lightfoot Labs Goatkeeper |
| **Script Mod Phase** | `HD2_PhaserScriptModPhase` | MXR Phase 90 |
| **Pebble Phaser** | `HD2_PhaserPebblePhaser` | Electro-Harmonix Small Stone |
| **Ubiquitous Vibe** | `HD2_PhaserUbiquitousVibe` | Shin-ei Uni-Vibe |
| **Gray Flanger** | `HD2_FlangerGrayFlanger` | MXR 117 Flanger |
| **Harmonic Flanger** | `HD2_FlangerHarmonicFlanger` | A/DA Flanger |
| **Courtesan Flange** | `HD2_FlangerCourtesanFlange` | Electro-Harmonix Deluxe Electric Mistress |
| **70s Chorus** | `HD2_Chorus70sChorus` | BOSS CE-1 |
| **PlastiChorus** | `HD2_ChorusPlastiChorus` | Arion SCH-Z (modded) |
| **Trinity Chorus** | `HD2_ChorusAmpegLiquifier` | Dytronics Tri-Stereo Chorus |
| **Bubble Vibrato** | `HD2_VibratoBubbleVibrato` | BOSS VB-2 Vibrato |
| **U-Vibe** *(Legacy)* | `HD2_MM4UVibe` | Shin-ei Uni-Vibe |
| **Script Phase** *(Legacy)* | `HD2_MM4ScriptPhase` | MXR Phase 90 (version script) |
| **Opto Tremolo** *(Legacy)* | `HD2_MM4OptoTremolo` | Fender Deluxe Reverb 1964 (tremolo) |
| **Bias Tremolo** *(Legacy)* | `HD2_MM4BiasTremolo` | Vox AC-15 Tremolo 1960 |
| **Analog Chorus** *(Legacy)* | `HD2_MM4AnalogChorus` | BOSS CE-1 |
| **Dimension** *(Legacy)* | `HD2_MM4Dimension` | Roland Dimension D |
| **Tri Chorus** *(Legacy)* | `HD2_MM4TriChorus` | Dytronics Tri-Stereo Chorus |
| **Analog Flanger** *(Legacy)* | `HD2_MM4AnalogFlanger` | MXR Flanger |
| **Jet Flanger** *(Legacy)* | `HD2_MM4JetFlanger` | A/DA Flanger |
| **AC Flanger** *(Legacy)* | `HD2_M13ACFlanger` | MXR Flanger |
| **80A Flanger** *(Legacy)* | `HD2_M1380AFlanger` | A/DA Flanger |
| **Dual Phaser** *(Legacy)* | `HD2_PhaserDeluxePhaser` | Mu-Tron Bi-Phase |
| **Panned Phaser** *(Legacy)* | `HD2_MM4PannedPhaser` | Ibanez Flying Pan |

---

## Delay — Modèles principaux

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **Transistor Tape** | `HD2_DelayTransistorTape` | Maestro Echoplex EP-3 |
| **Cosmos Echo** | `HD2_DelayCosmosEcho` | Roland RE-201 Space Echo |
| **Bucket Brigade** | `HD2_DelayBucketBrigade` | BOSS DM-2 |
| **Adriatic Delay** | `HD2_DelayAdriaticDelay` | BOSS DM-2 (Adrian Mod) |
| **Elephant Man** | `HD2_DelayElephantMan` | Electro-Harmonix Deluxe Memory Man |
| **Ducked Delay** | `HD2_DelayDuckedDelay` | TC Electronic 2290 |
| **Vintage Digital** | `HD2_DelayVintageDigital` | Original Line 6 |
| **Tube Echo** *(Legacy)* | `HD2_DL4TubeEchoStereo` | Maestro Echoplex EP-1 (tube) |
| **Tape Echo** *(Legacy)* | `HD2_DL4TapeEchoStereo` | Maestro Echoplex EP-3 |
| **Ping Pong** *(Legacy)* | `HD2_DL4PingPong` | TC Electronic 2290 |
| **Dynamic** *(Legacy)* | `HD2_DL4DynamicDelayStereo` | TC Electronic 2290 |
| **Echo Platter** *(Legacy)* | `HD2_DL4EchoPlatterStereo` | Binson EchoRec |
| **Analog Echo** *(Legacy)* | `HD2_DL4AnalogDelayStereo` | BOSS DM-2 |
| **Analog w/Mod** *(Legacy)* | `HD2_DL4AnalogDelayStereoMod` | Electro-Harmonix Deluxe Memory Man |
| **Multi-Head** *(Legacy)* | `HD2_DL4MultiheadStereo` | Roland RE-101 Space Echo |

---

## Reverb

Tous les modèles de reverb HD2 (Ganymede, Glitz, Plateaux, Searchlights, Hot Springs,
Nonlinear, Double Tank, Dynamic Hall/Room/Plate/Ambience/Bloom, Shimmer) sont des
**originaux Line 6** — aucun équivalent pédale réelle. Idem pour les Legacy reverbs.

---

## Wah

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **UK Wah 846** | `HD2_WahUKWah846` | Vox V846 |
| **Teardrop 310** | `HD2_WahTeardrop310` | Dunlop Cry Baby Fasel model 310 |
| **Fassel** | `HD2_WahFassel` | Dunlop Cry Baby Super |
| **Weeper** | `HD2_WahWeeper` | Arbiter Cry Baby |
| **Chrome** | `HD2_WahChrome` | Vox V847 |
| **Chrome Custom** | `HD2_WahChromeCustom` | Vox V847 (modded) |
| **Throaty** | `HD2_WahThroaty` | RMC Real McCoy 1 |
| **Vetta Wah** | `HD2_WahVettaWah` | Original Line 6 |
| **Colorful** | `HD2_WahColorful` | Colorsound Wah-fuzz |
| **Conductor** | `HD2_WahConductor` | Maestro Boomerang |
| **Teardrop Bass Q** | `HD2_WahTeardropBassQ` | Dunlop 105Q (modifié) |

---

## Filtre / Envelope

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **Mutant Filter** | `HD2_FilterMutantFilter` | Musitronics Mu-Tron III |
| **Mystery Filter** | `HD2_FilterMysterFilter` | Korg A3 |
| **Auto Filter** | `HD2_FilterAutoFilter` | Original Line 6 |
| **Asheville Pattrn** | `HD2_FilterAshevillePattrn` | Moog Moogerfooger MF-105M MuRF |
| **V Tron** *(Legacy)* | `HD2_FM4VTron` | Musitronics Mu-Tron III |
| **Tron Up** *(Legacy)* | `HD2_FM4TronUp` | Musitronics Mu-Tron III (up) |
| **Tron Down** *(Legacy)* | `HD2_FM4TronDown` | Musitronics Mu-Tron III (down) |
| **Seeker** *(Legacy)* | `HD2_FM4Seeker` | Z Vex Seek Wah |
| **Obi Wah** *(Legacy)* | `HD2_FM4ObiWah` | Oberheim voltage-controlled S&H filter |
| **Throbber** *(Legacy)* | `HD2_FM4Throbber` | Electrix Filter Factory |
| **Spin Cycle** *(Legacy)* | `HD2_FM4SpinCycle` | Craig Anderton's Wah/Anti-Wah |

---

## EQ

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **10 Band Graphic** | `HD2_EQGraphic10Band` | MXR 10-Band Graphic EQ |
| **Cali Q Graphic** | `HD2_CaliQ` | MESA/Boogie Mark IV Graphic EQ |
| Tous les autres EQ HD2 | — | Original Line 6 |

---

## Pitch / Synth

| Nom HX | Model ID | Équivalent réel |
|---|---|---|
| **Pitch Wham** | `HD2_PitchPitchWham` | Digitech Whammy |
| **Twin Harmony** | `HD2_PitchTwinHarmony` | Eventide H3000 |
| **Simple Pitch** | `HD2_PitchSimplePitch` | Original Line 6 |
| **Dual Pitch** | `HD2_PitchDualPitch` | Original Line 6 |
| **Boctaver** | `VIC_PitchBoctaver` | Boss OC-2 Octaver |
| **Bass Octaver** *(Legacy)* | `HD2_DM4BassOctaver` | EBS OctaBass |
| **Smart Harmony** *(Legacy)* | `HD2_M13TwoVoiceHarmony` | Eventide H3000 |
| **Attack Synth** *(Legacy)* | `HD2_FM4AttackSynth` | Korg X911 Guitar Synth |
| **Synth String** *(Legacy)* | `HD2_FM4SynthString` | Roland GR700 Guitar Synth |

---

## Lookup inversé — Pédale réelle → HX Model ID

Pour partir d'une pédale réelle et trouver l'équivalent HX rapidement.

| Pédale réelle | Nom HX | Model ID |
|---|---|---|
| A/DA Flanger | Harmonic Flanger | `HD2_FlangerHarmonicFlanger` |
| Analogman King of Tone | Tone Sovereign | `HD2_DistToneSovereign` |
| Analogman Prince of Tone | Heir Apparent | `HD2_DistHeirApparent` |
| Ampeg Opto Comp | Ampeg Opto Comp | `HD2_CompressorOptoComp` |
| Arbiter Fuzz Face | Arbitrator Fuzz | `HD2_DistArbitratorFuzz` |
| Arbiter Fuzz Face (Legacy) | Facial Fuzz | `HD2_DM4FacialFuzz` |
| Ampeg Scrambler Bass OD | Ampeg Scrambler | `HD2_DistAmpegScramblerOD` |
| Benadrian KWB | KWB | `HD2_DistKWB` |
| Binson EchoRec | Echo Platter *(Legacy)* | `HD2_DL4EchoPlatterStereo` |
| BOSS CE-1 | 70s Chorus | `HD2_Chorus70sChorus` |
| BOSS CS-1 | Blue Comp *(Legacy)* | `HD2_DM4BlueComp` |
| BOSS DM-2 | Bucket Brigade | `HD2_DelayBucketBrigade` |
| BOSS DM-2 w/mod | Adriatic Delay | `HD2_DelayAdriaticDelay` |
| BOSS DM-2 (Legacy) | Analog Echo | `HD2_DL4AnalogDelayStereo` |
| BOSS DS-1 (MIJ) | Deez One Vintage | `HD2_DistDeezOneVintage` |
| BOSS DS-1 (Keeley) | Deez One Mod | `HD2_DistDeezOneMod` |
| BOSS FZ-2 (Garbage) | Wringer Fuzz | `HD2_DistWringerFuzz` |
| BOSS HM-2 | Swedish Chainsaw | `HD2_DistSwedishChainsaw` |
| BOSS Metal Zone (Legacy) | Heavy Dist | `HD2_DM4HeavyDistortion` |
| BOSS Metal Zone MT-2 (Legacy) | Killer Z | `KillerZ` |
| BOSS OC-2 | Boctaver | `VIC_PitchBoctaver` |
| BOSS SD-1 | Stupor OD | `HD2_DistStuporOD` |
| BOSS VB-2 | Bubble Vibrato | `HD2_VibratoBubbleVibrato` |
| Carvin VLD1 | Legendary Drive | `HD2_DistLegendaryDrive` |
| Chandler Tube Driver | Valve Driver | `HD2_DistValveDriver` |
| Chandler Tube Driver (Legacy) | Tube Drive | `HD2_DM4TubeDrive` |
| Colorsound Overdriver (Legacy) | Colordrive | `HD2_DM4ColorDrive` |
| Dallas Rangemaster | Deranged Master | `HD2_DistDerangedMaster` |
| Darkglass B7K Ultra | Obsidian 7000 | `HD2_DistObsidian7000` |
| Digitech Whammy | Pitch Wham | `HD2_PitchPitchWham` |
| DOD OD-250 | Top Secret OD | `HD2_DistTopSecretOD` |
| DOD OD-250 (Legacy) | Overdrive | `HD2_DM4Overdrive` |
| Dunlop Cry Baby Super | Fassel | `HD2_WahFassel` |
| Earthquaker Plumes | Pillars | `HD2_DistPillars` |
| EBS OctaBass (Legacy) | Bass Octaver | `HD2_DM4BassOctaver` |
| EHX Big Muff Pi (Legacy) | Fuzz Pi | `HD2_DM4FuzzPi` |
| EHX Big Muff Triangle | Triangle Fuzz | `HD2_DistTriangleFuzz` |
| EHX Deluxe Memory Man | Elephant Man | `HD2_DelayElephantMan` |
| EHX Deluxe Memory Man (Legacy) | Analog w/Mod | `HD2_DL4AnalogDelayStereoMod` |
| EHX Ram's Head Big Muff '73 | Bighorn Fuzz | `HD2_DistRamsHead` |
| EHX Russian Big Muff | Dark Dove Fuzz | `HD2_DistDarkDoveFuzz` |
| Electrix Filter Factory | Throbber *(Legacy)* | `HD2_FM4Throbber` |
| Eventide H3000 | Twin Harmony | `HD2_PitchTwinHarmony` |
| Fulltone OCD | Compulsive Drive | `HD2_DistCompulsiveDrive` |
| Hermida Zendrive | Dhyana Drive | `HD2_DistDhyanaDrive` |
| Horizon Precision Drive | Horizon Drive | `HD2_DistHorizonDrive` |
| Ibanez TS808 | Scream 808 | `HD2_DistScream808` |
| Ibanez Tube Screamer (Legacy) | Screamer | `HD2_DM4Screamer` |
| Jordan Boss Tone | Pocket Fuzz | `HD2_DistPocketFuzz` |
| Klon Centaur | Minotaur | `HD2_DistMinotaur` |
| Korg A3 | Mystery Filter | `HD2_FilterMysterFilter` |
| Korg X911 (Legacy) | Attack Synth | `HD2_FM4AttackSynth` |
| Leslie 122 | 122 Rotary | `HD2_MM4RotaryDrumHorn` |
| Leslie 145 | 145 Rotary | `HD2_MM4RotaryDrumHorn` |
| Maestro Bass Brassmaster (Legacy) | Bronze Master | `Line6BronzeMaster` |
| Maestro Echoplex EP-1 (Legacy) | Tube Echo | `HD2_DL4TubeEchoStereo` |
| Maestro Echoplex EP-3 | Transistor Tape | `HD2_DelayTransistorTape` |
| Maestro Fuzz Tone (Legacy) | Buzz Saw | `HD2_DM4BuzzSaw` |
| MAXON SD9 | Hedgehog D9 | `HD2_DistHedgehogD9` |
| Moog MuRF MF-105M | Asheville Pattrn | `HD2_FilterAshevillePattrn` |
| Musitronics Mu-Tron III | Mutant Filter | `HD2_FilterMutantFilter` |
| MXR 10-Band EQ | 10 Band Graphic | `HD2_EQGraphic10Band` |
| MXR 117 Flanger | Gray Flanger | `HD2_FlangerGrayFlanger` |
| MXR Dyna Comp | Red Squeeze | `HD2_CompressorRedSqueeze` |
| MXR Dyna Comp (Legacy) | Red Comp | `HD2_DM4RedComp` |
| MXR Micro Amp (Legacy) | Boost Comp | `HD2_DM4BoostComp` |
| MXR Phase 90 | Script Mod Phase | `HD2_PhaserScriptModPhase` |
| Nobels ODR-1 | Prize Drive | `HD2_DistPrizeDrive` |
| Noble Bass DI | Regal Bass DI | `HD2_DistRegalBassDI` |
| PAiA Roctave (Legacy) | Sub Oct Fuzz | `HD2_DM4SubOctFuzz` |
| Paul Cochrane Timmy | Teemah! | `HD2_DistTeemah` |
| Pro Co RAT | Vermin Dist | `HD2_DistVerminDist` |
| Pro Co RAT LM308 | Ratatouille Dist | `HD2_DistRatatouilleDist` |
| Pro Co RAT (Legacy) | Classic Dist | `HD2_DM4ClassicDistortion` |
| RMC Real McCoy 1 | Throaty | `HD2_WahThroaty` |
| Roland Dimension D (Legacy) | Dimension | `HD2_MM4Dimension` |
| Roland GR700 (Legacy) | Synth String | `HD2_FM4SynthString` |
| Roland Jet Phaser (Legacy) | Jet Fuzz | `HD2_DM4JetFuzz` |
| Roland RE-201 Space Echo | Cosmos Echo | `HD2_DelayCosmosEcho` |
| Roland RE-101 (Legacy) | Multi-Head | `HD2_DL4MultiheadStereo` |
| Shin-ei Uni-Vibe | Ubiquitous Vibe | `HD2_PhaserUbiquitousVibe` |
| Subdecay Harmonic Antagonizer | Xenomorph Fuzz | `HD2_DistXenomorphFuzz` |
| TC Electronic 2290 | Ducked Delay | `HD2_DelayDuckedDelay` |
| Tech 21 SansAmp Bass DI | ZeroAmp Bass DI | `HD2_DistZeroAmpBassDI` |
| Teletronix LA-2A | LA Studio Comp | `HD2_CompressorLAStudioComp` |
| Tycobrahe Octavia | Tycoctavia Fuzz | `HD2_DistTycoctaviaFuzz` |
| Vox Tone Bender (Legacy) | Jumbo Fuzz | `HD2_DM4JumboFuzz` |
| Vox V846 | UK Wah 846 | `HD2_WahUKWah846` |
| Vox V847 | Chrome | `HD2_WahChrome` |
| Way Huge Red Llama (mod) | Alpaca Rouge | `HD2_DistAlpacaRouge` |
| Wounded Paw Battering Ram | Clawthorn Drive | `HD2_DistClawthornDrive` |
| Xotic EP Booster | Kinky Boost | `HD2_DistKinkyBoost` |
| Xotic SP Compressor | Kinky Comp | `HD2_CompressorKinkyComp` |
| Z.Vex Fuzz Factory | Industrial Fuzz | `HD2_DistIndustrialFuzz` |
| Z.Vex Seek Wah (Legacy) | Seeker | `HD2_FM4Seeker` |
