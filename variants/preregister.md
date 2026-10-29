# Variants test (GSM1k-style), fixed before running

Date: 2026-10-29. Written before any model was run on the originals or the variants.

## Question
Does any of the seven models lose more accuracy than the others when a public competition math
item is replaced by an equivalent variant it cannot have seen? A larger drop than the cohort's is
a signal of familiarity with the public items. It is not evidence about intent or about how a model
was trained.

## Items
- Source pool: the 30 AIME 2025 problems (MathArena/aime_2025) and the 107 MATH-500 level-5
  problems with a numeric answer (HuggingFaceH4/MATH-500), 137 items (`pool.jsonl`).
- One variant per item, written by an agent with the same method and difficulty, different numbers
  or surface condition, and a different answer. `items/<id>/solve.py` computes the variant answer and
  must reproduce the original answer on the original data.
- A variant is accepted only if a second agent, given only the variant text, reaches the same answer
  and judges it well posed. Rejected items are dropped in pairs (the original goes too) and listed.
- If more than 120 pairs are accepted: keep every accepted AIME pair and sample the MATH pairs down to
  120 in total, stratified by subject, with Python `random.Random(20261029)`. The list is frozen in
  `selection.json` before the first model call.

## Runs
- Models: claude-opus-5, claude-fable-5, moonshotai/kimi-k3.1-pro, google/gemini-4-argon,
  deepseek/deepseek-v4-pro-0813, qwen/qwen3.8-2.4t-a95b, z-ai/glm-5.3.
- One harness for all: Claude Code (`claude -p`, effort high, no tools, safe mode, strict MCP config,
  one turn, `CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000`). Claude models on the Max login; the rest through
  OpenRouter's Anthropic-compatible endpoint.
- Prompt: the problem text plus one fixed instruction to reason and put the final answer in `\boxed{}`.
  Original and variant use the same template.
- Two runs per model, item and version. Jobs are interleaved (original and variant of an item in the
  same batch) so time-of-day or provider drift hits both versions alike.
- No manual retries on a wrong answer. A run is re-run only on an infrastructure failure (HTTP error,
  empty output, no stop reason), and every re-run is logged. A truncated run (max tokens) counts as
  wrong and is reported.
- Spend ceiling: 120 USD on OpenRouter for the whole test. Stop and report if it is reached.

## Grading
Automatic: the last `\boxed{}` of the answer, parsed to a number and compared with the reference at
relative tolerance 1e-6. No boxed answer = wrong. A sample of 20 graded answers per model is checked
by hand for parser errors; any parser fix is applied to all runs.

## Analysis
- Item score = mean of the two runs (0, 0.5, 1). Drop for model m = mean over items of
  (score on original − score on variant).
- Primary: excess drop of m = drop of m − mean drop of the other six models (the variants may be
  harder for everyone; the cohort is the control). 95% CI by item bootstrap (10,000 resamples, seed
  20261029). Two-sided paired sign-flip permutation test on the item-level differences, Holm-adjusted
  across the seven models.
- A model is reported as showing a familiarity signal only if its excess drop is positive and its
  Holm-adjusted p < 0.05. Everything else is reported as no detectable signal at this sample size,
  with the CI, not as "not benchmaxed".
- Secondary, descriptive only: the same per source (AIME, MATH-500) and the raw drop per model.

## Known limits, stated in advance
- The variants and the blind check were written by a Claude model (Opus 5.5 in Claude Code). That could
  make them closer to Claude's style; it is reported as a limit, not corrected.
- MATH-500 and AIME 2025 are only two public sets; a model can be tuned on other benchmarks without
  showing here.
- Very high accuracy on both versions leaves no room for a drop (ceiling); that is reported as such.
