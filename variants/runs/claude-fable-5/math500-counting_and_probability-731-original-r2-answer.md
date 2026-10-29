Analicemos el problema paso a paso.

**Configuración.** Dividamos el rectángulo $ABCD$ en cuatro rectángulos congruentes (cuadrantes) mediante las dos rectas que pasan por $O$ paralelas a los lados. Por simetría, basta estudiar un cuadrante, por ejemplo el que tiene a $A$ como esquina.

**Observación clave.** Para cualquier punto dentro del cuadrante de $A$, el vértice más cercano de los cuatro es precisamente $A$: cualquier otro vértice está al menos tan lejos, porque hay que cruzar una de las líneas medias para acercarse a otro vértice. Por lo tanto, en ese cuadrante la condición "más cerca de $O$ que de cualquier vértice" se reduce a "más cerca de $O$ que de $A$".

**Región favorable en el cuadrante.** El conjunto de puntos más cercanos a $O$ que a $A$ es el semiplano que contiene a $O$ delimitado por la mediatriz del segmento $OA$. Ahora bien, el cuadrante es un rectángulo cuya diagonal es exactamente $OA$, y la mediatriz de $OA$ pasa por el punto medio $M$ de esa diagonal, que es el **centro de simetría** del rectángulo-cuadrante.

Cualquier recta que pase por el centro de un rectángulo lo divide en dos regiones congruentes (la rotación de $180°$ alrededor de $M$ intercambia ambas mitades y preserva el rectángulo). Por lo tanto, la mediatriz de $OA$ corta al cuadrante en dos partes de **igual área**: la mitad más cercana a $O$ y la mitad más cercana a $A$.

**Conclusión.** En cada uno de los cuatro cuadrantes, exactamente la mitad del área está más cerca de $O$ que del vértice correspondiente. Sumando, la probabilidad es $\tfrac{1}{2}$, independientemente del valor de $k = AB/AD$.

$$\boxed{\dfrac{1}{2}}$$