## Planteamiento

Coloco $\omega_3$ con centro $O_3$ en el origen, $P=(-12,0)$, $Q=(12,0)$, y el arco en $y\ge 0$.

**Posición de $\omega_2$ (radio $r$).** Su diámetro es una cuerda de $\omega_3$ de semilongitud $r$, así que su centro $O_2$ (punto medio de la cuerda) cumple $|O_3O_2| = \sqrt{144-r^2}$. Además, el arco de $\omega_2$ es tangente a $PQ$: la distancia de $O_2$ a la recta $PQ$ es $r$, y $T$ es el pie de esa perpendicular. Escribiendo $O_2=(x_c, r)$:

$$x_c^2 + r^2 = 144 - r^2 \;\Rightarrow\; x_c^2 = 144 - 2r^2.$$

Como $T=(x_c,0)$:

$$PT\cdot TQ = (12+x_c)(12-x_c) = 144 - x_c^2 = 2r^2.$$

**Condición de $\omega_1$ (radio 3, diámetro paralelo a $PQ$).** El diámetro de $\omega_1$ es una cuerda horizontal de $\omega_2$ de semilongitud $3$; su punto medio $O_1$ está en la vertical bajo $O_2$, a distancia $\sqrt{r^2-9}$:

$$O_1 = \big(x_c,\; r - \sqrt{r^2-9}\big).$$

El arco de $\omega_1$ debe ser tangente al diámetro de $\omega_2$, es decir, la distancia de $O_1$ a la recta de esa cuerda es $3$. Esa recta pasa por $O_2$ con normal unitaria $n = \dfrac{(x_c,\,r)}{\sqrt{144-r^2}}$, luego:

$$\big|(O_1-O_2)\cdot n\big| = \frac{r\sqrt{r^2-9}}{\sqrt{144-r^2}} = 3.$$

**Resolviendo:**

$$r^2(r^2-9) = 9(144 - r^2) \;\Rightarrow\; r^4 - 9r^2 = 1296 - 9r^2 \;\Rightarrow\; r^4 = 1296 \;\Rightarrow\; r^2 = 36.$$

Verificación rápida con $r=6$: $x_c = \sqrt{72}=6\sqrt2$, $O_2=(6\sqrt2, 6)$ con $|O_3O_2| = \sqrt{108}$ ✓; los extremos del diámetro de $\omega_2$, $(6\sqrt2 \pm 2\sqrt3,\; 6 \mp 2\sqrt6)$, satisfacen $x^2+y^2=144$ y quedan en el semiplano superior ✓.

Por lo tanto:

$$PT\cdot TQ = 2r^2 = 2\cdot 36 = \boxed{72}$$