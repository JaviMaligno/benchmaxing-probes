## Resolución

**Paso 1 — Simplificar.** Como $\gcd(22,100)=2$ y $2 \mid 38$, podemos dividir todo entre 2:

$$11x \equiv 19 \pmod{50}$$

**Paso 2 — Invertir 11 módulo 50.** Buscamos $y$ con $11y \equiv 1 \pmod{50}$:

$$11 \cdot 41 = 451 = 9\cdot 50 + 1 \equiv 1 \pmod{50}$$

Así que el inverso es 41.

**Paso 3 — Despejar $x$.**

$$x \equiv 41 \cdot 19 = 779 \equiv 779 - 15\cdot 50 = 29 \pmod{50}$$

**Paso 4 — Verificar.** $22 \cdot 29 = 638 = 6\cdot 100 + 38 \equiv 38 \pmod{100}$ ✓

**Paso 5 — Las dos soluciones positivas más pequeñas** son $x = 29$ y $x = 79$ (verificación: $22\cdot 79 = 1738 \equiv 38$ ✓).

**Promedio:**

$$\frac{29 + 79}{2} = \frac{108}{2} = 54$$

\boxed{54}