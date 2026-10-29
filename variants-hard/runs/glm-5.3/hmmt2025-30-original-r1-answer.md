## Planteamiento

Sea el prisma $[0,A]\times[0,B]\times[0,C]$ y el plano $px+qy+rz=1$ con $p,q,r>0$. Defino $a=pA,\ b=qB,\ c=rC$. Para que la sección sea un **hexágono** se necesita $0<a,b,c<1< a+b,\,b+c,\,c+a$. Entonces el plano cruza exactamente las seis aristas "medias", y los lados opuestos del hexágono (que yacen en caras opuestas) son paralelos: los pares son el $1^{\circ}$ con el $4^{\circ}$, el $2^{\circ}$ con el $5^{\circ}$, el $3^{\circ}$ con el $6^{\circ}$. Un cálculo directo de los vértices da:

$$\text{par en caras }x:\quad (b+c-1)K_1,\ (1-a)K_1,\qquad K_1=\sqrt{q^{-2}+r^{-2}}$$
$$\text{par en caras }z:\quad (1-c)K_2,\ (a+b-1)K_2,\qquad K_2=\sqrt{p^{-2}+q^{-2}}$$
$$\text{par en caras }y:\quad (a+c-1)K_3,\ (1-b)K_3,\qquad K_3=\sqrt{p^{-2}+r^{-2}}$$

## Resolución del sistema

Los datos en orden cíclico son $45,66,63,55,54,77$, así que los pares son $(45,55),(66,54),(63,77)$. Con $\alpha=1-a,\ \beta=1-b,\ \gamma=1-c$:

$$\frac{1-\beta-\gamma}{\alpha}=\frac{45}{55}=\frac{9}{11},\qquad \frac{1-\alpha-\beta}{\gamma}=\frac{54}{66}=\frac{9}{11},\qquad \frac{1-\alpha-\gamma}{\beta}=\frac{63}{77}=\frac{9}{11}.$$

Restando las ecuaciones dos a dos se obtiene $\alpha=\beta=\gamma$, y sustituyendo: $2\alpha = 1-\frac{9}{11}\alpha \Rightarrow \alpha=\beta=\gamma=\frac{11}{31}$, es decir $a=b=c=\frac{20}{31}$. Además $K_1=\frac{55}{\alpha}=155$, $K_2=\frac{66}{\gamma}=186$, $K_3=\frac{77}{\beta}=217$ (o sea $5\cdot31,\ 6\cdot31,\ 7\cdot31$).

Recuperando $u=p^{-2},\ v=q^{-2},\ w=r^{-2}$ (con $K_1^2=v+w$, etc.):

$$p^{-2}=\tfrac{K_2^2+K_3^2-K_1^2}{2}=28830=30\cdot31^2,\quad q^{-2}=5766=6\cdot31^2,\quad r^{-2}=18259=19\cdot31^2.$$

**Verificación explícita:** con $A=20\sqrt{30},\ B=20\sqrt6,\ C=20\sqrt{19}$ y plano $\frac{x}{\sqrt{30}}+\frac{y}{\sqrt6}+\frac{z}{\sqrt{19}}=31$, los vértices dan los lados $9\sqrt{25}=45$, $11\sqrt{36}=66$, $9\sqrt{49}=63$, $11\sqrt{25}=55$, $9\sqrt{36}=54$, $11\sqrt{49}=77$ en orden. ✓

## Distancia del centro

El centro es $\left(\frac{A}{2},\frac{B}{2},\frac{C}{2}\right)=\left(10\sqrt{30},10\sqrt6,10\sqrt{19}\right)$, y el valor del plano allí es $10+10+10=30$. Entonces

$$d=\frac{|30-31|}{\sqrt{\frac1{30}+\frac16+\frac1{19}}}=\frac{1}{\sqrt{144/570}}=\sqrt{\frac{95}{24}}=\frac{\sqrt{570}}{12}\approx 1.99.$$

$$\boxed{\dfrac{\sqrt{570}}{12}}$$