Para encontrar la longitud del segmento $PS$, podemos resolver el problema paso a paso utilizando geometría y el teorema del coseno (o coordenadas cartesianas).

### Paso 1: Determinar las longitudes en la base $QR$
Dado que los puntos $Q, T, U$ y $R$ están alineados en ese orden sobre el lado $QR$:
- La longitud desde $Q$ hasta $U$ es $QU = QT + TU = 11 + 13 = 24$.
- Como también sabemos que $UR = 24$, el punto $U$ es exactamente el **punto medio** del lado $QR$.
- La longitud total del lado del triángulo equilátero $\triangle PQR$ es $QR = QU + UR = 24 + 24 = 48$.

### Paso 2: Analizar el triángulo $\triangle PSU$
1. En el triángulo equilátero $\triangle PQR$ de lado $48$, como $U$ es el punto medio de la base $QR$, el segmento $PU$ es la altura correspondiente a $QR$. Por lo tanto:
   $$PU \perp QR \implies \angle PUT = 90^\circ$$
   La longitud de esta altura es:
   $$PU = \frac{\sqrt{3}}{2} \cdot QR = \frac{\sqrt{3}}{2} \cdot 48 = 24\sqrt{3}$$

2. En el triángulo equilátero $\triangle STU$ de lado $TU = 13$, tenemos que:
   $$SU = 13 \quad \text{y} \quad \angle SUT = 60^\circ$$

3. Como el punto $S$ está dentro de $\triangle PQR$, el ángulo $\angle PUS$ es la diferencia entre $\angle PUT$ y $\angle SUT$:
   $$\angle PUS = 90^\circ - 60^\circ = 30^\circ$$

### Paso 3: Aplicar el teorema del coseno en $\triangle PSU$
Usando el teorema del coseno en el triángulo $\triangle PSU$:
$$PS^2 = PU^2 + SU^2 - 2 \cdot PU \cdot SU \cdot \cos(\angle PUS)$$

Sustituyendo los valores conocidos ($PU = 24\sqrt{3}$, $SU = 13$ y $\cos(30^\circ) = \frac{\sqrt{3}}{2}$):
$$PS^2 = (24\sqrt{3})^2 + 13^2 - 2(24\sqrt{3})(13)\left(\frac{\sqrt{3}}{2}\right)$$
$$PS^2 = 1728 + 169 - 24 \cdot 13 \cdot 3$$
$$PS^2 = 1897 - 936 = 961$$

Tomando la raíz cuadrada en ambos lados:
$$PS = \sqrt{961} = 31$$

\boxed{31}