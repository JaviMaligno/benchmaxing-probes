## Planteamiento

Sea $f(t) = t^2 - 4t + 6$. La condición es que el conjunto de raíces de $x^2 + px + q = 0$ sea cerrado bajo $f$: si $t$ es raíz, $f(t)$ también lo es.

**Puntos fijos de $f$:** $f(t) = t \iff t^2 - 5t + 6 = 0 \iff t \in \{2, 3\}$.

## Análisis por casos

**Caso 1: raíz doble $t$.** Como $t$ es la única raíz, necesitamos $f(t) = t$, es decir $t = 2$ o $t = 3$:
- $(x-2)^2 = x^2 - 4x + 4$
- $(x-3)^2 = x^2 - 6x + 9$

**Caso 2: dos raíces distintas $a, b$, ambas fijas.** Entonces $\{a,b\} = \{2,3\}$:
- $(x-2)(x-3) = x^2 - 5x + 6$

**Caso 3: una raíz fija $c$, la otra $s \neq c$ con $f(s) = c$.**
- $c = 2$: $s^2 - 4s + 6 = 2 \Rightarrow (s-2)^2 = 0 \Rightarrow s = 2$, excluido.
- $c = 3$: $s^2 - 4s + 6 = 3 \Rightarrow s^2 - 4s + 3 = 0 \Rightarrow s = 1$ o $s = 3$. Con $s = 1$: las raíces $\{1, 3\}$ cumplen $f(1) = 3$ ✓ y $f(3) = 3$ ✓:
- $(x-1)(x-3) = x^2 - 4x + 3$

**Caso 4: ciclo de longitud 2, $f(a) = b$, $f(b) = a$ con $a \neq b$.** Entonces $f(f(t)) = t$. Calculando:
$$f(f(t)) - t = t^4 - 8t^3 + 24t^2 - 33t + 18 = (t^2 - 5t + 6)(t^2 - 3t + 3)$$
Excluyendo los puntos fijos, quedan las raíces de $t^2 - 3t + 3 = 0$, es decir $t = \frac{3 \pm i\sqrt{3}}{2}$. Si $a$ es una de ellas, $a^2 = 3a - 3$, luego $f(a) = 3a - 3 - 4a + 6 = 3 - a$, que es exactamente la otra raíz. El conjunto es cerrado bajo $f$ y da una ecuación con coeficientes reales:
- $x^2 - 3x + 3 = 0$

## Conteo

Las ecuaciones son: $x^2-4x+4$, $x^2-6x+9$, $x^2-5x+6$, $x^2-4x+3$ y $x^2-3x+3$ (esta última con raíces complejas conjugadas, pero con $p, q$ reales y cumpliendo la propiedad).

$$\boxed{5}$$