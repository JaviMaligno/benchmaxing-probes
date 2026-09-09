# Qualitative assessment against preregistered criteria
Date: 2026-09-09. Assessor: the same Codex assistant that drafted the cases; not independent or blind. Human editorial review pending. No aggregate ranking.

## D1 — double charge
Both find changed request IDs, disabled guard, tenant namespace and 24h/72h mismatch. Opus adds a durable intent before capture but leaves pending retry/ownership transitions incomplete. Fable checks final rows before sending but still records only after capture; it calls a post-expiry duplicate unavoidable rather than developing a safe stop. This calibration does not favor a general claim of Fable superiority.

## D2 — warehouse / D2b — printing
Both models in both variants address stable composite keys, durable intent and uncertainty outside the remote deduplication horizon. Both allow additional senders inside a locally checked window while an earlier sender can remain paused indefinitely. This violates the explicit at-most-one priority under an allowed schedule.
Counterexample: A completes its final local check and pauses; B sends at t=1h and finishes; A resumes at t=50h for D2 or t=10h for D2b. Remote deduplication has expired: two effects. DB fencing of receipt writes is too late. A time margin gives no guarantee for indefinite pauses.
Fable D2 acknowledges that the margin makes the race negligible, not impossible; no pause distribution was supplied. Fable D2b acknowledges the residual but then says stopping never sacrifices safety. Opus D2 claims the window and lease prevent the harmful overlap; its trace covers a worker paused AFTER sending, not the before-send schedule requested. Opus D2b calls the final check best-effort and nevertheless labels at-most-once prevention guaranteed.
A valid conservative reference design can grant exactly one durable non-transferable emission permit and refuse automated resend after arming that permit. The one permitted worker may eventually send once, or a crash before send may produce zero. The task explicitly allows uncertain work to remain blocked. This assumes client/network libraries do not silently retry beyond the modelled call. It is a safety reference, not a production implementation or exactly-once/liveness guarantee.
check_counterexample.py is a deliberately minimal model of this schedule, not execution of code written by either tested model. It verifies the two remote effects and the reference's one effect.

## D3 — permissions
Both give the eight central decisions correctly: allow C1; deny C2/C3; allow C4 without amounts; deny C5/C6/C7/C8. Both address identity/scope and role/permission changes plus deleted/restricted data invalidation. This is coverage of central criteria, not a claim that every sentence or implementation detail is perfect. The transcript is supplied as one prompt, not real multi-turn interaction.

## D4 — task mix and cost
Both compute the requested rates and times, distinguish percentage points/relative changes (rounding +170%), account for failure repair, and qualify causal inference and transport. Core arithmetic matches check_counterexample.py. This case does not discriminate these two runs; retain it rather than selecting on a preferred winner.

## Limits and accounting
Five cases per model, one comparable completed response per case; two cases share a mechanism. Cases were authored with a model; no dataset representativeness, repeatability estimate, independent judging or training-cause identification. Diagnostics/truncated runs excluded from comparisons. D2/D2b were written AFTER seeing D1. No claims about long repository sessions or human time saved.
All eight phase-2 runs succeeded/end_turn with exact requested model and overage=false. Phase-2 API-equivalent list cost: 1.270405 USD. Comparable D1 pair: 0.3565755 USD. Total equivalent for the ten compared responses: 1.6269805 USD. Prior diagnostic/truncated attempts have separate costs; original interrupted run unmeasured. These figures are not extra Max charges.
