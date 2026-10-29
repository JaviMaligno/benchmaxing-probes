"""Freeze selection.json from the variant workflow's results (workflow-results.json).

Accepted pairs only; if more than 120, keep every AIME pair and sample MATH-500 pairs down to
120, stratified by subject, with random.Random(20261029) (preregister.md)."""
import collections
import json
import pathlib
import random

from grade import to_number

ROOT = pathlib.Path(__file__).parent
CAP = 120


def main():
    pool = {json.loads(l)["id"]: json.loads(l) for l in open(ROOT / "pool.jsonl")}
    results = json.loads((ROOT / "workflow-results.json").read_text())
    accepted = [r for r in results if r["accepted"]]
    rejected = [{"id": r["id"], "reason": r["reason"]} for r in results if not r["accepted"]]
    aime = [r for r in accepted if r["id"].startswith("aime")]
    math = [r for r in accepted if not r["id"].startswith("aime")]
    if len(accepted) > CAP:
        rng = random.Random(20261029)
        by_subj = collections.defaultdict(list)
        for r in sorted(math, key=lambda r: r["id"]):
            by_subj[pool[r["id"]]["subject"]].append(r)
        room = CAP - len(aime)
        quota = {s: round(room * len(v) / len(math)) for s, v in by_subj.items()}
        while sum(quota.values()) > room:
            quota[max(quota, key=quota.get)] -= 1
        while sum(quota.values()) < room:
            quota[max(by_subj, key=lambda s: len(by_subj[s]) - quota[s])] += 1
        math = [r for s in sorted(by_subj) for r in rng.sample(by_subj[s], quota[s])]
    chosen = aime + sorted(math, key=lambda r: r["id"])
    items = []
    for r in chosen:
        p = pool[r["id"]]
        items.append({
            "id": r["id"], "source": p["source"], "subject": p["subject"],
            "original": p["problem"], "original_answer": p["answer"], "original_decimal": to_number(p["answer"]),
            "variant": r["author"]["variant_problem"], "variant_answer": r["author"]["answer_latex"],
            "variant_decimal": r["author"]["answer_decimal"], "change_summary": r["author"]["change_summary"],
        })
    out = {"frozen": "2026-10-29", "n": len(items), "n_accepted": len(accepted), "rejected": rejected, "items": items}
    (ROOT / "selection.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"accepted {len(accepted)}/{len(results)}; selected {len(items)} "
          f"({sum(i['source'] == 'AIME 2025' for i in items)} AIME); rejected {len(rejected)}")


if __name__ == "__main__":
    main()
