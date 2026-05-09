"""
hls_codec.py
Encode / décode les fichiers .hls (Line6 HX Edit setlist)

Format :
  JSON externe
  └── encoded_data  : Base64( zlib( JSON interne ) )

JSON interne :
  └── presets[]
      └── tone
          ├── dsp0 / dsp1  (blocs d'effets)
          ├── snapshot0..7 (états par scène)
          ├── footswitch   (assignation boutons)
          ├── controller   (pédale expression)
          └── global
"""

import json
import base64
import zlib
import copy
from pathlib import Path


# ──────────────────────────────────────────────
# DECODE
# ──────────────────────────────────────────────

def decode_hls(filepath: str) -> dict:
    """
    Lit un .hls et retourne le JSON interne (presets) décodé.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        outer = json.load(f)

    raw_b64 = outer["encoded_data"]
    compressed = base64.b64decode(raw_b64)
    decompressed = zlib.decompress(compressed)
    inner = json.loads(decompressed)
    return inner


def get_outer_meta(filepath: str) -> dict:
    """Retourne les métadonnées de l'enveloppe externe (device, appversion…)."""
    with open(filepath, "r", encoding="utf-8") as f:
        outer = json.load(f)
    return outer.get("meta", {})


# ──────────────────────────────────────────────
# ENCODE
# ──────────────────────────────────────────────

def encode_hls(inner: dict, meta: dict, output_path: str) -> None:
    """
    Prend le JSON interne + les métadonnées, produit un .hls valide.

    Paramètres
    ----------
    inner       : dict  – le JSON interne complet (clé "presets")
    meta        : dict  – métadonnées de l'enveloppe externe
                          (application, appversion, build_sha, device,
                           device_version, modifieddate, name)
    output_path : str   – chemin de sortie du fichier .hls
    """
    # Serialiser avec le meme style que HX Edit :
    #   - separateur items : "," (pas d'espace, la newline suit l'indentation)
    #   - separateur cle   : " : " (espaces autour des deux-points)
    inner_json_str = json.dumps(inner, separators=(",", " : "), indent=1)
    inner_bytes = inner_json_str.encode("utf-8")

    # CRC32 calcule sur les donnees DECOMPRESSEES (comportement HX Edit)
    crc = zlib.crc32(inner_bytes) & 0xFFFFFFFF

    # Compression zlib niveau 9 (identique a HX Edit)
    compressed = zlib.compress(inner_bytes, level=9)

    # Encodage Base64
    encoded = base64.b64encode(compressed).decode("ascii")

    outer = {
        "compression": {
            "crc32": crc,
            "decompressed_size": len(inner_bytes),
            "type": "zlib"
        },
        "encoded_data": encoded,
        "encoding": "Base64",
        "meta": meta,
        "schema": "L6Setlist",
        "version": 2
    }

    # newline='\n' : force les fins de ligne Unix comme HX Edit
    # (le mode texte Windows convertirait \n en \r\n, ce qui casse l'import)
    outer_str = json.dumps(outer, indent=1, separators=(",", " : "))
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(outer_str)

    print(f"Fichier ecrit : {output_path}")
    print(f"   {len(inner['presets'])} presets | "
          f"{len(inner_bytes):,} octets decompresses | "
          f"{len(compressed):,} octets comprimes")


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def list_presets(inner: dict) -> list[dict]:
    """Retourne la liste des presets avec leur index et nom."""
    result = []
    for i, p in enumerate(inner["presets"]):
        name = p.get("meta", {}).get("name", "(vide)")
        has_tone = "tone" in p
        result.append({"index": i, "name": name, "has_tone": has_tone})
    return result


def get_preset(inner: dict, index: int) -> dict:
    """Retourne un preset par index."""
    return inner["presets"][index]


def set_preset(inner: dict, index: int, preset: dict) -> None:
    """Remplace un preset à un index donné."""
    inner["presets"][index] = preset


def blank_inner(name: str = "HX Effects") -> dict:
    """Crée un JSON interne vide avec 128 slots."""
    return {
        "meta": {"name": name},
        "presets": [_empty_preset_slot() for _ in range(128)]
    }


def _empty_preset_slot() -> dict:
    """Slot de preset vide (sans tone, comme les emplacements non utilisés)."""
    return {"meta": {"name": "New Preset"}}


# ──────────────────────────────────────────────
# TEST RAPIDE
# ──────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    src = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/HX_Effects.hls"
    print(f"Décodage de : {src}")
    inner = decode_hls(src)
    presets = list_presets(inner)
    print(f"{len(presets)} presets détectés :")
    for p in presets[:10]:
        status = "✓" if p["has_tone"] else "·"
        print(f"  [{p['index']:03d}] {status} {p['name']}")
    if len(presets) > 10:
        print(f"  ... et {len(presets)-10} autres")
