# Variants test, hard bank: fixed before running

Date: 2026-10-29. Written after the first bank (`../variants/`) and before any model run on this one.

## Why a second bank
In the first bank five of seven models scored 0.96–1.00 on both versions and Gemini solved every run:
a ceiling that leaves no room to drop. This bank uses harder public final-answer competitions so the
frontier models still fail on some items.

## Items
- Source pool: every numeric-answer problem of HMMT February 2024 (27), HMMT February 2025 (29),
  CMIMC 2025 (39) and APEX 2025 (12), from MathArena on HuggingFace: 107 items (`pool.jsonl`).
  Chosen by competition difficulty, not by any model's results on them.
- Variants, verification and acceptance exactly as in `../variants/preregister.md` (same workflow;
  integer-answer originals get integer-answer variants). No cap: every accepted pair is used.

## Runs, grading, analysis
Identical to `../variants/preregister.md`: same seven models, same Claude Code harness and options
(including the 32k output cap), same prompt template, two runs per model, item and version, same grader
with its parser fixes from the first bank, same primary analysis (excess drop vs the other six, item
bootstrap CI, sign-flip test, Holm) and the same no-boxed sensitivity analysis. Spend ceiling: 90 USD on
OpenRouter.

## Known limits, stated in advance
- Everything listed for the first bank.
- Selection on the variant side: a variant is kept only if the Claude blind solver gets it right, while
  the original is kept whatever its difficulty. Accepted variants may therefore be easier than their
  originals, and closer to what Claude can solve. The cohort control absorbs a uniform shift; it does
  not absorb a shift that favours Claude, which is reported as a limit.
- Truncation at 32k is expected to be more frequent; it counts as wrong for both versions.
