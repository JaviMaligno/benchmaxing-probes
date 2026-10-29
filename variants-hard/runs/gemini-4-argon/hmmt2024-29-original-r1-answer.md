Para hallar la longitud de $CP$, podemos utilizar geometría y trigonometría.

### Paso 1: Análisis de los ángulos
Sea $\alpha = \angle BAC$. Como $X$ se encuentra en el segmento $\overline{AB}$, los puntos $A, X, B$ son colineales en ese orden, por lo que los ángulos $\angle AXC$ y $\angle BXC$ son suplementarios:
$$\angle AXC = 180^\circ - \angle BXC = 180^\circ - 60^\circ = 120^\circ$$

En el triángulo $\triangle AXC$, la suma de los ángulos internos es $180^\circ$, de modo que:
$$\angle ACX = 180^\circ - \angle XAC - \angle AXC = 180^\circ - \alpha - 120^\circ = 60^\circ - \alpha$$
Esto implica que $0^\circ < \alpha < 60^\circ$.

### Paso 2: Relaciones en el triángulo rectángulo
Sea $D$ el pie de la perpendicular trazada desde $B$ hacia el lado $\overline{AC}$. Como $BP \perp AC$ y $P$ está en el interior de $\triangle ABC$ (sobre el segmento $\overline{CX}$), los puntos $B, P, D$ son colineales en ese orden sobre dicha perpendicular.

En el triángulo rectángulo $\triangle ABD$ ($\angle ADB = 90^\circ$), con $AB = 6$:
$$AD = AB \cos\alpha = 6\cos\alpha$$
$$BD = AB \sin\alpha = 6\sin\alpha$$

Como $AC = 7$ y $BP = 4$, los catetos del triángulo rectángulo $\triangle PDC$ ($\angle PDC = 90^\circ$) son:
$$CD = AC - AD = 7 - 6\cos\alpha$$
$$PD = BD - BP = 6\sin\alpha - 4$$

### Paso 3: Cálculo de $CP$
Dado que $P$ pertenece al segmento $\overline{CX}$, tenemos que $\angle PCD = \angle ACX = 60^\circ - \alpha$. En el triángulo rectángulo $\triangle PDC$ con hipotenusa $CP$:
$$CD = CP \cos(60^\circ - \alpha) \implies 6\cos\alpha + CP \cos(60^\circ - \alpha) = 7$$
$$PD = CP \sin(60^\circ - \alpha) \implies 6\sin\alpha - CP \sin(60^\circ - \alpha) = 4$$

Elevamos ambas ecuaciones al cuadrado y las sumamos para eliminar $\alpha$:
$$(6\cos\alpha + CP \cos(60^\circ - \alpha))^2 + (6\sin\alpha - CP \sin(60^\circ - \alpha))^2 = 7^2 + 4^2$$

Desarrollando el miembro izquierdo y usando la identidad $\cos^2\theta + \sin^2\theta = 1$:
$$36(\cos^2\alpha + \sin^2\alpha) + CP^2(\cos^2(60^\circ - \alpha) + \sin^2(60^\circ - \alpha)) + 12 \cdot CP (\cos\alpha\cos(60^\circ - \alpha) - \sin\alpha\sin(60^\circ - \alpha)) = 49 + 16$$

Por la identidad del coseno de la suma de ángulos, $\cos A \cos B - \sin A \sin B = \cos(A+B)$, el término cruzado se simplifica a:
$$\cos\alpha\cos(60^\circ - \alpha) - \sin\alpha\sin(60^\circ - \alpha) = \cos(\alpha + 60^\circ - \alpha) = \cos 60^\circ = \frac{1}{2}$$

Sustituyendo este valor en la ecuación:
$$36 + CP^2 + 12 \cdot CP \left(\frac{1}{2}\right) = 65$$
$$CP^2 + 6 \cdot CP - 29 = 0$$

Aplicando la fórmula cuadrática y tomando la raíz positiva (ya que $CP > 0$):
$$CP = \frac{-6 + \sqrt{6^2 - 4(1)(-29)}}{2} = -3 + \sqrt{9 + 29} = \sqrt{38} - 3$$

\boxed{\sqrt{38}-3}