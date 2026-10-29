# Variants test: results (2026-10-29)

Design and analysis as fixed in `preregister.md`; incidents in `deviations.md`.

## What was run
- 120 pairs (29 AIME 2025, 91 MATH-500 level 5), each a public item and a verified equivalent variant
  (`selection.json`; 135/137 variants passed the blind check, 2 rejected and listed there).
- 7 models × 120 pairs × 2 versions × 2 runs = 3,360 runs, all through Claude Code, all completed.
  Spend: 48.81 USD on OpenRouter; Opus and Fable on Max plan usage.
- Automatic grading by the last `\boxed{}`. 60 runs had no boxed answer, 12 truncated at 32k tokens
  (GLM 10, Qwen 2), 3 boxed but non-numeric; all count as wrong. A hand check of 20 graded runs per
  model found no grading error.

## Primary result (n = 120 pairs)
| Model | Original | Variant | Drop | Excess drop | 95% CI | Holm p |
|---|---|---|---|---|---|---|
| Opus 5 | 0.971 | 0.971 | 0.000 | −0.002 | [−0.028, 0.024] | 1.00 |
| Fable 5 | 0.983 | 0.988 | −0.004 | −0.007 | [−0.031, 0.017] | 1.00 |
| Kimi K3.1 Pro | 0.967 | 0.958 | 0.008 | 0.008 | [−0.026, 0.040] | 1.00 |
| Gemini 4 Argon | 1.000 | 1.000 | 0.000 | −0.002 | [−0.020, 0.017] | 1.00 |
| DeepSeek V4 Pro | 0.875 | 0.833 | 0.042 | 0.047 | [−0.008, 0.103] | 0.69 |
| Qwen3.8 2.4T | 0.983 | 0.983 | 0.000 | −0.002 | [−0.031, 0.024] | 1.00 |
| GLM 5.3 | 0.921 | 0.954 | −0.033 | −0.041 | [−0.083, −0.002] | 0.36 |

No model meets the preregistered criterion (positive excess drop with Holm p < 0.05). At this sample
size, none shows a detectable familiarity signal on these two sets.

## Secondary
- Sensitivity, excluding the 26 items where any run of any model had no boxed answer (n = 94): still no
  signal; DeepSeek's excess drop shrinks to 0.011, Kimi's is 0.023 (CI [0.001, 0.050], Holm p 0.56).
- AIME only (n = 29, descriptive): DeepSeek 0.759 → 0.672, Kimi 0.897 → 0.862, Fable 0.966 → 0.948;
  Opus, Qwen and GLM do better on the variants; Gemini 1.000 on both.

## How far this goes
- **Ceiling.** Five of seven models score 0.96–1.00 on both versions; Gemini solves every run of every
  item. A model at ceiling has no room to drop, so this test cannot say much about Gemini, and little
  about the others on MATH-500, which is saturated. A harder set (recent olympiad problems) would be
  needed to test the frontier models where they still fail.
- **What "no signal" means.** The CIs rule out drops larger than about 3–4 points for most models,
  10 points for DeepSeek. It does not show that no model was tuned on public benchmarks, only that
  replacing these items with equivalents does not cost them accuracy.
- The variants and the blind check were written by a Claude model. Answers were often in Spanish
  (Claude Code language setting), the same for every model and version.
- One aside, not data: in the blind check of aime25-01, the Claude solver answered the original's 70
  to the variant, reading `18_b` as `b+7` as in the public `17_b`. The variant was rejected by rule.
