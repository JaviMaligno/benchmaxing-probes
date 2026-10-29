Vamos a plantearlo paso a paso.

**Planteamiento:** El trabajador deposita \$20,000 al final de cada año. Con tasa de interés compuesto $r$, al final del tercer año:

- El primer depósito ha rendido 2 años: $20000(1+r)^2$
- El segundo depósito ha rendido 1 año: $20000(1+r)$
- El tercer depósito se acaba de hacer: $20000$

**Ecuación:** Sea $x = 1+r$. Necesitamos:

$$20000(x^2 + x + 1) \geq 66200$$

$$x^2 + x + 1 \geq 3.31$$

$$x^2 + x - 2.31 \geq 0$$

**Resolviendo la cuadrática:**

$$x = \frac{-1 + \sqrt{1 + 4(2.31)}}{2} = \frac{-1 + \sqrt{10.24}}{2} = \frac{-1 + 3.2}{2} = 1.1$$

Por lo tanto $1 + r \geq 1.1$, es decir $r \geq 0.10$, o sea **10%**.

**Verificación:** con $r = 10\%$: $20000(1.21) + 20000(1.1) + 20000 = 24200 + 22000 + 20000 = 66200$ ✓

$$\boxed{10}$$