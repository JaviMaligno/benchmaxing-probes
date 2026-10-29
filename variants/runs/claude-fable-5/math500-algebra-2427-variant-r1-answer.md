Analicemos el problema paso a paso.

**Planteamiento:** La enfermera deposita \$25,000 al final de cada año. Con tasa de interés compuesto $r$, al final del tercer año:

- El primer depósito ganó interés durante 2 años: $25000(1+r)^2$
- El segundo depósito ganó interés durante 1 año: $25000(1+r)$
- El tercer depósito se acaba de hacer: $25000$

**Ecuación:**

$$25000\left[(1+r)^2 + (1+r) + 1\right] \geq 84360$$

Dividiendo entre 25,000:

$$(1+r)^2 + (1+r) + 1 \geq 3.3744$$

Sea $x = 1+r$:

$$x^2 + x - 2.3744 \geq 0$$

Resolviendo la cuadrática con igualdad:

$$x = \frac{-1 + \sqrt{1 + 4(2.3744)}}{2} = \frac{-1 + \sqrt{10.4976}}{2}$$

Como $3.24^2 = 10.4976$, tenemos:

$$x = \frac{-1 + 3.24}{2} = \frac{2.24}{2} = 1.12$$

Por lo tanto $r = 0.12$, es decir, una tasa del 12%.

**Verificación:** $25000(1.12^2 + 1.12 + 1) = 25000(1.2544 + 1.12 + 1) = 25000 \times 3.3744 = 84360$. ✓

$$\boxed{12}$$