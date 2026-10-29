## Planteamiento

Coloco coordenadas: como $\overline{AC}\perp\overline{CD}$, pongo $A=(0,0)$, $C=(c,0)$ con $\overline{AC}$ sobre el eje $x$, y $D=(c,h)$ con $h>0$.

**Paso 1: Usar la bisectriz.** Como $\overline{AC}$ biseca a $\angle BAD$, el rayo $\overrightarrow{AB}$ es la reflexión de $\overrightarrow{AD}$ respecto a la recta $AC$. Dirección de $\overrightarrow{AD}$: $(c,h)$, así que $\overrightarrow{AB}$ tiene dirección $(c,-h)$.

**Paso 2: Usar el paralelismo.** Como $\overline{BC}\parallel\overline{AD}$, la recta por $C$ tiene dirección $(c,h)$, y $B$ está sobre el rayo de dirección $(c,-h)$ desde $A$:
$$B=(c+t c,\; t h)$$
La reflexión de $B$ sobre el eje $x$ debe caer sobre el rayo $\overrightarrow{AD}$, es decir $(c(1+t),-th)=s(c,h)$. De la segunda coordenada: $s=-t$; sustituyendo en la primera:
$$c(1+t)=-tc \;\Rightarrow\; 1+t=-t \;\Rightarrow\; t=-\tfrac12$$
Por lo tanto $B=\left(\tfrac{c}{2},-\tfrac{h}{2}\right)$.

**Paso 3: Calcular las áreas.** La diagonal $\overline{AC}$ divide al trapecio:
$$[\triangle ACD]=\tfrac12\cdot c\cdot h, \qquad [\triangle ABC]=\tfrac12\left|\det\begin{pmatrix} c/2 & -h/2\\ c & 0\end{pmatrix}\right|=\tfrac12\cdot\tfrac{ch}{2}=\tfrac{ch}{4}$$

**Paso 4: Resolver.**
$$[\triangle ACD]=\tfrac{ch}{2}=2\cdot\tfrac{ch}{4}=2[\triangle ABC]$$
$$42=[\triangle ABC]+[\triangle ACD]=\tfrac{ch}{4}+\tfrac{ch}{2}=\tfrac{3ch}{4}$$
Así $ch=56$, y por lo tanto:
$$[\triangle ACD]=\tfrac12\cdot 56=28$$

**Verificación:** Con $c=7$, $h=8$: $A=(0,0)$, $B=(3.5,-4)$, $C=(7,0)$, $D=(7,8)$. Se cumple $\overline{BC}\parallel\overline{AD}$, la simetría respecto a $AC$ confirma la bisectriz, y $[ABCD]=14+28=42$. ✓

$$\boxed{28}$$