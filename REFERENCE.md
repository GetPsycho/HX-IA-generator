# HX Effects -- Reference des modeles

Liste generee automatiquement depuis `models_catalog.json`

(preamp exclus -- non disponible sur HX Effects)

**Total : 290 modeles**

## Sommaire

- [Distortion](#distortion) -- 46 modernes, 15 legacy
- [Dynamics](#dynamics) -- 11 modernes, 7 legacy
- [Gate](#gate) -- 2 modernes, 0 legacy
- [EQ](#eq) -- 8 modernes, 0 legacy
- [Modulation](#modulation) -- 28 modernes, 22 legacy
- [Delay](#delay) -- 28 modernes, 15 legacy
- [Reverb](#reverb) -- 13 modernes, 0 legacy
- [Pitch/Synth](#pitchsynth) -- 23 modernes, 7 legacy
- [Filter](#filter) -- 4 modernes, 11 legacy
- [Wah](#wah) -- 11 modernes, 0 legacy
- [Volume/Pan](#volumepan) -- 2 modernes, 0 legacy
- [Send/Return](#sendreturn) -- 12 modernes, 0 legacy
- [Fixed](#fixed) -- 10 modernes, 0 legacy
- [I/O](#io) -- 15 modernes, 0 legacy

## Distortion

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Alpaca Rouge | `HD2_DistAlpacaRouge` | `Drive` | generic_knob | 0.0 | 1.0 | 0.34 |
|  |  | `HiCut` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Volume` | generic_knob | 0.0 | 1.0 | 0.7 |
| Ampeg Scrambler | `HD2_DistAmpegScramblerOD` | `Drive` | generic_knob | 0.0 | 1.0 | 0.76 |
|  |  | `Blend` | generic_knob | 0.0 | 1.0 | 0.63 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.42 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.66 |
| Arbitrator Fuzz | `HD2_DistArbitratorFuzz` | `Fuzz` | generic_knob | 0.0 | 1.0 | 0.9 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.55 |
| Ballistic Fuzz | `HD2_DistBallisticFuzz` | `Sustain` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| Bighorn Fuzz | `HD2_DistRamsHead` | `Sustain` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| Bitcrusher | `HD2_DistBitcrusher` | `Gain` | volume_eq | 0.0 | 48.0 | 0.0 |
|  |  | `BitDepth` | bit_depth | 1.0 | 24.0 | 8.0 |
|  |  | `SampleRate` | frequency | 100.0 | 48000.0 | 18000.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Level` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `OpenThreshold` | volume_eq | -96.0 | 0.0 | -70.0 |
|  |  | `CloseThreshold` | volume_eq | -96.0 | 0.0 | -70.0 |
|  |  | `HoldTime` | time_ms_dist_hold_time | 0.01 | 0.8 | 0.01 |
|  |  | `Decay` | time_ms_dist_decay | 0.01 | 4.0 | 0.01 |
| Bronze Master | `Line6BronzeMaster` | `Drive` | percent | 0.0 | 1.0 | 0.6 |
|  |  | `tonality` | integer_slider | 1 | 8 | 4 |
|  |  | `mixture` | percent | 0.0 | 1.0 | 0.65 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Clawthorn Drive | `HD2_DistClawthornDrive` | `ODGain` | generic_knob | 0.0 | 1.0 | 0.44 |
|  |  | `ODTone` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `ODLevel` | generic_knob | 0.0 | 1.0 | 0.35 |
|  |  | `ODLowBoost` | off_on | False | True | True |
|  |  | `Fuzz` | off_on | False | True | True |
|  |  | `FuzzOct` | off_on | False | True | False |
|  |  | `FuzzGain` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `FuzzTone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `FuzzLevel` | generic_knob | 0.0 | 1.0 | 0.2 |
| Compulsive Drive | `HD2_DistCompulsiveDrive` | `Gain` | generic_knob | 0.0 | 1.0 | 0.66 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `LPHP` | low_peak_high_peak | False | True | False |
|  |  | `Version` | dist_version | False | True | False |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.65 |
| Dark Dove Fuzz | `HD2_DistDarkDoveFuzz` | `Sustain` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| Deez One Mod | `HD2_DistDeezOneMod` | `Drive` | generic_knob | 0.0 | 1.0 | 0.63 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Clipping` | clipping_sym | False | True | True |
| Deez One Vintage | `HD2_DistDeezOneVintage` | `Drive` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.75 |
| Deranged Master | `HD2_DistDerangedMaster` | `Drive` | generic_knob | 0.0 | 1.0 | 0.77 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.522 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dyhana Drive | `HD2_DistDhyanaDrive` | `Gain` | generic_knob | 0.0 | 1.0 | 0.44 |
|  |  | `Voice` | generic_knob | 0.0 | 1.0 | 0.56 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.44 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.4 |
| Hedgehog D9 | `HD2_DistHedgehogD9` | `Gain` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.27 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.68 |
| Heir Apparent | `HD2_DistHeirApparent` | `Gain` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Presence` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Clipping` | clipping_dist | 0 | 2 | 0 |
|  |  | `GainMod` | gain_mod | 0 | 1 | 1 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Voltage` | voltage | False | True | False |
| Horizon Drive | `HD2_DistHorizonDrive` | `Drive` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Attack` | horizon_attack | 0 | 5 | 1 |
|  |  | `Bright` | generic_knob | 0.0 | 1.0 | 0.37 |
|  |  | `Gate` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Gate_Range` | horizon_gaterange | False | True | False |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| Industrial Fuzz | `HD2_DistIndustrialFuzz` | `Compress` | generic_knob | 0.0 | 1.0 | 0.57 |
|  |  | `Gate` | generic_knob | 0.0 | 1.0 | 0.52 |
|  |  | `Drive` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Stability` | generic_knob | 0.0 | 1.0 | 0.73 |
|  |  | `Oscillator` | off_on | False | True | False |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.77 |
| KWB | `HD2_DistKWB` | `Gain` | generic_knob | 0.0 | 1.0 | 0.67 |
|  |  | `PushDiode` | diode | 0 | 3 | 1 |
|  |  | `PullDiode` | diode | 0 | 3 | 3 |
|  |  | `Bass` | volume_eq | -12.0 | 12.0 | 0.0 |
|  |  | `Treble` | volume_eq | -12.0 | 12.0 | 0.0 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.692 |
|  |  | `Asym` | generic_knob | 0.0 | 1.0 | 0.0 |
| Killer Z | `KillerZ` | `Dist` | percent | 0.0 | 1.0 | 0.67 |
|  |  | `Contour` | percent | 0.0 | 1.0 | 0.74 |
|  |  | `Gain` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mid Amt` | percent | 0.0 | 1.0 | 0.55 |
|  |  | `Mid Freq` | percent | 0.0 | 1.0 | 0.88 |
| Kinky Boost | `HD2_DistKinkyBoost` | `Drive` | generic_knob | 0.0 | 1.0 | 0.55 |
|  |  | `Boost` | off_on | False | True | False |
|  |  | `Bright` | off_on | False | True | False |
| Legendary Drive | `HD2_DistLegendaryDrive` | `Drive` | generic_knob | 0.0 | 1.0 | 0.77 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.54 |
|  |  | `Middle` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Presence` | generic_knob | 0.0 | 1.0 | 0.55 |
|  |  | `Volume` | generic_knob | 0.0 | 1.0 | 0.5 |
| Megaphone | `HD2_DistMegaphone` | `Grit` | generic_knob | 0.0 | 1.0 | 0.76 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Focus` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Space` | generic_knob | 0.0 | 1.0 | 0.4 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.79 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.68 |
| Minotaur | `HD2_DistMinotaur` | `Gain` | generic_knob | 0.0 | 1.0 | 0.42 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.53 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.6 |
| Obsidian 7000 | `HD2_DistObsidian7000` | `Drive` | generic_knob | 0.0 | 1.0 | 0.39 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Blend` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Grunt` | attack | 0 | 2 | 2 |
|  |  | `Attack` | attack | 0 | 2 | 1 |
|  |  | `Master` | generic_knob | 0.0 | 1.0 | 0.55 |
|  |  | `Bass` | volume | -20.0 | 20.0 | 5.5 |
|  |  | `LoMidFreq` | lo_mid_freq | 0 | 2 | 0 |
|  |  | `LoMid` | volume | -15.0 | 15.0 | -5.0 |
|  |  | `HiMidFreq` | hi_mid_freq | 0 | 2 | 0 |
|  |  | `HiMid` | volume | -15.0 | 15.0 | -4.6 |
|  |  | `Treble` | volume | -20.0 | 20.0 | -1.5 |
|  |  | `Distortion` | off_on | False | True | True |
| Pillars | `HD2_DistPillars` | `Gain` | generic_knob | 0.0 | 1.0 | 0.47 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Mode` | integer_slider_1based | 0 | 2 | 0 |
| Pocket Fuzz | `HD2_DistPocketFuzz` | `Drive` | generic_knob | 0.0 | 1.0 | 0.494 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.45 |
| Prize Drive | `HD2_DistPrizeDrive` | `Drive` | generic_knob | 0.0 | 1.0 | 0.42 |
|  |  | `Spectrum` | generic_knob | 0.0 | 1.0 | 0.74 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.4 |
|  |  | `Bass Cut` | off_on | False | True | True |
|  |  | `Voltage` | voltage | False | True | False |
| Ratatouille Dist | `HD2_DistRatatouilleDist` | `Gain` | generic_knob | 0.0 | 1.0 | 0.742 |
|  |  | `Filter` | generic_knob | 0.0 | 1.0 | 0.28 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.7 |
| Regal Bass DI | `HD2_DistRegalBassDI` | `Bass` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.45 |
|  |  | `Low Cut` | off_on | False | True | False |
|  |  | `Volume` | generic_knob | 0.0 | 1.0 | 0.23 |
| Scream 808 | `HD2_DistScream808` | `Gain` | generic_knob | 0.0 | 1.0 | 0.52 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.67 |
| Stupor OD | `HD2_DistStuporOD` | `Drive` | generic_knob | 0.0 | 1.0 | 0.625 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| Swedish Chainsaw | `HD2_DistSwedishChainsaw` | `Drive` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.6 |
| Teemah! | `HD2_DistTeemah` | `Gain` | generic_knob | 0.0 | 1.0 | 0.52 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Clipping` | clipping | 0 | 2 | 0 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.625 |
| Thrifter Fuzz | `HD2_DistThrifterFuzz` | `Drive` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Attack` | generic_knob | 0.0 | 1.0 | 0.36 |
|  |  | `Notch Freq` | frequency | 200.0 | 2500.0 | 1600.0 |
|  |  | `Notch Gain` | volume | -10.0 | 10.0 | -3.4 |
|  |  | `Thick` | off_on | 0 | 1 | 1 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.55 |
| Tone Sovereign | `HD2_DistToneSovereign` | `Gain 1` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone 1` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Presence 1` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Clipping 1` | clipping_dist | 0 | 2 | 1 |
|  |  | `GainMod 1` | gain_mod | 0 | 1 | 0 |
|  |  | `Level 1` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Gain 2` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Tone 2` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Presence 2` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Clipping 2` | clipping_dist | 0 | 2 | 0 |
|  |  | `GainMod 2` | gain_mod | 0 | 1 | 1 |
|  |  | `Level 2` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Voltage` | voltage | False | True | False |
| Top Secret OD | `HD2_DistTopSecretOD` | `Gain` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.83 |
| Triangle Fuzz | `HD2_DistTriangleFuzz` | `Sustain` | generic_knob | 0.0 | 1.0 | 0.83 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.56 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.81 |
| Tycoctavia Fuzz | `HD2_DistTycoctaviaFuzz` | `Fuzz` | generic_knob | 0.0 | 1.0 | 0.75 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.67 |
| Valve Driver | `HD2_DistValveDriver` | `Gain` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.55 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.66 |
| Vermin Dist | `HD2_DistVerminDist` | `Gain` | generic_knob | 0.0 | 1.0 | 0.68 |
|  |  | `Filter` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.85 |
| Vital Boost | `HD2_DistVitalBoost` | `Boost` | generic_knob | 0.0 | 1.0 | 0.5 |
| Vital Dist | `HD2_DistVitalDist` | `Gain` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Filter` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Clipping` | VitalDist_Clipping | 0 | 2 | 0 |
|  |  | `Octave` | generic_knob | 0.0 | 1.0 | 0.4 |
| Wringer Fuzz | `HD2_DistWringerFuzz` | `Gain` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `FuzzType` | fuzz_type | 0 | 1 | 0 |
| Xenomorph Fuzz | `HD2_DistXenomorphFuzz` | `Gain` | generic_knob | 0.0 | 1.0 | 0.875 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.578 |
|  |  | `Clipping` | clipping_dist_xenofuzz | 0 | 1 | 1 |
|  |  | `OscLevel` | generic_knob | 0.0 | 1.0 | 0.638 |
|  |  | `OscTone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `MinFreq` | frequency | 0.0 | 6000.0 | 55.0 |
|  |  | `MaxFreq` | frequency | 0.0 | 6000.0 | 880.0 |
|  |  | `WaveShape` | wave_shape_xenofuzz | 0 | 2 | 2 |
|  |  | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.5 |
| ZeroAmp Bass DI | `HD2_DistZeroAmpBassDI` | `Drive` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.59 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `Presence` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Blend` | generic_knob | 0.0 | 1.0 | 0.4 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.48 |
| Buzz Saw [L] | `HD2_DM4BuzzSaw` | `Drive` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.52 |
| Classic Dist [L] | `HD2_DM4ClassicDistortion` | `Drive` | percent | 0.0 | 1.0 | 0.78 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.48 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.36 |
| Colordrive [L] | `HD2_DM4ColorDrive` | `Drive` | percent | 0.0 | 1.0 | 0.77 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.8 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.55 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.64 |
| Facial Fuzz [L] | `HD2_DM4FacialFuzz` | `Drive` | percent | 0.0 | 1.0 | 0.92 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.75 |
| Fuzz Pi [L] | `HD2_DM4FuzzPi` | `Drive` | percent | 0.0 | 1.0 | 0.53 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.34 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.9 |
| Heavy Dist [L] | `HD2_DM4HeavyDistortion` | `Drive` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.73 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.31 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.59 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.73 |
| Jet Fuzz [L] | `HD2_DM4JetFuzz` | `Drive` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Tone` | percent | 0.0 | 1.0 | 0.27 |
|  |  | `Rate` | percent | 0.0 | 1.0 | 0.11 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.71 |
| Jumbo Fuzz [L] | `HD2_DM4JumboFuzz` | `Drive` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.5 |
| L6 Distortion [L] | `HD2_DM4Line6Distortion` | `Drive` | percent | 0.0 | 1.0 | 0.8 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.41 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.5 |
| L6 Drive [L] | `HD2_DM4Line6Drive` | `Drive` | percent | 0.0 | 1.0 | 0.92 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.89 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.69 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.5 |
| Octave Fuzz [L] | `HD2_DM4OctaveFuzz` | `Drive` | percent | 0.0 | 1.0 | 0.14 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.53 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.61 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.36 |
| Overdrive [L] | `HD2_DM4Overdrive` | `Drive` | percent | 0.0 | 1.0 | 0.52 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.65 |
| Screamer [L] | `HD2_DM4Screamer` | `Drive` | percent | 0.0 | 1.0 | 0.44 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.61 |
|  |  | `Tone` | percent | 0.0 | 1.0 | 0.73 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.53 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.8 |
| Sub Oct Fuzz [L] | `HD2_DM4SubOctFuzz` | `Drive` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Sub` | percent | 0.0 | 1.0 | 0.28 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.5 |
| Tube Drive [L] | `HD2_DM4TubeDrive` | `Drive` | percent | 0.0 | 1.0 | 0.59 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.53 |
|  |  | `Mid` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | percent | 0.0 | 1.0 | 0.82 |

## Dynamics

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| 3-Band Comp | `HD2_Compressor3BandComp` | `Ratio` | comp_ratio_3band | 0 | 6 | 2 |
|  |  | `Attack` | comp_attack | 0.0001 | 0.2 | 0.035 |
|  |  | `Release` | comp_release | 0.05 | 2.5 | 0.2 |
|  |  | `Lo X Freq` | frequency | 20.0 | 1000.0 | 400.0 |
|  |  | `Hi X Freq` | frequency | 1000.0 | 20000.0 | 3000.0 |
|  |  | `Level` | volume | -120.0 | 36.0 | 2.0 |
|  |  | `Lo Thresh` | volume | -80.0 | 0.0 | -40.0 |
|  |  | `Lo Gain` | volume | -60.0 | 30.0 | 3.5 |
|  |  | `Mid Thresh` | volume | -80.0 | 0.0 | -35.0 |
|  |  | `Mid Gain` | volume | -60.0 | 30.0 | 4.0 |
|  |  | `Hi Thresh` | volume | -80.0 | 0.0 | -50.0 |
|  |  | `Hi Gain` | volume | -60.0 | 30.0 | -2.0 |
|  |  | `Detector` | detector | False | True | True |
| Ampeg Opto Comp | `HD2_CompressorOptoComp` | `Compression` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Release` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Blend` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.65 |
| Autoswell | `HD2_CompressorAutoSwell` | `Threshold` | volume | -100.0 | 0.0 | -70.0 |
|  |  | `Rel Offset` | volume | -40.0 | 40.0 | 5.0 |
|  |  | `Attack` | time_ms | 0.1 | 5.0 | 0.4 |
|  |  | `Decay` | time_ms | 0.001 | 5.0 | 0.015 |
|  |  | `Taper` | volume_curve | False | True | True |
|  |  | `Level` | volume | -60.0 | 36.0 | 0.0 |
| Deluxe Comp | `HD2_CompressorDeluxeComp` | `Threshold` | volume | -60.0 | 0.0 | -37.1 |
|  |  | `Ratio` | comp_ratio | 0 | 5 | 3 |
|  |  | `Attack` | comp_attack | 0.0001 | 0.2 | 0.038 |
|  |  | `Release` | comp_release | 0.05 | 2.5 | 0.2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 36.0 | 7.0 |
|  |  | `Knee` | volume | 0.0 | 20.0 | 6.0 |
| Feedbacker | `VIC_FeedbackSim` | `Gain` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `FeedbackType` | feedback_type | 0 | 11 | 6 |
|  |  | `Attack` | feedbacker_time_ms | 0.15 | 6.0 | 0.5 |
|  |  | `ReleaseTime` | feedbacker_time_ms | 0.15 | 6.0 | 0.8 |
|  |  | `DryCtrl` | feedbacker_dryctrl | 0 | 2 | 0 |
|  |  | `DryLevel` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `Reference` | feedbacker_reference | 0 | 1 | 0 |
|  |  | `SilenceThresh` | volume | -120.0 | -30.0 | -100.0 |
|  |  | `OnsetThresh` | volume | 3.0 | 30.0 | 10.0 |
|  |  | `OffsetThresh` | volume | -40.0 | -2.0 | -6.0 |
|  |  | `Retrigger` | feedbacker_retrigger | 0 | 1 | 0 |
|  |  | `Trails` | off_on | False | True | True |
| Horizon Gate | `HD2_GateHorizonGate` | `Mode` | horizon_gatemode | 0 | 1 | 1 |
|  |  | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.846 |
|  |  | `Gate Range` | horizon_gaterange | False | True | False |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Kinky Comp | `HD2_CompressorKinkyComp` | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Attack` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Release` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | generic_knob | 0.0 | 1.0 | 0.5 |
| LA Studio Comp | `HD2_CompressorLAStudioComp` | `PeakReduction` | generic_knob | 0.0 | 1.0 | 0.78 |
|  |  | `Gain` | generic_knob | 0.0 | 1.0 | 0.62 |
|  |  | `Type` | comp_mode | False | True | False |
|  |  | `Emphasis` | generic_knob | 0.0 | 1.0 | 0.09 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -120.0 | 12.0 | 0.0 |
| Red Squeeze | `HD2_CompressorRedSqueeze` | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.44 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 12.0 | 5.4 |
| Rochester Comp | `HD2_CompressorRochesterComp` | `Gain` | volume_eq | -15.0 | 15.0 | 3.0 |
|  |  | `Threshold` | volume_eq | -40.0 | 22.0 | -24.0 |
|  |  | `Ratio` | rochester_ratio | 1.0 | 40.0 | 10.0 |
|  |  | `Attack` | time_ms | 0.0001 | 0.02 | 0.01 |
|  |  | `Release` | time_ms | 0.1 | 3.0 | 0.1 |
|  |  | `Level` | volume | -20.0 | 20.0 | 10.0 |
|  |  | `Knee` | volume | 0.0 | 20.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
| Transient Shaper | `HD2_CompressorTransientShaper` | `Attack` | volume | -30.0 | 30.0 | 6.96 |
|  |  | `Sustain` | volume | -30.0 | 30.0 | -6.2398 |
|  |  | `Gain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Blue Comp [L] | `HD2_DM4BlueComp` | `Sustain` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.92 |
| Blue Comp Treb [L] | `HD2_DM4BlueCompTreb` | `Sustain` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.61 |
| Boost Comp [L] | `HD2_DM4BoostComp` | `Drive` | raw_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Bass` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Comp` | raw_knob | 0.0 | 1.0 | 0.31 |
|  |  | `Treble` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Output` | raw_knob | 0.0 | 1.0 | 0.58 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Red Comp [L] | `HD2_DM4RedComp` | `Sustain` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.71 |
| Tube Comp [L] | `HD2_DM4TubeComp` | `Thresh` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.19 |
| Vetta Comp [L] | `HD2_DM4VettaComp` | `Sens` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.73 |
| Vetta Juice [L] | `HD2_DM4VettaJuice` | `Amount` | raw_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | raw_knob | 0.0 | 1.0 | 0.5 |

## Gate

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Hard Gate | `HD2_GateHardGate` | `OpenThreshold` | volume | -96.0 | 0.0 | -50.0 |
|  |  | `CloseThreshold` | volume | -96.0 | 0.0 | -60.0 |
|  |  | `HoldTime` | comp_hold_time | 0.01 | 0.8 | 0.01 |
|  |  | `Decay` | comp_decay_10_4000 | 0.01 | 4.0 | 0.01 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Noise Gate | `HD2_GateNoiseGate` | `Threshold` | volume | -96.0 | 0.0 | -48.0 |
|  |  | `Decay` | comp_decay_10_1000 | 0.01 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |

## EQ

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| 10 Band Graphic | `HD2_EQGraphic10Band` | `31p25Hz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `62p5Hz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `125Hz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `250Hz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `500Hz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `1kHz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `2kHz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `4kHz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `8kHz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `16kHz` | volume_eq | -15.0 | 15.0 | 0.0 |
|  |  | `Level` | volume_eq | -15.0 | 15.0 | 0.0 |
| Acoustic Sim | `L6SPB_AcousGtrSim` | `Mode` | poly_acoustic_sim | 0 | 3 | 0 |
|  |  | `Body` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Top` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Shimmer` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Cali Q Graphic | `HD2_CaliQ` | `80Hz` | volume_eq | -13.8 | 13.2 | 0.0 |
|  |  | `240Hz` | volume_eq | -13.3 | 13.2 | 0.0 |
|  |  | `750Hz` | volume_eq | -13.3 | 13.2 | 0.0 |
|  |  | `2200Hz` | volume_eq | -9.6 | 9.6 | 0.0 |
|  |  | `6600Hz` | volume_eq | -9.6 | 9.6 | 0.0 |
|  |  | `Level` | volume_eq | -15.0 | 15.0 | 0.0 |
| Low and High Cut | `HD2_EQLowCutHighCut` | `LowCut` | eq_low_cut | 19.9 | 1000.0 | 19.9 |
|  |  | `HighCut` | eq_high_cut | 1000.0 | 20100.0 | 20100.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Low/High Shelf | `HD2_EQLowShelfHighShelf` | `LowGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `LowFreq` | frequency | 20.0 | 2000.0 | 300.0 |
|  |  | `HighGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `HighFreq` | frequency | 400.0 | 15000.0 | 3000.0 |
|  |  | `Level` | volume | -60.0 | 12.0 | 0.0 |
| Parametric | `HD2_EQParametric` | `LowFreq` | frequency | 20.0 | 495.0 | 110.0 |
|  |  | `LowQ` | q_knob | 0.1 | 10.0 | 0.7 |
|  |  | `LowGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `MidFreq` | frequency | 125.0 | 8000.0 | 2000.0 |
|  |  | `MidQ` | q_knob | 0.1 | 10.0 | 0.7 |
|  |  | `MidGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `HighFreq` | frequency | 500.0 | 18000.0 | 8000.0 |
|  |  | `HighQ` | q_knob | 0.1 | 10.0 | 0.7 |
|  |  | `HighGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `LowCut` | eq_low_cut | 19.9 | 1000.0 | 19.9 |
|  |  | `HighCut` | eq_high_cut | 1000.0 | 20100.0 | 20100.0 |
|  |  | `Level` | volume | -60.0 | 12.0 | 0.0 |
| Simple EQ | `HD2_EQSimple3Band` | `LowGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `MidFreq` | frequency | 125.0 | 4000.0 | 600.0 |
|  |  | `MidGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `HighGain` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Level` | volume | -60.0 | 12.0 | 0.0 |
| Simple Tilt | `HD2_EQSimpleTilt` | `Tilt` | tilt | 0.0 | 1.0 | 0.5 |
|  |  | `CenterFreq` | frequency | 100.0 | 5000.0 | 1000.0 |
|  |  | `Level` | volume | -60.0 | 12.0 | 0.0 |

## Modulation

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| 4-Voice Chorus | `HD2_Chorus4Voice` | `Speed` | 4VoiceChorus_Rate | 0.1 | 2.0 | 0.5 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `NumVoices` | integer_slider | 2 | 4 | 4 |
|  |  | `HPFFrq` | frequency | 40.0 | 1000.0 | 266.0 |
|  |  | `HighShelf` | volume | -6.0 | 3.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| 60s Bias Trem | `HD2_Tremolo60sBiasTrem` | `Speed` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 0.73 |
|  |  | `Mode` | tremolo_mode | False | True | False |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| 70s Chorus | `HD2_Chorus70sChorus` | `ChorusIntensity` | generic_knob | 0.0 | 1.0 | 0.57 |
|  |  | `Mode` | chorus_mode | False | True | False |
|  |  | `VibratoRate` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `VibratoDepth` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Stereo` | stereo_classic | False | True | False |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 1.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
| AM Ring Mod | `HD2_RingModulatorAMRingMod` | `Frequency` | frequency | 5.0 | 4000.0 | 1280.0 |
|  |  | `AM` | off_on | False | True | True |
|  |  | `AMFreq` | frequency | 200.0 | 8000.0 | 1650.8 |
|  |  | `LFO` | off_on | False | True | False |
|  |  | `LFORate` | frequency | 0.0001 | 10.0 | 5.0 |
|  |  | `LFOShape` | lfo_shape | 0 | 5 | 2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.67 |
|  |  | `Level` | volume | -60.0 | 6.0 | 4.5 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Ampeg Liquifier | `HD2_ChorusAmpegLiquifier` | `Rate` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Mode` | single_dual | False | True | True |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 1 |
| Bleat Chop Trem | `HD2_TremoloPattern` | `Speed` | frequency | 0.0 | 15.0 | 1.0 |
|  |  | `WaveShape` | wave_shape_pattern_trem | 0 | 4 | 4 |
|  |  | `Step1` | pattern_trem_step | 0 | 17 | 2 |
|  |  | `Step2` | pattern_trem_step | 0 | 17 | 4 |
|  |  | `Step3` | pattern_trem_step | 0 | 17 | 8 |
|  |  | `Step4` | pattern_trem_step | 0 | 17 | 6 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Bubble Vibrato | `HD2_VibratoBubbleVibrato` | `Speed` | generic_knob | 0.0 | 1.0 | 0.632 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `RiseTime` | generic_knob | 0.0 | 1.0 | 0.66 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.554 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 3.0 |
|  |  | `RiseTimeSwitch` | off_on | False | True | True |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Chorus | `HD2_Chorus` | `Speed` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.81 |
|  |  | `Predelay` | generic_knob | 0.0 | 1.0 | 0.32 |
|  |  | `WaveShape` | wave_shape | 0 | 6 | 2 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Courtesan Flange | `HD2_FlangerCourtesanFlange` | `Rate` | generic_knob | 0.0 | 1.0 | 0.43 |
|  |  | `Range` | generic_knob | 0.0 | 1.0 | 0.71 |
|  |  | `Color` | generic_knob | 0.0 | 1.0 | 0.53 |
|  |  | `FilterMatrix` | off_on | False | True | False |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.125 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Deluxe Phaser | `HD2_PhaserDeluxePhaser` | `Rate` | frequency | 0.0 | 10.0 | 0.2 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.1 |
|  |  | `Offset` | generic_knob | 0.0 | 1.0 | 0.01 |
|  |  | `Feedback` | percent_feedback | -1.0 | 1.0 | 0.25 |
|  |  | `WaveShape` | wave_shape | 0 | 6 | 2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Stages` | integer_slider | 2 | 16 | 8 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Double Take | `HD2_DelayDoubleDouble` | `Doubles` | integer_slider_1based | 0 | 3 | 0 |
|  |  | `Slop` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.72 |
|  |  | `Source` | delay_source | 0 | 3 | 1 |
|  |  | `Dry Level` | volume | -60.0 | 9.0 | 0.0 |
|  |  | `Wet Level` | volume | -60.0 | 9.0 | 0.0 |
| Dynamix Flanger | `HD2_FlangerDynamixFlanger` | `Speed` | generic_knob | 0.0 | 1.0 | 0.044 |
|  |  | `Control Select` | control_select | 0 | 2 | 0 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.66 |
|  |  | `Manual` | generic_knob | 0.0 | 1.0 | 0.418 |
|  |  | `Mix` | dynamix_flanger_mix | 0.0 | 1.0 | 0.5 |
|  |  | `Phasing` | phasing | -1.0 | 1.0 | -1.0 |
|  |  | `Recycle` | out_in | False | True | True |
|  |  | `CV Dynamics` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Max Delay` | time_ms_dynamix_flanger | 0.01 | 0.0997 | 0.01 |
|  |  | `CV Tracking` | cv_polarity | False | True | False |
|  |  | `Env Lag` | time_ms_env_lag | 0.0 | 0.1 | 0.1 |
|  |  | `Env Input` | volume_eq | 0.0 | 70.0 | 70.0 |
|  |  | `CV Decay` | cv_delay | 0 | 2 | 2 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| FlexoVibe | `VIC_FlexoVibe` | `Speed` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Warp` | FlexoVibe_Warp | -1.0 | 1.0 | 0.0 |
|  |  | `PhaseOffset` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Gray Flanger | `HD2_FlangerGrayFlanger` | `Rate` | generic_knob | 0.0 | 1.0 | 0.16 |
|  |  | `Width` | generic_knob | 0.0 | 1.0 | 0.78 |
|  |  | `Manual` | generic_knob | 0.0 | 1.0 | 0.77 |
|  |  | `Regen` | generic_knob | 0.0 | 1.0 | 0.56 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.125 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Harmonic Flanger | `HD2_FlangerHarmonicFlanger` | `Rate` | generic_knob | 0.0 | 1.0 | 0.35 |
|  |  | `Width` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Manual` | generic_knob | 0.0 | 1.0 | 0.84 |
|  |  | `Enhance` | generic_knob | 0.0 | 1.0 | 0.28 |
|  |  | `Harmonic` | odd_even | False | True | True |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.125 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Harmonic Tremolo | `HD2_TremoloHarmonic` | `Speed` | frequency | 0.0 | 15.0 | 4.0 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `WaveShape` | wave_shape | 0 | 6 | 3 |
|  |  | `DutyCycle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `BassFreq` | frequency | 40.0 | 2000.0 | 500.0 |
|  |  | `TrebFreq` | frequency | 100.0 | 10000.0 | 700.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Optical Trem | `HD2_TremoloOpticalTrem` | `Speed` | generic_knob | 0.0 | 1.0 | 0.66 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 0.67 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Pebble Phaser | `HD2_PhaserPebblePhaser` | `Rate` | generic_knob | 0.0 | 1.0 | 0.35 |
|  |  | `Color` | off_on | False | True | False |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| PlastiChorus | `HD2_ChorusPlastiChorus` | `Rate` | generic_knob | 0.0 | 1.0 | 0.35 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.47 |
|  |  | `Mode` | chorus_mode | False | True | False |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.75 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Poly Detune | `L6SPB_PolyChorus` | `Blend` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Detune` | cents | -50.0 | 50.0 | 10.0 |
|  |  | `LowCut` | poly_chorus_lowcut | 0 | 8 | 0 |
|  |  | `HighCut` | poly_chorus_hicut | 0 | 4 | 4 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Random S&H | `SampleAndHold` | `Speed` | frequency | 0.0 | 15.0 | 0.7 |
|  |  | `Range` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.76 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Retro Reel | `HD2_RetroReel` | `WowFluttr` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `Saturation` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `TapeSpeed` | reel_inchespresec | 0 | 2 | 1 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Texture` | generic_knob | 0.0 | 1.0 | 0.625 |
| Script Mod Phase | `HD2_PhaserScriptModPhase` | `Rate` | generic_knob | 0.0 | 1.0 | 0.19 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Sweeper | `Sweeper` | `Speed` | frequency | 0.0 | 15.0 | 0.7 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.76 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Range` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Tape Eater | `TapeEater` | `Feedback` | percent | 0.0 | 1.0 | 0.65 |
|  |  | `Flutter` | percent | 0.0 | 1.0 | 0.9 |
|  |  | `Dist` | percent | 0.0 | 1.0 | 0.6 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Tremolo | `HD2_TremoloTremolo` | `Speed` | frequency | 0.0 | 15.0 | 3.0 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `WaveShape` | wave_shape | 0 | 6 | 3 |
|  |  | `DutyCycle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Ubiquitous Vibe | `HD2_PhaserUbiquitousVibe` | `Rate` | generic_knob | 0.0 | 1.0 | 0.29 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Mode` | chorus_mode | False | True | False |
|  |  | `LampBias` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Warble Eater | `Warble_Matic` | `Speed` | frequency | 0.0 | 15.0 | 0.7 |
|  |  | `Range` | percent | 0.0 | 1.0 | 0.38 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| 80A Flanger [L] | `HD2_M1380AFlanger` | `Speed` | frequency | 0.0 | 15.0 | 0.55 |
|  |  | `Range` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `Enhance` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Manual` | percent | 0.0 | 1.0 | 0.38 |
|  |  | `Harmonic` | even_odd | False | True | True |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| AC Flanger [L] | `HD2_M13ACFlanger` | `Speed` | frequency | 0.1 | 15.0 | 0.55 |
|  |  | `Width` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Regen` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `Manual` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Analog Chorus [L] | `HD2_MM4AnalogChorus` | `Speed` | frequency | 0.0 | 15.0 | 1.59 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.7 |
|  |  | `CH Vib` | chorus_mode | False | True | False |
|  |  | `Tone` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Analog Flanger [L] | `HD2_MM4AnalogFlanger` | `Speed` | frequency | 0.0 | 15.0 | 0.85 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.16 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.06 |
|  |  | `Manual` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Barberpole Phaser [L] | `HD2_MM4BarberpolePhaser` | `Speed` | frequency | 0.0 | 15.0 | 1.59 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Mode` | shift_mode | 0 | 2 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Bias Tremolo [L] | `HD2_MM4BiasTremolo` | `Speed` | frequency | 0.0 | 15.0 | 9.41 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Shape` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Volsens` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Dimension [L] | `HD2_MM4Dimension` | `SW1` | OFF_ON | False | True | False |
|  |  | `SW2` | OFF_ON | False | True | False |
|  |  | `SW3` | OFF_ON | False | True | False |
|  |  | `SW4` | OFF_ON | False | True | True |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dual Phaser [L] | `HD2_MM4DualPhaser` | `Speed` | frequency | 0.0 | 15.0 | 1.6 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `LFOShape` | lfo_shape_dualphaser | False | True | False |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Freq Shift [L] | `HD2_MM4FrequencyShifter` | `Speed` | frequency | 0.0 | 3520.0 | 110.0 |
|  |  | `Mode` | shift_mode | 0 | 2 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Jet Flanger [L] | `HD2_MM4JetFlanger` | `Speed` | frequency | 0.0 | 15.0 | 0.55 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.33 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `Manual` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Opto Tremolo [L] | `HD2_MM4OptoTremolo` | `Speed` | frequency | 0.0 | 15.0 | 7.55 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Shape` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `VolSens` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Panned Phaser [L] | `HD2_MM4PannedPhaser` | `Speed` | frequency | 0.0 | 15.0 | 3.83 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Pan` | pan_discrete | 0 | 2 | 0 |
|  |  | `Pan Speed` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Panner [L] | `HD2_MM4Panner` | `Speed` | frequency | 0.0 | 15.0 | 3.08 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Shape` | wave_shape_panner | 0 | 2 | 0 |
|  |  | `VolSen` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Pattern Trem [L] | `HD2_MM4PatternTrem` | `Speed` | frequency | 0.0 | 15.0 | 1.59 |
|  |  | `Step1` | pattern_trem_step | 0 | 17 | 2 |
|  |  | `Step2` | pattern_trem_step | 0 | 17 | 4 |
|  |  | `Step3` | pattern_trem_step | 0 | 17 | 4 |
|  |  | `Step4` | pattern_trem_step | 0 | 17 | 6 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Phaser [L] | `HD2_MM4Phaser` | `Speed` | frequency | 0.0 | 15.0 | 1.59 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Stage` | stage | 0 | 3 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Pitch Vibrato [L] | `HD2_MM4PitchVibrato` | `Speed` | frequency | 0.0 | 15.0 | 6.36 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Rise` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Volsens` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `RiseTimeSwitch` | off_on | False | True | True |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Ring Modulator [L] | `HD2_MM4RingModulator` | `Speed` | percent | 0.0 | 1.0 | 0.23 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Shape` | percent | 0.0 | 1.0 | 0.06 |
|  |  | `AM/FM` | percent | 0.0 | 1.0 | 0.03 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.92 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Rotary Drum [L] | `HD2_MM4RotaryDrum` | `Speed` | fast_slow | False | True | True |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Tone` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Drive` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Rotary Drum/Horn [L] | `HD2_MM4RotaryDrumHorn` | `Speed` | fast_slow | False | True | True |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Horn Depth` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Drive` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Script Phase [L] | `HD2_MM4ScriptPhase` | `Speed` | frequency | 0.0 | 15.0 | 1.59 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Tri Chorus [L] | `HD2_MM4TriChorus` | `Speed` | frequency | 0.0 | 15.0 | 2.34 |
|  |  | `Depth1` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Depth2` | percent | 0.0 | 1.0 | 0.91 |
|  |  | `Depth3` | percent | 0.0 | 1.0 | 0.53 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.86 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| U-Vibe [L] | `HD2_MM4UVibe` | `Speed` | frequency | 0.0 | 15.0 | 4.57 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.14 |
|  |  | `VolSens` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.89 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |

## Delay

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| ADT | `HD2_DelayADT` | `DelayDeck1` | time_ms | 0.0 | 0.02 | 0.003 |
|  |  | `DelayDeck2` | time_ms | 0.0 | 0.2 | 0.05 |
|  |  | `WowFlutter1` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `WowFlutter2` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `DistDeck1` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `DistDeck2` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Deck1Vol` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Deck2Vol` | volume | -60.0 | 6.0 | -3.0 |
|  |  | `Deck2Pol` | cv_polarity | 0 | 1 | 0 |
|  |  | `ModRate` | frequency | 0.1 | 8.0 | 0.5 |
|  |  | `ModDepth` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `TapeSpeed` | reel_inchespresec | 0 | 2 | 1 |
|  |  | `Texture` | generic_knob | 0.0 | 1.0 | 0.625 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 40.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 12000.0 |
|  |  | `Deck1Pan` | pan | 0.0 | 1.0 | 0.522 |
|  |  | `Deck2Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Threshold` | adt_threshold | 0.0 | 1.0 | 0.0 |
| Adriatic Delay | `HD2_DelayAdriaticDelay` | `Time` | time_ms_20_1800 | 0.02 | 1.8 | 0.4 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Noise` | generic_knob | 0.0 | 1.0 | 0.36 |
|  |  | `BBD Size` | bbd_size | 0 | 3 | 2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.3 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.22 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Adriatic Swell | `HD2_DelaySwellAdriatic` | `Time` | time_ms_20_1800 | 0.02 | 1.8 | 0.4 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Noise` | generic_knob | 0.0 | 1.0 | 0.36 |
|  |  | `BBD Size` | bbd_size | 0 | 3 | 2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.3 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.22 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.5 |
|  |  | `Threshold` | volume | -96.0 | 0.0 | -60.0 |
|  |  | `Attack` | time_ms | 0.1 | 5.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Bubble Echo | `L6BubbleEcho` | `Time` | time_ms_0_4000 | 0.02 | 2.0 | 0.545 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Speed` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Bucket Brigade | `HD2_DelayBucketBrigade` | `Time` | time_ms_20_300 | 0.02 | 0.3 | 0.238 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.43 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Noise` | generic_knob | 0.0 | 1.0 | 0.28 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Cosmos Echo | `HD2_DelayCosmosEcho` | `Time` | time_ms_0_2000 | 0.15 | 2.0 | 0.6 |
|  |  | `Ramp` | generic_knob | 0.0 | 1.0 | 0.75 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `WowFlutter` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Mode` | delay_heads | 0 | 5 | 4 |
|  |  | `Bass` | volume | -18.0 | 18.0 | 0.0 |
|  |  | `Treble` | volume | -18.0 | 18.0 | 0.0 |
|  |  | `FBTone` | generic_knob | 0.0 | 1.0 | 0.375 |
|  |  | `Splice` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `DryThru` | off_on | False | True | False |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Crisscross | `HD2_DelayCrissCross` | `TimeA` | time_ms_0_4000 | 0.0 | 2.0 | 0.557 |
|  |  | `TimeB` | time_ms_0_4000 | 0.0 | 2.0 | 0.337 |
|  |  | `FeedbackA` | percent | 0.0 | 1.0 | 0.55 |
|  |  | `FeedbackB` | percent | 0.0 | 1.0 | 0.7 |
|  |  | `PanA` | pan | 0.0 | 1.0 | 0.0 |
|  |  | `PanB` | pan | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Crossfeed` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 12.0 |
|  |  | `ModRate` | frequency | 0.1 | 10.0 | 0.8 |
|  |  | `ModDepth` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Shape` | crisscross_wave_shape | 2 | 3 | 3 |
|  |  | `Phase` | phase | 0 | 2 | 1 |
|  |  | `BitDepth` | crisscross_bitdepth | 0 | 7 | 4 |
|  |  | `SampleRate` | sample_rate | 0 | 7 | 3 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
| Ducked Delay | `HD2_DelayDuckedDelay` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.5 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.375 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 60.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 10300.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Threshold` | percent | 0.0 | 1.0 | 0.49 |
|  |  | `Ducking` | percent | 0.0 | 1.0 | 0.61 |
|  |  | `DynAttack` | time_ms_10_2000 | 0.01 | 2.0 | 0.56 |
|  |  | `DynRel` | time_ms_10_5000 | 0.01 | 5.0 | 0.51 |
|  |  | `DynType` | dyn_type | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Elephant Man | `HD2_DelayElephantMan` | `Time` | time_ms_20_500 | 0.02 | 0.5 | 0.375 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Mode` | chorus_mode | False | True | False |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.28 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.272 |
|  |  | `Noise` | generic_knob | 0.0 | 1.0 | 0.1 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Euclidean Delay | `Victoria_EuclideanDelay` | `Step Time` | time_ms_0_4000 | 0.0 | 0.5 | 0.136 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Steps` | integer_slider | 1 | 16 | 8 |
|  |  | `Fill` | integer_slider | 1 | 16 | 3 |
|  |  | `Rotate` | integer_slider | 0 | 15 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.422 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 80.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20000.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Glitch Delay | `Victoria_ShufflingDelay` | `Time` | time_ms_0_4000 | 0.01 | 4.0 | 1.0 |
|  |  | `Delay Div` | integer_slider | 1 | 16 | 4 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `SliceFdbk` | percent | 0.0 | 1.0 | 0.1 |
|  |  | `Shuffle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Octaves` | percent | 0.0 | 1.0 | 0.1 |
|  |  | `Reverse` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Seq Drift` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Smoothing` | percent | 0.0 | 0.5 | 0.1 |
|  |  | `Lock` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Glitch Delay | `VIC_DelayGlitch` | `Time` | time_ms_0_4000 | 0.01 | 4.0 | 1.0 |
|  |  | `Delay Div` | integer_slider | 1 | 16 | 4 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `SliceFdbk` | percent | 0.0 | 1.0 | 0.1 |
|  |  | `Shuffle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.1 |
|  |  | `Reverse` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Seq Drift` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Smoothing` | percent | 0.0 | 0.5 | 0.1 |
|  |  | `Interval 1` | integer_slider | -12 | 12 | -12 |
|  |  | `Interval 2` | integer_slider | -12 | 12 | 12 |
|  |  | `Low Cut` | eq_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `High Cut` | eq_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Lock` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Heliosphere | `HD2_DelayHeliosphere` | `Time` | time_ms_0_4000 | 0.0 | 4.0 | 0.8 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.85 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.1 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.442 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `VerbMix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `VerbDecay` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Mod/Chorus Echo | `HD2_DelayModChorusEcho` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.362 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.28 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 155.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 9540.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `ModulationMode` | delay_mod_mode | 0 | 2 | 1 |
|  |  | `Speed` | generic_knob | 0.0 | 1.0 | 0.022 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.49 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Multi Pass | `HD2_DelayMultiPass` | `Time` | time_ms_0_4000 | 0.0 | 4.0 | 1.2 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Pattern` | integer_slider_1based | 0 | 7 | 0 |
|  |  | `Mode` | delay_mode | False | True | False |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Tap1Pan` | pan | 0.0 | 1.0 | 0.422 |
|  |  | `Tap2Pan` | pan | 0.0 | 1.0 | 0.622 |
|  |  | `Tap3Pan` | pan | 0.0 | 1.0 | 0.2 |
|  |  | `Tap4Pan` | pan | 0.0 | 1.0 | 0.8 |
|  |  | `Tap5Pan` | pan | 0.0 | 1.0 | 0.022 |
|  |  | `Tap6Pan` | pan | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Phaze Eko | `L6PhazeEko` | `Time` | time_ms_0_4000 | 0.02 | 2.0 | 0.545 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Speed` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Pitch Echo | `HD2_DelayPitch` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.25 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Interval1` | integer_slider_signed | -13 | 13 | 5 |
|  |  | `Cents1` | cents | -50.0 | 50.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Poly Sustain | `L6SPB_InfSustain` | `Interval` | integer_slider_signed | -36 | 24 | 0 |
|  |  | `Attack` | time_ms | 0.1 | 5.0 | 0.5 |
|  |  | `Decay` | time_ms | 0.1 | 5.0 | 0.5 |
|  |  | `ModFreq` | frequency | 0.1 | 10.0 | 5.0 |
|  |  | `ModDepth` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `FX Level` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `RandDepth` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `RandSpeed` | generic_knob | 0.0 | 1.0 | 0.1 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `FreezeSwitch` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Poly Sustain | `VIC_DelayPolySustain` | `Interval` | integer_slider_signed | -36 | 24 | 0 |
|  |  | `Attack` | time_ms | 0.1 | 5.0 | 0.5 |
|  |  | `Decay` | time_ms | 0.1 | 5.0 | 0.5 |
|  |  | `ModFreq` | frequency | 0.1 | 10.0 | 5.0 |
|  |  | `ModDepth` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `FX Level` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `RandDepth` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `RandSpeed` | generic_knob | 0.0 | 1.0 | 0.1 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `AutoEQ` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Operation` | polysustain_operation | 0 | 2 | 2 |
|  |  | `FreezeSwitch` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Ratchet | `VIC_DelayRatchet` | `Time` | time_ms_0_4000 | 0.05 | 1.0 | 0.1 |
|  |  | `FX Level` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Operation` | stutterEdit_Operation | 0 | 2 | 2 |
|  |  | `Transport` | off_on | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Reverse Delay | `HD2_DelayReverseDelay` | `Time` | time_ms_0_4000 | 0.0 | 4.0 | 1.0 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Speed` | generic_knob | 0.0 | 1.0 | 0.022 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `ModulationMode` | delay_mod_mode | 0 | 2 | 0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Simple Delay | `HD2_DelaySimpleDelay` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.6 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.35 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Sweep Echo | `HD2_DelaySweepEcho` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.45 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.58 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 120.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 8000.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `FilterType` | mode_pass | 0 | 2 | 1 |
|  |  | `SweepShape` | sweep_shape | 0 | 5 | 0 |
|  |  | `SweepSpeed` | generic_knob | 0.0 | 1.0 | 0.34 |
|  |  | `SweepStart` | frequency | 40.0 | 470.0 | 205.0 |
|  |  | `SweepDepth` | frequency | 0.0 | 3250.0 | 2830.0 |
|  |  | `SweepResonance` | generic_knob | 0.0 | 1.0 | 0.45 |
|  |  | `SweepSymmetry` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `SweepSpread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Tesselator | `VIC_DelayStutterEdit` | `First` | time_ms_0_4000 | 0.05 | 1.0 | 0.1 |
|  |  | `Last` | time_ms_0_4000 | 0.05 | 1.0 | 0.2 |
|  |  | `Steps` | integer_slider | 1 | 50 | 8 |
|  |  | `Direction` | stutterEdit_Reverse | 0 | 2 | 0 |
|  |  | `Boomerang` | off_on | False | True | False |
|  |  | `Operation` | stutterEdit_Operation | 0 | 2 | 2 |
|  |  | `Ramp` | stutterEdit_Mode | 0 | 1 | 0 |
|  |  | `Speed` | percent | 0.0 | 2.0 | 1.0 |
|  |  | `Pitch` | integer_slider_signed | -12 | 12 | 0 |
|  |  | `HP Filter` | generic_knob | 0.0 | 1.0 | 0.0 |
|  |  | `LP Filter` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `FX Level` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `Transport` | off_on | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
| Transistor Tape | `HD2_DelayTransistorTape` | `Time` | time_ms_0_2000 | 0.0 | 2.0 | 0.507 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.54 |
|  |  | `WowFlutter` | generic_knob | 0.0 | 1.0 | 0.36 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 0.29 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Vintage Digital | `HD2_DelayVintageDigital` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.5 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `BitDepth` | delay_bit_depth | 0 | 7 | 4 |
|  |  | `SampleRate` | sample_rate | 0 | 7 | 3 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.2 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Vintage Digital | `HD2_DelayVintageDigitalV2` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.5 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `BitDepth` | delay_bit_depth | 0 | 7 | 4 |
|  |  | `SampleRate` | sample_rate | 0 | 7 | 3 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.2 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Vintage Swell | `HD2_DelaySwellVintageDigital` | `Time` | time_ms_0_8000 | 0.0 | 8.0 | 0.5 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `BitDepth` | delay_bit_depth | 0 | 7 | 7 |
|  |  | `SampleRate` | sample_rate | 0 | 7 | 7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 0.2 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Scale` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `Headroom` | volume | -12.0 | 12.0 | 0.0 |
|  |  | `Threshold` | volume | -96.0 | 0.0 | -60.0 |
|  |  | `Attack` | time_ms | 0.1 | 5.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Analog Echo [L] | `HD2_DL4AnalogDelayStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.255 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.23 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.56 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.23 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Analog w/Mod [L] | `HD2_DL4AnalogDelayStereoMod` | `Time` | time_ms | 0.0 | 2.0 | 0.47 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `ModSpeed` | percent | 0.0 | 1.0 | 0.34 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.84 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Auto-Vol Echo [L] | `HD2_DL4AutoVolStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.392 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.23 |
|  |  | `Swell` | percent | 0.0 | 1.0 | 0.81 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.44 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Digital [L] | `HD2_DL4DigDelay` | `Time` | time_ms | 0.0 | 2.0 | 0.751 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.6 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Digital w/Mod [L] | `HD2_DL4DigDelayWithMod` | `Time` | time_ms | 0.0 | 2.0 | 0.437 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.38 |
|  |  | `ModSpeed` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.59 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.31 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Dynamic [L] | `HD2_DL4DynamicDelayStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.437 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Threshold` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Ducking` | percent | 0.0 | 1.0 | 0.48 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.66 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Echo Platter [L] | `HD2_DL4EchoPlatterStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.225 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Wow Flt` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Drive` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `DryThru` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Lo Res [L] | `HD2_DL4LowResDelay` | `Time` | time_ms | 0.0 | 2.0 | 0.403 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.42 |
|  |  | `Tone` | percent | 0.0 | 1.0 | 0.42 |
|  |  | `Res` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.66 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Multi-Head [L] | `HD2_DL4MultiheadStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.554 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Heads 1-2` | heads12 | 0 | 3 | 1 |
|  |  | `Heads 3-4` | heads34 | 0 | 3 | 2 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Ping Pong [L] | `HD2_DL4PingPong` | `Time` | time_ms | 0.0 | 2.0 | 0.47 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.52 |
|  |  | `Offset` | percent | 0.0 | 1.0 | 0.52 |
|  |  | `Spread` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.72 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Reverse [L] | `HD2_DL4Reverse` | `Time` | time_ms | 0.0 | 2.0 | 2.0 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `ModSpeed` | percent | 0.0 | 1.0 | 0.06 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Stereo [L] | `HD2_DL4StereoDelay` | `LTime` | time_ms | 0.0 | 2.0 | 0.342 |
|  |  | `LFeedback` | percent | 0.0 | 1.0 | 0.55 |
|  |  | `RTime` | time_ms | 0.0 | 2.0 | 0.911 |
|  |  | `RFeedback` | percent | 0.0 | 1.0 | 0.66 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.73 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
| Sweep Echo [L] | `HD2_DL4SweepEchoStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.469 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.56 |
|  |  | `Speed` | percent | 0.0 | 1.0 | 0.33 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.91 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `DryThru` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Tape Echo [L] | `HD2_DL4TapeEchoStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.279 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Bass` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.31 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `DryThru` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Tube Echo [L] | `HD2_DL4TubeEchoStereo` | `Time` | time_ms | 0.0 | 2.0 | 0.169 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.11 |
|  |  | `Wow Flt` | percent | 0.0 | 1.0 | 0.31 |
|  |  | `Drive` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `DryThru` | off_on | False | True | True |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |

## Reverb

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Double Tank | `HD2_ReverbDoubleTank` | `Decay` | generic_knob | 0.0 | 1.0 | 0.43 |
|  |  | `Predelay` | time_ms_reverb | 0.0 | 0.2 | 0.0 |
|  |  | `Rate` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Modulation` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 169.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 6000.0 |
| Dynamic Ambience | `VIC_ReverbDynAmbience` | `RoomSize` | dynamicAmbience_room_size | 0 | 2 | 0 |
|  |  | `PreDelay` | time_ms | 0.0 | 0.05 | 0.005 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 5000 |
|  |  | `Diffusion` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `EarlyLateBlend` | dynamic_ambience_shape | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 100.0 |
|  |  | `HighCut` | mod_high_cut | 1000.0 | 20100.0 | 10000.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dynamic Bloom | `VIC_ReverbDynBloom` | `Decay` | time_sec_DynamicHall | 0.1 | 45.1 | 2.0 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 3720.0 |
|  |  | `MatrFreq` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `RiseTime` | rise_time | 0 | 2 | 1 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `BassFreq` | frequency | 20.0 | 500.0 | 100.0 |
|  |  | `BassBoost` | volume | -15.0 | 3.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 100.0 |
|  |  | `HighCut` | mod_high_cut | 1000.0 | 20100.0 | 10000.0 |
|  |  | `DuckingAmount` | generic_knob | 0.0 | 1.0 | 0.2 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dynamic Hall | `VIC_ReverbRotating` | `Decay` | time_sec_DynamicHall | 0.1 | 45.1 | 4.0 |
|  |  | `Predelay` | time_ms | 0.0 | 0.2 | 0.05 |
|  |  | `RoomSize` | room_size | 0 | 2 | 1 |
|  |  | `Diffusion` | percent | 0.0 | 1.0 | 0.7 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 3720.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Motion` | generic_knob | 0.0 | 1.0 | 0.29 |
|  |  | `BassFreq` | frequency | 20.0 | 500.0 | 100.0 |
|  |  | `BassBoost` | volume | -15.0 | 3.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 117.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 6300.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dynamic Plate | `VIC_DynPlate` | `Decay` | time_sec_DynamicHall | 0.1 | 45.1 | 2.0 |
|  |  | `PreDelay` | time_ms | 0.0 | 0.1 | 0.01 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 3720.0 |
|  |  | `MatrFreq` | generic_knob | 0.0 | 1.0 | 0.33 |
|  |  | `VarDelayAmpl` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `BassFreq` | frequency | 20.0 | 500.0 | 100.0 |
|  |  | `BassBoost` | volume | -15.0 | 3.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 100.0 |
|  |  | `HighCut` | mod_high_cut | 1000.0 | 20100.0 | 10000.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dynamic Room | `VIC_ReverbDynRoom` | `Decay` | time_sec | 0.1 | 3.0 | 1.2 |
|  |  | `PreDelay` | time_ms | 0.0 | 0.1 | 0.01 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 3720 |
|  |  | `Diffusion` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `MatrFreq` | generic_knob | 0.0 | 1.0 | 0.333 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `BassFreq` | frequency | 20.0 | 500.0 | 100.0 |
|  |  | `BassBoost` | volume | -15.0 | 3.0 | 0.0 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 100.0 |
|  |  | `HighCut` | mod_high_cut | 1000.0 | 20100.0 | 10000.0 |
|  |  | `ERLevel` | generic_knob_1to1 | 0.0 | 2.0 | 0.8 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Ganymede | `HD2_ReverbGanymede` | `Decay` | generic_knob | 0.0 | 1.0 | 0.65 |
|  |  | `Predelay` | time_ms_reverb | 0.0 | 0.2 | 0.04 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.72 |
|  |  | `Modulation` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.35 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Glitz | `HD2_ReverbGlitz` | `Decay` | generic_knob | 0.0 | 1.0 | 0.47 |
|  |  | `Predelay` | time_ms_reverb | 0.001 | 0.2 | 0.01 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 118 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 8000.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.19 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Delay` | time_ms_reverb | 0.001 | 0.2 | 0.044 |
|  |  | `Rate` | frequency | 0.1 | 8.0 | 1.838 |
|  |  | `Depth` | generic_knob | 0.0 | 1.0 | 0.384 |
|  |  | `Xover` | frequency | 100.0 | 10000.0 | 866.0 |
|  |  | `Mod Mix` | generic_knob | 0.0 | 1.0 | 0.35 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Hot Springs | `HD2_ReverbHxSpring` | `Dwell` | generic_knob | 0.0 | 1.0 | 0.4 |
|  |  | `Spring Count` | tenths_no_units | 1.0 | 3.0 | 2.0 |
|  |  | `Drip` | lo_med_high | 0 | 2 | 1 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 200.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 5000.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.37 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Nonlinear | `HD2_ReverbNonLinear` | `Decay` | feedbacker_time_ms | 0.05 | 2.0 | 1.0 |
|  |  | `Predelay` | feedbacker_time_ms | 0.0 | 0.5 | 0.0 |
|  |  | `Shape` | nonlinear_shape | 0 | 7 | 1 |
|  |  | `Late Dry` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Diffusion` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 80.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 8600.0 |
|  |  | `Mod` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Rate` | generic_knob | 0.0 | 1.0 | 0.066 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
| Plateaux | `HD2_ReverbPlateaux` | `Decay` | generic_knob | 0.0 | 1.0 | 0.47 |
|  |  | `Predelay` | time_ms_reverb | 0.0 | 0.2 | 0.0 |
|  |  | `Tone` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `Modulation` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.33 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Pitch1` | pitch | -24 | 24 | -12 |
|  |  | `Cents1` | cents | -50.0 | 50.0 | -0.8 |
|  |  | `Pitch2` | pitch | -24 | 24 | 7 |
|  |  | `Cents2` | cents | -50.0 | 50.0 | 0.4 |
|  |  | `PitchMix` | percent | 0.0 | 1.0 | 0.24 |
| Searchlights | `HD2_ReverbSearchlights` | `Decay` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Predelay` | time_ms_reverb | 0.0 | 0.2 | 0.07 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 196.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 6500.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.29 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Modulation` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `Speed` | generic_knob | 0.1 | 1.0 | 0.37 |
|  |  | `Intensity` | generic_knob | 0.0 | 1.0 | 0.63 |
|  |  | `Spread` | generic_knob | 0.0 | 1.0 | 1.0 |
| Shimmer | `VIC_ReverbShimmer` | `Mode` | Shimmer_Mode | False | True | True |
|  |  | `Shift1` | Shimmer_shift_OctaveStep | -12.0 | 12.0 | 12.0 |
|  |  | `Shift2` | Shimmer_shift_OctaveStep | -12.0 | 12.0 | 7.0 |
|  |  | `Intensity` | percent | 0.0 | 1.0 | 0.9 |
|  |  | `Feedback` | percent | 0.0 | 1.0 | 0.9 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Balance` | Shimmer_pitchblend | 0.0 | 1.0 | 0.5 |
|  |  | `Decay` | time_sec_DynamicHall | 0.1 | 45.1 | 4.0 |
|  |  | `Predelay` | time_ms | 0.0 | 0.2 | 0.15 |
|  |  | `RoomSize` | room_size | 0 | 2 | 2 |
|  |  | `Damping` | frequency | 500.0 | 20000.0 | 5000 |
|  |  | `Diffusion` | percent | 0.0 | 1.0 | 0.7 |
|  |  | `Motion` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 1000.0 | 120.0 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 6300.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |

## Pitch/Synth

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| 12-String | `L6SPB_12String` | `Blend` | generic_knob | 0.0 | 1.0 | 0.75 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| 12-String | `VIC_PitchTwelveString` | `Blend` | generic_knob | 0.0 | 1.0 | 0.75 |
|  |  | `Bass` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Treble` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `OnsetThresh` | polytwelvestring_plucktype | 0 | 2 | 1 |
| 3 Note Generator | `HD2_Synth3NoteGenerator` | `Osc1Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc1Octave` | integer_slider | 0 | 8 | 3 |
|  |  | `Osc1Note` | note_pitch | 0 | 11 | 0 |
|  |  | `Osc1Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc1Pan` | pan | 0.0 | 1.0 | 0.478 |
|  |  | `Osc1Glide` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Osc2Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc2Octave` | integer_slider | 0 | 8 | 3 |
|  |  | `Osc2Note` | note_pitch | 0 | 11 | 7 |
|  |  | `Osc2Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc2Pan` | pan | 0.0 | 1.0 | 0.544 |
|  |  | `Osc2Glide` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Osc3Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc3Octave` | integer_slider | 0 | 8 | 4 |
|  |  | `Osc3Note` | note_pitch | 0 | 11 | 4 |
|  |  | `Osc3Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc3Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Osc3Glide` | generic_knob | 0.0 | 1.0 | 0.25 |
|  |  | `Attack` | time_ms | 0.01 | 10.0 | 0.5 |
|  |  | `Decay` | time_ms | 0.01 | 10.0 | 3.0 |
|  |  | `DryLevel` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `DryPan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `RiseTimeSwitch` | off_on | False | True | True |
| 4 OSC Generator | `HD2_Synth4OSCGenerator` | `Osc1Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc1Freq` | frequency | 20.0 | 10000.0 | 110.0 |
|  |  | `Osc1Pan` | pan | 0.0 | 1.0 | 0.478 |
|  |  | `Osc1Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc2Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc2Freq` | frequency | 20.0 | 10000.0 | 220.0 |
|  |  | `Osc2Pan` | pan | 0.0 | 1.0 | 0.544 |
|  |  | `Osc2Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc3Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc3Freq` | frequency | 20.0 | 10000.0 | 440.0 |
|  |  | `Osc3Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Osc3Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Osc4Shape` | wave_shape | 0 | 4 | 3 |
|  |  | `Osc4Freq` | frequency | 20.0 | 10000.0 | 660.0 |
|  |  | `Osc4Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Osc4Level` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Attack` | time_ms | 0.01 | 10.0 | 0.5 |
|  |  | `Decay` | time_ms | 0.01 | 10.0 | 3.0 |
|  |  | `DryLevel` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `DryPan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `RiseTimeSwitch` | off_on | False | True | True |
| Analog Synth | `SynthAnalog` | `Wave` | wave_rezsynth | 0 | 7 | 1 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Decay` | percent | 0.0 | 1.0 | 0.88 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Boctaver | `VIC_PitchBoctaver` | `Oct1Level` | generic_knob | 0.0 | 1.0 | 0.6 |
|  |  | `Oct2Level` | generic_knob | 0.0 | 1.0 | 0.3 |
|  |  | `DryLevel` | generic_knob | 0.0 | 1.0 | 0.6 |
| Buzz Wave | `BuzzWave` | `Wave` | wave_buzz | 0 | 6 | 0 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.2 |
|  |  | `Decay` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.45 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Double Bass | `DoubleBass` | `-1oct G` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `-2oct G` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Dual Pitch | `HD2_PitchDualPitch` | `Interval1` | integer_slider_signed | -24 | 24 | 7 |
|  |  | `Cents1` | cents | -50.0 | 50.0 | 0.0 |
|  |  | `Time1` | time_ms_pitch | 0.0 | 0.1 | 0.0 |
|  |  | `LevelVoice1` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Interval2` | integer_slider_signed | -24 | 24 | 16 |
|  |  | `Cents2` | cents | -50.0 | 50.0 | -5.0 |
|  |  | `Time2` | time_ms_pitch | 0.0 | 0.1 | 0.0 |
|  |  | `LevelVoice2` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `PanVoice1` | pan | 0.0 | 1.0 | 0.125 |
|  |  | `PanVoice2` | pan | 0.0 | 1.0 | 0.875 |
|  |  | `PanDry` | pan | 0.0 | 1.0 | 0.5 |
| Pitch Wham | `HD2_PitchPitchWham` | `Pedal` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Heel` | pitch | -24 | 24 | -12 |
|  |  | `Toe` | pitch | -24 | 24 | 12 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Poly Bass Wham | `L6SPB_PolyBassWham` | `Position` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `HeelShift` | integer_slider_signed | -36 | 24 | 0 |
|  |  | `ToeShift` | integer_slider_signed | -36 | 24 | 12 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Poly Capo | `L6SPB_PolyDowntune` | `Interval` | integer_slider_signed | -12 | 12 | -2 |
|  |  | `Tracking` | poly_tracking | 0 | 3 | 3 |
|  |  | `AutoEQ` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Poly Pitch | `L6SPB_PolyPitch` | `Interval` | integer_slider_signed | -24 | 24 | 7 |
|  |  | `Cents` | cents | -50.0 | 50.0 | 0.0 |
|  |  | `ShiftTime` | time_ms | 0.0 | 8.0 | 0.0 |
|  |  | `ShiftCurve` | poly_shift_slicecurve | -5 | 5 | 0 |
|  |  | `ReturnTime` | time_ms | 0.0 | 8.0 | 0.0 |
|  |  | `ReturnCurve` | poly_shift_slicecurve | -5 | 5 | 0 |
|  |  | `Tracking` | poly_tracking | 0 | 3 | 3 |
|  |  | `AutoEQ` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `RiseFallSwitch` | off_on | False | True | False |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
| Poly Wham | `L6SPB_PolyWham` | `Position` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `HeelShift` | integer_slider_signed | -36 | 24 | 0 |
|  |  | `ToeShift` | integer_slider_signed | -36 | 24 | 12 |
|  |  | `Tracking` | poly_tracking | 0 | 3 | 3 |
|  |  | `AutoEQ` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Rez Synth | `RezSynth` | `Wave` | wave_rezsynth | 0 | 7 | 3 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.4 |
|  |  | `Decay` | percent | 0.0 | 1.0 | 0.65 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.65 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Saturn 5 RingMod | `Saturn5RingMod` | `Wave` | wave_rezsynth | 0 | 7 | 1 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Seismik Synth | `SeismicSynth` | `Wave` | wave_rezsynth | 0 | 7 | 4 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.6 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Simple Pitch | `HD2_PitchSimplePitch` | `Interval1` | integer_slider_signed | -24 | 24 | 7 |
|  |  | `Cents1` | cents | -50.0 | 50.0 | 0.0 |
|  |  | `Time1` | time_ms_pitch | 0.0 | 0.1 | 0.0 |
|  |  | `LevelVoice1` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `PanVoice1` | pan | 0.0 | 1.0 | 0.45 |
|  |  | `PanDry` | pan | 0.0 | 1.0 | 0.5 |
| String Theory | `SynthString` | `Wave` | wave_rezsynth | 0 | 7 | 4 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.76 |
|  |  | `Attack` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.76 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Synth FX | `SynthFX` | `Wave` | wave_rezsynth | 0 | 7 | 0 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Decay` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Synth Harmony | `SynthHarmony` | `Wave` | wave_rezsynth | 0 | 7 | 0 |
|  |  | `Interval1` | synthharmony_interval1 | 1 | 8 | 7 |
|  |  | `Interval2` | synthharmony_interval2 | 0 | 8 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.38 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Synth Lead | `SynthLead` | `Wave` | wave_rezsynth | 0 | 7 | 1 |
|  |  | `Filter` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Decay` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Twin Harmony | `HD2_PitchTwinHarmony` | `KeyVoice1` | key_voice | 0 | 11 | 0 |
|  |  | `ScaleVoice1` | scale_voice | 0 | 7 | 0 |
|  |  | `IntervalVoice1` | pitch_shift | -8 | 8 | -3 |
|  |  | `LevelVoice1` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `PanVoice1` | pan | 0.0 | 1.0 | 0.375 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `KeyVoice2` | key_voice | 0 | 11 | 0 |
|  |  | `ScaleVoice2` | scale_voice | 0 | 7 | 0 |
|  |  | `IntervalVoice2` | pitch_shift | -8 | 8 | 2 |
|  |  | `LevelVoice2` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `PanVoice2` | pan | 0.0 | 1.0 | 0.625 |
| Attack Synth [L] | `HD2_FM4AttackSynth` | `Freq` | percent | 0.0 | 1.0 | 0.8 |
|  |  | `Wave` | wave_synth | 0 | 2 | 2 |
|  |  | `Attack` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Bass Octaver [L] | `HD2_DM4BassOctaver` | `Tone` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Normal` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Octave` | percent | 0.0 | 1.0 | 0.85 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Growler [L] | `HD2_FM4Growler` | `Speed` | frequency | 0.0 | 15.0 | 0.84 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.84 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Octi Synth [L] | `HD2_FM4OctiSynth` | `Speed` | frequency | 0.0 | 15.0 | 0.1 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Q` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Depth` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Smart Harmony [L] | `HD2_M13TwoVoiceHarmony` | `Key` | key_voice | 0 | 11 | 0 |
|  |  | `Shift` | pitch_shift | -8 | 8 | 2 |
|  |  | `Scale` | scale_voice | 0 | 7 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Synth O Matic [L] | `HD2_FM4SynthOMatic` | `Frequency` | percent | 0.0 | 1.0 | 0.7 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Wave` | integer_slider | 0 | 7 | 6 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Synth String [L] | `HD2_FM4SynthString` | `Speed` | frequency | 0.0 | 15.0 | 0.69 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.89 |
|  |  | `Attack` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |

## Filter

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Asheville Pattrn | `HD2_FilterAshevillePattrn` | `Rate` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Pattern` | ashville_pattern | 0 | 20 | 4 |
|  |  | `Envelope` | generic_knob | 0.0 | 1.0 | 0.5 |
|  |  | `Voice` | ashville_voice | False | True | True |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Output` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Drive` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Direction` | ashville_direction | False | True | False |
|  |  | `LFO` | percent_zero_off | 0.0 | 1.0 | 0.0 |
|  |  | `Spread` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level1` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level2` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level3` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level4` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level5` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level6` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level7` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level8` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
|  |  | `SyncSelect2` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync2` | off_on | False | True | False |
| Auto Filter | `HD2_FilterAutoFilter` | `Mode` | mode_pass | 0 | 2 | 1 |
|  |  | `FilterGain` | volume_eq | 0.0 | 36.0 | 18.0 |
|  |  | `FilterQ` | filter_q | 1.0 | 10.0 | 7.5 |
|  |  | `Sens` | generic_knob | 0.0 | 1.0 | 0.4 |
|  |  | `Attack` | time_ms_filter_attack | 0.005 | 2.0 | 0.02 |
|  |  | `Decay` | time_ms_filter_decay | 0.005 | 3.0 | 0.35 |
|  |  | `Frequency` | frequency | 20.0 | 1000.0 | 50.0 |
|  |  | `FreqDepth` | frequency | 0.0 | 10000.0 | 3500.0 |
|  |  | `Direction` | down_up | False | True | True |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Mutant Filter | `HD2_FilterMutantFilter` | `Mode` | mode_pass | 0 | 2 | 1 |
|  |  | `Peak` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Gain` | generic_knob | 0.0 | 1.0 | 0.15 |
|  |  | `Range` | filter_range | False | True | False |
|  |  | `Drive` | down_up | False | True | True |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 1.0 |
| Mystery Filter | `HD2_FilterMysterFilter` | `Sensitivity` | generic_knob | 0.0 | 1.0 | 0.52 |
|  |  | `Frequency` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Resonance` | generic_knob | 0.0 | 1.0 | 0.8 |
|  |  | `Attack` | generic_knob | 0.0 | 1.0 | 0.13 |
|  |  | `Release` | generic_knob | 0.0 | 1.0 | 0.97 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | -1.0 |
| Comet Trails [L] | `HD2_FM4CometTrails` | `Speed` | frequency | 0.0 | 15.0 | 3.33 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Gain` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Obi Wah [L] | `HD2_FM4ObiWah` | `Speed` | frequency | 0.0 | 15.0 | 6.3 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.72 |
|  |  | `Type` | mode_pass | 0 | 2 | 1 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Q Filter [L] | `HD2_FM4QFilter` | `Freq` | percent | 0.0 | 1.0 | 0.27 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.75 |
|  |  | `Gain` | percent | 0.0 | 1.0 | 0.63 |
|  |  | `Type` | mode_pass | 0 | 2 | 1 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Seeker [L] | `HD2_FM4Seeker` | `Speed` | frequency | 0.0 | 15.0 | 5.8 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.39 |
|  |  | `Steps` | integer_steps | 2 | 9 | 8 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Slow Filter [L] | `HD2_FM4SlowFilter` | `Freq` | percent | 0.0 | 1.0 | 0.09 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.67 |
|  |  | `Speed` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mode` | up_down | False | True | False |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Spin Cycle [L] | `HD2_FM4SpinCycle` | `Speed` | frequency | 0.0 | 15.0 | 1.21 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.86 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.25 |
|  |  | `Vol Sens` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Throbber [L] | `HD2_FM4Throbber` | `Speed` | frequency | 0.0 | 15.0 | 4.8 |
|  |  | `Freq` | percent | 0.0 | 1.0 | 0.13 |
|  |  | `Q` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Wave` | wave_shape_throbber | 0 | 3 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |
| Tron Down [L] | `HD2_FM4TronDown` | `Freq` | percent | 0.0 | 1.0 | 0.69 |
|  |  | `Q` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Range` | filter_range | False | True | False |
|  |  | `Type` | mode_pass | 0 | 2 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Tron Up [L] | `HD2_FM4TronUp` | `Freq` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Q` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Range` | filter_range | False | True | False |
|  |  | `Type` | mode_pass | 0 | 2 | 1 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| V Tron [L] | `HD2_FM4VTron` | `Speed` | percent | 0.0 | 1.0 | 0.47 |
|  |  | `Start` | vowel_start | 0 | 4 | 0 |
|  |  | `End` | vowel_end | 0 | 4 | 4 |
|  |  | `Mode` | up_updown | False | True | True |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Voice Box [L] | `HD2_FM4VoiceBox` | `Speed` | frequency | 0.0 | 15.0 | 2.95 |
|  |  | `Start` | vowel_start | 0 | 4 | 0 |
|  |  | `End` | vowel_end | 0 | 4 | 2 |
|  |  | `Auto` | auto | 0 | 3 | 0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `SyncSelect1` | sync_note | 1 | 19 | 6 |
|  |  | `TempoSync1` | off_on | False | True | False |

## Wah

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Chrome | `HD2_WahChrome` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 470.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 2415.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Chrome Custom | `HD2_WahChromeCustom` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 300.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 1975.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Colorful | `HD2_WahColorful` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 280.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 2101.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Conductor | `HD2_WahConductor` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 392.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 922.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Fassel | `HD2_WahFassel` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 455.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 2155.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Teardrop 310 | `HD2_WahTeardrop310` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Teardrop Bass Q | `HD2_WahTeardropBassQ` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `Q Trim` | generic_knob | 0.0 | 1.0 | 1.0 |
|  |  | `Volume Trim` | generic_knob | 0.0 | 1.0 | 0.7 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Throaty | `HD2_WahThroaty` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 310.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 1735.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| UK Wah 846 | `HD2_WahUKWah846` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 4.0 |
| Vetta Wah | `HD2_WahVettaWah` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 300.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 2300.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |
| Weeper | `HD2_WahWeeper` | `Pedal` | percent_braced | 0.0 | 1.0 | 0.0 |
|  |  | `FcLow` | frequency | 20.0 | 500.0 | 435.0 |
|  |  | `FcHigh` | frequency | 500.0 | 5000.0 | 1901.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | 0.0 |

## Volume/Pan

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Gain | `HD2_VolPanGain` | `Gain` | volume | -120.0 | 12.0 | 0.0 |
| Volume | `HD2_VolPanVol` | `Pedal` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `VolumeTaper` | volume_curve | False | True | False |

## Send/Return

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| FX Loop 1 | `HD2_FXLoopMono1` | `Send` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Return` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
| FX Loop 2 | `HD2_FXLoopMono2` | `Send` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Return` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
| FX Loop 3 | `HD2_FXLoopMono3` | `Send` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Return` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
| FX Loop 4 | `HD2_FXLoopMono4` | `Send` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Return` | volume | -60.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
| Return 1 | `HD2_ReturnMono1` | `Return` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
| Return 2 | `HD2_ReturnMono2` | `Return` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
| Return 3 | `HD2_ReturnMono3` | `Return` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
| Return 4 | `HD2_ReturnMono4` | `Return` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 0.5 |
| Send 1 | `HD2_SendMono1` | `Send` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `DryThru` | volume | -120.0 | 6.0 | 0.0 |
| Send 2 | `HD2_SendMono2` | `Send` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `DryThru` | volume | -120.0 | 6.0 | 0.0 |
| Send 3 | `HD2_SendMono3` | `Send` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `DryThru` | volume | -120.0 | 6.0 | 0.0 |
| Send 4 | `HD2_SendMono4` | `Send` | volume | -120.0 | 6.0 | 0.0 |
|  |  | `DryThru` | volume | -120.0 | 6.0 | 0.0 |

## Fixed

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| 1 Switch Looper | `HD2_LooperOneSwitch` | `Playback` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `Overdub` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `lowCut` | frequency | 20.0 | 500.0 | 20.0 |
|  |  | `highCut` | frequency | 500.0 | 20000.0 | 20000.0 |
| 6 Switch Looper | `HD2_Looper` | `Playback` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `Overdub` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `lowCut` | frequency | 20.0 | 500.0 | 20.0 |
|  |  | `highCut` | frequency | 500.0 | 20000.0 | 20000.0 |
| @dt | `@dt` | _(aucun)_ | | | | |
| @global_params | `@global_params` | _(aucun)_ | | | | |
| @powercab | `@powercab` | _(aucun)_ | | | | |
| @variax | `@variax` | _(aucun)_ | | | | |
| IR 1024 | `HD2_ImpulseResponse1024` | `Index` | ir_select | 1 | 128 | 1 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | -18.0 |
| IR 2048 | `HD2_ImpulseResponse2048` | `Index` | ir_select | 1 | 128 | 1 |
|  |  | `LowCut` | mod_low_cut | 19.9 | 500.0 | 19.9 |
|  |  | `HighCut` | mod_high_cut | 500.0 | 20100.0 | 20100.0 |
|  |  | `Mix` | percent | 0.0 | 1.0 | 1.0 |
|  |  | `Level` | volume | -60.0 | 6.0 | -18.0 |
| Shuffling Looper | `ShufflingLooper` | `Slices` | shuffling_looper_slices | 0 | 8 | 4 |
|  |  | `SeqLength` | shuffling_looper_seqlength | 0 | 8 | 4 |
|  |  | `Shuffle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Octaves` | percent | 0.0 | 1.0 | 0.2 |
|  |  | `Reverse` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `Repeat` | percent | 0.0 | 1.0 | 0.2 |
|  |  | `Smoothing` | percent | 0.0 | 0.5 | 0.1 |
|  |  | `Seq Drift` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Playback` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `Low Cut` | frequency | 20.0 | 500.0 | 20.0 |
|  |  | `High Cut` | frequency | 500.0 | 20000.0 | 20000.0 |
| Shuffling Looper | `VIC_LooperShuffling` | `Slices` | shuffling_looper_slices | 0 | 8 | 4 |
|  |  | `SeqLength` | shuffling_looper_seqlength | 0 | 8 | 4 |
|  |  | `Shuffle` | percent | 0.0 | 1.0 | 0.5 |
|  |  | `Pitch` | percent | 0.0 | 1.0 | 0.2 |
|  |  | `Reverse` | percent | 0.0 | 1.0 | 0.3 |
|  |  | `Repeat` | percent | 0.0 | 1.0 | 0.2 |
|  |  | `Smoothing` | percent | 0.0 | 0.5 | 0.1 |
|  |  | `Seq Drift` | percent | 0.0 | 1.0 | 0.0 |
|  |  | `Playback` | volume | -60.0 | 0.0 | 0.0 |
|  |  | `Low Cut` | frequency | 20.0 | 500.0 | 20.0 |
|  |  | `High Cut` | frequency | 500.0 | 20000.0 | 20000.0 |
|  |  | `Interval 1` | integer_slider_signed | -12 | 12 | -12 |
|  |  | `Interval 2` | integer_slider_signed | -12 | 12 | 12 |
|  |  | `Midi Command` | integer_slider | 0 | 15 | 0 |

## I/O

| Nom | Model ID | Parametre | Type | Min | Max | Default |
|---|---|---|---|---|---|---|
| Input | `HD2_AppDSPFlow1Input` | `noiseGate` | off_on | False | True | False |
|  |  | `threshold` | volume | -96.0 | 0.0 | -48.0 |
|  |  | `decay` | time_ms_input | 0.01 | 1.0 | 0.5 |
| Input | `HD2_AppDSPFlow2Input` | `noiseGate` | off_on | False | True | False |
|  |  | `threshold` | volume | -96.0 | 0.0 | -48.0 |
|  |  | `decay` | time_ms_input | 0.01 | 1.0 | 0.5 |
| Input | `HelixPlugin_AppDSPFlow1Input` | `noiseGate` | off_on | False | True | False |
|  |  | `threshold` | volume | -96.0 | 0.0 | -48.0 |
|  |  | `decay` | time_ms_input | 0.01 | 1.0 | 0.5 |
| Input | `HelixFx_AppDSPFlowInput` | _(aucun)_ | | | | |
| Input | `HelixStomp_AppDSPFlowInput` | `noiseGate` | off_on | False | True | False |
|  |  | `threshold` | volume | -96.0 | 0.0 | -48.0 |
|  |  | `decay` | time_ms_input | 0.01 | 1.0 | 0.5 |
| Mixer | `HD2_AppDSPFlowJoin` | `A Level` | volume | -60.0 | 12.0 | 0.0 |
|  |  | `A Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `B Level` | volume | -60.0 | 12.0 | 0.0 |
|  |  | `B Pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `B Polarity` | polarity | False | True | False |
|  |  | `Level` | volume | -60.0 | 12.0 | 0.0 |
| Output | `HD2_AppDSPFlowOutput` | `pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `gain` | volume | -120.0 | 20.0 | 0.0 |
| Output | `HelixPlugin_AppDSPFlowOutput` | `pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `gain` | volume | -120.0 | 20.0 | 0.0 |
| Output | `HelixFx_AppDSPFlowOutput` | `pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `gain` | volume | -120.0 | 20.0 | 0.0 |
| Output | `HelixStomp_AppDSPFlowOutputMain` | `pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `gain` | volume | -120.0 | 20.0 | 0.0 |
| Output | `HelixStomp_AppDSPFlowOutputSend` | `pan` | pan | 0.0 | 1.0 | 0.5 |
|  |  | `gain` | volume | -120.0 | 20.0 | 0.0 |
|  |  | `Type` | stereo_mode | False | True | True |
| Split A/B | `HD2_AppDSPFlowSplitAB` | `RouteTo` | split_ab_route_to | 0.0 | 1.0 | 0.5 |
|  |  | `bypass` | off_on | False | True | False |
| Split Crossover | `HD2_AppDSPFlowSplitXOver` | `Frequency` | frequency | 25.0 | 15000.0 | 500.0 |
|  |  | `Reverse` | off_on | False | True | False |
|  |  | `bypass` | off_on | False | True | False |
| Split Dynamic | `HD2_AppDSPFlowSplitDyn` | `Threshold` | volume | -60.0 | 0.0 | -15.0 |
|  |  | `Attack` | time_ms | 0.05 | 5.0 | 0.86 |
|  |  | `Decay` | time_ms | 0.05 | 5.0 | 0.86 |
|  |  | `Reverse` | off_on | False | True | False |
|  |  | `bypass` | off_on | False | True | False |
| Split Y | `HD2_AppDSPFlowSplitY` | `BalanceA` | split_balance | 0.0 | 1.0 | 0.5 |
|  |  | `BalanceB` | split_balance | 0.0 | 1.0 | 0.5 |
|  |  | `bypass` | off_on | False | True | False |
