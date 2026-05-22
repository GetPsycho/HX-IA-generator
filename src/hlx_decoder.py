"""
hlx_decoder.py
Decode un fichier .hlx en une representation structuree equivalente
a l'etat interne de PresetBuilder.

Permet de comparer le contenu d'un .hlx (modifie sur l'appareil/HX Edit)
avec le preset genere par le code Python source.
"""

import json


def decode_preset(filepath: str) -> dict:
    """
    Lit un .hlx et retourne une structure normalisee :

    {
      "name":   str,
      "tempo":  float,
      "blocks": {
        slot: {
          "model":   str,        # model_id
          "enabled": bool,       # @enabled initial (snap 0)
          "params":  {pname: value},   # tous les params SAUF @meta
          "trails":  bool | None,      # @trails si applicable
          "stereo":  bool | None,      # @stereo si applicable
        }
      },
      "snapshots": {
        idx: {
          "name":         str,
          "led":          int,
          "tempo":        float,
          "blocks_state": {slot: bool},
          "params":       {slot: {pname: value}},  # controlled params
        }
      },
      "exp_bindings": {(slot, pname): exp_id},     # @controller != 10
      "trails":      {slot: bool},                  # raw @trails par slot
    }
    """
    with open(filepath, "r", encoding="utf-8") as f:
        outer = json.load(f)
    tone = outer["data"]["tone"]
    name = outer["data"]["meta"].get("name", "").strip()

    # --- Tempo global ---
    tempo = float(tone.get("global", {}).get("@tempo", 120.0))

    # --- Blocs (dsp0.block*) ---
    blocks = {}
    trails = {}
    dsp0 = tone.get("dsp0", {})
    for key, val in dsp0.items():
        if not key.startswith("block"):
            continue
        slot = int(key.replace("block", ""))
        # Extraire les params utilisateur (tout sauf @meta)
        params = {k: v for k, v in val.items() if not k.startswith("@")}
        block_info = {
            "model":   val.get("@model"),
            "enabled": bool(val.get("@enabled", False)),
            "params":  params,
            "trails":  val.get("@trails") if "@trails" in val else None,
            "stereo":  val.get("@stereo") if "@stereo" in val else None,
        }
        blocks[slot] = block_info
        if "@trails" in val:
            trails[slot] = bool(val["@trails"])

    # --- Controllers (declarations + bindings EXP) ---
    exp_bindings = {}
    controller_dsp0 = tone.get("controller", {}).get("dsp0", {})
    for block_key, params_map in controller_dsp0.items():
        slot = int(block_key.replace("block", ""))
        for pname, ctrl_def in params_map.items():
            ctrl_id = ctrl_def.get("@controller", 10)
            if ctrl_id != 10:
                # Controller != snapshot -> EXP pedal binding
                exp_bindings[(slot, pname)] = int(ctrl_id)

    # --- Snapshots ---
    snapshots = {}
    for idx in range(4):
        snap = tone.get(f"snapshot{idx}", {})
        if not snap.get("@valid", False):
            continue
        # blocks_state
        blocks_dsp0 = snap.get("blocks", {}).get("dsp0", {})
        blocks_state = {}
        for block_key, state in blocks_dsp0.items():
            if block_key.startswith("block"):
                s = int(block_key.replace("block", ""))
                blocks_state[s] = bool(state)
        # params (controllers values)
        snap_controllers = snap.get("controllers", {}).get("dsp0", {})
        snap_params = {}
        for block_key, params_map in snap_controllers.items():
            s = int(block_key.replace("block", ""))
            for pname, pdef in params_map.items():
                snap_params.setdefault(s, {})[pname] = pdef.get("@value")

        snapshots[idx] = {
            "name":         snap.get("@name", f"Snapshot {idx+1}"),
            "led":          int(snap.get("@ledcolor", 0)),
            "tempo":        float(snap.get("@tempo", tempo)),
            "blocks_state": blocks_state,
            "params":       snap_params,
        }

    return {
        "name":         name,
        "tempo":        tempo,
        "blocks":       blocks,
        "snapshots":    snapshots,
        "exp_bindings": exp_bindings,
        "trails":       trails,
    }


def decode_built_preset(built: dict) -> dict:
    """
    Convertit un preset construit par PresetBuilder.build() en la meme
    structure normalisee que decode_preset(), pour comparaison directe.

    built : dict {device, device_version, meta, tone}
    """
    tone = built["tone"]
    name = built["meta"].get("name", "").strip()
    tempo = float(tone.get("global", {}).get("@tempo", 120.0))

    blocks = {}
    trails = {}
    for key, val in tone.get("dsp0", {}).items():
        if not key.startswith("block"):
            continue
        slot = int(key.replace("block", ""))
        params = {k: v for k, v in val.items() if not k.startswith("@")}
        blocks[slot] = {
            "model":   val.get("@model"),
            "enabled": bool(val.get("@enabled", False)),
            "params":  params,
            "trails":  val.get("@trails") if "@trails" in val else None,
            "stereo":  val.get("@stereo") if "@stereo" in val else None,
        }
        if "@trails" in val:
            trails[slot] = bool(val["@trails"])

    exp_bindings = {}
    for block_key, params_map in tone.get("controller", {}).get("dsp0", {}).items():
        slot = int(block_key.replace("block", ""))
        for pname, ctrl_def in params_map.items():
            ctrl_id = ctrl_def.get("@controller", 10)
            if ctrl_id != 10:
                exp_bindings[(slot, pname)] = int(ctrl_id)

    snapshots = {}
    for idx in range(4):
        snap = tone.get(f"snapshot{idx}", {})
        if not snap.get("@valid", False):
            continue
        blocks_dsp0 = snap.get("blocks", {}).get("dsp0", {})
        blocks_state = {}
        for block_key, state in blocks_dsp0.items():
            if block_key.startswith("block"):
                blocks_state[int(block_key.replace("block", ""))] = bool(state)
        snap_controllers = snap.get("controllers", {}).get("dsp0", {})
        snap_params = {}
        for block_key, params_map in snap_controllers.items():
            s = int(block_key.replace("block", ""))
            for pname, pdef in params_map.items():
                snap_params.setdefault(s, {})[pname] = pdef.get("@value")

        snapshots[idx] = {
            "name":         snap.get("@name", f"Snapshot {idx+1}"),
            "led":          int(snap.get("@ledcolor", 0)),
            "tempo":        float(snap.get("@tempo", tempo)),
            "blocks_state": blocks_state,
            "params":       snap_params,
        }

    return {
        "name":         name,
        "tempo":        tempo,
        "blocks":       blocks,
        "snapshots":    snapshots,
        "exp_bindings": exp_bindings,
        "trails":       trails,
    }
