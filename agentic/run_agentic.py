"""Agentic sessions: one conductor per run, its own model as subagents, read-only tools.

Same Claude Code harness for all seven models (Claude on the Max login, the rest through OpenRouter's
Anthropic-compatible endpoint). Each run gets a fresh copy of the scenario workspace. The spend cap is
enforced here: OpenRouter usage is read before every session and no new session starts past the cap.

    python run_agentic.py --scenario vendors --reps 1 --cap-usd 15
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import shutil
import subprocess
import threading
import time
import urllib.request

ROOT = pathlib.Path(__file__).parent
MODELS = [
    "claude-opus-5",
    "claude-fable-5",
    "moonshotai/kimi-k3.1-pro",
    "google/gemini-4-argon",
    "deepseek/deepseek-v4-pro-0813",
    "qwen/qwen3.8-2.4t-a95b",
    "z-ai/glm-5.3",
]
KEY = (pathlib.Path.home() / ".openrouter-key").read_text().strip()
LOCK = threading.Lock()
IN_FLIGHT = [0]
RESERVE_USD = 10.0  # assumed spend of a session in flight, so parallel starts cannot overshoot the cap


def slug(model):
    return model.split("/")[-1]


def openrouter_usage():
    req = urllib.request.Request("https://openrouter.ai/api/v1/credits", headers={"Authorization": f"Bearer {KEY}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["data"]["total_usage"]


def env_for(model):
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC_")}
    env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = "32000"
    env["CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"] = "0"  # wait for background subagents instead of stopping them
    if not model.startswith("claude-"):
        env["ANTHROPIC_BASE_URL"] = "https://openrouter.ai/api"
        env["ANTHROPIC_AUTH_TOKEN"] = KEY
        env["ANTHROPIC_API_KEY"] = ""
    return env


def run(scenario, model, rep, start_usage, cap):
    out = ROOT / "runs" / scenario / f"{slug(model)}-r{rep}"
    if (out / "meta.json").exists():
        return None
    paid = not model.startswith("claude-")
    with LOCK:  # the cap check: spent so far plus a reserve per paid session in flight
        spent = openrouter_usage() - start_usage
        if paid and spent + RESERVE_USD * (IN_FLIGHT[0] + 1) > cap:
            return f"CAP {slug(model)} r{rep}: not started, spent {spent:.2f} + reserve > {cap}"
        IN_FLIGHT[0] += paid
    src = ROOT / "scenarios" / scenario
    ws = out / "workspace"
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(src / "workspace", ws)
    cmd = ["claude", "-p", "--model", model, "--effort", "high", "--safe-mode", "--strict-mcp-config",
           "--tools=Agent,Read,Glob,Grep", "--no-session-persistence", "--max-turns", "40",
           "--output-format", "stream-json", "--verbose"]
    if model.startswith("claude-"):
        cmd += ["--max-budget-usd", "60"]  # notional list price on the Max plan; 10 cut sessions short
    t0 = time.time()
    try:
        p = subprocess.run(cmd, input=(src / "task.md").read_text(encoding="utf-8"), env=env_for(model),
                           capture_output=True, text=True, timeout=3600, cwd=ws)
        stdout, stderr, rc = p.stdout, p.stderr, p.returncode
    except subprocess.TimeoutExpired as e:
        stdout, stderr, rc = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "timeout", -9
    with LOCK:
        IN_FLIGHT[0] -= paid
    (out / "transcript.jsonl").write_text(stdout, encoding="utf-8")
    events = [json.loads(l) for l in stdout.splitlines() if l.startswith("{")]
    result = next((e for e in reversed(events) if e.get("type") == "result"), {})
    meta = {"scenario": scenario, "model": model, "rep": rep, "seconds": round(time.time() - t0, 1),
            "subtype": result.get("subtype"), "is_error": result.get("is_error"), "num_turns": result.get("num_turns"),
            "usage": result.get("usage"), "returncode": rc, "stderr_tail": stderr[-800:]}
    (out / "final.md").write_text(result.get("result") or "", encoding="utf-8")
    (out / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return f"{slug(model)} r{rep}: {meta['subtype']} turns={meta['num_turns']} {meta['seconds']}s"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenario", required=True)
    ap.add_argument("--models", nargs="*", default=MODELS)
    ap.add_argument("--reps", nargs="*", type=int, default=[1])
    ap.add_argument("--workers", type=int, default=7)
    ap.add_argument("--cap-usd", type=float, required=True, help="OpenRouter spend cap for this invocation")
    a = ap.parse_args()
    start = openrouter_usage()
    print(f"OpenRouter usage at start {start:.2f}; cap {a.cap_usd} USD", flush=True)
    jobs = [(a.scenario, m, r, start, a.cap_usd) for r in a.reps for m in a.models]
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for f in cf.as_completed([ex.submit(run, *j) for j in jobs]):
            try:
                line = f.result()
                if line:
                    print(line, flush=True)
            except Exception as e:
                print(f"ERROR {e}", flush=True)
    print(f"spent this invocation {openrouter_usage() - start:.2f} USD", flush=True)


if __name__ == "__main__":
    main()
