## Planteamiento

La serie es geométrica con primer término $3$ y razón $r = \frac{5}{a}$:

$$3 + \frac{15}{a} + \frac{75}{a^2} + \cdots = 3 + 3\cdot\frac{5}{a} + 3\cdot\left(\frac{5}{a}\right)^2 + \cdots$$

**Condición de convergencia:** necesitamos $\left|\frac{5}{a}\right| < 1$, es decir, $a > 5$.

## Cálculo de la suma

$$S = \frac{3}{1 - \frac{5}{a}} = \frac{3a}{a-5}$$

Hacemos el cambio $k = a - 5$ (con $k$ entero positivo, ya que $a \geq 6$), entonces $a = k + 5$:

$$S = \frac{3(k+5)}{k} = 3 + \frac{15}{k}$$

## Condición de cuadrado perfecto

Para que $S$ sea un cuadrado perfecto (entero), como $3$ ya es entero, necesitamos que $\frac{15}{k}$ sea entero, es decir, $k \mid 15$. Los divisores positivos de $15$ son:

| $k$ | $a = k+5$ | $S = 3 + \frac{15}{k}$ | ¿Cuadrado? |
|---|---|---|---|
| 1 | 6 | 18 | No |
| 3 | 8 | 8 | No |
| 5 | 10 | 6 | No |
| 15 | 20 | 4 | ¡Sí, $4 = 2^2$! |

El menor $a$ que funciona es $a = 20$.

## Verificación

Con $a = 20$, la razón es $\frac{5}{20} = \frac{1}{4}$:

$$S = \frac{3}{1 - \frac{1}{4}} = \frac{3}{\frac{3}{4}} = 4 = 2^2 \checkmark$$

$$\boxed{20}$$