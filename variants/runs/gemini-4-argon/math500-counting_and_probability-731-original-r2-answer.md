Para hallar la probabilidad de que un punto elegido al azar en el interior del rectángulo $ABCD$ esté más cerca del centro $O$ que de cualquiera de los cuatro vértices, podemos utilizar la simetría de la figura.

**Paso 1: Configurar un sistema de coordenadas y usar la simetría**
Situemos el centro $O$ en el origen de coordenadas $(0,0)$, con los lados del rectángulo paralelos a los ejes coordenados. Sean $AB = 2a$ y $AD = 2b$, de modo que $\frac{AB}{AD} = \frac{a}{b} = k$. Los cuatro vértices se encuentran en $(\pm a, \pm b)$.

Los ejes coordenados dividen el rectángulo $ABCD$ en cuatro subrectángulos congruentes (uno en cada cuadrante). Por simetría, la probabilidad buscada en todo el rectángulo es igual a la probabilidad correspondiente dentro del subrectángulo del primer cuadrante, $R_1 = [0, a] \times [0, b]$, cuyo vértice del rectángulo original es $B(a, b)$.

**Paso 2: Analizar la condición de distancia en el primer cuadrante**
Para cualquier punto $P(x, y)$ en el primer cuadrante ($x \ge 0, y \ge 0$), el vértice más cercano de los cuatro es $B(a, b)$. Por lo tanto, $P$ está más cerca de $O(0,0)$ que de cualquiera de los cuatro vértices si y solo si está más cerca de $O(0,0)$ que de $B(a, b)$.

La frontera entre los puntos más cercanos a $O$ y los más cercanos a $B$ es la mediatriz del segmento $OB$, cuya ecuación se obtiene igualando las distancias al cuadrado:
$$x^2 + y^2 < (x - a)^2 + (y - b)^2$$
$$x^2 + y^2 < x^2 - 2ax + a^2 + y^2 - 2by + b^2$$
$$ax + by < \frac{a^2 + b^2}{2}$$

**Paso 3: Calcular la proporción del área**
Observemos que la recta frontera $ax + by = \frac{a^2 + b^2}{2}$ pasa por el punto medio del segmento $OB$, que es $M\left(\frac{a}{2}, \frac{b}{2}\right)$. 

El punto $M\left(\frac{a}{2}, \frac{b}{2}\right)$ es precisamente el centro de simetría del subrectángulo $R_1 = [0, a] \times [0, b]$. Dado que cualquier recta que pasa por el centro de un rectángulo lo divide en dos regiones congruentes de igual área (independientemente del valor de $k$), la región donde el punto está más cerca de $O$ que de $B$ ocupa exactamente la mitad del área de $R_1$.

Por simetría en los cuatro cuadrantes, el área favorable total es exactamente la mitad del área del rectángulo $ABCD$.

\boxed{\frac{1}{2}}