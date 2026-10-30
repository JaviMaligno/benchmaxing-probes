"""Score agentic runs: the final JSON against the scenario key, plus process measures from the transcript.

    python score.py --scenario vendors     # writes runs/<scenario>/scores.json and prints a table
"""
import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent


def final_json(text):
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, re.S)
    for b in reversed(blocks):
        try:
            return json.loads(b)
        except json.JSONDecodeError:
            continue
    return None


def final_text(d):
    """All the conductor's text, in order, ending with the result field: the deliverable is the last JSON
    block anywhere in it (with background subagents the conductor keeps talking after delivering)."""
    parts = []
    for line in (d / "transcript.jsonl").read_text(encoding="utf-8").splitlines():
        if line.startswith("{"):
            e = json.loads(line)
            if e.get("type") == "assistant" and e.get("parent_tool_use_id") is None:
                parts += [b.get("text", "") for b in e["message"].get("content", []) if b.get("type") == "text"]
    return "\n".join(parts + [(d / "final.md").read_text(encoding="utf-8")])


def norm(name, names):
    """Accept the vendor name or its folder slug ("Quarry Labs" / "quarry-labs")."""
    key = re.sub(r"[^a-z0-9]", "", (name or "").lower())
    for n in names:
        if re.sub(r"[^a-z0-9]", "", n.lower()) == key:
            return n
    return None


def process(transcript):
    """Conductor-level measures. A tool_use with no parent is the conductor's own call."""
    agent_calls, own_reads, prompts, checks_after = 0, 0, [], 0
    per_message = {}  # stream-json emits each content block as its own event; group by message id
    first_result_seen = False
    for line in transcript.splitlines():
        if not line.startswith("{"):
            continue
        e = json.loads(line)
        if e.get("type") == "user" and e.get("parent_tool_use_id") is None:
            content = e.get("message", {}).get("content", [])
            if isinstance(content, list) and any(c.get("type") == "tool_result" for c in content):
                first_result_seen = first_result_seen or agent_calls > 0
        if e.get("type") != "assistant" or e.get("parent_tool_use_id") is not None:
            continue
        uses = [b for b in e["message"].get("content", []) if b.get("type") == "tool_use"]
        agents = [b for b in uses if b["name"] in ("Agent", "Task")]
        agent_calls += len(agents)
        mid = e["message"].get("id")
        per_message[mid] = per_message.get(mid, 0) + len(agents)
        prompts += [json.dumps(b.get("input", {})) for b in agents]
        reads = [b for b in uses if b["name"] in ("Read", "Grep", "Glob") and "vendors" in json.dumps(b.get("input", {}))]
        own_reads += len(reads)
        if first_result_seen:
            checks_after += len(reads)
    joined = " ".join(prompts).lower()
    return {
        "agent_calls": agent_calls,
        "max_parallel_agents": max(per_message.values(), default=0),
        "conductor_reads_of_vendor_files": own_reads,
        "conductor_reads_after_first_result": checks_after,
        "briefs_pass_rate_0_86": "0.86" in joined,
        "briefs_pass_confirmed_rule": "confirmed" in joined or "policy.md" in joined,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenario", required=True)
    a = ap.parse_args()
    key = json.loads((ROOT / "scenarios" / a.scenario / "key.json").read_text())
    names = list(key["vendors"])
    traps = key["traps"]
    rows = []
    for meta_path in sorted((ROOT / "runs" / a.scenario).glob("*/meta.json")):
        d = meta_path.parent
        meta = json.loads(meta_path.read_text())
        ans = final_json(final_text(d)) or {}
        got = {norm(k, names): v for k, v in (ans.get("vendors") or {}).items()}
        fields, correct = 0, 0
        per = {}
        for n, k in key["vendors"].items():
            g = got.get(n) or {}
            try:
                c_ok = abs(float(g.get("cost_gbp")) - k["cost_gbp"]) <= 1.0
            except (TypeError, ValueError):
                c_ok = False
            p_ok = g.get("p1_counted") == k["p1_counted"]
            b_ok = g.get("breach") == k["breach"]
            per[n] = {"cost": c_ok, "p1": p_ok, "breach": b_ok}
            fields += 3
            correct += c_ok + p_ok + b_ok
        if isinstance(key["recommended"], list):
            rec = [norm(x, names) for x in (ans.get("recommended") or [])] if isinstance(ans.get("recommended"), list) else []
            rec_ok = rec == key["recommended"]
        else:
            rec = [norm(ans.get("recommended"), names)]
            rec_ok = rec[0] == key["recommended"]
        if isinstance(next(iter(traps.values())), list):  # generic: trap -> [[vendor, field], ...]
            fieldmap = {"cost": "cost", "p1": "p1", "breach": "breach"}
            trap_scores = {}
            for tname, items in traps.items():
                oks = []
                for vendor, field in items:
                    oks.append(vendor not in rec if field == "recommended" else per[vendor][fieldmap[field]])
                trap_scores[f"trap_{tname}"] = round(sum(oks) / len(oks), 2) if oks else None
        else:
            trap_scores = {
                "trap_policy_eur": per[traps["policy_vendor"]]["cost"],
                "trap_amendment": per[traps["amendment_vendor"]]["cost"],
                "trap_duplicates": per[traps["duplicate_vendor"]]["p1"],
                "trap_status_rule": all(per[n]["p1"] for n in names if n != traps["duplicate_vendor"]),
            }
        u = meta.get("usage") or {}
        rows.append({
            "run": d.name, "model": meta["model"], "subtype": meta["subtype"], "json_found": bool(ans),
            "fields_correct": correct, "fields_total": fields, "recommended_ok": rec_ok, **trap_scores,
            "turns": meta["num_turns"], "seconds": meta["seconds"],
            "output_tokens": u.get("output_tokens"),
            **process((d / "transcript.jsonl").read_text(encoding="utf-8")),
        })
    (ROOT / "runs" / a.scenario / "scores.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
    trap_cols = [c for c in rows[0] if c.startswith("trap_")] if rows else []
    cols = ["run", "fields_correct", "recommended_ok", *trap_cols, "agent_calls", "max_parallel_agents", "conductor_reads_of_vendor_files",
            "conductor_reads_after_first_result", "briefs_pass_rate_0_86", "briefs_pass_confirmed_rule", "turns", "seconds"]
    print(" | ".join(cols))
    for r in rows:
        print(" | ".join(str(r[c]) for c in cols))


if __name__ == "__main__":
    main()
