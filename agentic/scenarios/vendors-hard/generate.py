"""Scenario "vendors-hard": fifteen vendor folders, too much to re-read alone, and traps that sit across
folders or that a subagent working on one folder is likely to fall into.

Traps (each scored on the vendor fields it decides, listed in key.json):
  - fx_monthly: EUR and USD vendors convert at the month's rate in finance/fx-2026.csv (policy), not at
    one rate; the folders do not contain the rates;
  - amendment_chain: one vendor has amendment 1 (price cut) and amendment 2, which cancels amendment 1;
  - credit_note: one vendor has a retroactive credit note that reduces the total;
  - stale_summary: four folders contain a draft analyst summary with wrong totals and counts;
  - duplicates: two incident logs repeat incident ids;
  - status_rule: P1 counts only when status is confirmed (policy);
  - acquisition: corporate/notices.md says one vendor was acquired and its contract ends; it is not
    eligible for the recommendation even though its own folder does not say so.
Deliverable: per-vendor cost, counted P1, breach; the three cheapest eligible vendors, cheapest first.
"""
import csv
import datetime as dt
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).parent
WS = ROOT / "workspace"
SEED = 20261031
SERVICES = ["platform", "support", "storage", "api-calls"]
NAMES = ["Halden Systems", "Norvik Data", "Quarry Labs", "Tessel Cloud", "Ombra Analytics", "Larch Compute",
         "Vesper Metrics", "Ironbark IT", "Cobalt Ledger", "Fennel Networks", "Marlow Secure", "Pellucid AI",
         "Strand Hosting", "Kestrel Ops", "Brightwater Data"]
CURRENCY = {"Norvik Data": "EUR", "Cobalt Ledger": "EUR", "Pellucid AI": "USD", "Kestrel Ops": "USD", "Larch Compute": "EUR"}
AMEND_CHAIN = "Vesper Metrics"
CREDIT = "Strand Hosting"
STALE = ["Halden Systems", "Ironbark IT", "Fennel Networks", "Brightwater Data"]
DUPES = ["Tessel Cloud", "Marlow Secure"]
ACQUIRED = "Ironbark IT"


def slug(n):
    return n.lower().replace(" ", "-")


def main():
    rng = random.Random(SEED)
    if WS.exists():
        for p in sorted(WS.rglob("*"), reverse=True):
            p.unlink() if p.is_file() else p.rmdir()
    (WS / "finance").mkdir(parents=True)
    (WS / "corporate").mkdir()
    months = [dt.date(2026, m, 1) for m in range(1, 10)]
    fx = {m: {"EUR": round(0.84 + 0.004 * i + rng.uniform(-0.003, 0.003), 4),
              "USD": round(0.78 + 0.003 * i + rng.uniform(-0.003, 0.003), 4)} for i, m in enumerate(months)}
    with open(WS / "finance" / "fx-2026.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "EUR_to_GBP", "USD_to_GBP"])
        for m in months:
            w.writerow([m.isoformat()[:7], fx[m]["EUR"], fx[m]["USD"]])
    (WS / "policy.md").write_text(
        "# Procurement policy (applies to every vendor review)\n\n"
        "1. Report all costs in GBP. Convert each invoice line at the rate for its own month in\n"
        "   `finance/fx-2026.csv` (no single annual rate).\n"
        "2. Contract documents (contracts, amendments, credit notes) override invoices; later documents\n"
        "   override earlier ones. Analyst summaries and drafts are not sources.\n"
        "3. For SLA purposes count only incidents with severity P1 **and** status `confirmed`. An incident\n"
        "   id that appears more than once is one incident.\n"
        "4. A vendor breaches its SLA when its counted P1 incidents in the period exceed its contract threshold.\n"
        "5. Check `corporate/notices.md` before recommending any vendor.\n", encoding="utf-8")
    (WS / "corporate" / "notices.md").write_text(
        "# Corporate notices\n\n- 2026-03-02: office move to Level 4, no change to supplier contacts.\n"
        f"- 2026-08-18: {ACQUIRED} has been acquired by a competitor of ours. Its master services agreement\n"
        "  terminates on 31 December 2026 and it is **not eligible** for renewal.\n"
        "- 2026-09-01: new expense tool from October.\n", encoding="utf-8")
    key = {"vendors": {}, "traps": {k: [] for k in
           ["fx_monthly", "amendment_chain", "credit_note", "stale_summary", "duplicates", "status_rule", "acquisition"]}}
    for name in NAMES:
        d = WS / "vendors" / slug(name)
        d.mkdir(parents=True)
        cur = CURRENCY.get(name, "GBP")
        base = {s: round(rng.uniform(800, 2400), 2) for s in SERVICES}
        if name == ACQUIRED:  # cheap enough that ignoring the notice changes the top three
            base = {s: round(v * 0.75, 2) for s, v in base.items()}
        threshold = rng.choice([2, 3, 4])
        (d / "contract.md").write_text(
            f"# Master services agreement — {name}\n\nCurrency: {cur}\nInvoiced monthly, one line per service.\n"
            f"SLA: no more than {threshold} P1 incidents in any nine-month review period.\n"
            "Term: 1 January 2026 to 31 December 2027.\n" + "\nStandard clause text.\n" * 30, encoding="utf-8")
        total = 0.0
        with open(d / "invoices.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["invoice_id", "period", "service", "amount", "currency"])
            for k, m in enumerate(months):
                rate = fx[m][cur] if cur != "GBP" else 1.0
                for s in SERVICES:
                    if s == "api-calls":  # metered daily: one line per day
                        days = (months[k + 1] if k + 1 < len(months) else dt.date(2026, 10, 1)) - m
                        for day in range(days.days):
                            amt = round(base[s] / 30 * rng.uniform(0.6, 1.4), 2)
                            w.writerow([f"{slug(name)[:3].upper()}-{k + 1:02d}-api-{day + 1:02d}", m.isoformat()[:7], s,
                                        f"{amt:.2f}", cur])
                            total += amt * rate
                        continue
                    amt = round(base[s] * rng.uniform(0.9, 1.1), 2)
                    w.writerow([f"{slug(name)[:3].upper()}-{k + 1:02d}-{s[:3]}", m.isoformat()[:7], s, f"{amt:.2f}", cur])
                    total += amt * rate
        if name == AMEND_CHAIN:
            (d / "amendment-1-2026-04.md").write_text(
                f"# Amendment No. 1 — {name}\n\nSigned 10 April 2026. From 2026-05 all platform lines are discounted\n"
                "by 20%, settled by credit note at year end.\n", encoding="utf-8")
            (d / "amendment-2-2026-05.md").write_text(
                f"# Amendment No. 2 — {name}\n\nSigned 28 May 2026. Amendment No. 1 is cancelled in full; no\n"
                "discount applies to any period. Invoiced amounts stand.\n", encoding="utf-8")
            key["traps"]["amendment_chain"].append([name, "cost"])
        if name == CREDIT:
            credit = 3150.00
            (d / "credit-note-CN-0042.md").write_text(
                f"# Credit note CN-0042 — {name}\n\nIssued 30 September 2026 for SLA service credits covering\n"
                f"January–September 2026: {credit:.2f} {cur}. It reduces the period cost.\n", encoding="utf-8")
            total -= credit
            key["traps"]["credit_note"].append([name, "cost"])
        # incidents with a known counted number
        target = rng.choice([threshold - 1, threshold, threshold + 1, threshold + 2])
        target = max(target, 0)
        rows = []
        for i in range(rng.randint(5, 9)):
            rows.append([f"INC-{slug(name)[:3].upper()}{100 + i}", f"2026-{rng.randint(1, 9):02d}-{rng.randint(1, 28):02d}",
                         rng.choice(["P2", "P3"]), rng.choice(["confirmed", "disputed", "withdrawn"])])
        for j in range(target):
            rows.append([f"INC-{slug(name)[:3].upper()}{200 + j}", f"2026-{rng.randint(1, 9):02d}-{rng.randint(1, 28):02d}", "P1", "confirmed"])
        for j in range(rng.randint(1, 2)):
            rows.append([f"INC-{slug(name)[:3].upper()}{300 + j}", f"2026-{rng.randint(1, 9):02d}-{rng.randint(1, 28):02d}", "P1",
                         rng.choice(["disputed", "withdrawn"])])
        key["traps"]["status_rule"].append([name, "p1"])
        if name in DUPES and target:
            rows += [r[:] for r in rows if r[2] == "P1" and r[3] == "confirmed"][:2]
            key["traps"]["duplicates"].append([name, "p1"])
        rng.shuffle(rows)
        with open(d / "incidents.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["incident_id", "opened", "severity", "status"])
            w.writerows(rows)
        if name in STALE:
            (d / "analyst-summary-DRAFT.md").write_text(
                f"# {name}: review summary (draft, figures as of May 2026)\n\n"
                f"- Total cost Jan–Sep 2026: {total * rng.uniform(0.55, 0.7):.2f} GBP\n"
                f"- P1 incidents: {target + 2}\n- SLA: {'breached' if target + 2 > threshold else 'met'}\n\n"
                "Prepared by the previous analyst. To be finalised.\n", encoding="utf-8")
            key["traps"]["stale_summary"].append([name, "cost"])
        if cur != "GBP":
            key["traps"]["fx_monthly"].append([name, "cost"])
        key["vendors"][name] = {"cost_gbp": round(total, 2), "p1_counted": target, "breach": target > threshold}
    eligible = {n: v for n, v in key["vendors"].items() if not v["breach"] and n != ACQUIRED}
    key["recommended"] = sorted(eligible, key=lambda n: eligible[n]["cost_gbp"])[:3]
    ok_all = {n: v for n, v in key["vendors"].items() if not v["breach"]}
    key["acquisition_matters"] = ACQUIRED in sorted(ok_all, key=lambda n: ok_all[n]["cost_gbp"])[:3]
    key["traps"]["acquisition"] = [[ACQUIRED, "recommended"]]
    (ROOT / "key.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
    (ROOT / "task.md").write_text(
        "You are reviewing fifteen software vendors for a renewal decision. The workspace has one folder per\n"
        "vendor under `vendors/`, a procurement policy in `policy.md`, finance data in `finance/` and company\n"
        "notices in `corporate/`.\n\n"
        "Delegate the vendor folders to subagents (the Agent tool), running them in parallel; there is too\n"
        "much material for you to read it all yourself, so keep your own context for coordinating and\n"
        "integrating. Check what the subagents give you before you rely on it.\n\n"
        "For each vendor, give: total cost January–September 2026 in GBP, the number of P1 incidents that\n"
        "count for the SLA, and whether it breaches its SLA. Then recommend the three cheapest vendors that\n"
        "can be renewed, cheapest first.\n\n"
        "End your reply with exactly one JSON block in this shape, using the vendor names as written in the\n"
        "contracts:\n"
        "```json\n{\"vendors\": {\"<vendor name>\": {\"cost_gbp\": 0.0, \"p1_counted\": 0, \"breach\": false}},"
        " \"recommended\": [\"<vendor name>\", \"<vendor name>\", \"<vendor name>\"]}\n```\n", encoding="utf-8")
    print(json.dumps({"recommended": key["recommended"], "acquisition_matters": key["acquisition_matters"],
                      "breaches": [n for n, v in key["vendors"].items() if v["breach"]]}, indent=1))


if __name__ == "__main__":
    main()
