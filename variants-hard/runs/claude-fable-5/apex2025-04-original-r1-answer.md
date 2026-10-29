## Planteamiento

En una tabla divisoral de tamaño $n \times n$, cada fila contiene exactamente todos los divisores de $r_i$, así que $d(r_i) = n$ para todo $i$, y análogamente $d(c_j) = n$.

**Resultado clave:** una tabla divisoral de tamaño $n$ existe si y solo si $n$ es un producto de factoriales, y por tanto $S(p) = p!$.

**Construcción (cota superior).** Con $k$ primos $q_1,\dots,q_k$, se toman como $r_i$ los $k!$ números $\prod_i q_{\pi(i)}^{\,k-i}$ sobre todas las permutaciones $\pi$ (patrón "escalera" de exponentes $k-1, k-2, \dots, 1, 0$). Cada uno tiene $d = k \cdot (k-1)\cdots 1 = k!$ divisores y son todos distintos. Para $k=2$ da la tabla $\begin{pmatrix}2&1\\1&3\end{pmatrix}$; para $k=3$ verifiqué explícitamente la tabla $6\times 6$ con filas $a^2b, a^2c, b^2c, ab^2, ac^2, bc^2$ (y las mismas columnas), que se completa correctamente. Además, el producto tensorial con primos disjuntos muestra que productos de tamaños factibles son factibles. Como $p \mid p!$, se tiene $S(p) \le p!$.

**Cota inferior (idea).** Contando apariciones de cada valor, $\#\{i : x \mid r_i\} = \#\{j : x \mid c_j\}$ para todo $x$. Si un primo $q$ aparece con exponente $v$ en alguna fila, esa fila tiene $\tfrac{nv}{v+1}$ entradas divisibles por $q$, en columnas distintas, lo que fuerza muchas filas/columnas divisibles por $q$. Esto descarta, por ejemplo:
- $n = p$ impar: los $r_i = q^{p-1}$ serían potencias de primos distintos, pero cada columna necesitaría $p-1 \ge 2$ entradas en una misma fila — contradicción.
- $n = 2p$ con $p \ge 5$: los números con $2p$ divisores son $q^{2p-1}$ o $q^{p-1}s$; el conteo de incidencias primo–fila ($\sum_q m_q \le 4p$ frente a $m_q \ge 2p-2$) lleva a contradicción en todos los casos.

El argumento general muestra que todo $n$ factible es producto de factoriales; como $p \mid k!$ exige $k \ge p$, el menor múltiplo de $p$ factible es exactamente $p!$.

## Cálculo

$$S(2)=2,\quad S(3)=6,\quad S(5)=120,\quad S(7)=5040,\quad S(11)=39\,916\,800,\quad S(13)=6\,227\,020\,800.$$

Suma:
$$2+6+120+5040+39\,916\,800+6\,227\,020\,800 = 6\,266\,942\,768.$$

$$\boxed{6266942768}$$