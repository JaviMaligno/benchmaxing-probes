## Planteamiento

Coloco el hexágono regular de lado 1 centrado en el origen:

- $A(1,0)$, $B\left(\tfrac12,\tfrac{\sqrt3}{2}\right)$, $C\left(-\tfrac12,\tfrac{\sqrt3}{2}\right)$, $D(-1,0)$, $E\left(-\tfrac12,-\tfrac{\sqrt3}{2}\right)$, $F\left(\tfrac12,-\tfrac{\sqrt3}{2}\right)$

**Punto $G$** (medio de $\overline{CD}$): $G\left(-\tfrac34,\tfrac{\sqrt3}{4}\right)$.

## Qué par de lados es paralelo

El cuadrilátero $AGHF$ tiene lados $AG$, $GH$, $HF$, $FA$. Hay dos posibilidades:

- **$GH \parallel FA$**: la pendiente de $FA$ es $\sqrt3$, y la recta por $G$ con pendiente $\sqrt3$ corta a la recta $DE$ ($y=-\sqrt3(x+1)$) exactamente en $x=-1$, es decir en $D$ mismo. Caso degenerado, se descarta.
- **$AG \parallel HF$**: este da el punto válido, de ahí la unicidad de $H$.

## Cálculo de $H$

Pendiente de $AG$: $m=\dfrac{\sqrt3/4-0}{-3/4-1}=-\dfrac{\sqrt3}{7}$.

Recta por $F$ con esa pendiente, igualada a $\overline{DE}$:

$$-\sqrt3(x+1)=-\frac{\sqrt3}{2}-\frac{\sqrt3}{7}\left(x-\frac12\right)$$

Dividiendo por $\sqrt3$ y multiplicando por 7: $-7x-7=-3-x \Rightarrow x=-\tfrac23$.

Entonces $H\left(-\tfrac23,\,-\tfrac{\sqrt3}{3}\right)$, que efectivamente está entre $D$ y $E$.

## Altura desde $H$ hasta $\overline{AG}$

Recta $AG$: $\sqrt3\,x+7y-\sqrt3=0$.

$$d=\frac{\left|\sqrt3\left(-\tfrac23\right)+7\left(-\tfrac{\sqrt3}{3}\right)-\sqrt3\right|}{\sqrt{3+49}}=\frac{\tfrac{12\sqrt3}{3}}{2\sqrt{13}}=\frac{4\sqrt3}{2\sqrt{13}}=\frac{2\sqrt{39}}{13}$$

Esta es la altura del trapecio ($\approx 0{,}961$).

\boxed{\dfrac{2\sqrt{39}}{13}}