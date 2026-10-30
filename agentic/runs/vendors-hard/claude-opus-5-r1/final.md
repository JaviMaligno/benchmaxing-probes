Ya tengo los quince vendors. He verificado yo mismo los recuentos P1 y umbrales por grep directo, y las sumas mes→total de todos los grupos; los cuatro candidatos más baratos se recalcularon además de forma independiente y coinciden al penique.

## Resultados por vendor (enero–septiembre 2026)

| Vendor | Coste GBP | P1 computables | Umbral | Incumple |
|---|---|---|---|---|
| Kestrel Ops | 37.990,08 | 1 | 2 | No |
| Strand Hosting | 44.736,33 | 1 | 2 | No |
| Cobalt Ledger | 46.280,48 | 4 | 4 | No |
| Pellucid AI | 47.325,62 | 2 | 2 | No |
| Halden Systems | 50.394,31 | 4 | 4 | No |
| Brightwater Data | 59.129,65 | 1 | 2 | No |
| Tessel Cloud | 62.119,79 | 3 | 3 | No |
| Quarry Labs | 69.935,30 | 4 | 4 | No |
| Vesper Metrics | 78.466,33 | 3 | 4 | No |
| Ironbark IT | 36.687,16 | 3 | 3 | No — **no renovable** |
| Marlow Secure | 45.137,43 | 5 | 4 | **Sí** |
| Fennel Networks | 48.962,26 | 3 | 2 | **Sí** |
| Larch Compute | 49.428,61 | 4 | 3 | **Sí** |
| Ombra Analytics | 57.037,31 | 3 | 2 | **Sí** |
| Norvik Data | 50.989,43 | 6 | 4 | **Sí** |

## Puntos decisivos

- **Ironbark IT es el más barato de todos (36.687,16 GBP) y no incumple su SLA, pero queda excluido**: el aviso de `corporate/notices.md` del 18/08/2026 lo declara expresamente *no elegible para renovación* tras su adquisición por un competidor.
- **Vesper Metrics**: la Enmienda 2 (28/05/2026) anula la Enmienda 1 "en su totalidad; no aplica descuento a ningún periodo". Por tanto **no** se aplica el 20% a las líneas de plataforma: importan las cifras facturadas (2.028,09 GBP que *no* se descuentan).
- **Strand Hosting**: la nota de crédito CN-0042 resta 3.150,00 GBP (47.886,33 → 44.736,33). Sin aplicarla caería fuera del top 3.
- **Umbral estricto**: Cobalt Ledger (4/4), Halden Systems (4/4), Quarry Labs (4/4), Tessel Cloud (3/3) y Pellucid AI (2/2) están *exactamente* en el límite — no lo superan, así que no incumplen.
- **Deduplicación**: Tessel Cloud (INC-TES200, INC-TES201) y Marlow Secure (INC-MAR200, INC-MAR201) tienen ids repetidos. En Tessel esto decide el veredicto: 5 filas → 3 incidencias → sin incumplimiento.
- **Los cuatro borradores DRAFT están equivocados** (Halden, Ironbark, Fennel, Brightwater): inflan los P1 contando `disputed`/`withdrawn` y declaran incumplimientos inexistentes en Halden, Ironbark y Brightwater. No se han usado como fuente, conforme a la política.

## Recomendación: tres más baratos renovables

1. **Kestrel Ops** — 37.990,08 GBP (1 P1 de 2)
2. **Strand Hosting** — 44.736,33 GBP (1 P1 de 2)
3. **Cobalt Ledger** — 46.280,48 GBP (4 P1 de 4, justo en el límite)

El siguiente sería Pellucid AI (47.325,62 GBP); el margen sobre Cobalt es de 1.045 GBP, muy por encima de cualquier ambigüedad de redondeo (≤1,50 GBP).

**Salvedad de fiabilidad**: Bash estaba deshabilitado, así que toda la aritmética se hizo a mano. Mitigué esto con doble cálculo independiente en los cuatro candidatos (coincidencia exacta) y verificación propia de los 15 recuentos P1 y de las sumas mes→total. Halden, Quarry, Norvik, Tessel, Ombra, Larch, Vesper, Fennel, Marlow y Brightwater tienen un solo cálculo de coste, pero ninguno está lo bastante cerca del corte como para alterar el top 3.

```json
{"vendors": {"Halden Systems": {"cost_gbp": 50394.31, "p1_counted": 4, "breach": false}, "Norvik Data": {"cost_gbp": 50989.43, "p1_counted": 6, "breach": true}, "Quarry Labs": {"cost_gbp": 69935.30, "p1_counted": 4, "breach": false}, "Tessel Cloud": {"cost_gbp": 62119.79, "p1_counted": 3, "breach": false}, "Ombra Analytics": {"cost_gbp": 57037.31, "p1_counted": 3, "breach": true}, "Larch Compute": {"cost_gbp": 49428.61, "p1_counted": 4, "breach": true}, "Vesper Metrics": {"cost_gbp": 78466.33, "p1_counted": 3, "breach": false}, "Ironbark IT": {"cost_gbp": 36687.16, "p1_counted": 3, "breach": false}, "Cobalt Ledger": {"cost_gbp": 46280.48, "p1_counted": 4, "breach": false}, "Fennel Networks": {"cost_gbp": 48962.26, "p1_counted": 3, "breach": true}, "Marlow Secure": {"cost_gbp": 45137.43, "p1_counted": 5, "breach": true}, "Pellucid AI": {"cost_gbp": 47325.62, "p1_counted": 2, "breach": false}, "Strand Hosting": {"cost_gbp": 44736.33, "p1_counted": 1, "breach": false}, "Kestrel Ops": {"cost_gbp": 37990.08, "p1_counted": 1, "breach": false}, "Brightwater Data": {"cost_gbp": 59129.65, "p1_counted": 1, "breach": false}}, "recommended": ["Kestrel Ops", "Strand Hosting", "Cobalt Ledger"]}
```