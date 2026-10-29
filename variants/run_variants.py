"""Run the frozen original/variant pairs through Claude Code, one harness for all seven models.

Claude models use the first-party Max login; the rest go through OpenRouter's
Anthropic-compatible endpoint (same pattern as ../run_claude_code.py). One fresh process
per run, prompt on stdin. Jobs are interleaved by item so both versions share conditions.

    python run_variants.py --models z-ai/glm-5.3 --items aime25-01 --reps 1
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "runs"
MODELS = [
    "claude-opus-5",
    "claude-fable-5",
    "moonshotai/kimi-k3.1-pro",
    "google/gemini-4-argon",
    "deepseek/deepseek-v4-pro-0813",
    "qwen/qwen3.8-2.4t-a95b",
    "z-ai/glm-5.3",
]
TEMPLATE = "{problem}\n\nReason step by step, then give only the final answer inside \\boxed{{}}."


def slug(model):
    return model.split("/")[-1]


def env_for(model):
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC_")}
    env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = "32000"
    if not model.startswith("claude-"):
        env["ANTHROPIC_BASE_URL"] = "https://openrouter.ai/api"
        env["ANTHROPIC_AUTH_TOKEN"] = (pathlib.Path.home() / ".openrouter-key").read_text().strip()
        env["ANTHROPIC_API_KEY"] = ""
    return env


def run(model, item, version, rep):
    stem = OUT / slug(model) / f"{item['id']}-{version}-r{rep}"
    meta_path = stem.with_name(stem.name + "-meta.json")
    if meta_path.exists():
        prev = json.loads(meta_path.read_text())
        # end_turn, or truncation at the output cap (counts as wrong, never re-run; preregister.md)
        if prev.get("stop_reason") in ("end_turn", "max_tokens") or "output token maximum" in prev.get("stderr_tail", "") \
                or "output token maximum" in stem.with_name(stem.name + "-answer.md").read_text(encoding="utf-8"):
            return None
    stem.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--model", model, "--effort", "high", "--safe-mode", "--strict-mcp-config",
           "--tools=", "--no-session-persistence", "--max-turns", "1",
           "--output-format", "stream-json", "--verbose"]
    if model.startswith("claude-"):
        cmd += ["--max-budget-usd", "3"]
    prompt = TEMPLATE.format(problem=item[version])
    t0 = time.time()
    p = subprocess.run(cmd, input=prompt, env=env_for(model), capture_output=True, text=True,
                       timeout=1800, cwd=OUT)
    events = [json.loads(line) for line in p.stdout.splitlines() if line.startswith("{")]
    texts, models, stop = [], set(), None
    for e in events:
        if e.get("type") == "assistant":
            msg = e["message"]
            models.add(msg.get("model"))
            stop = msg.get("stop_reason") or stop
            texts += [b["text"] for b in msg.get("content", []) if b.get("type") == "text"]
    result = next((e for e in events if e.get("type") == "result"), {})
    stem.with_name(stem.name + "-answer.md").write_text("".join(texts), encoding="utf-8")
    meta = {
        "item": item["id"], "version": version, "rep": rep, "requested_model": model,
        "actual_models": sorted(m for m in models if m),
        "stop_reason": result.get("stop_reason") or stop, "subtype": result.get("subtype"),
        "is_error": result.get("is_error"), "seconds": round(time.time() - t0, 1),
        "cost_list_usd": result.get("total_cost_usd"), "usage": result.get("usage"),
        "returncode": p.returncode, "stderr_tail": p.stderr[-600:],
    }
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return f"{slug(model)} {stem.name}: {meta['stop_reason']} {meta['seconds']}s err={meta['is_error']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=MODELS)
    ap.add_argument("--items", nargs="*")
    ap.add_argument("--reps", nargs="*", type=int, default=[1, 2])
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    items = json.loads((ROOT / "selection.json").read_text())["items"]
    if a.items:
        items = [i for i in items if i["id"] in a.items]
    jobs = [(m, i, v, r) for r in a.reps for i in items for v in ("original", "variant") for m in a.models]
    with cf.ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(run, *j): j for j in jobs}
        for f in cf.as_completed(futs):
            try:
                line = f.result()
                if line:
                    print(line, flush=True)
            except Exception as e:  # report and continue; re-runs only for infrastructure failures
                m, i, v, r = futs[f]
                print(f"ERROR {slug(m)} {i['id']}-{v}-r{r}: {e}", flush=True)


if __name__ == "__main__":
    main()
