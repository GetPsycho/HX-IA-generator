"""
generate_reference.py
Génère REFERENCE.md : un document listant tous les effets disponibles
sur HX Effects avec leurs paramètres officiels.
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).parent
sys.path.insert(0, str(_ROOT / "src"))

from catalog import build_full_catalog, by_category, list_categories


CATEGORY_ORDER = [
    "Distortion", "Dynamics", "EQ", "Modulation", "Delay", "Reverb",
    "Pitch/Synth", "Filter", "Wah", "Volume/Pan", "Send/Return", "Looper",
    "Input", "Output", "Split", "Merge",
]


def generate(catalog: dict, output_path: str) -> None:
    lines = []
    lines.append("# HX Effects — Référence des modèles\n")
    lines.append("Liste générée automatiquement depuis `HX_ModelCatalog.json`\n")
    lines.append("(modèles Mono + Legacy uniquement — Stereo et Amp/Cab/Preamp/IR exclus)\n")

    lines.append(f"**Total : {len(catalog)} modèles**\n")

    # Stats par catégorie
    lines.append("## Sommaire\n")
    for cat in CATEGORY_ORDER:
        items = by_category(catalog, cat)
        if not items:
            continue
        n_mono   = sum(1 for m in items if not m.is_legacy())
        n_legacy = sum(1 for m in items if m.is_legacy())
        anchor = cat.lower().replace("/", "").replace(" ", "-")
        lines.append(f"- [{cat}](#{anchor}) — {n_mono} mono, {n_legacy} legacy")
    lines.append("")

    # Détails par catégorie
    for cat in CATEGORY_ORDER:
        items = by_category(catalog, cat)
        if not items:
            continue

        lines.append(f"## {cat}\n")
        lines.append("| Nom affiché | Model ID | Sub | Paramètres |")
        lines.append("|---|---|---|---|")

        for m in items:
            sub = "Legacy" if m.is_legacy() else "Mono"
            params = ", ".join(f"`{p}`" for p in m.param_names)
            params = params or "_(aucun)_"
            obs = " ✓" if m.defaults else ""
            lines.append(f"| {m.name}{obs} | `{m.id}` | {sub} | {params} |")
        lines.append("")
        lines.append("_✓ = valeurs par défaut observées dans HX_Effects.hls_\n")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Référence écrite : {output_path}")
    print(f"   {len(catalog)} modèles documentés")


if __name__ == "__main__":
    catalog = build_full_catalog(
        str(_ROOT / "data" / "HX_ModelCatalog.json"),
        str(_ROOT / "data" / "HX Effects.hls"),
    )
    generate(catalog, str(_ROOT / "REFERENCE.md"))
