## Solución

**Configuración.** Sea $F$ el pie de la perpendicular desde $B$ a $AC$ (de modo que $B$, $P$, $F$ son colineales, con $P$ entre $B$ y $F$). Sea $A = \angle BAC$.

**Ángulos clave.** Como $\angle BXC = 60°$, entonces $\angle AXC = 120°$. En el triángulo $AXC$:
$$\angle XCA = 180° - A - 120° = 60° - A.$$

**Triángulo rectángulo $PFC$.** Tiene ángulo recto en $F$ y $\angle PCF = 60° - A$, así que:
$$PF = PC\sin(60°-A), \qquad CF = PC\cos(60°-A).$$

**Dos ecuaciones.** Con $BF = 6\sin A$, $AF = 6\cos A$:
- $BF = BP + PF$: $\quad 6\sin A - 4 = PC\sin(60°-A)$
- $CF = AC - AF$: $\quad 7 - 6\cos A = PC\cos(60°-A)$

**Eliminar $PC$.** Dividiendo y reorganizando (multiplicando en cruz):
$$6\big[\sin(60°-A)\cos A + \cos(60°-A)\sin A\big] = 7\sin(60°-A) + 4\cos(60°-A),$$
y el lado izquierdo es $6\sin 60° = 3\sqrt{3}$. Con $\theta = 60° - A$:
$$7\sin\theta + 4\cos\theta = 3\sqrt{3}.$$

**Calcular $PC^2$.** Sumando los cuadrados de las dos ecuaciones:
$$PC^2 = (6\sin A - 4)^2 + (7 - 6\cos A)^2 = 101 - 48\sin A - 84\cos A.$$
Sustituyendo $A = 60° - \theta$ y simplificando:
$$48\sin A + 84\cos A = 6\big[\sqrt{3}\,(7\sin\theta + 4\cos\theta) + (7\cos\theta - 4\sin\theta)\big] = 6\big[9 + v\big],$$
donde $v = 7\cos\theta - 4\sin\theta$. Por lo tanto:
$$PC^2 = 101 - 54 - 6v = 47 - 6v.$$

**Hallar $v$.** Como $u = 7\sin\theta + 4\cos\theta = 3\sqrt{3}$ y $u^2 + v^2 = 65$:
$$v^2 = 65 - 27 = 38 \implies v = \sqrt{38}$$
(se toma el signo positivo: la restricción $7\sin\theta + 4\cos\theta = 3\sqrt{3}$ con $A \in (0°, 90°)$ da $\theta \approx 10.4°$, y entonces $v > 0$).

**Resultado.**
$$PC^2 = 47 - 6\sqrt{38} = 38 - 2\cdot 3\sqrt{38} + 9 = (\sqrt{38} - 3)^2.$$

$$\boxed{CP = \sqrt{38} - 3}$$