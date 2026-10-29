## Planteamiento

La serie es geométrica con primer término $t_1 = 4$ y razón

$$r = \frac{12/a}{4} = \frac{3}{a}$$

**Convergencia:** se requiere $|3/a| < 1$, es decir $a > 3$ (con $a$ entero positivo).

**Suma:**

$$S = \frac{t_1}{1-r} = \frac{4}{1 - \dfrac{3}{a}} = \frac{4a}{a-3}$$

## Búsqueda del menor $a$

Como $a > 3$, el candidato más pequeño es $a = 4$:

$$S = \frac{4\cdot 4}{4-3} = \frac{16}{1} = 16 = 4^2$$

Es un cuadrado perfecto, así que no hace falta probar valores mayores.

**Verificación:** con $a=4$ la serie es $4 + 3 + \frac{9}{4} + \frac{27}{16} + \cdots$, de razón $3/4$, cuya suma es $\frac{4}{1-3/4} = 16$. ✓

\boxed{4}