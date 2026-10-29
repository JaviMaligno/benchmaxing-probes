## Planteamiento con coordenadas

Coloco el hexágono regular con circunradio 1 (lado 1), con vértices en orden:

- $P = (1, 0)$
- $Q = \left(\tfrac12, \tfrac{\sqrt3}{2}\right)$
- $R = \left(-\tfrac12, \tfrac{\sqrt3}{2}\right)$
- $S = (-1, 0)$
- $T = \left(-\tfrac12, -\tfrac{\sqrt3}{2}\right)$
- $U = \left(\tfrac12, -\tfrac{\sqrt3}{2}\right)$

**Punto $X$:** sobre $\overline{RS}$ con $RX = \tfrac13$. Como $\vec{RS} = \left(-\tfrac12, -\tfrac{\sqrt3}{2}\right)$ tiene longitud 1:
$$X = R + \tfrac13\vec{RS} = \left(-\tfrac{2}{3}, \tfrac{\sqrt3}{3}\right)$$

**Punto $Y$:** parametrizo $Y = S + t\,\vec{ST} = \left(-1+\tfrac{t}{2},\ -\tfrac{t\sqrt3}{2}\right)$ con $t \in [0,1]$.

Para que $PXYU$ sea trapecio (con $Y$ interior al lado), necesito $\overline{PX} \parallel \overline{YU}$:

- $\vec{PX} = \left(-\tfrac{5}{3}, \tfrac{\sqrt3}{3}\right)$
- $\vec{YU} = \left(\tfrac{3-t}{2}, \tfrac{\sqrt3(t-1)}{2}\right)$

La condición de paralelismo (producto cruzado nulo):
$$-\tfrac{5}{3}\cdot\tfrac{\sqrt3(t-1)}{2} - \tfrac{\sqrt3}{3}\cdot\tfrac{3-t}{2} = 0 \;\Longrightarrow\; -5(t-1) - (3-t) = 0 \;\Longrightarrow\; t = \tfrac12$$

Entonces $Y = \left(-\tfrac34, -\tfrac{\sqrt3}{4}\right)$.

## Altura desde $Y$ hasta $\overline{PX}$

La recta $PX$ pasa por $P=(1,0)$ con dirección $(-5, \sqrt3)$; un vector normal es $(\sqrt3, 5)$, de norma $\sqrt{28} = 2\sqrt7$.

Con $\vec{PY} = \left(-\tfrac{7}{4}, -\tfrac{\sqrt3}{4}\right)$, la distancia es:
$$d = \frac{\left|\sqrt3\cdot\left(-\tfrac74\right) + 5\cdot\left(-\tfrac{\sqrt3}{4}\right)\right|}{2\sqrt7} = \frac{\tfrac{12\sqrt3}{4}}{2\sqrt7} = \frac{3\sqrt3}{2\sqrt7} = \frac{3\sqrt{21}}{14}$$

$$\boxed{\dfrac{3\sqrt{21}}{14}}$$