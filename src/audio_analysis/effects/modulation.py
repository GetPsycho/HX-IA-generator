"""
modulation.py
Detection de modulations periodiques (chorus, flanger, phaser, tremolo).

Principe : ces effets ajoutent une variation periodique au son :
- Phaser / Flanger : oscillation du spectre (notches qui bougent)
  -> visible dans le spectral_centroid qui varie periodiquement
- Chorus : delay court module en pitch
  -> visible dans le centroid + dans l'enveloppe RMS (legers battements)
- Tremolo : modulation d'amplitude
  -> visible dans l'enveloppe RMS

Methode : on calcule le centroid sur des fenetres de ~50ms, on lisse
legerement, puis FFT pour detecter une periodicite dominante dans
la plage 0.1-15 Hz (rates LFO typiques).
"""

import numpy as np
import librosa


_LFO_MIN_HZ = 0.10   # plus lent = pas vraiment perceptible comme modulation
_LFO_MAX_HZ = 15.0   # plus rapide = sort des LFO standards


def detect_modulation(y: np.ndarray, sr: int,
                       analysis_window_s: float = 30.0,
                       tempo_bpm: float = None) -> dict:
    """
    Detecte une eventuelle modulation periodique dans le signal.

    Args:
        y  : signal mono
        sr : sample rate
        analysis_window_s : fenetre d'analyse centrale (defaut 30s)
        tempo_bpm : tempo du morceau (optionnel) — utilise pour rejeter les pics
                    correspondant au tempo ou ses multiples (variations rythmiques
                    plutot que LFO)

    Returns:
        {
          "detected":      True | False,
          "type":          "phaser" | "chorus" | "tremolo" | "vibrato" | None,
          "rate_hz":       0.45,         # taux LFO detecte
          "depth_0_1":     0.30,         # profondeur estimee
          "confidence":    0.45,         # ratio peak vs background
          "centroid_var":  120.5,        # variation moyenne du centroid (info)
          "method":        "...",
        }
    """
    if len(y) == 0:
        return {"detected": False, "type": None, "rate_hz": None,
                "depth_0_1": 0.0, "confidence": 0.0,
                "method": "empty signal"}

    # Fenetre d'analyse centrale
    win_samples = int(analysis_window_s * sr)
    if len(y) > win_samples:
        mid = len(y) // 2
        seg = y[max(0, mid - win_samples // 2): mid + win_samples // 2]
    else:
        seg = y

    # Series temporelles : centroid (pour phaser/flanger) et RMS (pour tremolo/chorus depth)
    hop = 256
    centroid_series = librosa.feature.spectral_centroid(
        y=seg, sr=sr, hop_length=hop).flatten()
    rms_series = librosa.feature.rms(y=seg, hop_length=hop).flatten()

    if len(centroid_series) < 32:
        return {"detected": False, "type": None, "rate_hz": None,
                "depth_0_1": 0.0, "confidence": 0.0,
                "method": "signal too short"}

    # Sample rate des series temporelles (~sr/hop)
    series_sr = sr / hop

    # Normalisation : on enleve la moyenne pour ne garder que les variations
    centroid_demean = centroid_series - np.mean(centroid_series)
    centroid_var = float(np.std(centroid_series))

    # FFT pour trouver la periodicite dominante dans la plage LFO
    fft = np.abs(np.fft.rfft(centroid_demean * np.hanning(len(centroid_demean))))
    freqs = np.fft.rfftfreq(len(centroid_demean), 1.0 / series_sr)

    # Plage LFO
    lfo_mask = (freqs >= _LFO_MIN_HZ) & (freqs <= _LFO_MAX_HZ)
    if not np.any(lfo_mask):
        return {"detected": False, "type": None, "rate_hz": None,
                "depth_0_1": 0.0, "confidence": 0.0, "centroid_var": centroid_var,
                "method": "no LFO range available"}

    lfo_spec = fft[lfo_mask]
    lfo_freqs = freqs[lfo_mask]

    # Si tempo connu, masquer les pics rythmiques (tempo et multiples)
    # Une "vraie" modulation LFO ne se synchronise pas avec le tempo du morceau.
    if tempo_bpm is not None and tempo_bpm > 0:
        beat_hz = tempo_bpm / 60.0
        # Masque les harmoniques 0.5x, 1x, 2x, 4x du beat_hz (+/- 5% tolerance)
        for mult in (0.5, 1.0, 2.0, 4.0):
            target = beat_hz * mult
            tol = max(target * 0.05, 0.05)
            block_mask = (lfo_freqs >= target - tol) & (lfo_freqs <= target + tol)
            lfo_spec = np.where(block_mask, 0.0, lfo_spec)

    # Pic dominant (apres masquage)
    if lfo_spec.max() < 1e-9:
        return {"detected": False, "type": None, "rate_hz": None,
                "depth_0_1": round(depth_0_1, 2), "confidence": 0.0,
                "centroid_var": round(centroid_var, 1),
                "method": "all LFO peaks masked by tempo harmonics"}
    peak_idx = int(np.argmax(lfo_spec))
    peak_freq = float(lfo_freqs[peak_idx])
    peak_amp = float(lfo_spec[peak_idx])

    # Background : mediane du spectre LFO (sans le pic)
    background = float(np.median(lfo_spec))
    if background < 1e-9:
        background = 1e-9

    # Confidence : ratio peak / background
    peak_ratio = peak_amp / background
    confidence = min(peak_ratio / 10.0, 1.0)  # 10x bg = confidence 1.0

    # Profondeur estimee : amplitude relative du centroid var par rapport au centroid moyen
    centroid_mean = float(np.mean(centroid_series))
    depth_0_1 = min(centroid_var / (centroid_mean + 1e-9), 1.0) if centroid_mean > 0 else 0.0

    # Seuils stricts pour limiter les faux positifs (signal sature genere des
    # artefacts spectraux periodiques qui ressemblent a du LFO) :
    # - confidence >= 0.85 (pic vs background tres marque)
    # - depth_0_1 >= 0.20 (variation du centroid significative)
    # - pour les rates tres lents (<0.5 Hz), seuil encore plus strict
    if peak_freq < 0.5:
        detected = confidence >= 0.95 and depth_0_1 >= 0.25
    else:
        detected = confidence >= 0.85 and depth_0_1 >= 0.20

    if not detected:
        return {
            "detected":     False,
            "type":         None,
            "rate_hz":      round(peak_freq, 2),  # info meme si non detecte
            "depth_0_1":    round(depth_0_1, 2),
            "confidence":   round(confidence, 2),
            "centroid_var": round(centroid_var, 1),
            "method":       "spectral_centroid FFT, LFO 0.1-15Hz",
        }

    # Classification par taux
    if peak_freq < 0.5:
        mod_type = "phaser"   # tres lent : phaser slow
    elif peak_freq < 2.0:
        mod_type = "chorus"   # rate typique chorus / flanger lent
    elif peak_freq < 6.0:
        mod_type = "tremolo"  # tremolo classique
    else:
        mod_type = "vibrato"  # rapide

    return {
        "detected":     True,
        "type":         mod_type,
        "rate_hz":      round(peak_freq, 2),
        "depth_0_1":    round(depth_0_1, 2),
        "confidence":   round(confidence, 2),
        "centroid_var": round(centroid_var, 1),
        "method":       "spectral_centroid FFT, LFO 0.1-15Hz",
    }
