## Planteamiento

Buscamos subconjuntos de 9 asientos (de 17 en fila) tales que ningún ocupado tenga a sus dos vecinos ocupados. Esto equivale a cadenas binarias de longitud 17 con nueve 1s y **sin tres 1s consecutivos**: los asientos ocupados forman bloques de tamaño 1 o 2, separados por al menos un asiento vacío.

## Conteo por bloques

Supongamos que hay $k$ bloques de 1s, con $b$ bloques de tamaño 2 y $k-b$ de tamaño 1. Entonces:
$$2b + (k-b) = 9 \implies b = 9-k,$$
y necesitamos $0 \le 9-k \le k$, es decir $5 \le k \le 9$.

**Elección de tamaños de bloques:** elegir cuáles de los $k$ bloques tienen tamaño 2: $\binom{k}{9-k}$ formas.

**Colocación de los vacíos:** hay $17-9 = 8$ asientos vacíos que van en $k+1$ huecos (extremos pueden quedar vacíos, los $k-1$ huecos internos necesitan al menos uno). Reservando $k-1$ vacíos, quedan $9-k$ para repartir libremente en $k+1$ huecos:
$$\binom{(9-k) + k}{k} = \binom{9}{k}.$$

## Suma

$$N = \sum_{k=5}^{9} \binom{k}{9-k}\binom{9}{k}$$

| $k$ | $\binom{k}{9-k}$ | $\binom{9}{k}$ | Producto |
|---|---|---|---|
| 5 | 5 | 126 | 630 |
| 6 | 20 | 84 | 1680 |
| 7 | 21 | 36 | 756 |
| 8 | 8 | 9 | 72 |
| 9 | 1 | 1 | 1 |

$$N = 630 + 1680 + 756 + 72 + 1 = 3139$$

Por lo tanto, $N \bmod 1000 = 139$.

$$\boxed{139}$$