#!/usr/bin/env python3
"""Reference scorer for the Open Evaluation Methodology (draft).

Usage:
    python3 -I scorer/score.py cases.json outputs.json

cases.json   : [{"id", "dimension": "phoneme"|"tajweed", "group", "has_error": bool,
                 "rule": optional str, "demo": optional {"accent","age","gender"}}]
outputs.json : [{"id", "flagged": bool, "rule": optional str}]

Prints per-group scores (with 95% bootstrap CI) and, when `demo` is present,
the demographic robustness score. Standard library only.
"""
import json
import random
import sys
from collections import defaultdict

MIN_GROUP_RECORDINGS = 20
MIN_GROUP_RECITERS = 5  # enforced only if cases carry "reciter_id"


def f1_and_naming(rows, dimension):
    tp = sum(1 for c, o in rows if c["has_error"] and o["flagged"])
    fn = sum(1 for c, o in rows if c["has_error"] and not o["flagged"])
    fp = sum(1 for c, o in rows if not c["has_error"] and o["flagged"])
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    if dimension == "phoneme":
        return 100 * f1
    named = sum(1 for c, o in rows
                if c["has_error"] and o["flagged"] and o.get("rule") == c.get("rule"))
    naming = named / tp if tp else 0.0
    return min(100.0, 100 * (0.5 * f1 + 0.5 * naming))


def bootstrap_ci(rows, dimension, n=1000, seed=0):
    rng = random.Random(seed)
    vals = sorted(f1_and_naming([rng.choice(rows) for _ in rows], dimension)
                  for _ in range(n))
    return vals[int(0.025 * n)], vals[int(0.975 * n) - 1]


def demographic_score(group_scores):
    """min * (1 - gap/100); a tool scoring 0 everywhere gets 0."""
    if not group_scores:
        return None
    lo, hi = min(group_scores.values()), max(group_scores.values())
    return lo * (1 - (hi - lo) / 100)


def main(cases_path, outputs_path):
    cases = json.load(open(cases_path))
    outs = {o["id"]: o for o in json.load(open(outputs_path))}
    missing = [c["id"] for c in cases if c["id"] not in outs]
    if missing:
        sys.exit(f"missing outputs for {len(missing)} cases, e.g. {missing[:3]}")
    paired = [(c, outs[c["id"]]) for c in cases]

    by_group = defaultdict(list)
    for c, o in paired:
        by_group[(c["dimension"], c["group"])].append((c, o))
    for (dim, group), rows in sorted(by_group.items()):
        score = f1_and_naming(rows, dim)
        lo, hi = bootstrap_ci(rows, dim)
        print(f"{dim:9} {group:12} n={len(rows):4} score={score:5.1f} 95%CI=[{lo:.1f}, {hi:.1f}]")

    for axis in ("accent", "age", "gender"):
        groups = defaultdict(list)
        for c, o in paired:
            if c.get("demo"):
                groups[c["demo"][axis]].append((c, o))
        scores = {}
        for g, rows in groups.items():
            if len(rows) < MIN_GROUP_RECORDINGS:
                print(f"demo/{axis}: {g} excluded (n={len(rows)} < {MIN_GROUP_RECORDINGS})")
                continue
            scores[g] = sum(f1_and_naming([r for r in rows if r[0]["dimension"] == d], d)
                            for d in ("phoneme", "tajweed")
                            if any(r[0]["dimension"] == d for r in rows)) / \
                sum(1 for d in ("phoneme", "tajweed") if any(r[0]["dimension"] == d for r in rows))
        s = demographic_score(scores)
        if s is not None:
            print(f"demographic/{axis}: {s:.1f}  groups={ {k: round(v, 1) for k, v in scores.items()} }")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
