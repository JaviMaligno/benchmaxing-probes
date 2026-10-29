Para encontrar el valor de $n$, contemos cuántos cuadrados de cada tamaño se pueden formar utilizando los puntos de la cuadrícula de $3 \times n$.

Como la cuadrícula tiene $3$ filas de puntos con una distancia de $1$ unidad entre puntos adyacentes, la altura máxima de cualquier figura en esta cuadrícula es de $2$ unidades. Todo cuadrado con vértices en la cuadrícula está inscrito en una caja delimitadora (*bounding box*) cuadrada con lados paralelos a los ejes de tamaño $k \times k$, donde $k$ solo puede ser $1$ o $2$.

Analicemos los tres tamaños posibles de cuadrados:

1. **Cuadrados de lado $1$ (área $1$):**
   Estos cuadrados tienen lados paralelos a los ejes y ocupan una caja de $1 \times 1$.
   - En la dirección vertical ($3$ puntos), hay $3 - 1 = 2$ posiciones posibles.
   - En la dirección horizontal ($n$ puntos), hay $n - 1$ posiciones posibles.
   Por lo tanto, el número de cuadrados de lado $1$ es:
   $$2(n - 1)$$

2. **Cuadrados de lado $\sqrt{2}$ (área $2$):**
   Estos cuadrados están inclinados a $45^\circ$ y sus vértices son los puntos medios de los lados de una caja de $2 \times 2$. Cada caja de $2 \times 2$ contiene exactamente uno de estos cuadrados.
   - En la dirección vertical ($3$ puntos), hay $3 - 2 = 1$ posición posible.
   - En la dirección horizontal ($n$ puntos), hay $n - 2$ posiciones posibles.
   Por lo tanto, el número de cuadrados de lado $\sqrt{2}$ es:
   $$n - 2$$

3. **Cuadrados de lado $2$ (área $4$):**
   Estos cuadrados tienen lados paralelos a los ejes y sus vértices son las esquinas de una caja de $2 \times 2$. Al igual que en el caso anterior, hay un cuadrado de este tipo por cada caja de $2 \times 2$:
   $$n - 2$$

Sumando todos los cuadrados de los tres tamaños e igualando a $86$:
$$2(n - 1) + (n - 2) + (n - 2) = 86$$
$$2n - 2 + 2n - 4 = 86$$
$$4n - 6 = 86$$
$$4n = 92$$
$$n = 23$$

\boxed{23}