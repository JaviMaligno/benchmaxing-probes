# Deviations and incidents, hard bank (logged before looking at per-model results)

- 2026-10-29, cost stop: after 33 runs (APEX first, by id order) the OpenRouter cost was about 0.40 USD
  per run, mostly because models hit the 32k output cap and Claude Code keeps retrying up to 128k tokens
  (Qwen 0.78 USD per truncated run). The run was stopped; in-flight runs discarded (`runs/restarts.log`).
- A cost measurement on four HMMT/CMIMC items (rep 1, all seven models, both versions: hmmt2024-10,
  hmmt2025-15, cmimc2025-20, cmimc2025-35) gave 0.43 USD per item-version for the five OpenRouter
  models. These runs follow the protocol and are kept as data.
- Decision by the operator (Javier), on cost only: APEX 2025 (12 items) is excluded from the analysis
  entirely, and the bank runs **one** run per model, item and version instead of two. The APEX runs
  already made stay in `runs/` and are not analysed. `selection.json` now has 91 pairs; the frozen
  list with APEX is `selection-with-apex.json`. Item score = the single run (0 or 1).
- Grader as in the first bank (including its fixes). The same preregistered rules apply to truncation and
  missing `\boxed{}` answers.
- 2026-10-29/30, Max plan limit: 148 Claude runs (Opus 74, Fable 74) returned "You've hit your 5-hour limit"
  instead of an answer. This is an infrastructure failure, so they are re-run as preregistered; the
  failed outputs are kept in `runs/_limit-hit/`. The first bank had none.
