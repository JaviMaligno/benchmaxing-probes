Para hallar el área del triángulo $ACD$, denotada como $[\triangle ACD]$, analizamos las propiedades geométricas del trapecio $ABCD$ paso a paso:

1. **Relación de ángulos e isósceles:**
   Sea $\angle CAD = \theta$. Como $\overline{AC}$ biseca al ángulo $\angle BAD$, tenemos que:
   $$\angle BAC = \angle CAD = \theta$$
   Dado que $\overline{AD} \parallel \overline{BC}$, los ángulos alternos internos son iguales, por lo que:
   $$\angle BCA = \angle CAD = \theta$$
   Por lo tanto, en el triángulo $\triangle ABC$ tenemos que $\angle BAC = \angle BCA = \theta$, lo que implica que $\triangle ABC$ es un triángulo isósceles con $AB = BC$.

2. **Relación entre las bases $AD$ y $BC$:**
   Sea $AC = x$.
   - En el triángulo isósceles $\triangle ABC$, si trazamos la altura desde $B$ hasta el lado $\overline{AC}$, esta cae en su punto medio, dividiendo a $\overline{AC}$ en dos segmentos de longitud $\frac{x}{2}$. Usando trigonometría en uno de los triángulos rectángulos resultantes:
     $$\cos\theta = \frac{x/2}{BC} \implies BC = \frac{x}{2\cos\theta}$$
   - En el triángulo rectángulo $\triangle ACD$ (donde $\angle ACD = 90^\circ$ y $\angle CAD = \theta$), tenemos:
     $$\cos\theta = \frac{AC}{AD} = \frac{x}{AD} \implies AD = \frac{x}{\cos\theta}$$

   Comparando ambas expresiones, observamos que independientemente del valor de $\theta$:
   $$AD = 2BC$$

3. **Cálculo del área $[\triangle ACD]$:**
   Los triángulos $\triangle ABC$ y $\triangle ACD$ comparten la misma altura $h$ del trapecio (la distancia perpendicular entre las rectas paralelas $\overline{AD}$ y $\overline{BC}$). Por lo tanto, la razón entre sus áreas es igual a la razón entre sus bases:
   $$\frac{[\triangle ACD]}{[\triangle ABC]} = \frac{\frac{1}{2} \cdot AD \cdot h}{\frac{1}{2} \cdot BC \cdot h} = \frac{AD}{BC} = 2 \implies [\triangle ABC] = \frac{1}{2}[\triangle ACD]$$

   Como el área total del trapecio es $[ABCD] = [\triangle ABC] + [\triangle ACD] = 42$, sustituimos:
   $$\frac{1}{2}[\triangle ACD] + [\triangle ACD] = 42$$
   $$\frac{3}{2}[\triangle ACD] = 42$$
   $$[\triangle ACD] = 42 \cdot \frac{2}{3} = 28$$

\boxed{28}