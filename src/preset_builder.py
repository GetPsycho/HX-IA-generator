"""
preset_builder.py
Construit un preset HX Effects a partir du catalogue officiel.

Usage :
    from preset_builder import PresetBuilder, get_catalog

    pb = PresetBuilder("Smells LT Spirit", tempo=116.0)
    pb.add_block("HD2_GateNoiseGate",    slot=0)
    pb.add_block("HD2_DistVerminDist",   slot=1)
    pb.add_block("HD2_DelaySimpleDelay", slot=2)
    pb.add_block("HD2_ReverbGanymede",   slot=3)

    pb.add_snapshot(0, "Intro",   blocks_on=[0, 3])
    pb.add_snapshot(1, "Couplet", blocks_on=[0, 1, 3], params={1: {"Gain": 0.55}})

    preset = pb.build()
"""

import copy
from pathlib import Path
import catalog as cat_module


_CATALOG = None
_ROOT = Path(__file__).parent.parent
_CATALOG_PATH = str(_ROOT / "data" / "models_catalog.json")


def get_catalog(catalog_path: str = None) -> dict:
    """Retourne le catalogue (charge une seule fois)."""
    global _CATALOG
    if _CATALOG is None:
        _CATALOG = cat_module.build_full_catalog(catalog_path or _CATALOG_PATH)
    return _CATALOG


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
]

MAX_BLOCKS    = 8
MAX_SNAPSHOTS = 4   # HX Effects : 4 snapshots max

# Categories dont les blocs ont un champ @trails
_TRAILS_CATEGORIES = {"delay", "reverb", "sendreturn"}


def make_block(model_id: str, position: int, path: int = 0,
               enabled: bool = True, overrides: dict = None) -> dict:
    """
    Construit un bloc a partir d'un model_id officiel.
    Les valeurs par defaut viennent directement de models_catalog.json.
    """
    catalog = get_catalog()

    if model_id not in catalog:
        suggestions = cat_module.search(catalog, model_id)[:5]
        msg = f"Modele inconnu : '{model_id}'."
        if suggestions:
            msg += "\nPeut-etre :\n" + "\n".join(
                f"   - {m.id}  ({m.name})" for m in suggestions)
        raise ValueError(msg)

    info = catalog[model_id]

    block = {
        "@enabled":            enabled,
        "@model":              model_id,
        "@no_snapshot_bypass": False,
        "@path":               path,
        "@position":           position,
        "@stereo":             False,
        "@type":               info.type_id,
    }

    # Les blocs delay/reverb/sendreturn ont un flag @trails
    if info.category in _TRAILS_CATEGORIES:
        block["@trails"] = False

    for p in info.params:
        block[p.id] = p.default

    if overrides:
        valid_ids = {p.id for p in info.params}
        for k, v in overrides.items():
            if k not in valid_ids and not k.startswith("@"):
                print(f"WARNING: parametre '{k}' non documente pour {model_id} "
                      f"(officiels : {info.param_ids()})")
            block[k] = v

    return block


class PresetBuilder:

    def __init__(self, name: str, tempo: float = 120.0):
        self.name         = name.strip()[:32]
        self.tempo        = tempo
        self._blocks      = {}   # slot -> bloc dict
        self._block_models = {}  # slot -> model_id
        self._snapshots   = {}   # idx  -> snapshot def

    def add_block(self, model_id: str, slot: int,
                  enabled_default: bool = True,
                  overrides: dict = None) -> "PresetBuilder":
        if not (0 <= slot < MAX_BLOCKS):
            raise ValueError(f"Slot invalide : {slot}")
        block = make_block(model_id, position=slot + 1,
                           enabled=enabled_default, overrides=overrides)
        self._blocks[slot]       = block
        self._block_models[slot] = model_id
        return self

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

        catalog = get_catalog()
        if params:
            for slot, ovr in params.items():
                if slot not in self._block_models:
                    print(f"WARNING: snapshot '{name}' : slot {slot} sans bloc")
                    continue
                model_id = self._block_models[slot]
                info = catalog[model_id]
                for p_name, value in ovr.items():
                    p = info.param(p_name)
                    if p is None:
                        print(f"WARNING: snapshot '{name}', slot {slot} ({info.name}) : "
                              f"param '{p_name}' inconnu. Disponibles : {info.param_ids()}")
                    elif isinstance(p.min, (int, float)) and isinstance(value, (int, float)):
                        if not (p.min <= value <= p.max):
                            print(f"WARNING: {p_name}={value} hors bornes "
                                  f"[{p.min}..{p.max}] pour {model_id} ({p.display_type})")

        self._snapshots[index] = {
            "name":         name.strip()[:16],
            "led":          led,
            "blocks_state": blocks_state,
            "params":       params or {},
            "tempo":        tempo if tempo is not None else self.tempo,
        }
        return self

    def build(self) -> dict:
        tone = {}

        # dsp0 : split + blocs utilisateur + join + inputs/outputs
        dsp0 = {}
        dsp0["split"] = {
            "@enabled":            True,
            "@model":              "HD2_AppDSPFlowSplitY",
            "@no_snapshot_bypass": False,
            "@position":           0,
            "BalanceA":            0.5,
            "BalanceB":            0.5,
            "bypass":              False,
        }
        for slot, block in self._blocks.items():
            dsp0[f"block{slot}"] = copy.deepcopy(block)
        dsp0["join"] = {
            "@enabled":            True,
            "@model":              "HD2_AppDSPFlowJoin",
            "@no_snapshot_bypass": False,
            "@position":           9,
            "A Level":             0.0,
            "A Pan":               0.5,
            "B Level":             0.0,
            "B Pan":               0.5,
            "B Polarity":          False,
            "Level":               0.0,
        }
        dsp0["inputA"]  = {"@input": 1, "@model": "HelixFx_AppDSPFlowInput"}
        dsp0["inputB"]  = {"@input": 0, "@model": "HelixFx_AppDSPFlowInput"}
        dsp0["outputA"] = {"@model": "HelixFx_AppDSPFlowOutput", "@output": 1,
                           "gain": 0.0, "pan": 0.5}
        dsp0["outputB"] = {"@model": "HelixFx_AppDSPFlowOutput", "@output": 0,
                           "gain": 0.0, "pan": 0.5}
        tone["dsp0"] = dsp0

        # dsp1 : vide pour HX Effects
        tone["dsp1"] = {}

        tone["global"] = {
            "@DtSelect": 2, "@PowercabMode": 0, "@PowercabSelect": 2,
            "@PowercabVoicing": 0, "@current_snapshot": 0,
            "@cursor_dsp": 0, "@cursor_group": "block0",
            "@cursor_path": 0, "@cursor_position": 1,
            "@guitarinputZ": 0, "@guitarpad": 0,
            "@model": "@global_params", "@pedalstate": 0,
            "@tempo": self.tempo, "@topology0": "A", "@topology1": 0,
        }

        # Params qui varient entre snapshots -> doivent etre declares dans tone.controller
        catalog = get_catalog()
        snap_controlled = {}  # (slot, pname) -> ParamInfo or None
        for snap_def in self._snapshots.values():
            for slot, overrides in snap_def["params"].items():
                model_id = self._block_models[slot]
                info = catalog[model_id]
                for pname in overrides:
                    key = (slot, pname)
                    if key not in snap_controlled:
                        snap_controlled[key] = info.param(pname)

        controller_dsp0 = {}
        for (slot, pname), p_info in snap_controlled.items():
            block_key = f"block{slot}"
            if block_key not in controller_dsp0:
                controller_dsp0[block_key] = {}
            if p_info is None:
                pmin, pmax = 0.0, 1.0
            elif isinstance(p_info.min, bool):
                pmin, pmax = False, True
            else:
                pmin, pmax = float(p_info.min), float(p_info.max)
            controller_dsp0[block_key][pname] = {
                "@controller":        10,
                "@max":               pmax,
                "@min":               pmin,
                "@snapshot_disable":  False,
            }

        tone["controller"] = {"dsp0": controller_dsp0}

        # Valeurs de base des blocs (pour les snapshots qui ne specifient pas un param controle)
        block_base_params = {
            slot: {k: v for k, v in block.items() if not k.startswith("@")}
            for slot, block in self._blocks.items()
        }

        # 4 snapshots (limite hardware HX Effects)
        for idx in range(MAX_SNAPSHOTS):
            if idx in self._snapshots:
                tone[f"snapshot{idx}"] = _build_snapshot(
                    self._snapshots[idx], dsp0, snap_controlled, block_base_params
                )
            else:
                tone[f"snapshot{idx}"] = _empty_snapshot(idx)
        tone["variax"]     = {}

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
            flag = " [Legacy]" if info.is_legacy() else ""
            lines.append(f"  [{slot}] {state}  {info.name}{flag} ({info.category})")

        lines.append("\nSNAPSHOTS :")
        for idx in range(MAX_SNAPSHOTS):
            if idx in self._snapshots:
                snap = self._snapshots[idx]
                on_slots = [s for s, v in snap["blocks_state"].items() if v]
                lines.append(f"  [{idx}] {snap['name']:<16} actifs: {on_slots}")
        return "\n".join(lines)


def _build_snapshot(snap_def: dict, dsp0_blocks: dict,
                    snap_controlled: dict, block_base_params: dict) -> dict:
    blocks_dsp0 = {}
    for block_key in dsp0_blocks:
        if not block_key.startswith("block"):
            continue
        slot = int(block_key.replace("block", ""))
        blocks_dsp0[block_key] = snap_def["blocks_state"].get(slot, False)

    # Valeurs explicitement definies pour ce snapshot
    explicit = {}  # (slot, pname) -> value
    for slot, overrides in snap_def["params"].items():
        for pname, value in overrides.items():
            explicit[(slot, pname)] = value

    # Tous les params declares dans tone.controller doivent avoir une valeur
    # dans chaque snapshot (valeur explicite ou valeur de base du bloc)
    controllers_dsp0 = {}
    for (slot, _pname), _ in snap_controlled.items():
        block_key = f"block{slot}"
        if block_key not in dsp0_blocks:
            continue
        if block_key not in controllers_dsp0:
            controllers_dsp0[block_key] = {}

    for (slot, pname), _ in snap_controlled.items():
        block_key = f"block{slot}"
        if block_key not in dsp0_blocks:
            continue
        if (slot, pname) in explicit:
            value = explicit[(slot, pname)]
        else:
            value = block_base_params.get(slot, {}).get(pname, 0.0)
        controllers_dsp0[block_key][pname] = {"@fs_enabled": False, "@value": value}

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
        fs_dsp0[f"block{slot}"] = {
            "@fs_enabled":   block.get("@enabled", False),
            "@fs_index":     slot,
            "@fs_label":     info.name[:12],
            "@fs_ledcolor":  DEFAULT_SNAPSHOT_COLORS[slot % len(DEFAULT_SNAPSHOT_COLORS)],
            "@fs_momentary": False,
            "@fs_primary":   True,
        }
    return {"dsp0": fs_dsp0}
