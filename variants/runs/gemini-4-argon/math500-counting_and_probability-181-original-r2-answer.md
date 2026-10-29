Para hallar el valor de $n$, contemos cuántos cuadrados de cada uno de los tres tamaños posibles se pueden formar cuyos vértices sean puntos de la cuadrícula de $3 \times n$ puntos.

Supongamos que la distancia entre puntos adyacentes (horizontal o verticalmente) es $1$. Como la cuadrícula tiene $3$ filas de puntos, la altura máxima de cualquier figura es $2$ unidades. Por lo tanto, los tres tamaños posibles de cuadrados son:

1. **Cuadrados de lado $1$ (alineados con la cuadrícula):**
   Cada uno de estos cuadrados ocupa una subcuadrícula de $2 \times 2$ puntos. 
   - En la dirección vertical (de $3$ puntos) hay $3 - 1 = 2$ posiciones posibles.
   - En la dirección horizontal (de $n$ puntos) hay $n - 1$ posiciones posibles.
   
   En total, hay $2(n - 1)$ cuadrados de lado $1$.

2. **Cuadrados de lado $2$ (alineados con la cuadrícula):**
   Cada uno de estos cuadrados ocupa una subcuadrícula de $3 \times 3$ puntos.
   - En la dirección vertical hay $3 - 2 = 1$ posición posible.
   - En la dirección horizontal hay $n - 2$ posiciones posibles.
   
   En total, hay $n - 2$ cuadrados de lado $2$.

3. **Cuadrados de lado $\sqrt{2}$ (inclinados a $45^\circ$):**
   Cada cuadrado inclinado de lado $\sqrt{2}$ está inscrito exactamente dentro de una subcuadrícula de $3 \times 3$ puntos (sus vértices son los puntos medios de los lados del cuadrado de lado $2$).
   - Por cada subcuadrícula de $3 \times 3$ puntos hay exactamente $1$ cuadrado de este tamaño.
   
   En total, hay $n - 2$ cuadrados de lado $\sqrt{2}$.

Sumando las cantidades de cuadrados de los tres tamaños e igualando a $70$, obtenemos:
$$2(n - 1) + (n - 2) + (n - 2) = 70$$
$$2n - 2 + 2n - 4 = 70$$
$$4n - 6 = 70$$
$$4n = 76$$
$$n = 19$$

\boxed{19}