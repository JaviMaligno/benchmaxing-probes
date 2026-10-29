## Solución

**Configuración.** Coloco el rectángulo con centro $O$ en el origen, con semilados $a$ y $b$, de modo que los vértices son $(\pm a, \pm b)$. Por simetría, basta analizar un cuadrante, por ejemplo el rectángulo $[0,a]\times[0,b]$, cuyo vértice del rectángulo original es $V=(a,b)$.

**Reducción a un solo vértice.** Para cualquier punto de ese cuadrante, el vértice más cercano de los cuatro es precisamente $V$ (los otros tres están al menos igual de lejos, por simetría de reflexión respecto a los ejes). Por lo tanto, la condición "más cerca de $O$ que de cualquier vértice" se reduce, dentro del cuadrante, a "más cerca de $O$ que de $V$".

**La mediatriz bisecta el cuadrante.** El conjunto de puntos equidistantes de $O=(0,0)$ y $V=(a,b)$ es la mediatriz del segmento $OV$, que pasa por su punto medio $\left(\tfrac{a}{2},\tfrac{b}{2}\right)$. Pero ese punto medio es exactamente el **centro del rectángulo** $[0,a]\times[0,b]$.

Cualquier recta que pase por el centro de un rectángulo lo divide en dos regiones de igual área (son congruentes por simetría central respecto a ese punto: la rotación de $180°$ alrededor del centro lleva el rectángulo en sí mismo y una región en la otra).

**Conclusión.** En cada cuadrante, exactamente la mitad del área está más cerca de $O$ que del vértice correspondiente, sin importar los valores de $a$ y $b$. Por lo tanto la probabilidad total es $\tfrac12$, independientemente de la razón $k = AB/AD$.

$$\boxed{\dfrac{1}{2}}$$