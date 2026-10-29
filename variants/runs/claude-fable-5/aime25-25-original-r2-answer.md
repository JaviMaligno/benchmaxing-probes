Debemos contar los subconjuntos de 8 sillas (de 16 en fila) tales que ninguna silla ocupada sea adyacente a otras dos ocupadas; es decir, cadenas binarias de longitud 16 con ocho 1s sin tres 1s consecutivos.

**Planteamiento por bloques.** Los 1s forman bloques de tamaño 1 o 2. Si hay $k$ bloques, con $j$ bloques de tamaño 2 y $k-j$ de tamaño 1, entonces $2j+(k-j)=8$, de donde $j=8-k$. Para que $0\le j\le k$ se necesita $4\le k\le 8$. Las formas de ordenar los tamaños de los bloques son $\binom{k}{8-k}$.

**Colocación de los ceros.** Hay 8 ceros que se reparten en $k+1$ huecos (antes, entre y después de los bloques), con los $k-1$ huecos internos conteniendo al menos un cero. Tras asignar un cero obligatorio a cada hueco interno quedan $8-(k-1)=9-k$ ceros libres para $k+1$ huecos:
$$\binom{(9-k)+k}{k}=\binom{9}{k}.$$

**Suma total:**
$$N=\sum_{k=4}^{8}\binom{k}{8-k}\binom{9}{k}$$

- $k=4$: $\binom{4}{4}\binom{9}{4}=1\cdot 126=126$
- $k=5$: $\binom{5}{3}\binom{9}{5}=10\cdot 126=1260$
- $k=6$: $\binom{6}{2}\binom{9}{6}=15\cdot 84=1260$
- $k=7$: $\binom{7}{1}\binom{9}{7}=7\cdot 36=252$
- $k=8$: $\binom{8}{0}\binom{9}{8}=1\cdot 9=9$

$$N=126+1260+1260+252+9=2907$$

El residuo módulo 1000 es:

$$\boxed{907}$$