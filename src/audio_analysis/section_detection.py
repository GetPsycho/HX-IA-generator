"""
section_detection.py
Detection des sections d'un morceau (intro / verse / chorus / bridge / outro)
via clustering spectral Laplacien sur une matrice de recurrence beat-synced.

Reference : McFee & Ellis (2014), "Analyzing song structure with spectral clustering"
Approche standard dans la communaute MIR (Music Information Retrieval).

Le pipeline :
1. Extraire features beat-synced (MFCC + chroma)
2. Matrice de recurrence (similarite entre tous les beats)
3. Filtrage temporel (median filter sur les diagonales)
4. Laplacien normalise + decomposition en valeurs propres
5. K-means sur les K premiers vecteurs propres -> labels de cluster par beat
6. Conversion beats -> segments temporels
7. Heuristique de labellisation : intro/verse/chorus/bridge/outro
"""

from collections import Counter
import numpy as np
import librosa
import scipy.linalg
import scipy.ndimage
import scipy.sparse.csgraph
import sklearn.cluster
import sklearn.preprocessing


def detect_sections(y: np.ndarray, sr: int, num_clusters: int = 5) -> list:
    """
    Detecte les sections d'un morceau.

    Args:
        y : signal audio mono
        sr : sample rate
        num_clusters : nombre de clusters cibles (5 = intro/verse/chorus/bridge/outro)

    Returns:
        Liste de dicts :
        [
          {
            "start": 0.0,
            "end": 12.8,
            "duration_s": 12.8,
            "cluster": "A",        # lettre du cluster (groupe de segments similaires)
            "label": "intro",      # heuristique : intro/verse/chorus/bridge/outro
          },
          ...
        ]
    """
    # Beat tracking pour synchroniser les features
    _, beats = librosa.beat.beat_track(y=y, sr=sr, trim=False)

    # Features : MFCC (timbre) + chroma (harmonie)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

    # Sync sur les beats (mediane par fenetre)
    mfcc_sync = librosa.util.sync(mfcc, beats, aggregate=np.median)
    chroma_sync = librosa.util.sync(chroma, beats, aggregate=np.median)

    # Stack et normalisation
    features = np.vstack([mfcc_sync, chroma_sync])

    # Matrice de recurrence (affinite, symetrique)
    R = librosa.segment.recurrence_matrix(features, mode="affinity", sym=True)

    # Filtrage temporel : lisse les diagonales de R pour eviter les transitions parasites
    R_filt = scipy.ndimage.median_filter(R, size=(7, 7))

    # Laplacien normalise + decomposition
    L = scipy.sparse.csgraph.laplacian(R_filt, normed=True)
    evals, evecs = scipy.linalg.eigh(L)

    # Clamp num_clusters au nombre de beats disponibles
    n_beats = len(beats)
    k = min(num_clusters, max(2, n_beats // 4))

    # K-means sur les K premiers vecteurs propres (normaliss L2)
    X = evecs[:, :k]
    X = sklearn.preprocessing.normalize(X, norm="l2", axis=1)
    km = sklearn.cluster.KMeans(n_clusters=k, n_init=10, random_state=0)
    cluster_labels = km.fit_predict(X)

    # Conversion : labels per-beat -> segments contigus
    beat_times = librosa.frames_to_time(beats, sr=sr)
    sections_raw = []
    if len(cluster_labels) == 0:
        return sections_raw

    current_label = cluster_labels[0]
    start_idx = 0
    for i in range(1, len(cluster_labels)):
        if cluster_labels[i] != current_label:
            sections_raw.append({
                "start_beat": start_idx,
                "end_beat":   i - 1,
                "cluster":    int(current_label),
            })
            start_idx = i
            current_label = cluster_labels[i]
    sections_raw.append({
        "start_beat": start_idx,
        "end_beat":   len(cluster_labels) - 1,
        "cluster":    int(current_label),
    })

    # Conversion en temps (secondes)
    total_duration_s = float(len(y)) / sr
    sections = []
    for s in sections_raw:
        start_t = float(beat_times[s["start_beat"]]) if s["start_beat"] < len(beat_times) else 0.0
        # Fin = debut du segment suivant, ou fin du morceau pour le dernier
        next_start = s["end_beat"] + 1
        if next_start < len(beat_times):
            end_t = float(beat_times[next_start])
        else:
            end_t = total_duration_s
        sections.append({
            "start":      round(start_t, 2),
            "end":        round(end_t, 2),
            "duration_s": round(end_t - start_t, 2),
            "cluster":    chr(ord("A") + s["cluster"]),  # 'A', 'B', 'C', ...
        })

    # Filtre : eliminer les segments trop courts (< 4s) en les fusionnant avec le suivant
    sections = _merge_short_segments(sections, min_duration=4.0)

    # Labellisation heuristique
    labels = _label_sections(sections)
    for sec, lbl in zip(sections, labels):
        sec["label"] = lbl

    return sections


def _merge_short_segments(sections: list, min_duration: float = 4.0) -> list:
    """Fusionne les segments < min_duration avec le suivant (ou precedent si dernier)."""
    if not sections:
        return sections

    merged = []
    i = 0
    while i < len(sections):
        s = dict(sections[i])
        # Tant que la section est trop courte et qu'il y a un suivant, on fusionne
        while s["duration_s"] < min_duration and i + 1 < len(sections):
            nxt = sections[i + 1]
            s["end"] = nxt["end"]
            s["duration_s"] = round(s["end"] - s["start"], 2)
            # Garde le cluster majoritaire (en temps)
            if nxt["duration_s"] > sections[i]["duration_s"]:
                s["cluster"] = nxt["cluster"]
            i += 1
        merged.append(s)
        i += 1
    return merged


def _label_sections(sections: list) -> list:
    """
    Heuristique de labellisation :
    - 1ere section = "intro"
    - derniere section = "outro" (sauf si meme cluster que chorus -> "chorus")
    - cluster le plus frequent (hors intro/outro) = "chorus"
    - 2eme cluster le plus frequent = "verse"
    - autres clusters = "bridge"

    Les labels repetes sont numerotes : verse_1, verse_2, chorus_1, chorus_2, ...
    """
    if not sections:
        return []

    if len(sections) == 1:
        return ["main"]

    # Comptage des clusters (toutes positions)
    cluster_counts = Counter(s["cluster"] for s in sections)
    sorted_clusters = [c for c, _ in cluster_counts.most_common()]

    chorus_cluster = sorted_clusters[0] if len(sorted_clusters) > 0 else None
    verse_cluster = sorted_clusters[1] if len(sorted_clusters) > 1 else None

    labels = []
    counts = {"verse": 0, "chorus": 0, "bridge": 0}

    for i, s in enumerate(sections):
        c = s["cluster"]
        is_first = (i == 0)
        is_last = (i == len(sections) - 1)

        if is_first:
            labels.append("intro")
        elif is_last and c != chorus_cluster:
            labels.append("outro")
        elif c == chorus_cluster:
            counts["chorus"] += 1
            labels.append(f"chorus_{counts['chorus']}")
        elif c == verse_cluster:
            counts["verse"] += 1
            labels.append(f"verse_{counts['verse']}")
        else:
            counts["bridge"] += 1
            labels.append(f"bridge_{counts['bridge']}")

    return labels
