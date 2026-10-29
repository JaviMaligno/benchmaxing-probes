Para encontrar la probabilidad de que un punto elegido al azar en el interior del rectángulo $ABCD$ esté más cerca del centro $O$ que de cualquiera de los cuatro vértices, podemos utilizar la simetría de la figura:

1. **División en cuadrantes:** 
   Situemos el centro $O$ en el origen de coordenadas $(0,0)$, con los lados del rectángulo paralelos a los ejes. Si $AD = 2h$ y $AB = 2w$ (donde $w/h = k$), los ejes de coordenadas dividen el rectángulo $ABCD$ en cuatro rectángulos más pequeños e iguales, cada uno de dimensiones $w \times h$ y ubicado en uno de los cuatro cuadrantes.

2. **Reducción a un solo cuadrante:**
   Por simetría, la probabilidad buscada en todo el rectángulo $ABCD$ es igual a la probabilidad dentro del subrectángulo del primer cuadrante $[0, w] \times [0, h]$. Para cualquier punto $P(x, y)$ con $x \ge 0$ e $y \ge 0$, el vértice más cercano de los cuatro es $B(w, h)$. Por lo tanto, $P$ está más cerca de $O$ que de cualquiera de los cuatro vértices si y solo si está más cerca de $O(0,0)$ que de $B(w,h)$.

3. **Mediatriz del segmento $OB$:**
   El conjunto de puntos que equidistan de $O(0,0)$ y $B(w,h)$ es la mediatriz del segmento $OB$. Esta recta pasa por el punto medio de $OB$, que es $\left(\frac{w}{2}, \frac{h}{2}\right)$.

4. **Simetría central del subrectángulo:**
   El punto $\left(\frac{w}{2}, \frac{h}{2}\right)$ es precisamente el centro geométrico del subrectángulo $[0, w] \times [0, h]$. Toda recta que pasa por el centro de un rectángulo lo divide en dos regiones congruentes de igual área, independientemente de la proporción $k$ entre sus lados.

Por consiguiente, la región de puntos más cercanos a $O$ que a $B$ ocupa exactamente la mitad del área de cada subrectángulo, y por tanto la mitad del área total de $ABCD$.

\boxed{\frac{1}{2}}