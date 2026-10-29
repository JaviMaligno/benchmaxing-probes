Para hallar el área del triángulo $XPS$, analizamos geométrica y trigonométricamente la configuración de los dos círculos circunscritos tangentes en $X$.

### Paso 1: Planteamiento de ángulos y diámetros desde $X$
Como $PQXRS$ es un pentágono convexo, los rayos que parten del vértice $X$ hacia los demás vértices aparecen en orden cíclico como $XQ, XP, XS, XR$. 
Sean $\alpha = \angle QXP$ y $\beta = \angle SXR$. Dado que $\angle QXR = 120^{\circ}$ y $\angle PXS = 90^{\circ}$, tenemos que:
$$\alpha + \beta = \angle QXR - \angle PXS = 120^{\circ} - 90^{\circ} = 30^{\circ}.$$

Sean $\omega_1$ y $\omega_2$ las circunferencias circunscritas a los triángulos $XPQ$ y $XRS$, respectivamente. Como $\omega_1$ y $\omega_2$ pasan por $X$ y son tangentes interiormente, su punto de tangencia es necesariamente $X$, y sus centros se encuentran sobre un mismo rayo que parte de $X$.

Sean $XY$ el diámetro de $\omega_1$ desde $X$ y $XZ$ el diámetro de $\omega_2$ desde $X$. Entonces $X, Y, Z$ son colineales y $Y, Z$ están sobre el mismo rayo desde $X$. Por la ley de los senos en $\triangle XPQ$ y $\triangle XRS$:
$$PQ = XY \sin \alpha, \qquad RS = XZ \sin \beta.$$
Como $PQ = RS$, se cumple que $XY \sin \alpha = XZ \sin \beta$.

### Paso 2: Coordenadas cartesianas con origen en $X$
Ubicamos el origen de coordenadas en $X(0,0)$, de modo que el rayo $XP$ coincida con el semieje positivo $x$ y el rayo $XS$ (perpendicular a $XP$, pues $\angle PXS = 90^{\circ}$) coincida con el semieje positivo $y$. En este sistema:
- $P = (XP, 0)$ y $S = (0, XS)$.
- Como $XQ = 3$ forma un ángulo $-\alpha$ con el eje $x$ positivo, $Q = (3 \cos \alpha, -3 \sin \alpha)$.
- Como $XR = 6$ forma un ángulo $90^{\circ} + \beta$ con el eje $x$ positivo, $R = (-6 \sin \beta, 6 \cos \beta)$.

Dado que $XY$ es el diámetro de $\omega_1$, tenemos $\angle XPY = \angle XQY = 90^{\circ}$. Por tanto:
1. La proyección de $Y$ sobre el eje $x$ es $P$, luego $\vec{XY} = (XP, y_Y)$.
2. Como $QY \perp XQ$, el producto escalar cumple $\vec{XY} \cdot \vec{XQ} = XQ^2 = 9$, es decir:
   $$XP \cos \alpha - y_Y \sin \alpha = 3.$$

Análogamente, como $XZ$ es el diámetro de $\omega_2$, tenemos $\angle XSZ = \angle XRZ = 90^{\circ}$. Por tanto:
1. La proyección de $Z$ sobre el eje $y$ es $S$, luego $\vec{XZ} = (x_Z, XS)$.
2. Como $RZ \perp XR$, el producto escalar cumple $\vec{XZ} \cdot \vec{XR} = XR^2 = 36$, es decir:
   $$-x_Z \sin \beta + XS \cos \beta = 6.$$

### Paso 3: Uso de la condición $PQ = RS$
Como $\vec{XY}$ y $\vec{XZ}$ tienen la misma dirección y $XY \sin \alpha = XZ \sin \beta$, definimos el vector común:
$$\vec{V} = (u, v) = \vec{XY} \sin \alpha = \vec{XZ} \sin \beta.$$
Igualando las componentes de $\vec{V}$:
- De la primera componente de $\vec{XY} \sin \alpha$: $u = XP \sin \alpha$, y por tanto $y_Y \sin \alpha = v$.
- De la segunda componente de $\vec{XZ} \sin \beta$: $v = XS \sin \beta$, y por tanto $x_Z \sin \beta = u$.

Sustituyendo $y_Y \sin \alpha = v$ y $x_Z \sin \beta = u$ en las ecuaciones de perpendicularidad anteriores, obtenemos el sistema:
$$\begin{cases}
XP \cos \alpha - XS \sin \beta = 3, \\
XP \sin \alpha - XS \cos \beta = -6.
\end{cases}$$

### Paso 4: Relación entre las áreas
Resolvemos para $XP$ aplicando la regla de Cramer. El determinante del sistema para $(XP, -XS)$ es:
$$\Delta = \cos \alpha \cos \beta - \sin \alpha \sin \beta = \cos(\alpha + \beta) = \cos 30^{\circ} = \frac{\sqrt{3}}{2}.$$
Por lo tanto:
$$\frac{\sqrt{3}}{2} XP = 3 \cos \beta + 6 \sin \beta.$$
Multiplicando ambos miembros por $XS$:
$$\frac{\sqrt{3}}{2} XP \cdot XS = 3 XS \cos \beta + 6 XS \sin \beta.$$
De la segunda ecuación del sistema sabemos que $XS \cos \beta = XP \sin \alpha + 6$. Sustituyendo esta expresión:
$$\frac{\sqrt{3}}{2} XP \cdot XS = 3(XP \sin \alpha + 6) + 6 XS \sin \beta = 3 XP \sin \alpha + 6 XS \sin \beta + 18.$$

Observamos ahora que las áreas de los tres triángulos que conforman el pentágono son:
$$[XPS] = \frac{1}{2} XP \cdot XS, \qquad [XPQ] = \frac{1}{2} \cdot 3 \cdot XP \sin \alpha, \qquad [XRS] = \frac{1}{2} \cdot 6 \cdot XS \sin \beta.$$
Sustituyendo $XP \cdot XS = 2[XPS]$, $3 XP \sin \alpha = 2[XPQ]$ y $6 XS \sin \beta = 2[XRS]$ en la identidad anterior:
$$\sqrt{3} [XPS] = 2[XPQ] + 2[XRS] + 18.$$

### Paso 5: Cálculo del área de $\triangle XPS$
Dado que el área total del pentágono es $[PQXRS] = [XPQ] + [XRS] + [XPS] = 27$, tenemos que $[XPQ] + [XRS] = 27 - [XPS]$. Sustituyendo esto en nuestra ecuación:
$$\sqrt{3} [XPS] = 2(27 - [XPS]) + 18 = 72 - 2[XPS].$$
Agrupando términos y despejando $[XPS]$:
$$(2 + \sqrt{3}) [XPS] = 72 \implies [XPS] = \frac{72}{2 + \sqrt{3}} = 72(2 - \sqrt{3}) = 144 - 72\sqrt{3}.$$

\boxed{144 - 72\sqrt{3}}