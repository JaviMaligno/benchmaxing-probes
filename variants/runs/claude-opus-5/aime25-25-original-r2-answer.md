## Planteamiento

La condición "nadie se sienta junto a dos personas" significa que no hay tres sillas ocupadas consecutivas. Hay que contar las cadenas binarias de longitud 16 con ocho 1 (ocupadas) y ocho 0, sin tres 1 seguidos.

**Bloques de unos:** los 1 se agrupan en bloques maximales de tamaño 1 o 2. Si hay $k$ bloques y $j$ de ellos son de tamaño 2:
$$2j + (k-j) = 8 \implies j = 8-k,$$
lo que exige $4 \le k \le 8$. El orden de los bloques da $\binom{k}{8-k}$ opciones.

**Distribución de ceros:** los 8 ceros van en $k+1$ huecos, y los $k-1$ huecos internos necesitan al menos un cero. Quedan $9-k$ ceros libres entre $k+1$ huecos:
$$\binom{(9-k)+k}{k} = \binom{9}{k}.$$

## Suma

$$N = \sum_{k=4}^{8} \binom{k}{8-k}\binom{9}{k}$$

| $k$ | $\binom{k}{8-k}$ | $\binom{9}{k}$ | producto |
|---|---|---|---|
| 4 | 1 | 126 | 126 |
| 5 | 10 | 126 | 1260 |
| 6 | 15 | 84 | 1260 |
| 7 | 7 | 36 | 252 |
| 8 | 1 | 9 | 9 |

$$N = 126 + 1260 + 1260 + 252 + 9 = 2907$$

Por tanto $N \equiv 907 \pmod{1000}$.

\boxed{907}