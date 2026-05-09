"""
preset_builder.py (v2)
Construit un preset HX Effects à partir du catalogue officiel.

Usage simple :
    from preset_builder import PresetBuilder, get_catalog

    cat = get_catalog()  # chargé une seule fois en mémoire

    pb = PresetBuilder("Smells LT Spirit", tempo=116.0)
    pb.add_block("HD2_GateNoiseGate", slot=0)
    pb.add_block("HD2_DistVerminDist", slot=1)   # ProCo Rat
    pb.add_block("HD2_DelaySimpleDelay", slot=2)
    pb.add_block("HD2_ReverbTile", slot=3)

    pb.add_snapshot(0, "Intro",   blocks_on=[0, 3])
    pb.add_snapshot(1, "Couplet", blocks_on=[0, 1, 3], params={1: {"Distortion": 0.5}})
    ...

    preset = pb.build()
"""

import copy
from pathlib import Path
import catalog as cat_module


# ─────────────────────────────────────────────────────────
# CHARGEMENT GLOBAL DU CATALOGUE (lazy, singleton)
# ─────────────────────────────────────────────────────────

_CATALOG = None
_ROOT = Path(__file__).parent.parent
_CATALOG_PATH  = str(_ROOT / "data" / "HX_ModelCatalog.json")
_REFERENCE_HLS = str(_ROOT / "data" / "HX Effects.hls")


def get_catalog(catalog_path: str = None, reference_hls: str = None) -> dict:
    """Retourne le catalogue (chargé une seule fois)."""
    global _CATALOG
    if _CATALOG is None:
        cp = catalog_path or _CATALOG_PATH
        rh = reference_hls or _REFERENCE_HLS
        _CATALOG = cat_module.build_full_catalog(cp, rh)
    return _CATALOG


# ─────────────────────────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────────────────────

LED_COLORS = {
    "off":    0,
    "red":    16711680,
    "green":  65408,
    "blue":   255,
    "yellow": 16776960,
    "orange": 16744448,
    "pink":   16711765,
    "white":  16777215,
    "cyan":   65535,
}

DEFAULT_SNAPSHOT_COLORS = [
    LED_COLORS["green"],
    LED_COLORS["yellow"],
    LED_COLORS["orange"],
    LED_COLORS["red"],
    LED_COLORS["cyan"],
    LED_COLORS["blue"],
    LED_COLORS["pink"],
    LED_COLORS["white"],
]

MAX_BLOCKS    = 8
MAX_SNAPSHOTS = 8


# ─────────────────────────────────────────────────────────
# DÉFAUTS HEURISTIQUES (quand non observés dans les presets)
# ─────────────────────────────────────────────────────────

def _guess_default(param_name: str):
    """Heuristique pour deviner une valeur par défaut raisonnable."""
    name = param_name.lower()

    # Booléens fréquents
    if name in ("bypass", "stereo", "trails", "polarity", "type",
                "tempo_sync", "tempo_sync1", "tempo_sync2", "volumetaper"):
        return False

    # Niveaux : 0 dB
    if name in ("level", "gain", "volume"):
        return 0.0
    if name in ("mix", "blend"):
        return 0.5

    # Fréquences
    if "highcut" in name or "high_cut" in name:
        return 8000.0
    if "lowcut" in name or "low_cut" in name:
        return 100.0

    # Time / Delay
    if "time" in name or "delay" in name:
        return 0.4

    # SyncSelect : 6 = quart de note (observé)
    if "syncselect" in name:
        return 6

    # Sélecteurs
    if "select" in name or "mode" in name or "version" in name:
        return 0

    # Par défaut : milieu de course
    return 0.5


# ─────────────────────────────────────────────────────────
# CONSTRUCTION D'UN BLOC
# ─────────────────────────────────────────────────────────

def make_block(model_id: str, position: int, path: int = 0,
               enabled: bool = True, overrides: dict = None) -> dict:
    """
    Construit un bloc à partir d'un model_id officiel.

    Le bloc est rempli avec :
      1. Les valeurs par défaut OBSERVÉES (depuis HX_Effects.hls de référence)
      2. À défaut, des valeurs heuristiques

    Surcharges utilisateur validées contre les paramètres officiels.
    """
    catalog = get_catalog()

    if model_id not in catalog:
        suggestions = cat_module.search(catalog, model_id)[:5]
        msg = f"Modèle inconnu : '{model_id}'."
        if suggestions:
            msg += "\nPeut-être :\n" + "\n".join(
                f"   - {m.id}  ({m.name})" for m in suggestions)
        raise ValueError(msg)

    info = catalog[model_id]

    block = {
        "@enabled":  enabled,
        "@model":    model_id,
        "@no_snapshot_bypass": False,
        "@path":     path,
        "@position": position,
        "@type":     info.type_id,
    }

    # Extras observés (@stereo, @trails…)
    extras = info.defaults.get("__extras__", {}) if info.defaults else {}
    for k, v in extras.items():
        block[k] = v

    # Paramètres : ordre officiel du catalogue
    for pname in info.param_names:
        if info.defaults and pname in info.defaults:
            block[pname] = info.defaults[pname]
        else:
            block[pname] = _guess_default(pname)

    # Surcharges utilisateur
    if overrides:
        for k, v in overrides.items():
            if k not in info.param_names and not k.startswith("@"):
                print(f"⚠️  Paramètre '{k}' non documenté pour {model_id} "
                      f"(officiels : {info.param_names})")
            block[k] = v

    return block


# ─────────────────────────────────────────────────────────
# PRESET BUILDER
# ─────────────────────────────────────────────────────────

class PresetBuilder:

    def __init__(self, name: str, tempo: float = 120.0):
        self.name      = name.strip()[:32]
        self.tempo     = tempo
        self._blocks   = {}      # slot → bloc dict
        self._block_models = {}  # slot → model_id
        self._snapshots = {}     # idx → snapshot def

    # ── BLOCS ─────────────────────────────────────────────

    def add_block(self, model_id: str, slot: int,
                  enabled_default: bool = True,
                  overrides: dict = None) -> "PresetBuilder":
        """Ajoute un effet par son model_id officiel (ex: 'HD2_DistRamsHead')."""
        if not (0 <= slot < MAX_BLOCKS):
            raise ValueError(f"Slot invalide : {slot}")

        block = make_block(model_id, position=slot + 1,
                           enabled=enabled_default, overrides=overrides)
        self._blocks[slot] = block
        self._block_models[slot] = model_id
        return self

    # ── SNAPSHOTS ─────────────────────────────────────────

    def add_snapshot(self, index: int, name: str,
                     blocks_on: list,
                     params: dict = None,
                     color=None,
                     tempo: float = None) -> "PresetBuilder":
        if not (0 <= index < MAX_SNAPSHOTS):
            raise ValueError(f"Index snapshot invalide : {index}")

        if color is None:
            led = DEFAULT_SNAPSHOT_COLORS[index % len(DEFAULT_SNAPSHOT_COLORS)]
        elif isinstance(color, str):
            led = LED_COLORS.get(color.lower(), 0)
        else:
            led = int(color)

        blocks_state = {slot: (slot in blocks_on) for slot in self._blocks}

        # Validation des params surchargés
        catalog = get_catalog()
        if params:
            for slot, ovr in params.items():
                if slot not in self._block_models:
                    print(f"⚠️  Snapshot '{name}' : slot {slot} sans bloc")
                    continue
                model_id = self._block_models[slot]
                info = catalog[model_id]
                for p_name in ovr:
                    if p_name not in info.param_names:
                        print(f"⚠️  Snapshot '{name}', slot {slot} ({info.name}) : "
                              f"param '{p_name}' inconnu. "
                              f"Disponibles : {info.param_names}")

        self._snapshots[index] = {
            "name":         name.strip()[:16],
            "led":          led,
            "blocks_state": blocks_state,
            "params":       params or {},
            "tempo":        tempo if tempo is not None else self.tempo,
        }
        return self

    # ── BUILD ─────────────────────────────────────────────

    def build(self) -> dict:
        tone = {}

        # 1. dsp0
        dsp0 = {}
        for slot, block in self._blocks.items():
            dsp0[f"block{slot}"] = copy.deepcopy(block)
        dsp0["inputA"]  = {"@model": "HelixFx_AppDSPFlowInput",  "@input": 1}
        dsp0["inputB"]  = {"@model": "HelixFx_AppDSPFlowInput",  "@input": 0}
        dsp0["outputA"] = {"@model": "HelixFx_AppDSPFlowOutput", "@output": 1,
                           "gain": 0.0, "pan": 0.5}
        dsp0["outputB"] = {"@model": "HelixFx_AppDSPFlowOutput", "@output": 0,
                           "gain": 0.0, "pan": 0.5}
        tone["dsp0"] = dsp0

        # 2. dsp1 minimal
        tone["dsp1"] = {
            "inputA":  {"@model": "HelixFx_AppDSPFlowInput",  "@input": 0},
            "outputA": {"@model": "HelixFx_AppDSPFlowOutput", "@output": 0,
                        "gain": 0.0, "pan": 0.5},
        }

        # 3. global
        tone["global"] = {
            "@DtSelect": 2, "@PowercabMode": 0, "@PowercabSelect": 2,
            "@PowercabVoicing": 0, "@current_snapshot": 0,
            "@cursor_dsp": 0, "@cursor_group": "block0",
            "@cursor_path": 0, "@cursor_position": 1,
            "@guitarinputZ": 0, "@guitarpad": 0,
            "@model": "@global_params", "@pedalstate": 0,
            "@tempo": self.tempo, "@topology0": "A", "@topology1": 0,
        }

        # 4. snapshots
        for idx in range(MAX_SNAPSHOTS):
            if idx in self._snapshots:
                tone[f"snapshot{idx}"] = _build_snapshot(
                    self._snapshots[idx], dsp0)
            else:
                tone[f"snapshot{idx}"] = _empty_snapshot(idx)

        # 5. footswitch
        tone["footswitch"]  = _build_footswitch(self._blocks, self._block_models)
        tone["controller"]  = {"dsp0": {}}
        tone["variax"]      = {}

        return {
            "device":         2162693,
            "device_version": 58720256,
            "meta":           {"build_sha": "d972399",
                               "name": f" {self.name} "},
            "tone":           tone,
        }

    def summary(self) -> str:
        catalog = get_catalog()
        lines = [f"\n{'='*55}",
                 f"PRESET : {self.name}  (tempo={self.tempo})",
                 "="*55, "\nBLOCS :"]
        for slot in sorted(self._blocks):
            model_id = self._block_models[slot]
            info = catalog[model_id]
            state = "ON " if self._blocks[slot].get("@enabled") else "OFF"
            tag = " [Legacy]" if info.is_legacy() else ""
            lines.append(f"  [{slot}] {state}  {info.name}{tag} ({info.category})")

        lines.append("\nSNAPSHOTS :")
        for idx in range(MAX_SNAPSHOTS):
            if idx in self._snapshots:
                snap = self._snapshots[idx]
                on_slots = [s for s, v in snap["blocks_state"].items() if v]
                lines.append(f"  [{idx}] {snap['name']:<16} actifs: {on_slots}")
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────
# HELPERS INTERNES
# ─────────────────────────────────────────────────────────

def _build_snapshot(snap_def: dict, dsp0_blocks: dict) -> dict:
    blocks_dsp0 = {}
    for block_key in dsp0_blocks:
        if not block_key.startswith("block"):
            continue
        slot = int(block_key.replace("block", ""))
        blocks_dsp0[block_key] = snap_def["blocks_state"].get(slot, False)

    controllers_dsp0 = {}
    for slot, overrides in snap_def["params"].items():
        block_key = f"block{slot}"
        if block_key not in dsp0_blocks:
            continue
        ctrl = {}
        for pname, value in overrides.items():
            ctrl[pname] = {"@fs_enabled": False, "@value": value}
        if ctrl:
            controllers_dsp0[block_key] = ctrl

    return {
        "@custom_name":  True,
        "@ledcolor":     snap_def["led"],
        "@name":         snap_def["name"],
        "@pedalstate":   0,
        "@tempo":        snap_def["tempo"],
        "@valid":        True,
        "blocks":        {"dsp0": blocks_dsp0},
        "controllers":   {"dsp0": controllers_dsp0},
    }


def _empty_snapshot(index: int) -> dict:
    return {
        "@custom_name": False,
        "@ledcolor":    0,
        "@name":        f"Snapshot {index+1}",
        "@pedalstate":  0,
        "@tempo":       120.0,
        "@valid":       False,
        "blocks":       {"dsp0": {}},
        "controllers":  {"dsp0": {}},
    }


def _build_footswitch(blocks: dict, models: dict) -> dict:
    catalog = get_catalog()
    fs_dsp0 = {}
    for slot, block in blocks.items():
        info = catalog[models[slot]]
        label = info.name[:12]
        fs_dsp0[f"block{slot}"] = {
            "@fs_enabled":   block.get("@enabled", False),
            "@fs_index":     slot,
            "@fs_label":     label,
            "@fs_ledcolor":  DEFAULT_SNAPSHOT_COLORS[slot % len(DEFAULT_SNAPSHOT_COLORS)],
            "@fs_momentary": False,
            "@fs_primary":   True,
        }
    return {"dsp0": fs_dsp0}


# ─────────────────────────────────────────────────────────
# TEST
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    pb = PresetBuilder("Smells LT Spirit", tempo=116.0)
    pb.add_block("HD2_GateNoiseGate",     slot=0)
    pb.add_block("HD2_DistVerminDist",    slot=1)  # ProCo Rat
    pb.add_block("HD2_Chorus",            slot=2)
    pb.add_block("HD2_DelaySimpleDelay",  slot=3)
    pb.add_block("HD2_ReverbTile",        slot=4)

    pb.add_snapshot(0, "Intro Clean",  blocks_on=[0, 4])
    pb.add_snapshot(1, "Couplet",      blocks_on=[0, 1, 2, 4],
                    params={1: {"Distortion": 0.55}})
    pb.add_snapshot(2, "Refrain",      blocks_on=[0, 1, 4],
                    params={1: {"Distortion": 0.75}})
    pb.add_snapshot(3, "Solo",         blocks_on=[0, 1, 3, 4],
                    params={1: {"Distortion": 0.80}})

    print(pb.summary())
    preset = pb.build()
    print("\n✅ Preset construit")
