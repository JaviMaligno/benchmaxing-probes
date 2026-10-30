# Agentic study: results (2026-10-29)

Question: does a model that looks strong on benchmarks also hold up when it has to run a job through
subagents (delegate, pass the shared rules on, integrate, check)? Same harness for all seven models.

## Harness
- Claude Code headless (`claude -p --effort high`), Claude models on the Max login, the other five through
  OpenRouter's Anthropic-compatible endpoint. Subagents are the same model as the conductor.
- Tools: `Agent, Read, Glob, Grep` only. Bash was left out because the permission classifier blocks
  unattended Bash sessions; it also means sums over CSVs have to be done by reasoning.
- Fresh copy of the workspace per run; `--max-turns 40`, timeout 1 h, background subagents awaited.
- Scoring (`score.py`): the last JSON block of the conductor against `key.json`; cost within 1 GBP,
  counted P1 and breach exact; one score per trap; process measures from the transcript.

## Scenarios
- `vendors`: 5 vendor folders, policy outside the folders (EUR rate, confirmed-P1 rule), one amendment,
  one log with duplicate ids. 15 fields + recommendation.
- `vendors-hard`: 15 folders (~400K of material, daily-metered invoice lines), seven traps: monthly FX
  rates in a separate file, an amendment cancelled by a later one, a credit note, four stale draft
  summaries, duplicate incident ids, the confirmed-P1 rule, and an acquisition notice outside the vendor
  folders that removes a vendor otherwise in the top three. 45 fields + top three.

## Results (one run per model and scenario)
| Model | vendors | vendors-hard | Traps (hard) | Max parallel subagents (hard) | Conductor check reads (hard) | Time (hard) |
|---|---|---|---|---|---|---|
| Opus 5 | 15/15 | 45/45 | 7/7 | 5 | 8 | 40 min |
| Fable 5 | 15/15 | 45/45 | 7/7 | 5 | 7 | 10.5 min |
| Kimi K3.1 Pro | 15/15 | 45/45 | 7/7 | 15 | 42 | 23 min |
| Gemini 4 Argon | 15/15 | 45/45 | 7/7 | 5 | 35 | 40 min |
| DeepSeek V4 Pro | 15/15 | 45/45 | 7/7 | 5 | 26 | 13 min |
| GLM 5.3 | 15/15 | 45/45 | 7/7 | 15 | 31 | 8.5 min |
| Qwen3.8 2.4T | 15/15 | timeout | — | 5 | 0 | > 60 min |

All recommendations correct where an answer was given. Qwen on `vendors-hard`: four of its five
subagent groups finished; in the fifth, a nested subagent summing ~300 invoice lines by hand had not
finished after 55 minutes.

## Reading
- Both scenarios are at ceiling on accuracy. No model, Kimi and Gemini included, is worse at this kind of
  delegated work than its benchmark standing suggests; the study cannot rank them on accuracy.
- The differences are in process: how many subagents at once (5 or 15), how much the conductor re-reads
  to check its subagents (7–8 reads for the Claude models, 26–42 for the others), and wall time (8.5 to
  40 minutes). These are one run each and are observations, not a ranking.
- Qwen's failure is one run; it is not known whether it repeats.

## Deviations and cost
- The first `vendors-hard` pilot ran with harness faults (background subagents stopped after a 10-minute
  wait, Opus cut by a 10 USD budget flag, an empty result field); those runs are kept in
  `runs/vendors-hard/_invalid-harness/` and were re-run after the fix. Gemini's and Kimi's first runs
  were valid and are kept.
- The pilot overshot its 25 USD cap (39.41 USD) because the cap was only checked at session start; the
  runner now reserves spend per session in flight. Re-run: 22.85 USD. OpenRouter total for the agentic
  study: about 66 USD including `vendors`.
- A full run (3 runs per model) was not done: with both scenarios at ceiling it would not change the
  conclusion.
