"""
catalog.py
Catalogue dynamique des modèles HX Effects.

Source de vérité :
  - HX_ModelCatalog.json   : liste officielle des modèles + paramètres
  - HelixControls.json     : formats et plages de valeurs (validation)
  - HX_Effects.hls (réf.)  : valeurs par défaut observées dans les presets

Filtres appliqués pour HX Effects :
  - Garde uniquement Mono + Legacy (pas Stereo)
  - Exclut Amp/Cab/Preamp/IR (HX Effects ne fait pas d'amp modeling)

Exposition :
  - load_catalog(catalog_path)        → dict {model_id: ModelInfo}
  - extract_defaults(hls_path)        → dict {model_id: {param: value}}
  - build_full_catalog(...)           → fusion des deux + métadonnées
"""

import json
import base64
import zlib
from pathlib import Path
from dataclasses import dataclass, field

# ─────────────────────────────────────────────────────────
# CONFIG : ce qui est exclu pour le HX Effects
# ─────────────────────────────────────────────────────────
EXCLUDED_CATEGORIES = {"Amp", "Preamp", "Cab", "IR", "Connected Devices", "None"}
KEEP_SUBCATEGORIES  = {"Mono", "Legacy"}

# Catégories sans sous-cat à inclure
DIRECT_CATEGORIES = {"Input", "Output", "Split", "Merge"}

# Mapping catégorie → @type interne (observé dans les .hls)
CATEGORY_TYPE_ID = {
    "Distortion":  0,
    "Dynamics":    0,
    "EQ":          1,
    "Modulation":  2,
    "Pitch/Synth": 3,
    "Filter":      4,
    "Wah":         4,
    "Volume/Pan":  0,
    "Delay":       7,
    "Reverb":      7,
    "Send/Return": 7,
    "Looper":      7,
}


# ─────────────────────────────────────────────────────────
# DATACLASS
# ─────────────────────────────────────────────────────────

@dataclass
class ModelInfo:
    """Description d'un modèle d'effet."""
    id:           str            # ex: "HD2_DistRamsHead"
    name:         str            # ex: "Ram's Head"
    category:     str            # ex: "Distortion"
    subcategory:  str            # "Mono" / "Legacy" / ""
    type_id:      int            # @type interne
    param_names:  list[str]      # ordre officiel des paramètres
    defaults:     dict           # valeurs par défaut observées (peut être vide)

    def is_legacy(self) -> bool:
        return self.subcategory == "Legacy"

    def __str__(self):
        flag = " [Legacy]" if self.is_legacy() else ""
        return f"{self.name}{flag} ({self.category}) — {len(self.param_names)} params"


# ─────────────────────────────────────────────────────────
# CHARGEMENT DU CATALOGUE OFFICIEL
# ─────────────────────────────────────────────────────────

def load_catalog(catalog_path: str) -> dict[str, ModelInfo]:
    """
    Charge HX_ModelCatalog.json et retourne {model_id: ModelInfo}.
    Filtre automatiquement les catégories non pertinentes pour HX Effects.
    """
    with open(catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = {}

    for cat in data["categories"]:
        cat_name = cat.get("name")
        if cat_name in EXCLUDED_CATEGORIES:
            continue

        type_id = CATEGORY_TYPE_ID.get(cat_name, 7)

        # Catégories directes (Input/Output/Split/Merge)
        if "models" in cat:
            if cat_name not in DIRECT_CATEGORIES:
                continue
            for m in cat["models"]:
                info = _extract_model(m, cat_name, "", type_id)
                result[info.id] = info
            continue

        # Catégories avec sous-catégories
        for sub in cat.get("subcategories", []):
            sub_name = sub.get("name", "")
            if sub_name not in KEEP_SUBCATEGORIES:
                continue
            for m in sub.get("models", []):
                info = _extract_model(m, cat_name, sub_name, type_id)
                result[info.id] = info

    return result


def _extract_model(m: dict, category: str, subcategory: str,
                   type_id: int) -> ModelInfo:
    """Extrait un ModelInfo depuis l'entrée brute du catalogue."""
    # Les params sont une liste de dicts {nom: null}
    param_names = []
    for p in m.get("params", []):
        if isinstance(p, dict):
            for k in p.keys():
                param_names.append(k)
        elif isinstance(p, str):
            param_names.append(p)

    return ModelInfo(
        id=m["id"],
        name=m.get("name", m["id"]),
        category=category,
        subcategory=subcategory,
        type_id=type_id,
        param_names=param_names,
        defaults={},
    )


# ─────────────────────────────────────────────────────────
# EXTRACTION DES VALEURS PAR DÉFAUT depuis un .hls existant
# ─────────────────────────────────────────────────────────

def extract_defaults(hls_path: str) -> dict[str, dict]:
    """
    Parcourt tous les presets d'un .hls et collecte, pour chaque modèle,
    un échantillon de valeurs par défaut (premier exemple rencontré).

    Retourne : {model_id: {param_name: value, ...}, ...}
    """
    with open(hls_path, "r", encoding="utf-8") as f:
        outer = json.load(f)
    inner = json.loads(zlib.decompress(base64.b64decode(outer["encoded_data"])))

    defaults = {}
    extras   = {}   # @stereo, @trails, @no_snapshot_bypass

    for preset in inner.get("presets", []):
        if "tone" not in preset:
            continue
        for dsp_key in ("dsp0", "dsp1"):
            if dsp_key not in preset["tone"]:
                continue
            for block_key, block in preset["tone"][dsp_key].items():
                if not isinstance(block, dict):
                    continue
                model = block.get("@model")
                if not model:
                    continue

                # Première occurrence rencontrée → on prend ses valeurs
                if model in defaults:
                    continue

                params = {k: v for k, v in block.items()
                          if not k.startswith("@")}
                meta_extras = {k: v for k, v in block.items()
                               if k in ("@stereo", "@trails",
                                        "@no_snapshot_bypass")}

                defaults[model] = params
                extras[model]   = meta_extras

    return {"params": defaults, "extras": extras}


# ─────────────────────────────────────────────────────────
# CATALOGUE COMPLET (modèles + défauts fusionnés)
# ─────────────────────────────────────────────────────────

def build_full_catalog(model_catalog_path: str,
                       reference_hls: str = None) -> dict[str, ModelInfo]:
    """
    Construit le catalogue complet :
    - Liste des modèles depuis HX_ModelCatalog.json
    - Valeurs par défaut depuis un .hls de référence (optionnel)
    """
    catalog = load_catalog(model_catalog_path)

    if reference_hls and Path(reference_hls).exists():
        ext = extract_defaults(reference_hls)
        defaults_map = ext["params"]
        extras_map   = ext["extras"]

        for model_id, info in catalog.items():
            if model_id in defaults_map:
                info.defaults = dict(defaults_map[model_id])
                info.defaults["__extras__"] = extras_map.get(model_id, {})

    return catalog


# ─────────────────────────────────────────────────────────
# RECHERCHE / FILTRAGE
# ─────────────────────────────────────────────────────────

def search(catalog: dict, query: str) -> list[ModelInfo]:
    """Recherche par nom (insensible à la casse, partiel)."""
    q = query.lower().strip()
    matches = []
    for info in catalog.values():
        if q in info.name.lower() or q in info.id.lower():
            matches.append(info)
    return matches


def by_category(catalog: dict, category: str,
                include_legacy: bool = True) -> list[ModelInfo]:
    """Liste les modèles d'une catégorie."""
    result = []
    for info in catalog.values():
        if info.category != category:
            continue
        if not include_legacy and info.is_legacy():
            continue
        result.append(info)
    return sorted(result, key=lambda x: (x.is_legacy(), x.name))


def list_categories(catalog: dict) -> list[str]:
    """Liste les catégories présentes."""
    return sorted({m.category for m in catalog.values()})


def stats(catalog: dict) -> dict:
    """Statistiques du catalogue."""
    by_cat = {}
    for m in catalog.values():
        key = (m.category, m.subcategory)
        by_cat[key] = by_cat.get(key, 0) + 1
    with_defaults = sum(1 for m in catalog.values() if m.defaults)
    return {
        "total":         len(catalog),
        "with_defaults": with_defaults,
        "by_category":   by_cat,
    }


# ─────────────────────────────────────────────────────────
# TEST RAPIDE
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    catalog = build_full_catalog(
        "/mnt/user-data/uploads/HX_ModelCatalog.json",
        "/mnt/user-data/uploads/HX_Effects.hls"
    )

    s = stats(catalog)
    print(f"\n📦 {s['total']} modèles chargés "
          f"({s['with_defaults']} avec défauts observés)\n")

    # Test recherche
    print("=== Recherche 'rat' ===")
    for m in search(catalog, "rat"):
        print(f"  {m}")

    print("\n=== Recherche 'tube' ===")
    for m in search(catalog, "tube"):
        print(f"  {m}")

    print("\n=== Distortion (Mono uniquement) ===")
    for m in by_category(catalog, "Distortion", include_legacy=False)[:10]:
        print(f"  {m.name:<25} {m.id:<35} params: {m.param_names}")

    # Test détail d'un modèle
    print("\n=== Détail HD2_DistRamsHead ===")
    m = catalog["HD2_DistRamsHead"]
    print(f"  Nom        : {m.name}")
    print(f"  Catégorie  : {m.category} / {m.subcategory}")
    print(f"  Params     : {m.param_names}")
    print(f"  Défauts    : {m.defaults}")
