## Resolución

Sea $N = \underline{p}\,\underline{q}\,\underline{r}\,\underline{s} = 1000p + 100q + 10r + s$ y $M = \underline{q}\,\underline{r}\,\underline{s}\,\underline{p} = 1000q + 100r + 10s + p$.

**Relación clave:** calculemos $10N$:
$$10N = 10000p + 1000q + 100r + 10s = 9999p + (1000q + 100r + 10s + p) = 9999p + M.$$

Por lo tanto, $M = 10N - 9999p$.

**Condición:** si $m \mid N$, entonces $m \mid M$ si y solo si $m \mid 9999p$, donde $p$ es el dígito inicial de $N$.

**¿Qué dígitos iniciales $p$ aparecen?** Como $m \le 99$, los múltiplos consecutivos de $m$ están separados por a lo más $99 < 1000$, así que todo intervalo $[d000,\, d999]$ con $d = 1, \dots, 9$ contiene algún múltiplo de $m$ de cuatro dígitos. Es decir, **todos** los dígitos iniciales $p = 1, \dots, 9$ ocurren.

Entonces la condición exige $m \mid 9999p$ para cada $p \in \{1, \dots, 9\}$. En particular, tomando $p = 1$: se necesita $m \mid 9999$. Y recíprocamente, si $m \mid 9999$, entonces $m \mid 9999p$ para todo $p$, y la propiedad se cumple siempre.

**Divisores de dos dígitos de $9999$:** factorizamos $9999 = 3^2 \cdot 11 \cdot 101$. Sus divisores son $1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999$. Los de dos dígitos son:
$$11, \quad 33, \quad 99.$$

**Suma:** $11 + 33 + 99 = 143$.

$$\boxed{143}$$