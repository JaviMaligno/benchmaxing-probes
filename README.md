# Benchmaxing: local probes accompanying the article

Two exact model IDs: `claude-opus-5`, `claude-fable-5`; Claude Code 2.1.266, first-party Claude.ai Max, effort high, no tools, safe mode, strict MCP configuration, 8192 output tokens, one turn, fresh sessions. Models receive the identical Spanish case per pair.

- `D1-prompt.txt` and `D1-*-fixed-answer.md`: comparable calibration pair.
- `D2.txt`, `D2b.txt`, `D3.txt`, `D4.txt`: frozen expansion prompts.
- `*-answer.md`: complete response text reconstructed from text blocks.
- `preregister.md`, `criteria.json`: expansion criteria fixed before its runs.
- `manifest.json`, `calibration-manifest.json`: per-run usage and outcome metadata.
- `assessment.md`: qualitative adjudication, limits and costs.
- `check_counterexample.py`: offline schedule counterexample and arithmetic oracle.
- `counterexample-results.json`: output of that check.
- `protocol.md`, `execution-review.md`: historical diagnostic record; later corrections supersede earlier status statements.

The export omits private chain-of-thought/signature blocks, raw CLI initialization, machine paths in logs, session identifiers and auth data. Historical prose filenames are retained so the corrections remain auditable. Timing is process wall time, not a controlled latency benchmark.

## Recheck without calling models

`python check_counterexample.py`

## Re-run one case (consumes your plan usage)

With Claude Code authenticated, use a fresh process, supply the selected UTF-8 prompt on stdin, then close stdin. Example options:

`claude -p --model claude-opus-5 --effort high --safe-mode --strict-mcp-config --tools= --no-session-persistence --max-turns 1 --max-budget-usd 0.65 --output-format stream-json --verbose`

Set `CLAUDE_CODE_MAX_OUTPUT_TOKENS=8192` for that process; capture stdout/stderr separately. Substitute `claude-fable-5` for the paired run. Check the emitted actual model, end_turn, success and no paid overage. Sum all assistant text blocks; result alone can omit earlier fragments after continuation. Stop and inspect errors rather than retrying blindly. `max-turns` is not a hard HTTP-request limit and the budget option is not a guarantee against one in-flight request overshooting.

The experiment used one valid run per case/model. It cannot estimate variability, establish an overall winner, or demonstrate how either model was trained.

## Read the article

The accompanying article is a draft awaiting review. This repository contains the evidence, not a general model ranking. Prompts and responses can be read directly on GitHub; use Code → Download ZIP or clone the repository to run the offline check.
