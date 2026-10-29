## Planteamiento

La condición "ningún invitado está sentado junto a dos otros invitados" significa que ningún asiento ocupado tiene ambos vecinos ocupados, es decir: **no hay tres asientos ocupados consecutivos**. Equivalentemente, los bloques (rachas) de asientos ocupados tienen longitud 1 o 2.

## Conteo

Sea $k$ el número de bloques de ocupados y $a$ el número de bloques de tamaño 2. Como hay 9 ocupados:
$$2a + (k-a) = 9 \implies a = 9-k$$
con $0 \le a \le k$, lo que exige $5 \le k \le 9$.

**Elección de los tamaños de los bloques:** $\binom{k}{9-k}$ maneras de decidir cuáles bloques tienen tamaño 2.

**Colocación de los 8 asientos vacíos:** hay $k+1$ huecos (antes, entre y después de los bloques); los $k-1$ internos requieren al menos un vacío. Quedan $8-(k-1) = 9-k$ vacíos libres para repartir entre $k+1$ huecos:
$$\binom{(9-k)+k}{k} = \binom{9}{k}$$

Por tanto:
$$N = \sum_{k=5}^{9} \binom{k}{9-k}\binom{9}{k}$$

| $k$ | $\binom{k}{9-k}$ | $\binom{9}{k}$ | producto |
|---|---|---|---|
| 5 | 5 | 126 | 630 |
| 6 | 20 | 84 | 1680 |
| 7 | 21 | 36 | 756 |
| 8 | 8 | 9 | 72 |
| 9 | 1 | 1 | 1 |

$$N = 630+1680+756+72+1 = 3139$$

(Verificación del método: aplicado al caso análogo de 16 asientos con 8 invitados da $2907$, el valor conocido.)

$$3139 \equiv 139 \pmod{1000}$$

\boxed{139}