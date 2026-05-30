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


def detect_sections(y: np.ndarray, sr: int,
                     num_clusters: int = 5,
                     min_segment_duration: float = 8.0) -> dict:
    """
    Detecte les sections d'un morceau.

    Args:
        y : signal audio mono
        sr : sample rate
        num_clusters : nombre de clusters cibles (5 = intro/verse/chorus/bridge/outro)
        min_segment_duration : duree min d'un segment apres merge (s)

    Returns:
        {
          "segments": [
            {"start": 0.0, "end": 12.8, "duration_s": 12.8,
             "cluster": "A", "label": "intro", "label_certainty": "high"},
            ...
          ],
          "cluster_summary": {
            "A": {"occurrences": 5, "total_duration_s": 183.2,
                  "is_intro": true, "is_outro": true},
            "B": {"occurrences": 1, "total_duration_s": 6.5, ...},
            ...
          },
          "notes": [
            "Le cluster 'A' apparait a l'intro ET de facon recurrente ailleurs",
            "Sections sub-10s peuvent etre des transitions plutot que des sections",
          ]
        }
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

    # Filtre : eliminer les segments trop courts en les fusionnant avec le suivant
    sections = _merge_short_segments(sections, min_duration=min_segment_duration)

    # Labellisation heuristique (utilise la frequence sur les sections du milieu)
    labels_with_certainty = _label_sections(sections)
    for sec, (lbl, cert) in zip(sections, labels_with_certainty):
        sec["label"] = lbl
        sec["label_certainty"] = cert

    # Resume des clusters : occurrences, duree totale, positions specials
    cluster_summary = _build_cluster_summary(sections)

    # Notes interpretatives pour le consommateur du rapport (= Claude)
    notes = _build_interpretation_notes(sections, cluster_summary)

    return {
        "segments":        sections,
        "cluster_summary": cluster_summary,
        "notes":           notes,
    }


def _build_cluster_summary(sections: list) -> dict:
    """Resume par cluster : nb d'occurrences, duree totale, bookend (intro/outro)."""
    if not sections:
        return {}
    intro_cluster = sections[0]["cluster"]
    outro_cluster = sections[-1]["cluster"]
    summary = {}
    for s in sections:
        c = s["cluster"]
        if c not in summary:
            summary[c] = {
                "occurrences":      0,
                "total_duration_s": 0.0,
                "is_intro":         (c == intro_cluster),
                "is_outro":         (c == outro_cluster),
            }
        summary[c]["occurrences"] += 1
        summary[c]["total_duration_s"] = round(
            summary[c]["total_duration_s"] + s["duration_s"], 2
        )
    return summary


def _build_interpretation_notes(sections: list, cluster_summary: dict) -> list:
    """Notes textuelles pour faciliter l'interpretation par Claude."""
    notes = []
    if not sections or not cluster_summary:
        return notes

    intro_cluster = sections[0]["cluster"]
    intro_summary = cluster_summary.get(intro_cluster, {})

    # Cas frequent (AYGGMW, Hysteria, etc.) : intro = riff signature qui revient
    if intro_summary.get("occurrences", 0) >= 2:
        n = intro_summary["occurrences"]
        notes.append(
            f"Le cluster '{intro_cluster}' (intro) apparait {n} fois au total — "
            f"probablement le riff signature recurrent (intro + transitions + outro). "
            f"L'heuristique le labellise 'chorus_N' apres l'intro, mais il peut s'agir "
            f"de 'instrumental' ou 'riff_return' selon le morceau."
        )

    # Detection des mini-segments restants (< 10s) qui peuvent etre des transitions
    short_segments = [i for i, s in enumerate(sections)
                      if s["duration_s"] < 10.0 and i not in (0, len(sections) - 1)]
    if short_segments:
        notes.append(
            f"Segments courts (<10s) detectes en positions {short_segments} : "
            f"peuvent etre des transitions/pre-chorus plutot que de vraies sections."
        )

    # Si un cluster n'apparait qu'une fois au milieu, c'est probablement un bridge
    singletons_middle = [c for c, info in cluster_summary.items()
                         if info["occurrences"] == 1
                         and not info["is_intro"]
                         and not info["is_outro"]]
    if singletons_middle:
        notes.append(
            f"Clusters singleton dans le milieu : {singletons_middle} — "
            f"souvent des bridges ou sections uniques."
        )

    return notes


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
    Heuristique de labellisation (avec niveau de certitude par label).

    Regles :
    - 1ere section = "intro" (high)
    - derniere section : si meme cluster que chorus → "chorus_N_outro" (medium),
                        sinon → "outro" (high)
    - Analyse du milieu (hors intro/outro) :
      * cluster le plus frequent en milieu → "chorus_N" (high si >=2 occurrences,
                                                         medium sinon)
      * 2eme cluster le plus frequent → "verse_N" (medium)
      * clusters singletons → "bridge_N" (low)

    Retourne : liste de tuples (label, certainty) ou certainty in {"high","medium","low"}.
    """
    if not sections:
        return []

    if len(sections) == 1:
        return [("main", "low")]

    if len(sections) == 2:
        return [("intro", "high"), ("outro", "high")]

    # Analyse du milieu (exclut la 1ere et la derniere section)
    middle = sections[1:-1]
    middle_counts = Counter(s["cluster"] for s in middle)
    ranked = [c for c, _ in middle_counts.most_common()]
    chorus_cluster = ranked[0] if len(ranked) >= 1 else None
    verse_cluster = ranked[1] if len(ranked) >= 2 else None

    chorus_count = middle_counts.get(chorus_cluster, 0)
    verse_count = middle_counts.get(verse_cluster, 0) if verse_cluster else 0

    results = []
    counts = {"verse": 0, "chorus": 0, "bridge": 0}

    for i, s in enumerate(sections):
        c = s["cluster"]
        is_first = (i == 0)
        is_last = (i == len(sections) - 1)

        if is_first:
            results.append(("intro", "high"))
        elif is_last:
            if c == chorus_cluster and chorus_count >= 2:
                counts["chorus"] += 1
                results.append((f"chorus_{counts['chorus']}_outro", "medium"))
            else:
                results.append(("outro", "high"))
        elif c == chorus_cluster and chorus_count >= 2:
            counts["chorus"] += 1
            certainty = "high" if chorus_count >= 3 else "medium"
            results.append((f"chorus_{counts['chorus']}", certainty))
        elif c == verse_cluster and verse_count >= 2:
            counts["verse"] += 1
            results.append((f"verse_{counts['verse']}", "medium"))
        else:
            counts["bridge"] += 1
            results.append((f"bridge_{counts['bridge']}", "low"))

    return results
