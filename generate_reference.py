"""
generate_reference.py
Genere REFERENCE.md : liste de tous les effets HX Effects avec
leurs parametres officiels (min, max, default, displayType).
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent
sys.path.insert(0, str(_ROOT / "src"))

from catalog import build_full_catalog, by_category, list_categories


CATEGORY_ORDER = [
    "distortion", "compressor", "gate", "eq", "modulation", "delay", "reverb",
    "pitch-synth", "filter", "wah", "volumepan", "sendreturn", "fixed", "io",
]

CATEGORY_LABELS = {
    "distortion":  "Distortion",
    "compressor":  "Dynamics",
    "gate":        "Gate",
    "eq":          "EQ",
    "modulation":  "Modulation",
    "delay":       "Delay",
    "reverb":      "Reverb",
    "pitch-synth": "Pitch/Synth",
    "filter":      "Filter",
    "wah":         "Wah",
    "volumepan":   "Volume/Pan",
    "sendreturn":  "Send/Return",
    "fixed":       "Fixed",
    "io":          "I/O",
}


def generate(catalog: dict, output_path: str) -> None:
    lines = []
    lines.append("# HX Effects -- Reference des modeles\n")
    lines.append("Liste generee automatiquement depuis `models_catalog.json`\n")
    lines.append("(preamp exclus -- non disponible sur HX Effects)\n")

    total = len(catalog)
    lines.append(f"**Total : {total} modeles**\n")

    lines.append("## Sommaire\n")
    for cat in CATEGORY_ORDER:
        items = by_category(catalog, cat)
        if not items:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        n_modern = sum(1 for m in items if not m.is_legacy())
        n_legacy = sum(1 for m in items if m.is_legacy())
        anchor = label.lower().replace("/", "").replace(" ", "-")
        lines.append(f"- [{label}](#{anchor}) -- {n_modern} modernes, {n_legacy} legacy")
    lines.append("")

    for cat in CATEGORY_ORDER:
        items = by_category(catalog, cat)
        if not items:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"## {label}\n")
        lines.append("| Nom | Model ID | Parametre | Type | Min | Max | Default |")
        lines.append("|---|---|---|---|---|---|---|")

        for m in items:
            flag = " [L]" if m.is_legacy() else ""
            if not m.params:
                lines.append(f"| {m.name}{flag} | `{m.id}` | _(aucun)_ | | | | |")
                continue
            for i, p in enumerate(m.params):
                name_col = f"{m.name}{flag}" if i == 0 else ""
                id_col   = f"`{m.id}`"       if i == 0 else ""
                lines.append(
                    f"| {name_col} | {id_col} | `{p.id}` | {p.display_type} "
                    f"| {p.min} | {p.max} | {p.default} |"
                )

        lines.append("")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Reference ecrite : {output_path}")
    print(f"   {total} modeles documentes")


if __name__ == "__main__":
    catalog = build_full_catalog(
        str(_ROOT / "data" / "catalog" / "models_catalog.json"),
    )
    generate(catalog, str(_ROOT / "REFERENCE.md"))
