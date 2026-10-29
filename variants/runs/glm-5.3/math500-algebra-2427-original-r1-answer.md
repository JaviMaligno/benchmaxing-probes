# Resolución paso a paso

**Planteamiento:**

El trabajador deposita $20 000 al final de cada año. Con tasa compuesta $r$:

- El 1er depósito genera interés durante 2 años: $20000(1+r)^2$
- El 2º depósito genera interés durante 1 año: $20000(1+r)$
- El 3er depósito no genera interés aún: $20000$

**Ecuación:**

$$20000(1+r)^2 + 20000(1+r) + 20000 = 66200$$

Dividiendo entre 20000 y sea $x = 1+r$:

$$x^2 + x + 1 = 3.31 \quad\Rightarrow\quad x^2 + x - 2.31 = 0$$

**Resolviendo la ecuación cuadrática:**

$$x = \frac{-1 + \sqrt{1 + 4(2.31)}}{2} = \frac{-1 + \sqrt{10.24}}{2} = \frac{-1 + 3.2}{2} = 1.1$$

Por lo tanto, $r = 0.10 = 10\%$.

**Verificación:**

$$20000(1.1)^2 + 20000(1.1) + 20000 = 24200 + 22000 + 20000 = 66200 \checkmark$$

\boxed{10}