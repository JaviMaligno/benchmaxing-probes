## Planteamiento

Que nadie se siente junto a dos personas significa que no haya **tres sillas ocupadas consecutivas**. Hay que contar los subconjuntos de 8 sillas (de 16 en fila) sin tres consecutivas.

Las sillas ocupadas forman bloques de tamaño 1 o 2, separados por al menos una silla vacía.

Sea $k$ el número de bloques. Si hay $a$ bloques de tamaño 2 y $b$ de tamaño 1:
- $a+b=k$, $2a+b=8$ ⟹ $a=8-k$, $b=2k-8$, con $4\le k\le 8$.

**Orden de los bloques:** elegir qué $8-k$ de los $k$ bloques son dobles: $\binom{k}{8-k}$.

**Colocación de las 8 sillas vacías:** hay $k+1$ huecos; los $k-1$ internos requieren $\ge 1$. Quedan $8-(k-1)=9-k$ vacías libres entre $k+1$ huecos: $\binom{9-k+k}{k}=\binom{9}{k}$.

## Suma

$$N=\sum_{k=4}^{8}\binom{k}{8-k}\binom{9}{k}$$

| $k$ | $\binom{k}{8-k}$ | $\binom{9}{k}$ | producto |
|---|---|---|---|
| 4 | 1 | 126 | 126 |
| 5 | 10 | 126 | 1260 |
| 6 | 15 | 84 | 1260 |
| 7 | 7 | 36 | 252 |
| 8 | 1 | 9 | 9 |

$$N = 126+1260+1260+252+9 = 2907$$

Por lo tanto $2907 \equiv 907 \pmod{1000}$.

\boxed{907}