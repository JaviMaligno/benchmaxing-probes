# Resolución paso a paso

**Paso 1: Identificar la razón común.**

La serie es $4 + \frac{12}{a} + \frac{36}{a^2} + \cdots$, con razón común:
$$r = \frac{12/a}{4} = \frac{3}{a}$$

**Paso 2: Condiciones de convergencia.**

Para que la serie infinita converja (y la suma sea positiva), necesitamos $|r| < 1$, es decir, $a > 3$. Como $a$ es entero positivo, $a \geq 4$.

**Paso 3: Calcular la suma.**

$$S = \frac{4}{1 - \frac{3}{a}} = \frac{4a}{a-3} = \frac{4(a-3) + 12}{a-3} = 4 + \frac{12}{a-3}$$

**Paso 4: Imponer que sea un cuadrado perfecto.**

Sea $S = k^2$ con $k$ entero positivo:
$$k^2 - 4 = \frac{12}{a-3} \quad\Rightarrow\quad a - 3 = \frac{12}{k^2 - 4}$$

Como $a-3$ debe ser entero positivo, $k^2 - 4$ debe ser un divisor positivo de $12$:

| $k^2 - 4$ | $k^2$ | ¿Cuadrado perfecto? |
|---|---|---|
| 1 | 5 | No |
| 2 | 6 | No |
| 3 | 7 | No |
| 4 | 8 | No |
| 6 | 10 | No |
| 12 | 16 | Sí ($k = 4$) |

**Paso 5: Hallar $a$.**

La única posibilidad es $k^2 = 16$, que da:
$$a - 3 = \frac{12}{12} = 1 \quad\Rightarrow\quad a = 4$$

**Verificación:** Con $a = 4$, la serie es $4 + 3 + \frac{9}{4} + \cdots$ y $S = \frac{4}{1 - 3/4} = 16 = 4^2$. ✓

$$\boxed{4}$$