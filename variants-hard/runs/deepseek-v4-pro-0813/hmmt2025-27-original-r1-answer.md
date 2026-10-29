Voy a resolver el problema paso a paso.

**Datos:**
- $AB=6$, $AC=8$, $BC=7$
- $\angle ABP = \angle ACP$
- $\dfrac{BP}{PC}=\dfrac{1}{2}$
- $P$ interior al triángulo

Queremos $\dfrac{[BPC]}{[ABC]}$.

---

**Paso 1: Relación entre las áreas**

Como $P$ está sobre el segmento que une... bueno, en realidad $P$ no está necesariamente sobre $BC$. Pero sabemos que $BP:PC=1:2$.

Consideremos la recta $BC$. Si $P$ estuviera sobre $BC$, entonces $[BPC]=0$, lo cual no es el caso porque $P$ es interior. Entonces $P$ forma un triángulo con $B$ y $C$, y su área es $\frac12 \cdot BC \cdot h_P$, donde $h_P$ es la distancia de $P$ a la recta $BC$.

El área de $ABC$ es $\frac12 \cdot BC \cdot h_A$, donde $h_A$ es la altura desde $A$.

Por lo tanto,
$$\frac{[BPC]}{[ABC]}=\frac{h_P}{h_A}.$$

---

**Paso 2: Localizar P usando la condición de ángulos**

La condición $\angle ABP=\angle ACP$ es clave. Interpretémosla.

Sea $\alpha=\angle ABP=\angle ACP$.

En el triángulo $ABC$, aplicamos la ley de senos o el teorema de la bisectriz generalizado...

Una idea útil: la condición $\angle ABP=\angle ACP$ significa que los puntos $B$ y $C$ "ven" el segmento $AP$ bajo ángulos complementarios en cierto sentido. De hecho, esta es la condición de que $A$, $B$, $C$, $P$ sean concíclicos **o** estén en una configuración especial.

Revisemos: Si $A$, $B$, $C$, $P$ fueran concíclicos, entonces $\angle ABP$ y $\angle ACP$ subtienden el mismo arco $AP$. Efectivamente, $\angle ABP$ subtiende el arco $AP$ (desde $B$), y $\angle ACP$ también subtiende el arco $AP$ (desde $C$). Si $B$ y $C$ están del mismo lado de la cuerda $AP$, estos ángulos serían iguales.

Así que $A$, $B$, $C$, $P$ son concíclicos, con $B$ y $C$ del mismo lado de $AP$.

---

**Paso 3: Usar el teorema de Ptolomeo (o potencia de punto)**

Como $A$, $B$, $C$, $P$ son concíclicos (en ese orden cíclico), el cuadrilátero $ABPC$ es cíclico.

Por el teorema de Ptolomeo para el cuadrilátero $ABPC$ (con diagonales $AP$ y $BC$):
$$AB\cdot PC + AC\cdot BP = AP\cdot BC.$$

Sustituimos $AB=6$, $AC=8$, $BC=7$, y $BP=x$, $PC=2x$ (por la razón $1:2$):
$$6(2x)+8(x)=AP\cdot 7,$$
$$12x+8x=7\,AP,$$
$$20x=7\,AP,$$
$$AP=\frac{20x}{7}.$$

---

**Paso 4: Usar la ley de cosenos en BPC**

En el triángulo $BPC$, conocemos $BC=7$, $BP=x$, $PC=2x$.

Sea $\theta=\angle BPC$. Por la ley de cosenos:
$$BC^2=BP^2+PC^2-2(BP)(PC)\cos\theta,$$
$$49=x^2+4x^2-4x^2\cos\theta,$$
$$49=5x^2-4x^2\cos\theta. \quad (1)$$

---

**Paso 5: Ángulos en el cuadrilátero cíclico**

Como $ABPC$ es cíclico, los ángulos opuestos suman $180^\circ$:
$$\angle BAC + \angle BPC=180^\circ.$$

Además, en el cuadrilátero cíclico, $\angle BPC$ subtiende el arco $BC$ que no contiene a $P$, igual que $\angle BAC$.

Entonces $\theta=\angle BPC$ y $\phi=\angle BAC$ son suplementarios: $\theta+\phi=180^\circ$. Por lo tanto, $\cos\theta=-\cos\phi$.

---

**Paso 6: Calcular $\cos\phi$ con la ley de cosenos en ABC**

En $ABC$:
$$BC^2=AB^2+AC^2-2(AB)(AC)\cos\phi,$$
$$49=36+64-96\cos\phi,$$
$$49=100-96\cos\phi,$$
$$96\cos\phi=51,$$
$$\cos\phi=\frac{51}{96}=\frac{17}{32}.$$

Entonces $\cos\theta=-\frac{17}{32}$.

---

**Paso 7: Hallar $x$**

Sustituimos en (1):
$$49=5x^2-4x^2\left(-\frac{17}{32}\right),$$
$$49=5x^2+\frac{68}{32}x^2,$$
$$49=5x^2+\frac{17}{8}x^2,$$
$$49=\frac{40}{8}x^2+\frac{17}{8}x^2=\frac{57}{8}x^2,$$
$$x^2=49\cdot \frac{8}{57}=\frac{392}{57}.$$

---

**Paso 8: Calcular la razón de áreas**

Queremos $\dfrac{[BPC]}{[ABC]}$.

$$[BPC]=\frac12(BP)(PC)\sin\theta=\frac12(x)(2x)\sin\theta=x^2\sin\theta.$$

$$[ABC]=\frac12(AB)(AC)\sin\phi=\frac12(6)(8)\sin\phi=24\sin\phi.$$

Como $\theta$ y $\phi$ son suplementarios, $\sin\theta=\sin\phi$. Entonces:
$$\frac{[BPC]}{[ABC]}=\frac{x^2\sin\theta}{24\sin\phi}=\frac{x^2}{24}.$$

Sustituimos $x^2=\frac{392}{57}$:
$$\frac{[BPC]}{[ABC]}=\frac{392/57}{24}=\frac{392}{57\cdot 24}=\frac{392}{1368}.$$

Simplificamos: $392=8\cdot 49$ y $1368=8\cdot 171$, así que:
$$\frac{392}{1368}=\frac{49}{171}.$$

Y $171=9\cdot 19$, $49=7^2$, no comparten factores.

---

**Resultado final:**
$$\boxed{\frac{49}{171}}$$