Trabajemos con coordenadas vectoriales con origen en $P$.

**Configuración.** Sea $P$ el origen, y sean $\vec{q}$, $\vec{r}$ los vectores de posición de $Q$ y $R$. Entonces:
- Centroide: $G = \frac{\vec{q}+\vec{r}}{3}$
- Punto medio de $PQ$: $U = \frac{\vec{q}}{2}$

**Localizar $M$.** La recta por $G$ paralela a $QR$ está a $\frac{2}{3}$ del camino de $P$ hacia $QR$ (porque $G$ está sobre la mediana $PS$ con $PG = \frac{2}{3}PS$). Por semejanza, corta a $PQ$ en $M = \frac{2}{3}\vec{q}$ y a $PR$ en $N = \frac{2}{3}\vec{r}$.

**Área de $UMG$.** Calculo los vectores desde $U$:

$$M - U = \frac{2}{3}\vec{q} - \frac{1}{2}\vec{q} = \frac{\vec{q}}{6}$$

$$G - U = \frac{\vec{q}+\vec{r}}{3} - \frac{\vec{q}}{2} = -\frac{\vec{q}}{6} + \frac{\vec{r}}{3}$$

El área es la mitad del valor absoluto del producto cruz:

$$\text{Área} = \frac{1}{2}\left|\frac{\vec{q}}{6} \times \left(-\frac{\vec{q}}{6} + \frac{\vec{r}}{3}\right)\right| = \frac{1}{2}\cdot\frac{1}{18}\left|\vec{q}\times\vec{r}\right|$$

Como $[PQR] = \frac{1}{2}|\vec{q}\times\vec{r}| = 270$, se tiene $|\vec{q}\times\vec{r}| = 540$, y por tanto:

$$[UMG] = \frac{540}{36} = 15$$

$$\boxed{15}$$