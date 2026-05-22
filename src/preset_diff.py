"""
preset_diff.py
Compare deux structures de preset (code Python vs .hlx modifie sur disque)
et produit un rapport diff lisible.

Strategie : ne signaler que les ecarts significatifs entre les deux versions,
en categorisant par type (block params, snapshot params, blocks_state, etc.).
"""


def _fmt(value):
    """Format compact d'une valeur pour l'affichage diff."""
    if isinstance(value, float):
        # Eviter 0.7000000001 — afficher 0.7
        return f"{value:g}"
    if isinstance(value, bool):
        return "True" if value else "False"
    return str(value)


def _values_equal(a, b, tol: float = 1e-4) -> bool:
    """Compare deux valeurs avec tolerance pour les floats."""
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < tol
    return a == b


def diff_presets(code_preset: dict, disk_preset: dict) -> list:
    """
    Compare deux presets normalises (structure decode_preset).

    Retourne une liste de "changements" structures :
    [
      {"kind": "block_param", "slot": 1, "model": "...", "param": "Gain",
       "code": 0.68, "disk": 0.72},
      {"kind": "snap_param", "snap_idx": 2, "snap_name": "Solo",
       "slot": 1, "param": "Level", "code": 0.92, "disk": 0.85},
      {"kind": "blocks_state", "snap_idx": 2, "snap_name": "Solo",
       "slot": 4, "code": True, "disk": False},
      {"kind": "snap_meta", "snap_idx": 2, "field": "name",
       "code": "Solo", "disk": "Lead"},
      {"kind": "trails", "slot": 3, "code": True, "disk": False},
      {"kind": "tempo", "code": 93.0, "disk": 95.0},
      {"kind": "exp_binding", "slot": 2, "param": "Pedal",
       "code": 1, "disk": None},   # ajoute/supprime
    ]
    """
    changes = []

    # --- Tempo global ---
    if not _values_equal(code_preset["tempo"], disk_preset["tempo"]):
        changes.append({
            "kind": "tempo",
            "code": code_preset["tempo"],
            "disk": disk_preset["tempo"],
        })

    # --- Block params (valeurs de bloc en dehors des snapshots) ---
    code_blocks = code_preset["blocks"]
    disk_blocks = disk_preset["blocks"]
    all_slots = sorted(set(code_blocks) | set(disk_blocks))

    # Identifier les params controles par snapshot pour les exclure de la
    # comparaison des "block defaults" — ils sont compares dans la section snap
    snap_controlled_params = set()
    for snap in code_preset["snapshots"].values():
        for slot, params in snap["params"].items():
            for pname in params:
                snap_controlled_params.add((slot, pname))
    for snap in disk_preset["snapshots"].values():
        for slot, params in snap["params"].items():
            for pname in params:
                snap_controlled_params.add((slot, pname))

    for slot in all_slots:
        if slot not in code_blocks:
            changes.append({
                "kind":  "block_added",
                "slot":  slot,
                "model": disk_blocks[slot]["model"],
            })
            continue
        if slot not in disk_blocks:
            changes.append({
                "kind":  "block_removed",
                "slot":  slot,
                "model": code_blocks[slot]["model"],
            })
            continue

        code_blk = code_blocks[slot]
        disk_blk = disk_blocks[slot]
        model = code_blk["model"]

        # Different model = bloc remplace
        if code_blk["model"] != disk_blk["model"]:
            changes.append({
                "kind":       "block_model_changed",
                "slot":       slot,
                "code_model": code_blk["model"],
                "disk_model": disk_blk["model"],
            })
            continue

        # Compare params (excluant ceux controles par snapshot)
        code_params = code_blk["params"]
        disk_params = disk_blk["params"]
        all_params = sorted(set(code_params) | set(disk_params))
        for pname in all_params:
            if (slot, pname) in snap_controlled_params:
                continue  # gere dans la section snap
            cv = code_params.get(pname)
            dv = disk_params.get(pname)
            if not _values_equal(cv, dv):
                changes.append({
                    "kind":  "block_param",
                    "slot":  slot,
                    "model": model,
                    "param": pname,
                    "code":  cv,
                    "disk":  dv,
                })

        # Compare trails
        if code_blk.get("trails") != disk_blk.get("trails"):
            if code_blk.get("trails") is not None or disk_blk.get("trails") is not None:
                changes.append({
                    "kind":  "trails",
                    "slot":  slot,
                    "model": model,
                    "code":  code_blk.get("trails"),
                    "disk":  disk_blk.get("trails"),
                })

    # --- Snapshots ---
    code_snaps = code_preset["snapshots"]
    disk_snaps = disk_preset["snapshots"]
    all_snap_idx = sorted(set(code_snaps) | set(disk_snaps))

    for idx in all_snap_idx:
        if idx not in code_snaps:
            changes.append({"kind": "snap_added", "snap_idx": idx,
                            "snap_name": disk_snaps[idx]["name"]})
            continue
        if idx not in disk_snaps:
            changes.append({"kind": "snap_removed", "snap_idx": idx,
                            "snap_name": code_snaps[idx]["name"]})
            continue

        code_snap = code_snaps[idx]
        disk_snap = disk_snaps[idx]
        snap_name_code = code_snap["name"].strip()
        snap_name_disk = disk_snap["name"].strip()

        # Meta (nom, couleur, tempo)
        if snap_name_code != snap_name_disk:
            changes.append({
                "kind": "snap_meta", "snap_idx": idx, "field": "name",
                "snap_name": snap_name_code,
                "code": snap_name_code, "disk": snap_name_disk,
            })
        if code_snap["led"] != disk_snap["led"]:
            changes.append({
                "kind": "snap_meta", "snap_idx": idx, "field": "led",
                "snap_name": snap_name_code,
                "code": code_snap["led"], "disk": disk_snap["led"],
            })
        if not _values_equal(code_snap["tempo"], disk_snap["tempo"]):
            changes.append({
                "kind": "snap_meta", "snap_idx": idx, "field": "tempo",
                "snap_name": snap_name_code,
                "code": code_snap["tempo"], "disk": disk_snap["tempo"],
            })

        # blocks_state (on/off par slot)
        code_state = code_snap["blocks_state"]
        disk_state = disk_snap["blocks_state"]
        all_state_slots = sorted(set(code_state) | set(disk_state))
        for slot in all_state_slots:
            cs = code_state.get(slot, False)
            ds = disk_state.get(slot, False)
            if cs != ds:
                changes.append({
                    "kind":      "blocks_state",
                    "snap_idx":  idx,
                    "snap_name": snap_name_code,
                    "slot":      slot,
                    "code":      cs,
                    "disk":      ds,
                })

        # snap params (controlled values)
        code_sparams = code_snap["params"]
        disk_sparams = disk_snap["params"]
        all_sparam_slots = sorted(set(code_sparams) | set(disk_sparams))
        for slot in all_sparam_slots:
            code_pmap = code_sparams.get(slot, {})
            disk_pmap = disk_sparams.get(slot, {})
            all_p = sorted(set(code_pmap) | set(disk_pmap))
            for pname in all_p:
                cv = code_pmap.get(pname)
                dv = disk_pmap.get(pname)
                if not _values_equal(cv, dv):
                    changes.append({
                        "kind":      "snap_param",
                        "snap_idx":  idx,
                        "snap_name": snap_name_code,
                        "slot":      slot,
                        "param":     pname,
                        "code":      cv,
                        "disk":      dv,
                    })

    # --- EXP bindings ---
    code_exp = code_preset["exp_bindings"]
    disk_exp = disk_preset["exp_bindings"]
    all_keys = set(code_exp) | set(disk_exp)
    for key in all_keys:
        slot, pname = key
        cv = code_exp.get(key)
        dv = disk_exp.get(key)
        if cv != dv:
            changes.append({
                "kind":  "exp_binding",
                "slot":  slot,
                "param": pname,
                "code":  cv,
                "disk":  dv,
            })

    return changes


def format_diff(preset_name: str, changes: list) -> str:
    """Format les changements en rapport lisible."""
    if not changes:
        return f"=== {preset_name} ===\n  (aucune difference)\n"

    lines = [f"=== {preset_name} ==="]

    # Grouper par categorie pour clarte
    by_kind = {}
    for c in changes:
        by_kind.setdefault(c["kind"], []).append(c)

    # Tempo
    for c in by_kind.get("tempo", []):
        lines.append(f"  Tempo : {_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # Block params (defaults)
    if "block_param" in by_kind:
        lines.append("\n  Block params (defaults) :")
        by_slot = {}
        for c in by_kind["block_param"]:
            by_slot.setdefault((c["slot"], c["model"]), []).append(c)
        for (slot, model), items in sorted(by_slot.items()):
            lines.append(f"    Bloc {slot} ({model}) :")
            for c in items:
                lines.append(f"      {c['param']} : {_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # Snapshot params (overrides per snap)
    if "snap_param" in by_kind:
        lines.append("\n  Snapshot params (overrides) :")
        by_snap = {}
        for c in by_kind["snap_param"]:
            by_snap.setdefault((c["snap_idx"], c["snap_name"]), []).append(c)
        for (idx, name), items in sorted(by_snap.items()):
            lines.append(f"    Snapshot {idx} ({name}) :")
            for c in items:
                lines.append(f"      Bloc {c['slot']} {c['param']} : "
                             f"{_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # blocks_state (on/off per snap)
    if "blocks_state" in by_kind:
        lines.append("\n  Snapshot blocks_state (on/off) :")
        by_snap = {}
        for c in by_kind["blocks_state"]:
            by_snap.setdefault((c["snap_idx"], c["snap_name"]), []).append(c)
        for (idx, name), items in sorted(by_snap.items()):
            lines.append(f"    Snapshot {idx} ({name}) :")
            for c in items:
                arrow = "+ active" if c["disk"] else "- desactive"
                lines.append(f"      Bloc {c['slot']} : {arrow}")

    # Snap meta (name/led/tempo)
    if "snap_meta" in by_kind:
        lines.append("\n  Snapshot meta :")
        for c in by_kind["snap_meta"]:
            lines.append(f"    Snapshot {c['snap_idx']} ({c['snap_name']}) "
                         f"{c['field']} : {_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # Trails
    if "trails" in by_kind:
        lines.append("\n  Trails :")
        for c in by_kind["trails"]:
            lines.append(f"    Bloc {c['slot']} ({c['model']}) @trails : "
                         f"{_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # EXP bindings
    if "exp_binding" in by_kind:
        lines.append("\n  EXP pedal bindings :")
        for c in by_kind["exp_binding"]:
            lines.append(f"    Bloc {c['slot']} {c['param']} : "
                         f"@controller {_fmt(c['code'])} -> {_fmt(c['disk'])}")

    # Bloc added/removed/changed
    for kind, label in [("block_added", "ajoute"), ("block_removed", "supprime"),
                         ("block_model_changed", "model change")]:
        if kind in by_kind:
            lines.append(f"\n  Blocs {label} :")
            for c in by_kind[kind]:
                if kind == "block_model_changed":
                    lines.append(f"    Bloc {c['slot']} : {c['code_model']} -> {c['disk_model']}")
                else:
                    lines.append(f"    Bloc {c['slot']} ({c.get('model')})")

    # Snap added/removed
    for kind, label in [("snap_added", "ajoute"), ("snap_removed", "supprime")]:
        if kind in by_kind:
            lines.append(f"\n  Snapshots {label} :")
            for c in by_kind[kind]:
                lines.append(f"    Snapshot {c['snap_idx']} ({c['snap_name']})")

    return "\n".join(lines) + "\n"
