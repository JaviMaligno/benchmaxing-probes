# Expansion (2026-10-28): five more models, repeats of D2/D2b

## What was run
- **Round 1, all five cases, one run per model:** Kimi K3.1 Pro, Gemini 4 Argon, DeepSeek V4 Pro (0813), Qwen3.8 2.4T-A95B and GLM 5.3. They ran through OpenRouter's chat API (`run_openrouter.py` → `openrouter/`), with no system prompt, reasoning effort high and 16,384 max tokens. The prompts are the frozen Spanish ones. Claude's round-1 answers are the original September runs.
- **Repeats, D2 and D2b × 3 per model, seven models:** these ran through Claude Code 2.1.312 (`run_claude_code.py` → `repeats/`), with the same options as the September runs: effort high, no tools, safe mode, strict MCP config, one turn and `CLAUDE_CODE_MAX_OUTPUT_TOKENS=8192`. Opus 5 and Fable 5 used the first-party Max login. The other five used the same harness pointed at OpenRouter's Anthropic-compatible endpoint. It is not verified that `--effort high` reaches the non-Claude models the same way.
- All 67 runs ended with stop/end_turn on the requested model. Spend: 2.09 USD on OpenRouter. The Claude repeats used Max plan usage.

## Grading
Blind grading was done by subagents. Answers were shuffled and relabelled; the mappings are in `grading/`. The criteria are the preregistered ones in `criteria.json`. Criterion 5 was operationalised with the four-step schedule from `assessment.md`: A checks and pauses, B sends, the dedup record expires, A sends. The round-1 judge also graded the September Opus/Fable answers blind and reproduced their published verdicts (D1 incomplete, D2/D2b guarantee fails, D3/D4 covered). The grader is a model, as before; it is neither human nor independent of the model family tested.

## Criterion 5 (at most one external effect): runs where the guarantee holds
| Model | D2 | D2b | Total |
|---|---|---|---|
| Opus 5 | 0/4 | 0/4 | 0/8 |
| Fable 5 | 0/4 | 0/4 | 0/8 |
| Kimi K3.1 Pro | 3/4 | 4/4 | 7/8 |
| Gemini 4 Argon | 2/4 | 4/4 | 6/8 |
| DeepSeek V4 Pro | 0/4 | 2/4 | 2/8 |
| Qwen3.8 2.4T | 0/4 | 2/4 | 2/8 |
| GLM 5.3 | 0/4 | 1/4 | 1/8 |

Each cell is one round-1 run plus three repeats. Per-run verdicts are in `grading/criterion5-verdicts.json`.

The failing designs share one transition. After a lease expires, B automatically takes over an in-flight item inside a time window (the dedup horizon minus a margin), protected only by DB-side fencing. The holding designs never transfer the emission permit: an abandoned in-flight item goes to a blocked/uncertain state for review, and a crash before send can leave zero effects.

## Other cases (round 1 only, one run each)
- **D1:** only Gemini 4 Argon is complete: an intent row before capture, retry with the same key under 24 h, and a stop for manual reconciliation at or after 24 h. Every other model, including Opus and Fable, is incomplete.
- **D3:** all seven models meet every criterion.
- **D4:** all figures are correct for all seven. DeepSeek is partial (it does not rebut "triplica" and states the projection as fact in its rewrite). Qwen omits the relative improvement.

## Limits
These are synthetic cases authored with a model, and D2/D2b share a mechanism. Rounds 1 and 2 used two harnesses for the non-Claude models. Four runs per model and case cannot give a precise rate. This shows that the D2/D2b failure is not shared by all frontier models. It does not show how any model was trained, and it says nothing about benchmaxing of Opus specifically: Fable fails the same way.
