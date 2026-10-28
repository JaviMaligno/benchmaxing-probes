"""Repeat runs through Claude Code, same options as the original Claude runs (see README).

Claude models use the first-party Max login. Other models go through the same
Claude Code harness pointed at OpenRouter's Anthropic-compatible endpoint, so every
repeat shares one harness. One fresh process per run, prompt on stdin.

    python run_claude_code.py --models claude-opus-5 --cases D2 --reps 1 2 3
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "repeats"
CASES = {"D1": "D1-prompt.txt", "D2": "D2.txt", "D2b": "D2b.txt", "D3": "D3.txt", "D4": "D4.txt"}
MODELS = [
    "claude-opus-5",
    "claude-fable-5",
    "moonshotai/kimi-k3.1-pro",
    "google/gemini-4-argon",
    "deepseek/deepseek-v4-pro-0813",
    "qwen/qwen3.8-2.4t-a95b",
    "z-ai/glm-5.3",
]


def slug(model):
    return model.split("/")[-1]


def env_for(model):
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC_")}
    env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = "8192"
    if not model.startswith("claude-"):
        env["ANTHROPIC_BASE_URL"] = "https://openrouter.ai/api"
        env["ANTHROPIC_AUTH_TOKEN"] = (pathlib.Path.home() / ".openrouter-key").read_text().strip()
        env["ANTHROPIC_API_KEY"] = ""
    return env


def run(model, case, rep):
    stem = OUT / f"{case}-{slug(model)}-r{rep}"
    meta_path = stem.with_name(stem.name + "-meta.json")
    if meta_path.exists() and json.loads(meta_path.read_text()).get("stop_reason") == "end_turn":
        return f"skip {stem.name}"
    cmd = ["claude", "-p", "--model", model, "--effort", "high", "--safe-mode", "--strict-mcp-config",
           "--tools=", "--no-session-persistence", "--max-turns", "1",
           "--output-format", "stream-json", "--verbose"]
    if model.startswith("claude-"):
        cmd += ["--max-budget-usd", "0.65"]
    t0 = time.time()
    p = subprocess.run(cmd, input=(ROOT / CASES[case]).read_text(encoding="utf-8"), env=env_for(model),
                       capture_output=True, text=True, timeout=900, cwd=OUT)
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
        "case": case, "rep": rep, "requested_model": model, "actual_models": sorted(m for m in models if m),
        "stop_reason": result.get("stop_reason") or stop, "subtype": result.get("subtype"),
        "is_error": result.get("is_error"), "seconds": round(time.time() - t0, 1),
        "cost_list_usd": result.get("total_cost_usd"), "usage": result.get("usage"),
        "returncode": p.returncode, "stderr_tail": p.stderr[-600:],
    }
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return f"{stem.name}: {meta['stop_reason']} {meta['actual_models']} {meta['seconds']}s err={meta['is_error']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=MODELS)
    ap.add_argument("--cases", nargs="*", default=["D2", "D2b"])
    ap.add_argument("--reps", nargs="*", type=int, default=[1, 2, 3])
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    jobs = [(m, c, r) for m in a.models for c in a.cases for r in a.reps]
    with cf.ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(run, *j): j for j in jobs}
        for f in cf.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:  # report and continue; no blind retries
                print(f"ERROR {futs[f]}: {e}", flush=True)


if __name__ == "__main__":
    main()
