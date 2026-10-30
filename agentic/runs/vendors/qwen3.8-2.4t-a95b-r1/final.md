He verificado personalmente los cinco informes contra los datos crudos (facturas, incidentes, contratos y la enmienda de quarry-labs). Todos los cálculos cuadran. Resumen de la verificación:

## Resultados por vendor (enero–septiembre 2026)

| Vendor | Coste total (GBP) | P1 contabilizados | Umbral SLA | ¿Incumple? |
|---|---|---|---|---|
| **Halden Systems** | £45.654,00 | 2 (INC-HA200, INC-HA201; INC-HA300 es `disputed`) | 3 | No |
| **Norvik Data** | £41.790,84 (48.594 EUR × 0,86) | 5 (INC-NO200–NO204; INC-NO300 `disputed`) | 4 | **Sí** (5 > 4) |
| **Quarry Labs** | £39.158,00 | 2 (INC-QU200, INC-QU201; QU300 `disputed`, QU103 `withdrawn`) | 2 | No (2 no excede 2) |
| **Tessel Cloud** | £52.925,00 | 3 (TE200, TE201, TE202 — TE201 y TE200 aparecen duplicados en el CSV y cuentan una sola vez; TE103 `withdrawn`, TE300 `disputed`) | 3 | No (en el límite exacto) |
| **Ombra Analytics** | £44.880,00 | 6 (OM200–OM205; OM107 y OM300 `disputed`) | 5 | **Sí** (6 > 5) |

### Notas clave de la verificación
- **Quarry Labs**: la enmienda (20/06/2026) baja el precio a £44/asiento desde 2026-07-01 y obliga a recalcular cualquier factura emitida al precio antiguo para periodos posteriores. La factura QUA-202607 (88 asientos × £51 = £4.488) debe reajustarse a 88 × £44 = £3.872 (abono de £616). Coste real: **£39.158** (£39.774 tal como se facturó). La enmienda no cambia el umbral SLA.
- **Tessel Cloud**: sin deduplicar, el recuento ingenuo daría 5 P1 y mostraría un incumplimiento falso; la política (regla 3) lo deja en 3, exactamente en el umbral.
- **Norvik Data**: único vendor con facturas en EUR; conversión al tipo fijo interno 1 EUR = 0,86 GBP.

## Recomendación

De los tres vendors que **no** incumplen su SLA (Quarry £39.158, Halden £45.654, Tessel £52.925), el más barato es **Quarry Labs** con £39.158,00. Advertencia: Quarry está exactamente en su umbral de 2 P1 — cualquier P1 confirmado adicional en el periodo de revisión provocaría incumplimiento, por lo que conviene vigilar la resolución del INC-QU300 (actualmente `disputed`).

```json
{"vendors": {"halden-systems": {"cost_gbp": 45654.00, "p1_counted": 2, "breach": false}, "norvik-data": {"cost_gbp": 41790.84, "p1_counted": 5, "breach": true}, "quarry-labs": {"cost_gbp": 39158.00, "p1_counted": 2, "breach": false}, "tessel-cloud": {"cost_gbp": 52925.00, "p1_counted": 3, "breach": false}, "ombra-analytics": {"cost_gbp": 44880.00, "p1_counted": 6, "breach": true}}, "recommended": "quarry-labs"}
```