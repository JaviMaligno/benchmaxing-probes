Los quince informes están completos y he verificado personalmente, archivo a archivo, los datos críticos de cada uno: nombre exacto del contrato, umbral del SLA, recuento de P1 confirmados (con deduplicación de ids repetidos) y veredicto de incumplimiento. El agente de Kestrel Ops, que falló a mitad de respuesta, fue recalculado de forma independiente por un segundo agente con resultado idéntico (37 990.08 GBP, 1 P1).

# Resultado de la revisión de renovación (enero–septiembre 2026)

| Proveedor | Coste GBP | P1 contados | Umbral | ¿Incumple SLA? |
|---|---:|---:|---:|---|
| Ironbark IT | 36 687.16 | 3 | 3 | No — pero **no elegible** para renovación (aviso corporativo 18/08/2026) |
| Kestrel Ops | 37 990.08 | 1 | 2 | No |
| Strand Hosting | 44 736.33 | 1 | 2 | No |
| Marlow Secure | 45 137.43 | 5 | 4 | **Sí** |
| Cobalt Ledger | 46 280.48 | 4 | 4 | No (en el límite) |
| Pellucid AI | 47 325.62 | 2 | 2 | No (en el límite) |
| Fennel Networks | 48 962.26 | 3 | 2 | **Sí** |
| Larch Compute | 49 428.61 | 4 | 3 | **Sí** |
| Halden Systems | 50 394.31 | 4 | 4 | No (en el límite) |
| Norvik Data | 50 989.43 | 6 | 4 | **Sí** |
| Ombra Analytics | 57 037.31 | 3 | 2 | **Sí** |
| Brightwater Data | 59 129.65 | 1 | 2 | No |
| Tessel Cloud | 62 119.79 | 3 | 3 | No (en el límite) |
| Quarry Labs | 69 935.30 | 4 | 4 | No (en el límite) |
| Vesper Metrics | 78 466.33 | 3 | 4 | No |

Notas metodológicas clave:

- **Conversiones**: solo Norvik Data, Larch Compute y Cobalt Ledger facturan en EUR, y Pellucid AI y Kestrel Ops en USD; cada línea se convirtió a la tasa de su propio mes. El resto factura directamente en GBP (la tabla FX no aplica).
- **Documentos contractuales sobre facturas**: la Enmienda 2 de Vesper Metrics anula el descuento de la Enmienda 1 («Invoiced amounts stand»), así que se suman los importes facturados íntegros; la nota de crédito CN-0042 de Strand Hosting (3 150.00 GBP) reduce su coste del periodo.
- **Incidentes**: solo cuentan P1 **y** `confirmed` dentro del periodo, deduplicados por id (afectó a Tessel Cloud, Marlow Secure —cuyas repeticiones de MAR200/MAR201 se cuentan una vez pese a lo cual sigue incumpliendo—). Los P1 `disputed`/`withdrawn` quedan excluidos, razón por la que los analyst-summary-DRAFT (que los contaban) eran incorrectos y no se usaron como fuente.
- **Ironbark IT** es el más barato pero el aviso corporativo del 18/08/2026 lo excluye de toda renovación, así que no entra en la recomendación pese a cumplir su SLA.

## Recomendación: los tres más baratos renovables

1. **Kestrel Ops** — 37 990.08 GBP, 1 P1 confirmado frente a un umbral de 2: el más barato de los elegibles y con buen margen de SLA.
2. **Strand Hosting** — 44 736.33 GBP (ya descontada la nota de crédito de 3 150 GBP), 1 P1 confirmado frente a un umbral de 2.
3. **Cobalt Ledger** — 46 280.48 GBP, 4 P1 confirmados, justo en su umbral de 4; renovable, aunque sin margen y con dos P1 en disputa que conviene vigilar.

```json
{"vendors": {"Halden Systems": {"cost_gbp": 50394.31, "p1_counted": 4, "breach": false}, "Norvik Data": {"cost_gbp": 50989.43, "p1_counted": 6, "breach": true}, "Quarry Labs": {"cost_gbp": 69935.30, "p1_counted": 4, "breach": false}, "Tessel Cloud": {"cost_gbp": 62119.79, "p1_counted": 3, "breach": false}, "Ombra Analytics": {"cost_gbp": 57037.31, "p1_counted": 3, "breach": true}, "Larch Compute": {"cost_gbp": 49428.61, "p1_counted": 4, "breach": true}, "Vesper Metrics": {"cost_gbp": 78466.33, "p1_counted": 3, "breach": false}, "Ironbark IT": {"cost_gbp": 36687.16, "p1_counted": 3, "breach": false}, "Cobalt Ledger": {"cost_gbp": 46280.48, "p1_counted": 4, "breach": false}, "Fennel Networks": {"cost_gbp": 48962.26, "p1_counted": 3, "breach": true}, "Marlow Secure": {"cost_gbp": 45137.43, "p1_counted": 5, "breach": true}, "Pellucid AI": {"cost_gbp": 47325.62, "p1_counted": 2, "breach": false}, "Strand Hosting": {"cost_gbp": 44736.33, "p1_counted": 1, "breach": false}, "Kestrel Ops": {"cost_gbp": 37990.08, "p1_counted": 1, "breach": false}, "Brightwater Data": {"cost_gbp": 59129.65, "p1_counted": 1, "breach": false}}, "recommended": ["Kestrel Ops", "Strand Hosting", "Cobalt Ledger"]}
```