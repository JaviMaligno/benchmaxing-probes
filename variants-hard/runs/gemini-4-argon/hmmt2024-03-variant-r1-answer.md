Para encontrar todos los enteros positivos de dos dígitos $m$ que cumplen la propiedad dada, expresemos los números en términos de sus dígitos en base 10.

Sea $N = \underline{p}\,\underline{q}\,\underline{r}\,\underline{s}$ un número de cuatro dígitos, donde $p \in \{1, 2, \dots, 9\}$ y $q, r, s \in \{0, 1, \dots, 9\}$. Su valor en base 10 es:
$$N = 1000p + 100q + 10r + s$$

El número obtenido al rotar los dígitos es $N' = \underline{q}\,\underline{r}\,\underline{s}\,\underline{p}$, cuyo valor en base 10 es:
$$N' = 1000q + 100r + 10s + p$$

Observamos que podemos relacionar $N$ y $N'$ multiplicando $N$ por $10$:
$$10N = 10000p + 1000q + 100r + 10s = 9999p + (1000q + 100r + 10s + p) = 9999p + N'$$

Despejando $N'$, obtenemos:
$$N' = 10N - 9999p$$

Sabemos por hipótesis que $N$ es un múltiplo de $m$, por lo que $m \mid 10N$. Para que $N'$ también sea múltiplo de $m$, es necesario y suficiente que:
$$m \mid 9999p$$

Dado que $m$ es un número de dos dígitos ($10 \le m \le 99$), en el intervalo de números de cuatro dígitos que comienzan con $p = 1$ (es decir, el conjunto $\{1000, 1001, \dots, 1999\}$, que contiene $1000$ enteros consecutivos) siempre existe al menos un múltiplo de $m$.

Tomando un múltiplo de $m$ en dicho intervalo (para el cual $p = 1$), la condición $m \mid 9999p$ exige que:
$$m \mid 9999$$

Recíprocamente, si $m \mid 9999$, entonces $m \mid 9999p$ para cualquier dígito $p$, lo que garantiza que $N' = 10N - 9999p$ siempre será múltiplo de $m$ cuando $N$ lo sea.

Factorizamos $9999$ en factores primos:
$$9999 = 9 \times 1111 = 3^2 \times 11 \times 101$$

Los divisores positivos de $9999$ son:
$$1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999$$

De estos divisores, los que tienen exactamente dos dígitos son $11$, $33$ y $99$.

Finalmente, calculamos la suma de todos los valores posibles de $m$:
$$11 + 33 + 99 = 143$$

\boxed{143}