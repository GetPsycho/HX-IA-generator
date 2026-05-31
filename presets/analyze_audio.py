"""
analyze_audio.py
Lance le pipeline d'analyse audio sur un fichier et sauvegarde le rapport
dans audio_analysis/<nom>_analysis.json.

USAGE :
  python presets/analyze_audio.py <chemin_audio>
  python presets/analyze_audio.py "songs/Hysteria.mp3"

Le rapport JSON peut ensuite etre lu par le skill /new-preset pour enrichir
l'analyse (tonalite, BPM, sections, effets selon la version du pipeline).
"""

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from audio_analysis import analyze_file

ANALYSIS_DIR = _ROOT / "audio_analysis"


def _fmt_time(seconds: float) -> str:
    """Format mm:ss"""
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    audio_path = sys.argv[1]
    print(f"Analyse en cours : {audio_path}")
    print("(librosa charge le fichier, calcul chromagram + tempo — ~10-30s selon duree)")

    try:
        result = analyze_file(audio_path)
    except FileNotFoundError as e:
        print(f"ERREUR : {e}")
        sys.exit(1)

    # Affichage console resume
    print()
    print("=" * 65)
    print(f"  Rapport d'analyse audio  (pipeline v{result['pipeline_version']})")
    print("=" * 65)
    print(f"  Fichier  : {result['filename']}")
    print(f"  Duree    : {result['duration_s']:.1f}s")
    print(f"  Tonalite : {result['key']['name_fr']:<15} "
          f"(confiance {result['key']['confidence']:.2f}, "
          f"score {result['key']['score']:.2f})")
    # Top-3 alternatives si confidence faible
    alts = result['key'].get('alternatives')
    if alts:
        print(f"             confidence faible -> top {len(alts)} candidats :")
        for a in alts:
            print(f"               - {a['name_fr']:<15} (score {a['score']:.3f})")
    print(f"  Tempo    : {result['tempo']['bpm']:.1f} BPM   "
          f"(arrondi : {result['tempo']['bpm_int']})")
    # Alternatives /2 et *2 (utile car librosa confond moitie/double)
    if 'alternatives' in result['tempo']:
        alts_bpm = result['tempo']['alternatives']
        print(f"             alternatives : {alts_bpm[0]:.1f} BPM (/2) ou "
              f"{alts_bpm[1]:.1f} BPM (x2)")
    if 'note' in result['tempo']:
        print(f"             {result['tempo']['note']}")
    print(f"  Beats    : {result['tempo']['n_beats']}")
    sections_info = result.get("sections", {})
    segments = sections_info.get("segments", []) if isinstance(sections_info, dict) else []
    if segments:
        print()
        print(f"  Sections detectees ({len(segments)}) :")
        for i, s in enumerate(segments):
            start = _fmt_time(s["start"])
            end = _fmt_time(s["end"])
            dur = s["duration_s"]
            cert = s.get("label_certainty", "?")
            print(f"    [{i}] {start} -> {end} ({dur:>5.1f}s) "
                  f"cluster={s['cluster']}  label={s['label']:<20} [{cert}]")

        # Resume des clusters
        cluster_summary = sections_info.get("cluster_summary", {})
        if cluster_summary:
            print()
            print("  Resume des clusters :")
            for c, info in sorted(cluster_summary.items()):
                tags = []
                if info.get("is_intro"):
                    tags.append("intro")
                if info.get("is_outro"):
                    tags.append("outro")
                tag_str = f" [{', '.join(tags)}]" if tags else ""
                print(f"    {c} : {info['occurrences']}x  "
                      f"total {info['total_duration_s']:.1f}s{tag_str}")

        # Notes interpretatives
        notes = sections_info.get("notes", [])
        if notes:
            print()
            print("  Notes interpretatives :")
            for note in notes:
                print(f"    - {note}")

    # ----- Effets (v3.2) -----
    effects = result.get("effects")
    if effects:
        print()
        print(f"  Effets (source : {result.get('effects_source', '?')}) :")

        sat = effects.get("saturation", {})
        if sat:
            print(f"    Saturation : {sat.get('level_label', '?'):<10} "
                  f"(score {sat.get('level_0_1', 0):.2f})")

        comp = effects.get("compression", {})
        if comp:
            print(f"    Compression: {comp.get('level', '?'):<10} "
                  f"(crest {comp.get('crest_factor_db', 0):.1f} dB, "
                  f"DR {comp.get('dynamic_range_db', 0):.1f} dB)")

        eq = effects.get("eq", {})
        if eq:
            bands = eq.get("bands_db", {})
            print(f"    EQ balance : {eq.get('balance', '?')}")
            for b in ("low", "low_mid", "mid", "high_mid", "high"):
                if b in bands:
                    sign = "+" if bands[b] >= 0 else ""
                    print(f"      {b:<9}: {sign}{bands[b]:.1f} dB")

        dly = effects.get("delay", {})
        if dly:
            if dly.get("detected"):
                print(f"    Delay      : detecte ~{dly.get('time_ms', 0):.0f} ms "
                      f"(force {dly.get('peak_strength', 0):.2f}, "
                      f"confiance {dly.get('confidence', 0):.2f})")
            else:
                print(f"    Delay      : non detecte")

        mod = effects.get("modulation", {})
        if mod:
            if mod.get("detected"):
                print(f"    Modulation : {mod.get('type', '?'):<8} "
                      f"rate {mod.get('rate_hz', 0):.2f} Hz, "
                      f"depth {mod.get('depth_0_1', 0):.2f} "
                      f"(confiance {mod.get('confidence', 0):.2f})")
            else:
                print(f"    Modulation : non detectee")

        rev = effects.get("reverb", {})
        if rev:
            if rev.get("detected"):
                print(f"    Reverb     : RT60 ~{rev.get('rt60_s', 0):.2f}s, "
                      f"wet ~{rev.get('wet_estimate_0_1', 0):.2f} "
                      f"({rev.get('n_decays_analyzed', 0)} onsets, "
                      f"confiance {rev.get('confidence', 0):.2f})")
            else:
                print(f"    Reverb     : non detectee/courte")

    # Section-by-section effects
    section_effects = result.get("section_effects", [])
    if section_effects:
        print()
        print("  Effets par section (intensite / saturation / EQ) :")
        for se in section_effects:
            label = se.get("label", "?")
            cluster = se.get("cluster", "?")
            start_t = _fmt_time(se.get("start", 0))
            end_t = _fmt_time(se.get("end", 0))
            intensity = se.get("intensity", "?")
            rms_ratio = se.get("rms_ratio", 0)
            int_str = f"int={intensity:<10}({rms_ratio:.2f})"
            effects = se.get("effects")
            if effects is None:
                reason = se.get("skip_reason", "?")
                print(f"    [{cluster}] {label:<20} {start_t}->{end_t} : {int_str}  SKIP ({reason})")
                continue
            sat = effects.get("saturation", {})
            eq = effects.get("eq", {})
            sat_str = f"sat={sat.get('level_label', '?'):<8}({sat.get('level_0_1', 0):.2f})"
            eq_str = f"eq={eq.get('balance', '?')}"
            src = se.get("effects_source", "guitar_stem")
            src_tag = " [MIX]" if src == "full_mix_fallback" else ""
            print(f"    [{cluster}] {label:<20} {start_t}->{end_t} : "
                  f"{int_str}  {sat_str}  {eq_str}{src_tag}")

    print("=" * 65)

    # Sauvegarde JSON
    ANALYSIS_DIR.mkdir(exist_ok=True)
    out_name = Path(audio_path).stem + "_analysis.json"
    out_path = ANALYSIS_DIR / out_name
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"\nRapport sauve : {out_path.relative_to(_ROOT)}")


if __name__ == "__main__":
    main()
