## Planteamiento

Buscamos subconjuntos de 8 sillas (de 16 en fila) tales que ninguna persona quede junto a otras dos. Esto equivale a contar cadenas binarias de longitud 16 con ocho 1s (ocupadas) y ocho 0s (vacías), **sin tres 1s consecutivos**.

## Conteo por bloques

Las sillas ocupadas forman bloques de tamaño 1 o 2 (tamaño 3 o más está prohibido), separados por al menos una silla vacía.

Sea $b$ el número de bloques de tamaño 2 y $a$ el de tamaño 1, con $a + 2b = 8$. El total de bloques es $k = a + b = 8 - b$.

**Ordenar los bloques:** hay $\binom{k}{b}$ formas de intercalar los bloques simples y dobles.

**Colocar las 8 sillas vacías:** hay $k+1$ huecos (antes, entre y después de los bloques), y los $k-1$ huecos internos necesitan al menos una silla vacía. Tras asignar esas $k-1$, quedan $9-k$ vacías para repartir libremente en $k+1$ huecos:
$$\binom{(9-k) + k}{k} = \binom{9}{k}$$

## Suma sobre los casos

| $b$ | $k$ | $\binom{k}{b}$ | $\binom{9}{k}$ | Producto |
|---|---|---|---|---|
| 0 | 8 | 1 | 9 | 9 |
| 1 | 7 | 7 | 36 | 252 |
| 2 | 6 | 15 | 84 | 1260 |
| 3 | 5 | 10 | 126 | 1260 |
| 4 | 4 | 1 | 126 | 126 |

$$N = 9 + 252 + 1260 + 1260 + 126 = 2907$$

El residuo al dividir entre 1000 es:

$$\boxed{907}$$