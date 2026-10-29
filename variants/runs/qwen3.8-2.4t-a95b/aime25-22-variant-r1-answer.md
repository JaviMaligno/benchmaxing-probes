Factorizamos $675 = 3^3 \cdot 5^2$.

El número de divisores positivos de $675$ es $(3+1)(2+1) = 12$, así que $|S| = 12$ y hay $2^{12} = 4096$ subconjuntos posibles de $S$.

Cada divisor tiene la forma $3^a 5^b$ con $0 \le a \le 3$ y $0 \le b \le 2$. Para que el mcm de $T$ sea $675$, necesitamos:
- que algún elemento de $T$ tenga $a = 3$, y
- que algún elemento de $T$ tenga $b = 2$.

Usamos inclusión-exclusión. Contamos los subconjuntos "malos":

- Subconjuntos donde todos los elementos tienen $a \le 2$: hay $3 \cdot 3 = 9$ divisores posibles, dando $2^9 = 512$ subconjuntos.
- Subconjuntos donde todos los elementos tienen $b \le 1$: hay $4 \cdot 2 = 8$ divisores posibles, dando $2^8 = 256$ subconjuntos.
- Intersección (ambas condiciones): $3 \cdot 2 = 6$ divisores, dando $2^6 = 64$ subconjuntos.

Por inclusión-exclusión, el número de subconjuntos cuyo mcm es exactamente $675$ es:

$$2^{12} - 2^9 - 2^8 + 2^6 = 4096 - 512 - 256 + 64 = 3392.$$

Todos estos son no vacíos (el subconjunto vacío tiene mcm $1$), así que la probabilidad es

$$\frac{3392}{4096} = \frac{53}{64}.$$

Como $53$ es primo y no divide a $64$, la fracción ya está reducida. Entonces $m = 53$, $n = 64$, y

$$m + n = 53 + 64 = 117.$$

$$\boxed{117}$$