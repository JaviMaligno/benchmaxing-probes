## Solución

**Paso 1 — Simplificar.** Como $\gcd(22,100)=2$ y $2 \mid 38$, la congruencia tiene solución y se puede dividir todo por 2:

$$11x \equiv 19 \pmod{50}$$

**Paso 2 — Invertir 11 módulo 50.** Buscamos $y$ con $11y \equiv 1 \pmod{50}$:

$$11 \cdot 41 = 451 = 9\cdot 50 + 1 \equiv 1 \pmod{50}$$

Así que $11^{-1} \equiv 41 \pmod{50}$.

**Paso 3 — Despejar $x$.**

$$x \equiv 41 \cdot 19 = 779 \equiv 779 - 15\cdot 50 = 29 \pmod{50}$$

**Verificación:** $22 \cdot 29 = 638 = 6\cdot 100 + 38 \equiv 38 \pmod{100}$. ✓

**Paso 4 — Las dos soluciones más pequeñas.** Son $x = 29$ y $x = 29 + 50 = 79$ (comprobación: $22\cdot 79 = 1738 \equiv 38 \pmod{100}$ ✓).

**Promedio:**

$$\frac{29 + 79}{2} = \frac{108}{2} = 54$$

\boxed{54}