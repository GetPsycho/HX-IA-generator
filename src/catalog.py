"""
catalog.py
Catalogue des modeles HX Effects depuis models_catalog.json.

Source de verite : data/models_catalog.json
  - 403 modeles, vraies valeurs min/max/default/displayType par parametre
  - Filtrage : preamp exclu (non disponible sur HX Effects)

API publique :
  build_full_catalog(models_catalog_path) -> dict {model_id: ModelInfo}
  search(catalog, query)                  -> list[ModelInfo]
  by_category(catalog, category)          -> list[ModelInfo]
  list_categories(catalog)               -> list[str]
  stats(catalog)                         -> dict
"""

import json
from pathlib import Path
from dataclasses import dataclass

EXCLUDED_CATEGORIES = {"preamp"}

CATEGORY_TYPE_ID = {
    "distortion":  0,
    "compressor":  0,
    "gate":        0,
    "eq":          1,
    "modulation":  2,
    "pitch-synth": 3,
    "filter":      4,
    "wah":         4,
    "volumepan":   0,
    "delay":       7,
    "reverb":      7,
    "sendreturn":  7,
    "fixed":       7,
    "io":          7,
}

_LEGACY_MARKERS = ("_DM4", "_MM4", "_DL4", "_FM4", "_M13", "_M1380")


@dataclass
class ParamInfo:
    id:           str
    name:         str
    display_type: str
    min:          object  # float ou bool selon le param
    max:          object
    default:      object


@dataclass
class ModelInfo:
    id:       str
    name:     str
    category: str
    type_id:  int
    params:   list  # list[ParamInfo]

    def is_legacy(self) -> bool:
        return any(m in self.id for m in _LEGACY_MARKERS)

    def param(self, param_id: str):
        """Retourne le ParamInfo pour un param_id, ou None."""
        for p in self.params:
            if p.id == param_id:
                return p
        return None

    def param_ids(self) -> list:
        return [p.id for p in self.params]

    def __str__(self):
        flag = " [Legacy]" if self.is_legacy() else ""
        return f"{self.name}{flag} ({self.category}) -- {len(self.params)} params"


def build_full_catalog(models_catalog_path: str) -> dict:
    """
    Charge models_catalog.json et retourne {model_id: ModelInfo}.
    Filtre la categorie 'preamp' (non disponible sur HX Effects).
    """
    with open(models_catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = {}
    for model_id, entry in data.items():
        cat = entry.get("category", "")
        if cat in EXCLUDED_CATEGORIES:
            continue
        params = [
            ParamInfo(
                id=p["id"],
                name=p["name"],
                display_type=p.get("displayType", ""),
                min=p["min"],
                max=p["max"],
                default=p["default"],
            )
            for p in entry.get("params", [])
        ]
        result[model_id] = ModelInfo(
            id=model_id,
            name=entry["name"],
            category=cat,
            type_id=CATEGORY_TYPE_ID.get(cat, 7),
            params=params,
        )

    return result


def search(catalog: dict, query: str) -> list:
    """Recherche par nom ou ID (insensible a la casse, partiel)."""
    q = query.lower().strip()
    return [
        info for info in catalog.values()
        if q in info.name.lower() or q in info.id.lower()
    ]


def by_category(catalog: dict, category: str) -> list:
    """Liste les modeles d'une categorie, tries par (legacy, nom)."""
    return sorted(
        (m for m in catalog.values() if m.category == category),
        key=lambda x: (x.is_legacy(), x.name),
    )


def list_categories(catalog: dict) -> list:
    """Liste les categories presentes."""
    return sorted({m.category for m in catalog.values()})


def stats(catalog: dict) -> dict:
    by_cat = {}
    for m in catalog.values():
        by_cat[m.category] = by_cat.get(m.category, 0) + 1
    return {"total": len(catalog), "by_category": by_cat}


if __name__ == "__main__":
    _root = Path(__file__).parent.parent
    catalog = build_full_catalog(str(_root / "data" / "catalog" / "models_catalog.json"))

    s = stats(catalog)
    print(f"\n{s['total']} modeles charges\n")
    for cat, n in sorted(s["by_category"].items()):
        print(f"  {cat:<15} {n}")

    print("\n=== Recherche 'vermin' ===")
    for m in search(catalog, "vermin"):
        print(f"  {m}")
        for p in m.params:
            print(f"    {p.id:<20} {p.display_type:<25} [{p.min}..{p.max}]  def={p.default}")

    print("\n=== Distortion (5 premiers) ===")
    for m in by_category(catalog, "distortion")[:5]:
        print(f"  {m.name:<25} {m.id}")
