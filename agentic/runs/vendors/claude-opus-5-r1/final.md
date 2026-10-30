Los cinco informes están verificados contra los ficheros originales. Revisé cada carpeta yo mismo y la aritmética cuadra en todos los casos; corregí nada, pero sí confirmé los dos puntos donde un error habría cambiado el resultado (la deduplicación de Tessel y la re-tarificación de Quarry).

## Resultados por vendor

| Vendor | Coste ene–sep 2026 (GBP) | P1 contadas | Umbral | ¿Incumple? |
|---|---|---|---|---|
| **Quarry Labs** | 39.158,00 | 2 | 2 | No (justo en el límite) |
| **Norvik Data** | 41.790,84 | 5 | 4 | **Sí** |
| **Ombra Analytics** | 44.880,00 | 6 | 5 | **Sí** |
| **Halden Systems** | 45.654,00 | 2 | 3 | No |
| **Tessel Cloud** | 52.925,00 | 3 | 3 | No (justo en el límite) |

## Puntos que decidieron el resultado

- **Quarry Labs** — la enmienda de junio baja el precio a 44,00 GBP/asiento desde el 01-07-2026 y obliga a re-tarificar por nota de crédito cualquier factura emitida al precio antiguo. `QUA-202607` se facturó a 51,00: 88 × 7,00 = **616,00 GBP de crédito**. Facturado = 39.774,00 → ajustado = **39.158,00**.
- **Tessel Cloud** — el log tiene 13 filas pero 11 ids: `INC-TE201` e `INC-TE200` están duplicados. Sin deduplicar saldrían 5 P1 y parecería incumplimiento; deduplicadas son **3**, que no supera el umbral de 3.
- **Norvik Data** — único vendor en EUR: 48.594,00 EUR × 0,86 = **41.790,84 GBP**. Incumple por una sola incidencia (5 vs 4).
- **Ombra Analytics** — 6 P1 confirmadas frente a un umbral de 5. Tiene además dos P1 `disputed` que, correctamente, no se cuentan.
- En los cinco vendors, la P1 `INC-*-300` del 14-05-2026 está `disputed` y queda excluida por la regla 2.

## Recomendación: **Quarry Labs**

Es el más barato (39.158,00 GBP) de los tres que no incumplen su SLA. La recomendación es robusta al punto más interpretable del análisis: incluso sin aplicar la nota de crédito de la enmienda (39.774,00 GBP) seguiría siendo el más económico.

Dos salvedades para el expediente, no para la decisión: Quarry está al 100 % de su margen de SLA (2 de 2) y tiene `INC-QU300` en disputa — si se confirmara, pasaría a 3 e incumpliría. Tessel está igualmente sin margen (3 de 3, con `INC-TE300` en disputa). El único con holgura real es Halden (2 de 3), a 6.496,00 GBP más de coste.

```json
{"vendors": {"Quarry Labs": {"cost_gbp": 39158.0, "p1_counted": 2, "breach": false}, "Norvik Data": {"cost_gbp": 41790.84, "p1_counted": 5, "breach": true}, "Ombra Analytics": {"cost_gbp": 44880.0, "p1_counted": 6, "breach": true}, "Halden Systems": {"cost_gbp": 45654.0, "p1_counted": 2, "breach": false}, "Tessel Cloud": {"cost_gbp": 52925.0, "p1_counted": 3, "breach": false}}, "recommended": "Quarry Labs"}
```