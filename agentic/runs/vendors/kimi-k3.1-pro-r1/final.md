### Resultado de enero–septiembre de 2026

| Proveedor | Coste total (GBP) | P1 computables | Umbral SLA | Incumple |
|---|---:|---:|---:|---|
| Halden Systems | 45.654,00 | 2 | 3 | No |
| Norvik Data | 41.790,84 | 5 | 4 | **Sí** |
| Quarry Labs | **39.158,00** | 2 | 2 | No |
| Tessel Cloud | 52.925,00 | 3 | 3 | No |
| Ombra Analytics | 44.880,00 | 6 | 5 | **Sí** |

Se han contado únicamente los P1 `confirmed`, deduplicando por ID. Norvik Data se convirtió a **48.594 EUR × 0,86 = 41.790,84 GBP**. En Quarry Labs, la factura de julio se revaloró de 4.488 a 3.872 GBP conforme a la enmienda, aplicando el crédito de 616 GBP.

**Recomendación: Quarry Labs**, por ser el proveedor más barato que no incumple su SLA.

```json
{"vendors":{"Halden Systems":{"cost_gbp":45654.0,"p1_counted":2,"breach":false},"Norvik Data":{"cost_gbp":41790.84,"p1_counted":5,"breach":true},"Quarry Labs":{"cost_gbp":39158.0,"p1_counted":2,"breach":false},"Tessel Cloud":{"cost_gbp":52925.0,"p1_counted":3,"breach":false},"Ombra Analytics":{"cost_gbp":44880.0,"p1_counted":6,"breach":true}},"recommended":"Quarry Labs"}
```