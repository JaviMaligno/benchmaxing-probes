## Planteamiento

La serie es geométrica con primer término $t_1 = 3$ y razón

$$r = \frac{15/a}{3} = \frac{5}{a}.$$

Para que converja se necesita $|5/a| < 1$, es decir $a > 5$ (con $a$ entero positivo).

## Suma

$$S = \frac{3}{1 - \frac{5}{a}} = \frac{3a}{a-5}.$$

Reescribiendo con $d = a - 5 > 0$:

$$S = 3 + \frac{15}{d}.$$

## Condición de cuadrado perfecto

Para que $S$ sea entero, $d$ debe dividir a $15$: $d \in \{1, 3, 5, 15\}$, lo que da

| $d$ | $a$ | $S$ |
|---|---|---|
| 1 | 6 | 18 |
| 3 | 8 | 8 |
| 5 | 10 | 6 |
| 15 | 20 | $4 = 2^2$ ✓ |

El único caso que funciona entre estos es $a = 20$.

Además, ningún valor intermedio sirve aunque se admitieran cuadrados de racionales: como $S = \dfrac{3a(a-5)}{(a-5)^2}$, haría falta que $3a(a-5)$ fuera cuadrado perfecto, y al recorrer $a = 6, 7, \ldots, 19$ se obtiene $18, 42, 72, 108, 150, 198, 252, 312, 378, 450, 528, 612, 702, 798$ — ninguno es cuadrado. Para $a = 20$: $3 \cdot 20 \cdot 15 = 900 = 30^2$ ✓.

\boxed{20}