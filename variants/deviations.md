# Deviations and incidents (logged while running, before looking at per-model results)

- 2026-10-29, restart: the runner was restarted with 24 workers instead of 12 (throughput only). Runs in
  flight at the restart were discarded and run again from scratch. See `runs/restarts.log`.
- Truncation at the 32k output cap (GLM, Qwen on some AIME items): counted as wrong, never re-run, as
  preregistered. Flagged `truncated` in `grades.json`.
- The harness gives no tools and one turn. About 3% of runs end with the model announcing a Python check
  or writing a tool call, with no `\boxed{}` answer. They count as wrong as preregistered (no boxed answer
  = wrong). Added, as a secondary sensitivity analysis not in the preregistration: the same analysis
  excluding every item where any run of any model has no boxed answer (`analyze.py --sensitivity`).
- Claude Code applied the operator's language setting, so many answers are written in Spanish. The prompt
  is English and identical across versions and models.
- Grader fixes applied to all runs: doubled backslashes (`\\frac`) and a one-element set (`\{3\}`).
