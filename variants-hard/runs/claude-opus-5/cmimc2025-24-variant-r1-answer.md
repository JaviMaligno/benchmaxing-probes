## Planteamiento

Coloco el hexágono regular con centro en el origen:

- $P=(1,0)$, $Q=(\tfrac12,\tfrac{\sqrt3}{2})$, $R=(-\tfrac12,\tfrac{\sqrt3}{2})$, $S=(-1,0)$, $T=(-\tfrac12,-\tfrac{\sqrt3}{2})$, $U=(\tfrac12,-\tfrac{\sqrt3}{2})$

**Punto $X$:** el vector unitario de $R$ hacia $S$ es $(-\tfrac12,-\tfrac{\sqrt3}{2})$, así que
$$X = R + \tfrac13\left(-\tfrac12,-\tfrac{\sqrt3}{2}\right) = \left(-\tfrac23,\ \tfrac{\sqrt3}{3}\right)$$

**Punto $Y$:** parametrizo $Y = S + t\left(\tfrac12,-\tfrac{\sqrt3}{2}\right) = \left(-1+\tfrac t2,\ -\tfrac{t\sqrt3}{2}\right)$ con $t\in[0,1]$.

## Condición de trapecio

Si se pidiera $\overline{XY}\parallel\overline{PU}$, resulta $t=0$ (es decir $Y=S$), caso degenerado. Luego el par paralelo debe ser $\overline{PX}\parallel\overline{YU}$.

- $X-P = \left(-\tfrac53,\ \tfrac{\sqrt3}{3}\right)$, con dirección $(-5,\sqrt3)$.
- $U-Y = \left(\tfrac32-\tfrac t2,\ \tfrac{\sqrt3(t-1)}{2}\right)$

Imponiendo proporcionalidad:
$$\frac{3-t}{-5} = t-1 \implies 3-t = -5t+5 \implies t=\tfrac12$$

Entonces $Y=\left(-\tfrac34,\ -\tfrac{\sqrt3}{4}\right)$. Se verifica que no es paralelogramo: $|PX| = \tfrac{2\sqrt7}{3}\approx 1{,}764$ mientras $|YU| = \tfrac{\sqrt7}{2}\approx 1{,}323$.

## Altura desde $Y$ hasta $\overline{PX}$

La recta $PX$ pasa por $P=(1,0)$ con dirección $(-5,\sqrt3)$; un vector normal es $(\sqrt3,5)$, de norma $\sqrt{28}=2\sqrt7$.

Con $Y-P=\left(-\tfrac74,-\tfrac{\sqrt3}{4}\right)$:
$$(Y-P)\cdot(\sqrt3,5) = -\tfrac{7\sqrt3}{4}-\tfrac{5\sqrt3}{4} = -3\sqrt3$$

$$d = \frac{3\sqrt3}{2\sqrt7} = \frac{3\sqrt{21}}{14}\approx 0{,}982$$

$$\boxed{\dfrac{3\sqrt{21}}{14}}$$