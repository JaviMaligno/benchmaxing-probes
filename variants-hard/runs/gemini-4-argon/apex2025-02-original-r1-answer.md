Para hallar el mayor número real $k$ tal que la desigualdad $a_1 + a_2 > k a_3$ se cumpla para todo polígono simple $P$ formado por las aristas de un tablero de ajedrez infinito, analizaremos la vecindad de cada casilla unitaria del tablero (tanto dentro como fuera de $P$) que tiene exactamente $3$ aristas sobre el borde $\partial P$.

### 1. Cota superior: $k \le \frac{1}{2}$ (Demostración de que $a_1 + a_2 > \frac{1}{2}a_3$)

Sea $A_i$ el conjunto de casillas unitarias del plano (interiores o exteriores a $P$) que tienen exactamente $i$ de sus aristas en el borde $\partial P$, de modo que $|A_i| = a_i$ para $i \in \{1, 2, 3\}$.

Consideremos cualquier casilla $S \in A_3$. Sus tres aristas en $\partial P$ son consecutivas; llamemos $e_1, e_2, e_3$ a dichas aristas en orden a lo largo del contorno de $S$, de modo que $e_2$ es la arista central de las tres, y sean $v_1 = e_1 \cap e_2$ y $v_2 = e_2 \cap e_3$ los dos vértices de $S$ que unen $e_2$ con $e_1$ y $e_3$, respectivamente.

Sea $T(S)$ la casilla unitaria adyacente a $S$ a través de su arista central $e_2$. Observemos qué ocurre con las cuatro aristas de $T(S)$:
1. La arista $e_2$ pertenece a $\partial P$.
2. Como $P$ es un polígono que no se interseca a sí mismo, en cada vértice de la cuadrícula inciden a lo sumo $2$ aristas de $\partial P$. En el vértice $v_1$ ya inciden $e_1$ y $e_2$, y en el vértice $v_2$ ya inciden $e_2$ y $e_3$. Por lo tanto, **ninguna otra arista de la cuadrícula que incida en $v_1$ o en $v_2$ puede pertenecer a $\partial P$**.
3. En particular, las dos aristas de $T(S)$ perpendiculares a $e_2$ (que inciden en $v_1$ y $v_2$, respectivamente) **no pertenecen a $\partial P$**.
4. En consecuencia, las únicas aristas de $T(S)$ que pueden pertenecer a $\partial P$ son $e_2$ y, a lo sumo, la arista de $T(S)$ opuesta y paralela a $e_2$.

Esto demuestra dos propiedades fundamentales:
- Para toda casilla $S \in A_3$, su casilla asociada $T(S)$ tiene exactamente $1$ o $2$ aristas en $\partial P$, es decir, $T(S) \in A_1 \cup A_2$.
- Si $T \in A_1$, a lo sumo **una** casilla $S \in A_3$ puede cumplir $T(S) = T$ (pues $T$ solo tiene una arista en $\partial P$).
- Si $T \in A_2$, a lo sumo **dos** casillas $S \in A_3$ pueden cumplir $T(S) = T$ (una por cada una de las dos aristas de $T$ en $\partial P$).

Contando los elementos de $A_3$ según su imagen bajo la aplicación $S \mapsto T(S)$, obtenemos:
$$a_3 = |A_3| = \sum_{T \in A_1 \cup A_2} |\{S \in A_3 : T(S) = T\}| \le a_1 + 2a_2 = 2(a_1 + a_2) - a_1.$$

Además, considerando la caja delimitadora (*bounding box*) de $P$, las casillas exteriores inmediatamente adyacentes a las aristas extremas superior, inferior, izquierda y derecha de $P$ tienen exactamente $1$ arista en $\partial P$, por lo que siempre se cumple $a_1 \ge 4 > 0$. Por consiguiente:
$$a_3 \le 2(a_1 + a_2) - 4 < 2(a_1 + a_2) \implies a_1 + a_2 > \frac{1}{2}a_3.$$

---

### 2. Optimalidad de $k = \frac{1}{2}$

Para ver que $k$ no puede ser mayor que $\frac{1}{2}$, construimos una familia de polígonos $P_{m,n}$ formados por $m$ «peines dobles» horizontales de longitud $2n-1$ apilados verticalmente y unidos en su extremo izquierdo por una columna vertical:
- Para cada $j \in \{0, 1, \dots, m-1\}$, el $j$-ésimo peine tiene una espina horizontal de casillas $[x, x+1] \times [4j, 4j+1]$ para $x = 1, 2, \dots, 2n-1$, junto con dientes superiores $[2i-1, 2i] \times [4j+1, 4j+2]$ y dientes inferiores $[2i-1, 2i] \times [4j-1, 4j]$ para cada $i \in \{1, \dots, n\}$.
- La columna izquierda $[0, 1] \times [0, 4m-3]$ conecta las espinas de los $m$ peines sin que el borde $\partial P_{m,n}$ se interseque a sí mismo en ningún vértice ni arista.

En el interior de esta estructura de $m \times n$ bloques periódicos, por cada bloque $(i, j)$:
- Hay $4$ casillas en $A_3$: los dos dientes interiores (superior e inferior) en $x = 2i-1$ y las dos cavidades exteriores (superior e inferior) entre dientes consecutivos en $x = 2i$.
- Hay únicamente $2$ casillas en $A_1 \cup A_2$: la casilla de la espina $[2i, 2i+1] \times [4j, 4j+1]$ (que pertenece a $A_2$ y separa las dos cavidades exteriores) y la casilla exterior $[2i-1, 2i] \times [4j+2, 4j+3]$ (que pertenece a $A_2$ y separa el diente superior del peine $j$ del diente inferior del peine $j+1$). Las demás casillas internas del bloque tienen $0$ aristas en $\partial P_{m,n}$.

Sumando sobre todos los bloques y teniendo en cuenta que los efectos de borde crecen como $O(m + n)$, tenemos:
$$a_3 = 4mn + O(m + n), \qquad a_1 + a_2 = 2mn + O(m + n).$$
Tomando $m, n \to \infty$, el cociente $\frac{a_1 + a_2}{a_3}$ tiende a $\frac{2}{4} = \frac{1}{2}$. Por tanto, el mayor número real $k$ que satisface la condición es $\frac{1}{2}$.

\boxed{\frac{1}{2}}