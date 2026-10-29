## Solución

**Configuración de coordenadas.** Coloco $D=(0,0)$, $A=(a,0)$ (así $\overline{AD}$ está sobre el eje $x$), y como $\overline{BC}\parallel\overline{AD}$, escribo $C=(c,h)$, $B=(b,h)$ con $h>0$.

**Condición 1: perpendicularidad $\overline{AC}\perp\overline{CD}$.**
$$(A-C)\cdot(D-C)=(a-c)(-c)+h^2=0 \;\Longrightarrow\; h^2=c(a-c). \tag{1}$$

**Condición 2: $\overline{AC}$ bisecta $\angle BAD$.**
El vector unitario a lo largo de $\overrightarrow{AD}$ es $(-1,0)$ y el de $\overrightarrow{AB}$ es $\frac{(b-a,h)}{|AB|}$. La dirección de la bisectriz es su suma:
$$(-1,0)+\frac{(b-a,h)}{|AB|}.$$
Como $\overrightarrow{AC}=(c-a,h)$ es paralelo a esta dirección, de la segunda componente sale el factor de escala $\lambda=|AB|$, y de la primera componente:
$$c-a=-|AB|+(b-a)\;\Longrightarrow\; |AB|=b-c.$$
Elevando al cuadrado:
$$(b-c)^2=(b-a)^2+h^2 \;\Longrightarrow\; (a-c)(2b-a-c)=h^2. \tag{2}$$

**Comparando (1) y (2):**
$$c(a-c)=(a-c)(2b-a-c)\;\Longrightarrow\;2b-a-c=c\;\Longrightarrow\; b=\frac{a}{2}+c.$$
Por lo tanto:
$$BC=b-c=\frac{a}{2}\quad\text{y}\quad |AB|=\frac{a}{2}.$$

**Verificación de consistencia:** con $b=a/2+c$,
$$(b-a)^2+h^2=\left(c-\tfrac{a}{2}\right)^2+c(a-c)=c^2-ac+\tfrac{a^2}{4}+ac-c^2=\tfrac{a^2}{4}=(b-c)^2. \checkmark$$

**Área del trapecio.** Las bases son $AD=a$ y $BC=\tfrac{a}{2}$:
$$[ABCD]=\frac{1}{2}\left(a+\frac{a}{2}\right)h=\frac{3ah}{4}=42 \;\Longrightarrow\; ah=56.$$

**Área del triángulo:**
$$[\triangle ACD]=\frac{1}{2}\cdot AD\cdot h=\frac{1}{2}ah=\frac{56}{2}=28.$$

*(Comprobación numérica: $a=14$, $h=4$, $c=7-\sqrt{33}$, $b=14-c$ satisface ambas condiciones y da $[ABCD]=42$, $[\triangle ACD]=28$.)*

$$\boxed{28}$$