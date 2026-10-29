Analicemos la estructura del número formado.

**Caso 1: día de un dígito (d = 1..9).** El número es $N = 10m + d$.
- $m \mid N \iff m \mid d$ (pues $m \mid 10m$).
- $d \mid N \iff d \mid 10m$.

Como $m \geq 6$ y $d \leq 9$, la condición $m \mid d$ fuerza $d = m$:
- **Junio 6:** $66$; $6 \mid 66$ ✓ (y $6 \mid 60$ ✓). Lucky.
- **Julio 7:** $77$; ✓. Lucky.
- **Agosto 8:** $88$; ✓. Lucky.

**Caso 2: día de dos dígitos (d = 10..31).** El número es $N = 100m + d$.
- $m \mid N \iff m \mid d$.
- $d \mid N \iff d \mid 100m$.

**Junio (m = 6, d ≤ 30):** múltiplos de 6 entre 10 y 30: 12, 18, 24, 30. ¿Cuáles dividen a 600?
- $12 \mid 600$ ✓, $18 \nmid 600$, $24 \nmid 600$, $30 \mid 600$ ✓ → **Junio 12 y Junio 30**.

**Julio (m = 7, d ≤ 31):** múltiplos de 7: 14, 21, 28. ¿Cuáles dividen a 700?
- $14 \mid 700$ ✓, $21 \nmid 700$, $28 \mid 700$ ✓ → **Julio 14 y Julio 28**.

**Agosto (m = 8, d ≤ 31):** múltiplos de 8: 16, 24. ¿Cuáles dividen a 800?
- $16 \mid 800$ ✓, $24 \nmid 800$ → **Agosto 16**.

**Conteo:** Junio tiene 3 (días 6, 12, 30), Julio tiene 3 (días 7, 14, 28), Agosto tiene 2 (días 8, 16).

$$3 + 3 + 2 = \boxed{8}$$