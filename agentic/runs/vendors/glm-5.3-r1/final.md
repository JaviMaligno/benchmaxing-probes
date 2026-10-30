Los cinco informes han llegado y ya he verificado personalmente cada cifra contra los archivos fuente (contratos, enmienda, facturas e incidencias). Todo cuadra. Detalles de la verificación:

- **Halden Systems**: 1.087 asientos × 42,00 GBP = 45.654,00 GBP ✓. P1 confirmadas: INC-HA201, INC-HA200 (INC-HA300 está `disputed`, excluida) = 2 ✓. Umbral: ≤ 3 → 2 ≤ 3, **sin incumplimiento** ✓.
- **Norvik Data**: 48.594,00 EUR × 0,86 = 41.790,84 GBP ✓. P1 confirmadas: INC-NO200/201/202/203/204 = 5 ✓ (INC-NO300 `disputed`, excluida). Umbral: ≤ 4 → 5 > 4, **incumple** ✓.
- **Quarry Labs**: la enmienda (firmada el 20/06/2026) baja el precio de 51,00 a 44,00 GBP desde el 01/07/2026 y obliga a re-tarificar la factura de julio emitida al precio antiguo (88 × 44 = 3.872,00 en lugar de 4.488,00). Total efectivo: 27.234 (ene–jun) + 3.872 + 3.960 + 4.092 = **39.158,00 GBP** ✓ (el valor nominal sin re-tarificar sería 39.774,00 GBP). P1 confirmadas: INC-QU200, INC-QU201 = 2 ✓ (INC-QU300 `disputed` e INC-QU103 `withdrawn`, excluidas). Umbral: ≤ 2 → 2 ≤ 2, **sin incumplimiento** (justo en el límite) ✓.
- **Tessel Cloud**: 1.450 asientos × 36,50 = 52.925,00 GBP ✓. Ojo al registro: INC-TE200 e INC-TE201 aparecen **duplicadas** en el CSV; sin deduplicar darían 5 P1 y un incumplimiento falso. Deduplicadas: INC-TE200/201/202 = 3 ✓ (INC-TE103 `withdrawn`, INC-TE300 `disputed`, excluidas). Umbral: ≤ 3 → 3 ≤ 3, **sin incumplimiento** ✓.
- **Ombra Analytics**: suma de facturas = 44.880,00 GBP ✓. P1 confirmadas: INC-OM200/201/202/203/204/205 = 6 ✓ (INC-OM107 e INC-OM300 `disputed`, excluidas). Umbral: ≤ 5 → 6 > 5, **incumple** ✓.

## Resumen

| Proveedor | Costo ene–sep 2026 (GBP) | P1 contadas | Umbral SLA | ¿Incumple? |
|---|---:|---:|---:|---|
| halden-systems | 45.654,00 | 2 | 3 | No |
| norvik-data | 41.790,84 | 5 | 4 | **Sí** |
| quarry-labs | 39.158,00 | 2 | 2 | No |
| tessel-cloud | 52.925,00 | 3 | 3 | No |
| ombra-analytics | 44.880,00 | 6 | 5 | **Sí** |

## Recomendación

**quarry-labs** es el proveedor más barato que no incumple su SLA: 39.158,00 GBP (coste efectivo tras la re-tarificación de la enmienda de junio) y 2 P1 confirmadas frente a su umbral de 2. La recomendación es robusta: incluso si se sumara el valor nominal de las facturas sin re-tarificar (39.774,00 GBP), seguiría siendo el más barato de los que cumplen (halden-systems, 45.654,00 GBP; tessel-cloud, 52.925,00 GBP). Conviene tener presente que va justamente al límite de su SLA — una sola P1 confirmada más en el periodo habría supuesto incumplimiento — y que tanto norvik-data como ombra-analytics quedan descartados por superarlo.

```json
{"vendors": {"halden-systems": {"cost_gbp": 45654.0, "p1_counted": 2, "breach": false}, "norvik-data": {"cost_gbp": 41790.84, "p1_counted": 5, "breach": true}, "quarry-labs": {"cost_gbp": 39158.0, "p1_counted": 2, "breach": false}, "tessel-cloud": {"cost_gbp": 52925.0, "p1_counted": 3, "breach": false}, "ombra-analytics": {"cost_gbp": 44880.0, "p1_counted": 6, "breach": true}}, "recommended": "quarry-labs"}
```