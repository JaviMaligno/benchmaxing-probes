Para encontrar el valor de $n$, podemos contar cuántos cuadrados de cada tamaño se pueden formar utilizando los puntos de la cuadrícula de $3 \times n$ (que tiene una altura de $2$ unidades y un ancho de $n - 1$ unidades).

Todo cuadrado con vértices en la cuadrícula está inscrito en una caja delimitadora (*bounding box*) cuadrada de tamaño $k \times k$ con lados paralelos a los ejes. Como la cuadrícula tiene solo $3$ filas de puntos, la altura máxima es de $2$ unidades, por lo que $k$ solo puede ser $1$ o $2$:

1. **Cajas de $1 \times 1$:**
   Cada caja de $1 \times 1$ contiene exactamente $1$ cuadrado de lado $1$.
   En una cuadrícula de $3 \times n$ puntos, hay $(3 - 1)(n - 1) = 2(n - 1)$ cuadrados de lado $1$.

2. **Cajas de $2 \times 2$:**
   Cada caja de $2 \times 2$ contiene $2$ cuadrados que tocan sus cuatro lados:
   - $1$ cuadrado paralelo a los ejes de lado $2$.
   - $1$ cuadrado inclinado de lado $\sqrt{1^2 + 1^2} = \sqrt{2}$ (con vértices en los puntos medios de los lados de la caja de $2 \times 2$).
   
   En la cuadrícula de $3 \times n$ puntos, hay $(3 - 2)(n - 2) = n - 2$ cajas de $2 \times 2$, lo que aporta $2(n - 2)$ cuadrados en total ($n - 2$ de lado $2$ y $n - 2$ de lado $\sqrt{2}$).

Estos corresponden exactamente a los tres tamaños diferentes de cuadrados mencionados en el problema (lados $1$, $\sqrt{2}$ y $2$). Sumando el total de cuadrados e igualando a $86$:

$$2(n - 1) + 2(n - 2) = 86$$
$$2n - 2 + 2n - 4 = 86$$
$$4n - 6 = 86$$
$$4n = 92$$
$$n = 23$$

\boxed{23}