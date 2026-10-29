Para calcular el área $[\triangle PRS]$, analicemos las propiedades geométricas del trapecio $PQRS$ paso a paso:

1. **Relación de ángulos:**
   Sea $\theta = \angle RPS$. Como $\overline{PR}$ biseca el ángulo $\angle QPS$, tenemos que:
   $$\angle QPR = \angle RPS = \theta$$
   Además, dado que $\overline{PS} \parallel \overline{QR}$, por ángulos alternos internos se cumple que:
   $$\angle PRQ = \angle RPS = \theta$$

2. **Análisis del triángulo $\triangle PQR$:**
   En $\triangle PQR$, como $\angle QPR = \angle PRQ = \theta$, el triángulo es isósceles con $PQ = QR$. 
   Trazando la altura desde $Q$ hacia la base $\overline{PR}$, esta divide a $\overline{PR}$ en dos segmentos iguales de longitud $\frac{1}{2}PR$. Usando trigonometría básica en uno de los triángulos rectángulos resultantes:
   $$\cos\theta = \frac{PR / 2}{QR} \implies PR = 2 \cdot QR \cos\theta$$

3. **Análisis del triángulo rectángulo $\triangle PRS$:**
   Dado que $\overline{PR} \perp \overline{RS}$, el ángulo $\angle PRS = 90^\circ$. En el triángulo rectángulo $\triangle PRS$, tenemos que:
   $$\cos\theta = \frac{PR}{PS} \implies PR = PS \cos\theta$$

4. **Relación entre las bases y las áreas:**
   Igualando las dos expresiones para $PR$:
   $$2 \cdot QR \cos\theta = PS \cos\theta$$
   Como $0^\circ < \theta < 90^\circ$, $\cos\theta \neq 0$, por lo que podemos dividir ambos lados entre $\cos\theta$:
   $$PS = 2 \cdot QR \implies QR = \frac{1}{2} PS$$

   Los triángulos $\triangle PQR$ y $\triangle PRS$ tienen la misma altura $h$ (la distancia perpendicular entre las rectas paralelas $\overline{QR}$ y $\overline{PS}$). Por lo tanto, la razón entre sus áreas es igual a la razón entre sus bases:
   $$\frac{[\triangle PQR]}{[\triangle PRS]} = \frac{\frac{1}{2} \cdot QR \cdot h}{\frac{1}{2} \cdot PS \cdot h} = \frac{QR}{PS} = \frac{1}{2}$$
   Es decir, $[\triangle PQR] = \frac{1}{2}[\triangle PRS]$.

5. **Cálculo final:**
   El área total del trapecio es la suma de las áreas de ambos triángulos:
   $$[PQRS] = [\triangle PQR] + [\triangle PRS] = 45$$
   Sustituyendo $[\triangle PQR] = \frac{1}{2}[\triangle PRS]$:
   $$\frac{1}{2}[\triangle PRS] + [\triangle PRS] = 45$$
   $$\frac{3}{2}[\triangle PRS] = 45 \implies [\triangle PRS] = 30$$

\boxed{30}