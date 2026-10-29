# Solución paso a paso

**Paso 1: Entender la función.**
- Para $x \leq 3$: $f(x) = 3-x$, que es decreciente y cubre $[0, \infty)$ (desde $f(-\infty^+) = \infty$ hasta $f(3)=0$).
- Para $x > 3$: $f(x) = -x^3+2x^2+3x$. Evaluando en $x = 3$: $-27+18+9 = 0$, y su derivada $f'(x) = -3x^2+4x+3$ cumple $f'(3) = -12 < 0$, así que en $(3,\infty)$ es decreciente hacia $-\infty$. Su rango es $(-\infty, 0)$.

Los dos rangos no se solapan, así que $f$ es inyectiva y $f^{-1}$ está bien definida.

**Paso 2: Calcular $f^{-1}(0)$.**
Resolver $f(x) = 0$:
- Rama 1: $3 - x = 0 \Rightarrow x = 3$ ✓ (válido, pues $3 \leq 3$).
- Rama 2: $-x^3+2x^2+3x = 0$ con $x > 3$ daría valores negativos (la rama es decreciente desde $0$), no hay solución.

Por lo tanto $f^{-1}(0) = 3$.

**Paso 3: Calcular $f^{-1}(6)$.**
Como $6 > 0$, debe estar en el rango de la primera rama:
$$3 - x = 6 \Rightarrow x = -3 \quad ✓ \text{ (válido, pues } -3 \leq 3)$$

Por lo tanto $f^{-1}(6) = -3$.

**Paso 4: Sumar.**
$$f^{-1}(0) + f^{-1}(6) = 3 + (-3) = 0$$

$$\boxed{0}$$