"""Run the frozen probe prompts against non-Claude models through OpenRouter.

Same cases and prompts as the Claude runs: one turn, no tools, no system prompt,
reasoning effort high, one run per model and case. Key read from ~/.openrouter-key.

    python run_openrouter.py                 # all models x all cases
    python run_openrouter.py --models moonshotai/kimi-k3.1-pro --cases D2
"""
import argparse
import concurrent.futures as cf
import json
import pathlib
import time
import urllib.request

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "openrouter"
CASES = {"D1": "D1-prompt.txt", "D2": "D2.txt", "D2b": "D2b.txt", "D3": "D3.txt", "D4": "D4.txt"}
MODELS = [
    "moonshotai/kimi-k3.1-pro",
    "google/gemini-4-argon",
    "deepseek/deepseek-v4-pro-0813",
    "qwen/qwen3.8-2.4t-a95b",
    "z-ai/glm-5.3",
]
MAX_TOKENS = 16384  # reasoning + answer; Claude runs capped output at 8192


def slug(model):
    return model.split("/")[1]


def run(model, case):
    target = OUT / f"{case}-{slug(model)}-answer.md"
    meta_path = OUT / f"{case}-{slug(model)}-meta.json"
    if meta_path.exists() and json.loads(meta_path.read_text()).get("finish_reason") == "stop":
        return f"skip {case} {model}"
    body = {
        "model": model,
        "messages": [{"role": "user", "content": (ROOT / CASES[case]).read_text(encoding="utf-8")}],
        "max_tokens": MAX_TOKENS,
        "reasoning": {"effort": "high", "exclude": True},
        "usage": {"include": True},
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": "Bearer " + (pathlib.Path.home() / ".openrouter-key").read_text().strip(),
            "Content-Type": "application/json",
        },
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=900) as r:
        data = json.load(r)
    choice = data["choices"][0]
    target.write_text(choice["message"].get("content") or "", encoding="utf-8")
    meta = {
        "case": case,
        "requested_model": model,
        "actual_model": data.get("model"),
        "provider": data.get("provider"),
        "finish_reason": choice.get("finish_reason"),
        "seconds": round(time.time() - t0, 1),
        "usage": data.get("usage"),
    }
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return f"{case} {model}: {meta['finish_reason']} {meta['seconds']}s cost={(data.get('usage') or {}).get('cost')}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=MODELS)
    ap.add_argument("--cases", nargs="*", default=list(CASES))
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    jobs = [(m, c) for m in a.models for c in a.cases]
    with cf.ThreadPoolExecutor(10) as ex:
        futs = {ex.submit(run, m, c): (m, c) for m, c in jobs}
        for f in cf.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:  # report and continue; no blind retries
                print(f"ERROR {futs[f]}: {e}", flush=True)


if __name__ == "__main__":
    main()
