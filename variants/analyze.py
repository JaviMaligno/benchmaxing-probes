"""Preregistered analysis (preregister.md): drop and excess drop per model, bootstrap CI,
paired sign-flip permutation test, Holm across the seven models. Reads grades.json."""
import collections
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).parent
SEED, B = 20261029, 10000


def main(sensitivity=False):
    grades = json.loads((ROOT / "grades.json").read_text())
    if sensitivity:  # deviations.md: drop items where any run of any model has no \boxed{} answer
        noboxed = {g["item"] for g in grades if g["boxed"] is None}
        grades = [g for g in grades if g["item"] not in noboxed]
    cell = collections.defaultdict(list)
    for g in grades:
        cell[(g["model"], g["item"], g["version"])].append(1.0 if g["correct"] else 0.0)
    models = sorted({g["model"] for g in grades})
    source = {g["item"]: g["source"] for g in grades}
    items = sorted(i for i in source if all(len(cell[(m, i, v)]) == 2 for m in models for v in ("original", "variant")))
    score = lambda m, i, v: sum(cell[(m, i, v)]) / 2
    diff = {m: [score(m, i, "original") - score(m, i, "variant") for i in items] for m in models}

    def excess(m, idx):
        own = sum(diff[m][k] for k in idx) / len(idx)
        others = [sum(diff[o][k] for k in idx) / len(idx) for o in models if o != m]
        return own - sum(others) / len(others)

    rng = random.Random(SEED)
    n, full = len(items), list(range(len(items)))
    out = {"n_items": n, "models": {}}
    for m in models:
        boots = sorted(excess(m, [rng.randrange(n) for _ in full]) for _ in range(B))
        # sign-flip on item-level excess differences
        ex_items = [diff[m][k] - sum(diff[o][k] for o in models if o != m) / (len(models) - 1) for k in full]
        obs = abs(sum(ex_items))
        hits = sum(abs(sum(x if rng.random() < 0.5 else -x for x in ex_items)) >= obs - 1e-12 for _ in range(B))
        per_source = {}
        for s in sorted(set(source.values())):
            ks = [k for k in full if source[items[k]] == s]
            per_source[s] = {
                "n": len(ks),
                "acc_original": round(sum(score(m, items[k], "original") for k in ks) / len(ks), 3),
                "acc_variant": round(sum(score(m, items[k], "variant") for k in ks) / len(ks), 3),
                "excess_drop": round(excess(m, ks), 3),
            }
        out["models"][m] = {
            "acc_original": round(sum(score(m, i, "original") for i in items) / n, 3),
            "acc_variant": round(sum(score(m, i, "variant") for i in items) / n, 3),
            "drop": round(sum(diff[m]) / n, 3),
            "excess_drop": round(excess(m, full), 3),
            "ci95": [round(boots[int(0.025 * B)], 3), round(boots[int(0.975 * B) - 1], 3)],
            "p_raw": (hits + 1) / (B + 1),
            "by_source": per_source,
        }
    # Holm
    order = sorted(models, key=lambda m: out["models"][m]["p_raw"])
    running = 0.0
    for r, m in enumerate(order):
        running = max(running, min(1.0, (len(models) - r) * out["models"][m]["p_raw"]))
        out["models"][m]["p_holm"] = round(running, 4)
        out["models"][m]["signal"] = out["models"][m]["excess_drop"] > 0 and running < 0.05
    out["sensitivity_no_unboxed"] = sensitivity
    (ROOT / ("results-sensitivity.json" if sensitivity else "results.json")).write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"n items = {n}")
    print(f"{'model':28} {'orig':>6} {'var':>6} {'drop':>6} {'excess':>7} {'CI95':>16} {'p_holm':>7}")
    for m in models:
        r = out["models"][m]
        print(f"{m:28} {r['acc_original']:6.3f} {r['acc_variant']:6.3f} {r['drop']:6.3f} {r['excess_drop']:7.3f} "
              f"{str(r['ci95']):>16} {r['p_holm']:7.4f}{'  SIGNAL' if r['signal'] else ''}")


if __name__ == "__main__":
    import sys
    main(sensitivity="--sensitivity" in sys.argv)
