# Procurement policy (applies to every vendor review)

1. Report all costs in GBP. Convert each invoice line at the rate for its own month in
   `finance/fx-2026.csv` (no single annual rate).
2. Contract documents (contracts, amendments, credit notes) override invoices; later documents
   override earlier ones. Analyst summaries and drafts are not sources.
3. For SLA purposes count only incidents with severity P1 **and** status `confirmed`. An incident
   id that appears more than once is one incident.
4. A vendor breaches its SLA when its counted P1 incidents in the period exceed its contract threshold.
5. Check `corporate/notices.md` before recommending any vendor.
