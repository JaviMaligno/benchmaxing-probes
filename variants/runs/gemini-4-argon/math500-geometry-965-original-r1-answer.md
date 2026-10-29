Para encontrar el área del triángulo $ACD$, denotada como $[\triangle ACD]$, podemos analizar las propiedades geométricas del trapecio paso a paso:

1. **Ángulos alternos internos y bisectriz:**
   Sea $\angle CAD = \theta$. Como $\overline{AC}$ biseca al ángulo $\angle BAD$, tenemos que:
   $$\angle BAC = \angle CAD = \theta$$
   Además, dado que $\overline{AD} \parallel \overline{BC}$, los ángulos alternos internos son iguales, por lo que:
   $$\angle BCA = \angle CAD = \theta$$

2. **Triángulo isósceles $\triangle ABC$:**
   En el triángulo $\triangle ABC$, como $\angle BAC = \angle BCA = \theta$, el triángulo es isósceles con $AB = BC$. 
   Si trazamos la altura desde $B$ hacia el lado $\overline{AC}$, esta biseca a $\overline{AC}$, de modo que:
   $$AC = 2 \cdot BC \cos\theta$$

3. **Relación entre las bases en el triángulo rectángulo $\triangle ACD$:**
   Dado que $\overline{AC} \perp \overline{CD}$, el triángulo $\triangle ACD$ es rectángulo en $C$. Usando trigonometría básica en $\triangle ACD$:
   $$\cos\theta = \frac{AC}{AD} \implies AC = AD \cos\theta$$
   Igualando ambas expresiones para $AC$:
   $$AD \cos\theta = 2 \cdot BC \cos\theta \implies AD = 2 \cdot BC$$

4. **Relación de áreas:**
   El área del trapecio $ABCD$ es la suma de las áreas de los triángulos $\triangle ABC$ y $\triangle ACD$. Como las bases $\overline{AD}$ y $\overline{BC}$ son paralelas, ambos triángulos tienen la misma altura $h$ (la altura del trapecio):
   $$[\triangle ABC] = \frac{1}{2} BC \cdot h$$
   $$[\triangle ACD] = \frac{1}{2} AD \cdot h = \frac{1}{2} (2 \cdot BC) \cdot h = 2 [\triangle ABC]$$

5. **Cálculo final:**
   Sustituyendo en el área total del trapecio:
   $$[ABCD] = [\triangle ABC] + [\triangle ACD] = \frac{1}{2}[\triangle ACD] + [\triangle ACD] = \frac{3}{2}[\triangle ACD]$$
   Dado que $[ABCD] = 42$:
   $$\frac{3}{2}[\triangle ACD] = 42 \implies [\triangle ACD] = 42 \cdot \frac{2}{3} = 28$$

\boxed{28}