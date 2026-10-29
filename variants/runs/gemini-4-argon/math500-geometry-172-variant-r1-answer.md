Para encontrar el área del triángulo $UMG$, podemos razonar paso a paso utilizando las propiedades del baricentro (centroide) y la semejanza de triángulos:

1. **Propiedad del baricentro en las medianas:**
   Las tres medianas $PS$, $QT$ y $RU$ dividen al triángulo $PQR$ en $6$ triángulos más pequeños de igual área. El triángulo $PUG$ es uno de estos $6$ triángulos, por lo que su área es:
   $$\text{Área}(\triangle PUG) = \frac{1}{6} \text{Área}(\triangle PQR) = \frac{270}{6} = 45$$

2. **Posición de los puntos $U$ y $M$ sobre el lado $PQ$:**
   - Como $U$ es el punto medio de $PQ$, tenemos que:
     $$PU = \frac{1}{2} PQ$$
   - El baricentro $G$ divide a la mediana $PS$ en una razón de $2:1$, es decir:
     $$\frac{PG}{PS} = \frac{2}{3}$$
   - Dado que la recta $MN$ pasa por $G$ y es paralela a $QR$, por el teorema de Tales (o semejanza entre $\triangle PMN$ y $\triangle PQR$), la razón se conserva sobre el lado $PQ$:
     $$\frac{PM}{PQ} = \frac{PG}{PS} = \frac{2}{3} \implies PM = \frac{2}{3} PQ$$

3. **Relación entre los segmentos $UM$ y $PU$:**
   Como los puntos $P, U, M, Q$ son colineales en ese orden, la longitud del segmento $UM$ es:
   $$UM = PM - PU = \frac{2}{3} PQ - \frac{1}{2} PQ = \frac{1}{6} PQ$$
   Comparando las longitudes de $UM$ y $PU$:
   $$\frac{UM}{PU} = \frac{\frac{1}{6} PQ}{\frac{1}{2} PQ} = \frac{1}{3}$$

4. **Cálculo del área de $\triangle UMG$:**
   Los triángulos $UMG$ y $PUG$ comparten la misma altura trazada desde el vértice $G$ hacia la recta $PQ$. Por lo tanto, la razón de sus áreas es igual a la razón de sus bases:
   $$\frac{\text{Área}(\triangle UMG)}{\text{Área}(\triangle PUG)} = \frac{UM}{PU} = \frac{1}{3}$$
   Sustituyendo el área de $\triangle PUG$:
   $$\text{Área}(\triangle UMG) = \frac{1}{3} \times 45 = 15$$

\boxed{15}