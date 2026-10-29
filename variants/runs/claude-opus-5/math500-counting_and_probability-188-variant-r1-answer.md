## Planteamiento

El punto $(a,b)$ se distribuye uniformemente en el cuadrado $(0,4)\times(0,4)$, de área $16$.

Para que exista un triángulo de lados $2$, $a$, $b$ se requiere la desigualdad triangular:

- $a + b > 2$
- $|a - b| < 2$

(las dos condiciones $2 + a > b$ y $2 + b > a$ equivalen a $|a-b| < 2$).

## Cálculo del área desfavorable

**Región 1: $a + b \le 2$.** Triángulo de vértices $(0,0)$, $(2,0)$, $(0,2)$, con área $\tfrac{1}{2}\cdot 2\cdot 2 = 2$.

**Región 2: $a - b \ge 2$.** Aquí $a\in[2,4]$ y $b\in[0,a-2]$, así que el área es
$$\int_2^4 (a-2)\,da = 2.$$

**Región 3: $b - a \ge 2$.** Por simetría, área $2$.

Estas tres regiones se solapan solo en conjuntos de medida nula (por ejemplo, $a-b\ge 2$ junto con $a+b\le 2$ fuerza $b=0$). El área desfavorable total es
$$2 + 2 + 2 = 6.$$

## Probabilidad

$$P = \frac{16 - 6}{16} = \frac{10}{16} = \frac{5}{8}$$

\boxed{\dfrac{5}{8}}