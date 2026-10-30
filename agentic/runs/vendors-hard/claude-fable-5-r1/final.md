Todas las verificaciones cuadran: recalculé a mano el mes de enero de Kestrel Ops línea a línea (5.331,62 USD × 0,7816 = 4.167,19 GBP, idéntico al informe), y los umbrales de SLA, nombres contractuales, monedas, recuentos de incidentes de los candidatos y la nota de crédito de Strand coinciden con lo reportado por los subagentes. Aquí está el consolidado.

## Resultados por proveedor (enero–septiembre 2026)

| Proveedor | Coste total (GBP) | P1 contados | Umbral | ¿Incumple SLA? |
|---|---:|---:|---:|---|
| Halden Systems | 50.394,31 | 4 | 4 | No |
| Norvik Data | 50.989,43 | 6 | 4 | **Sí** |
| Quarry Labs | 69.935,30 | 4 | 4 | No |
| Tessel Cloud | 62.119,79 | 3 | 3 | No |
| Ombra Analytics | 57.037,31 | 3 | 2 | **Sí** |
| Larch Compute | 49.428,61 | 4 | 3 | **Sí** |
| Vesper Metrics | 78.466,33 | 3 | 4 | No |
| Ironbark IT | 36.687,16 | 3 | 3 | No |
| Cobalt Ledger | 46.280,48 | 4 | 4 | No |
| Fennel Networks | 48.962,26 | 3 | 2 | **Sí** |
| Marlow Secure | 45.137,43 | 5 | 4 | **Sí** |
| Pellucid AI | 47.325,62 | 2 | 2 | No |
| Strand Hosting | 44.736,33 | 1 | 2 | No |
| Kestrel Ops | 37.990,08 | 1 | 2 | No |
| Brightwater Data | 59.129,65 | 1 | 2 | No |

Notas clave del análisis:

- **Conversión FX**: Norvik Data y Cobalt Ledger facturan en EUR y Kestrel Ops y Pellucid AI en USD; cada línea se convirtió con el tipo de su propio mes según `finance/fx-2026.csv`, como exige la política. El resto factura en GBP.
- **Documentos contractuales**: la nota de crédito CN-0042 de Strand Hosting resta 3.150,00 GBP al periodo (47.886,33 → 44.736,33). En Vesper Metrics, la enmienda 2 (mayo) anula íntegramente el descuento del 20 % de la enmienda 1, así que no se aplica descuento alguno. Los cuatro `analyst-summary-DRAFT.md` (Halden, Ironbark, Fennel, Brightwater) se ignoraron por política; todos contenían cifras parciales ("as of May 2026") y recuentos de P1 que incluían incidentes `disputed`/`withdrawn`.
- **Incidentes**: solo cuentan P1 con estado `confirmed`, deduplicados por id (Tessel y Marlow tenían filas repetidas). Los casos al límite exacto del umbral (Tessel 3/3, Halden 4/4, Quarry 4/4, Cobalt 4/4, Pellucid 2/2, Ironbark 3/3) no incumplen, porque la política exige **exceder** el umbral.
- **Elegibilidad**: Ironbark IT es el más barato (36.687,16 GBP) y no incumple su SLA, pero el aviso corporativo del 18-08-2026 lo declara **no elegible para renovación** (adquirido por un competidor; su contrato termina el 31-12-2026), así que queda fuera de la recomendación.

## Recomendación

Los tres proveedores renovables más baratos (sin incumplimiento de SLA y elegibles), de más barato a más caro:

1. **Kestrel Ops** — 37.990,08 GBP
2. **Strand Hosting** — 44.736,33 GBP
3. **Cobalt Ledger** — 46.280,48 GBP

```json
{"vendors": {"Halden Systems": {"cost_gbp": 50394.31, "p1_counted": 4, "breach": false}, "Norvik Data": {"cost_gbp": 50989.43, "p1_counted": 6, "breach": true}, "Quarry Labs": {"cost_gbp": 69935.30, "p1_counted": 4, "breach": false}, "Tessel Cloud": {"cost_gbp": 62119.79, "p1_counted": 3, "breach": false}, "Ombra Analytics": {"cost_gbp": 57037.31, "p1_counted": 3, "breach": true}, "Larch Compute": {"cost_gbp": 49428.61, "p1_counted": 4, "breach": true}, "Vesper Metrics": {"cost_gbp": 78466.33, "p1_counted": 3, "breach": false}, "Ironbark IT": {"cost_gbp": 36687.16, "p1_counted": 3, "breach": false}, "Cobalt Ledger": {"cost_gbp": 46280.48, "p1_counted": 4, "breach": false}, "Fennel Networks": {"cost_gbp": 48962.26, "p1_counted": 3, "breach": true}, "Marlow Secure": {"cost_gbp": 45137.43, "p1_counted": 5, "breach": true}, "Pellucid AI": {"cost_gbp": 47325.62, "p1_counted": 2, "breach": false}, "Strand Hosting": {"cost_gbp": 44736.33, "p1_counted": 1, "breach": false}, "Kestrel Ops": {"cost_gbp": 37990.08, "p1_counted": 1, "breach": false}, "Brightwater Data": {"cost_gbp": 59129.65, "p1_counted": 1, "breach": false}}, "recommended": ["Kestrel Ops", "Strand Hosting", "Cobalt Ledger"]}
```