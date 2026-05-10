"""
hlx_codec.py
Encode / decode les fichiers .hlx (preset individuel HX Edit).

Format : JSON brut, pas de compression.

Structure externe :
{
  "data"    : { "device", "device_version", "meta", "tone" },
  "meta"    : { "original": 0, "pbn": 0, "premium": 0 },
  "schema"  : "L6Preset",
  "version" : 6
}
"""

import copy
import json
import time

_HLX_META_BASE = {
    "application": "HX Edit",
    "appversion":  58851328,
    "build_sha":   "d972399",
}

_VARIAX_DEFAULTS = {
    "@variax_customtuning": True,
    "@variax_lockctrls":    0,
    "@variax_magmode":      True,
    "@variax_model":        0,
    "@variax_str1level":    1.0, "@variax_str1tuning": 0,
    "@variax_str2level":    1.0, "@variax_str2tuning": 0,
    "@variax_str3level":    1.0, "@variax_str3tuning": 0,
    "@variax_str4level":    1.0, "@variax_str4tuning": 0,
    "@variax_str5level":    1.0, "@variax_str5tuning": 0,
    "@variax_str6level":    1.0, "@variax_str6tuning": 0,
    "@variax_toneknob":     -0.10,
    "@variax_volumeknob":   -0.10,
}


def encode_hlx(preset: dict, output_path: str) -> None:
    """
    Ecrit un .hlx a partir du dict retourne par PresetBuilder.build().

    preset      : dict { device, device_version, meta, tone }
    output_path : chemin de sortie  (ex: "output/AYGGMW.hlx")
    """
    tone = copy.deepcopy(preset["tone"])

    # Variax : template complet (requis par HX Edit)
    tone["variax"] = dict(_VARIAX_DEFAULTS)

    # Snapshots : supprimer la cle "controllers" quand elle est vide
    for key in list(tone.keys()):
        if key.startswith("snapshot"):
            snap = tone[key]
            if "controllers" in snap:
                if not snap["controllers"].get("dsp0"):
                    del snap["controllers"]

    meta = dict(_HLX_META_BASE)
    meta["modifieddate"] = int(time.time())
    meta["name"] = preset["meta"]["name"]

    outer = {
        "data": {
            "device":         preset["device"],
            "device_version": preset["device_version"],
            "meta":           meta,
            "tone":           tone,
        },
        "meta":    {"original": 0, "pbn": 0, "premium": 0},
        "schema":  "L6Preset",
        "version": 6,
    }

    out_str = json.dumps(outer, indent=1, separators=(",", " : "))
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out_str)

    name = preset["meta"]["name"].strip()
    print(f"Preset ecrit : {output_path}  ({name})")


def decode_hlx(filepath: str) -> dict:
    """Lit un .hlx et retourne le dict tone."""
    with open(filepath, "r", encoding="utf-8") as f:
        outer = json.load(f)
    return outer["data"]["tone"]
