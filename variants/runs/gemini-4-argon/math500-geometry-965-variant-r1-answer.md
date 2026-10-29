Para calcular el área $[\triangle PRS]$, analicemos las propiedades geométricas del trapecio $PQRS$ paso a paso:

1. **Relación de ángulos e isósceles en $\triangle PQR$:**
   Sea $\theta = \angle RPS$. Como $\overline{PR}$ biseca al ángulo $\angle QPS$, tenemos que:
   $$\angle QPR = \angle RPS = \theta$$
   Además, dado que $\overline{PS} \parallel \overline{QR}$, los ángulos alternos internos son iguales, por lo que:
   $$\angle PRQ = \angle RPS = \theta$$
   En el triángulo $PQR$, como $\angle QPR = \angle PRQ = \theta$, concluimos que $\triangle PQR$ es isósceles con $PQ = QR$.

2. **Relación entre las bases $PS$ y $QR$:**
   En el triángulo rectángulo $PRS$ (donde $\angle PRS = 90^\circ$), tenemos que:
   $$PR = PS \cos\theta$$
   Por otro lado, en el triángulo isósceles $PQR$ con lados iguales $PQ = QR$ y ángulos basales $\theta$, al trazar la altura desde $Q$ hacia la base $PR$ obtenemos:
   $$PR = 2 \cdot QR \cos\theta$$
   Igualando ambas expresiones para $PR$:
   $$PS \cos\theta = 2 \cdot QR \cos\theta$$
   Como $0^\circ < \theta < 90^\circ$, $\cos\theta \neq 0$, podemos dividir por $\cos\theta$ para obtener:
   $$PS = 2 \cdot QR$$

3. **Cálculo del área $[\triangle PRS]$:**
   Los triángulos $\triangle PRS$ y $\triangle PQR$ comparten la misma altura $h$ (la distancia perpendicular entre las bases paralelas $\overline{PS}$ y $\overline{QR}$). Por lo tanto, la razón entre sus áreas es igual a la razón entre sus bases:
   $$\frac{[\triangle PRS]}{[\triangle PQR]} = \frac{\frac{1}{2} \cdot PS \cdot h}{\frac{1}{2} \cdot QR \cdot h} = \frac{PS}{QR} = 2$$
   De este modo, $[\triangle PQR] = \frac{1}{2}[\triangle PRS]$.

   Sabemos que el área total del trapecio es $[PQRS] = [\triangle PRS] + [\triangle PQR] = 45$. Sustituyendo la relación anterior:
   $$[\triangle PRS] + \frac{1}{2}[\triangle PRS] = 45$$
   $$\frac{3}{2}[\triangle PRS] = 45 \implies [\triangle PRS] = 30$$

\boxed{30}