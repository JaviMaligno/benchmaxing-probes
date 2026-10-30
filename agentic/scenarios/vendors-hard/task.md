You are reviewing fifteen software vendors for a renewal decision. The workspace has one folder per
vendor under `vendors/`, a procurement policy in `policy.md`, finance data in `finance/` and company
notices in `corporate/`.

Delegate the vendor folders to subagents (the Agent tool), running them in parallel; there is too
much material for you to read it all yourself, so keep your own context for coordinating and
integrating. Check what the subagents give you before you rely on it.

For each vendor, give: total cost January–September 2026 in GBP, the number of P1 incidents that
count for the SLA, and whether it breaches its SLA. Then recommend the three cheapest vendors that
can be renewed, cheapest first.

End your reply with exactly one JSON block in this shape, using the vendor names as written in the
contracts:
```json
{"vendors": {"<vendor name>": {"cost_gbp": 0.0, "p1_counted": 0, "breach": false}}, "recommended": ["<vendor name>", "<vendor name>", "<vendor name>"]}
```
