La verificación contra los ficheros originales confirma los cinco informes: los umbrales de SLA, los recuentos de incidentes (incluida la deduplicación en tessel-cloud y los estados `disputed`/`withdrawn` excluidos) y las cifras de facturación coinciden. Resultado final:

## Resumen por proveedor (enero–septiembre 2026)

| Proveedor | Coste (GBP) | P1 contados | Umbral SLA | ¿Incumple? |
|---|---|---|---|---|
| halden-systems | 45.654,00 | 2 | 3 | No |
| norvik-data | 41.790,84 | 5 | 4 | **Sí** |
| quarry-labs | 39.158,00 | 2 | 2 | No |
| tessel-cloud | 52.925,00 | 3 | 3 | No |
| ombra-analytics | 44.880,00 | 6 | 5 | **Sí** |

Notas relevantes de la revisión:

- **norvik-data** factura en EUR; el total es 48.594,00 EUR × 0,86 = 41.790,84 GBP. Con 5 incidentes P1 confirmados frente a un umbral de 4, incumple su SLA.
- **quarry-labs** tiene una enmienda efectiva el 2026-07-01 que baja el precio a 44,00 GBP/plaza y obliga a re-tarificar las facturas emitidas al precio antiguo para periodos posteriores. La factura de julio se emitió a 51,00 GBP/plaza, así que el coste contado es el re-tarificado (88 × 44 = 3.872,00 GBP); conviene verificar que se reciba la nota de crédito de 616,00 GBP. Con 2 incidentes P1 confirmados y umbral de 2, queda justo en el límite sin superarlo: no incumple (la regla exige "superar" el umbral).
- **tessel-cloud** tenía dos filas duplicadas en el registro (INC-TE200 e INC-TE201 repetidos); sin deduplicar habría parecido un incumplimiento. Tras aplicar la regla de deduplicación quedan 3 P1 contados, justo en su umbral de 3: no incumple.
- **ombra-analytics** acumula 6 incidentes P1 confirmados frente a un umbral de 5: incumple.
- En todos los proveedores quedó excluido un incidente P1 `disputed` del 2026-05-14 (y algunos `withdrawn`); si alguno de esos disputados se confirmara más adelante, tessel-cloud y quarry-labs pasarían a incumplir, así que vale la pena vigilarlos antes de la renovación.

**Recomendación:** renovar con **quarry-labs**, el proveedor más barato (39.158,00 GBP) de los tres que no incumplen su SLA.

```json
{"vendors": {"halden-systems": {"cost_gbp": 45654.0, "p1_counted": 2, "breach": false}, "norvik-data": {"cost_gbp": 41790.84, "p1_counted": 5, "breach": true}, "quarry-labs": {"cost_gbp": 39158.0, "p1_counted": 2, "breach": false}, "tessel-cloud": {"cost_gbp": 52925.0, "p1_counted": 3, "breach": false}, "ombra-analytics": {"cost_gbp": 44880.0, "p1_counted": 6, "breach": true}}, "recommended": "quarry-labs"}
```