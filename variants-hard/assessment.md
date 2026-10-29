# Variants test, hard bank: results (2026-10-30)

Design in `preregister.md`; deviations (APEX dropped and one run instead of two, both on cost; 148
Claude runs re-run after a Max plan limit) in `deviations.md`.

## What was run
- 91 pairs: HMMT February 2024 (26), HMMT February 2025 (27), CMIMC 2025 (38). 103 of 107 variants
  passed the blind check; APEX 2025 (12) was then excluded on cost.
- 7 models × 91 pairs × 2 versions × 1 run = 1,274 runs, all through Claude Code, all completed.
  Spend on OpenRouter for this bank: 128.71 USD, including the APEX runs that were stopped.
- Same grader as the first bank, extended (last `=` segment, `\frac{a}5`, exact comparison for answers
  too large for a float), and re-applied to the first bank with no change to its results. 125 runs had
  no boxed answer and 30 were truncated; all count as wrong. A hand check of 20 graded runs per model
  found no grading error.

## Primary result (n = 91 pairs, one run each)
| Model | Original | Variant | Drop | Excess drop | 95% CI | Holm p |
|---|---|---|---|---|---|---|
| Opus 5 | 0.846 | 0.769 | 0.077 | 0.071 | [−0.016, 0.161] | 0.95 |
| Fable 5 | 0.901 | 0.846 | 0.055 | 0.046 | [−0.027, 0.123] | 1.00 |
| Kimi K3.1 Pro | 0.824 | 0.758 | 0.066 | 0.059 | [−0.057, 0.176] | 1.00 |
| Gemini 4 Argon | 0.978 | 0.989 | −0.011 | −0.031 | [−0.092, 0.026] | 1.00 |
| DeepSeek V4 Pro | 0.604 | 0.670 | −0.066 | −0.095 | [−0.212, 0.027] | 0.95 |
| Qwen3.8 2.4T | 0.901 | 0.912 | −0.011 | −0.031 | [−0.097, 0.035] | 1.00 |
| GLM 5.3 | 0.758 | 0.758 | 0.000 | −0.018 | [−0.106, 0.070] | 1.00 |

No model meets the preregistered criterion. As in the first bank, none shows a detectable familiarity
signal.

## Secondary
- Sensitivity, excluding the 40 items where any run of any model had no boxed answer (n = 51): still no
  signal. Opus's excess drop falls from 0.071 to 0.013; Kimi's is 0.082 (CI [−0.026, 0.196]).
- Opus left 34 of 182 runs without a boxed answer (14 originals, 20 variants): on hard items it writes
  tool calls the harness does not have, sometimes with invented outputs, and stops. Most of its raw drop
  comes from that, not from wrong answers.

## How far this goes
- The ceiling moved but did not go away for Gemini (0.978 and 0.989). It is the most accurate model on
  both banks and shows no drop on either; this test still cannot rule out familiarity for a model that
  solves almost everything.
- One run per item makes the CIs wide: drops below about 12–15 points cannot be excluded for Kimi,
  DeepSeek and GLM.
- The blind check keeps only variants a Claude model solved, which can make the variants easier and
  closer to Claude; the cohort control absorbs a uniform shift only.
- Everything else from `../variants/assessment.md` applies.
