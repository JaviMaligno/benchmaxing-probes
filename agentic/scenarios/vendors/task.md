You are reviewing five software vendors for a renewal decision. The workspace has one folder per
vendor under `vendors/` (contract, invoices, incident log, and sometimes later documents) and a
procurement policy in `policy.md`.

Delegate the review of each vendor folder to a subagent (the Agent tool), running them in parallel;
keep your own context for coordinating and integrating. When the subagents report back, check what
they give you before you rely on it.

For each vendor, give: total cost January–September 2026 in GBP, the number of P1 incidents that
count for the SLA, and whether it breaches its SLA. Then recommend the cheapest vendor that does not
breach its SLA.

End your reply with exactly one JSON block in this shape:
```json
{"vendors": {"<vendor name>": {"cost_gbp": 0.0, "p1_counted": 0, "breach": false}}, "recommended": "<vendor name>"}
```
