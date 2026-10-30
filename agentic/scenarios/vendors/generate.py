"""Scenario "vendors": a conductor must delegate five vendor folders to subagents and integrate.

Writes the sandbox (workspace/), the task prompt (task.md) and the answer key (key.json), seeded.
Coordination traps, each scored separately:
  - policy: invoices of one vendor are in EUR; the conversion rate and the "count only P1 incidents
    with status confirmed" rule live in workspace/policy.md, outside the vendor folders, so the
    conductor has to pass them to its subagents (or apply them itself);
  - amendment: one vendor has a later amendment that changes its unit price from a given date;
  - duplicates: one incident log repeats incident ids, which must be counted once.
"""
import csv
import datetime as dt
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).parent
WS = ROOT / "workspace"
SEED = 20261030
EUR_TO_GBP = 0.86

VENDORS = [
    # name, currency, unit price per seat-month, seats, P1 threshold, amendment (date, new price) or None
    ("Halden Systems", "GBP", 42.0, 120, 3, None),
    ("Norvik Data", "EUR", 39.0, 140, 4, None),
    ("Quarry Labs", "GBP", 51.0, 90, 2, ("2026-07-01", 44.0)),
    ("Tessel Cloud", "GBP", 36.5, 160, 3, None),
    ("Ombra Analytics", "GBP", 40.0, 125, 5, None),
]
DUPLICATE_VENDOR = "Tessel Cloud"


def months():
    return [dt.date(2026, m, 1) for m in range(1, 10)]  # January to September 2026


def main():
    rng = random.Random(SEED)
    if WS.exists():
        for p in sorted(WS.rglob("*"), reverse=True):
            p.unlink() if p.is_file() else p.rmdir()
    WS.mkdir(parents=True)
    (WS / "policy.md").write_text(
        "# Procurement policy (applies to every vendor review)\n\n"
        f"1. Report all costs in GBP. Convert EUR invoices at the fixed internal rate 1 EUR = {EUR_TO_GBP} GBP.\n"
        "2. For SLA purposes count only incidents with severity P1 **and** status `confirmed`.\n"
        "   Incidents marked `disputed` or `withdrawn` do not count.\n"
        "3. An incident id that appears more than once in a log is one incident.\n"
        "4. A vendor breaches its SLA when its counted P1 incidents in the period exceed the threshold\n"
        "   in its contract.\n", encoding="utf-8")
    key = {"vendors": {}}
    for name, cur, price, seats, threshold, amendment in VENDORS:
        slug = name.lower().replace(" ", "-")
        d = WS / "vendors" / slug
        d.mkdir(parents=True)
        (d / "contract.md").write_text(
            f"# Master services agreement — {name}\n\nCurrency: {cur}\n"
            f"Price: {price:.2f} {cur} per seat per month, invoiced monthly in arrears.\n"
            f"SLA: no more than {threshold} P1 incidents in any nine-month review period.\n"
            "Term: 1 January 2026 to 31 December 2027.\n" + "\nBoilerplate clause.\n" * 40, encoding="utf-8")
        total = 0.0
        with open(d / "invoices.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["invoice_id", "period", "seats", "unit_price", "currency", "amount"])
            for k, m in enumerate(months()):
                s = seats + rng.randint(-6, 6)
                up = price
                if amendment and m >= dt.date.fromisoformat(amendment[0]):
                    up = amendment[1]
                # invoices before the amendment was signed still show the old price for July: the
                # amendment says the July invoice must be re-rated (a credit note follows)
                shown = price if (amendment and m == dt.date(2026, 7, 1)) else up
                w.writerow([f"{slug[:3].upper()}-{2026}{k + 1:02d}", m.isoformat()[:7], s, f"{shown:.2f}", cur,
                            f"{s * shown:.2f}"])
                total += s * up
        if amendment:
            (d / "amendment-2026-06.md").write_text(
                f"# Amendment No. 1 — {name}\n\nSigned 20 June 2026.\n\n"
                f"From {amendment[0]} the price is {amendment[1]:.2f} {cur} per seat per month.\n"
                "Any invoice issued at the old price for a period on or after that date is re-rated at the new\n"
                "price; the difference is settled by credit note.\n", encoding="utf-8")
        gbp = total * (EUR_TO_GBP if cur == "EUR" else 1.0)
        # incidents
        rows, counted = [], 0
        n = rng.randint(6, 10)
        for i in range(n):
            sev = rng.choice(["P1", "P2", "P2", "P3"])
            status = rng.choice(["confirmed", "confirmed", "confirmed", "disputed", "withdrawn"])
            rows.append([f"INC-{slug[:2].upper()}{100 + i}", f"2026-{rng.randint(1, 9):02d}-{rng.randint(1, 28):02d}", sev,
                         status])
            counted += sev == "P1" and status == "confirmed"
        # make the SLA outcome interesting: force a known number of counted P1s around the threshold
        target = {"Halden Systems": 2, "Norvik Data": 5, "Quarry Labs": 2, "Tessel Cloud": 3, "Ombra Analytics": 6}[name]
        rows = [r for r in rows if not (r[2] == "P1" and r[3] == "confirmed")]
        for j in range(target):
            rows.append([f"INC-{slug[:2].upper()}{200 + j}", f"2026-{rng.randint(1, 9):02d}-{rng.randint(1, 28):02d}", "P1",
                         "confirmed"])
        # a disputed P1 everywhere, so the status rule matters
        rows.append([f"INC-{slug[:2].upper()}300", "2026-05-14", "P1", "disputed"])
        if name == DUPLICATE_VENDOR:  # repeat two confirmed P1 ids: raw count 5, true count 3
            rows += [r[:] for r in rows if r[2] == "P1" and r[3] == "confirmed"][:2]
        rng.shuffle(rows)
        with open(d / "incidents.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["incident_id", "opened", "severity", "status"])
            w.writerows(rows)
        key["vendors"][name] = {"cost_gbp": round(gbp, 2), "p1_counted": target, "breach": target > threshold}
    ok = {n: v for n, v in key["vendors"].items() if not v["breach"]}
    key["recommended"] = min(ok, key=lambda n: ok[n]["cost_gbp"])
    key["traps"] = {"policy_vendor": "Norvik Data", "amendment_vendor": "Quarry Labs", "duplicate_vendor": DUPLICATE_VENDOR}
    (ROOT / "key.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
    (ROOT / "task.md").write_text(
        "You are reviewing five software vendors for a renewal decision. The workspace has one folder per\n"
        "vendor under `vendors/` (contract, invoices, incident log, and sometimes later documents) and a\n"
        "procurement policy in `policy.md`.\n\n"
        "Delegate the review of each vendor folder to a subagent (the Agent tool), running them in parallel;\n"
        "keep your own context for coordinating and integrating. When the subagents report back, check what\n"
        "they give you before you rely on it.\n\n"
        "For each vendor, give: total cost January–September 2026 in GBP, the number of P1 incidents that\n"
        "count for the SLA, and whether it breaches its SLA. Then recommend the cheapest vendor that does not\n"
        "breach its SLA.\n\n"
        "End your reply with exactly one JSON block in this shape:\n"
        "```json\n{\"vendors\": {\"<vendor name>\": {\"cost_gbp\": 0.0, \"p1_counted\": 0, \"breach\": false}},"
        " \"recommended\": \"<vendor name>\"}\n```\n", encoding="utf-8")
    print(json.dumps(key, indent=1))


if __name__ == "__main__":
    main()
