Contamos los cuadrados de cada tamaño en una cuadrícula de puntos de 3 filas y $n$ columnas:

**Cuadrados de lado 1 (alineados):** la cuadrícula tiene $2 \times (n-1)$ celdas unitarias, así que hay $2(n-1)$.

**Cuadrados de lado 2 (alineados):** su caja ocupa $3\times 3$ puntos, que cabe exactamente en las 3 filas; horizontalmente hay $n-2$ posiciones, es decir $n-2$ cuadrados.

**Cuadrados inclinados de lado $\sqrt{2}$:** por ejemplo con vértices $(1,0),(2,1),(1,2),(0,1)$; su caja también es de $3\times 3$ puntos, así que hay $n-2$. (Cuadrados inclinados mayores, como los de lado $\sqrt{5}$, necesitarían 4 filas, así que no caben.)

Sumando:
$$2(n-1) + (n-2) + (n-2) = 4n - 6 = 70$$

De donde $4n = 76$ y $n = 19$.

$$\boxed{19}$$