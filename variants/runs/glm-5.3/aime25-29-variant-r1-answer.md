## Planteamiento

Sea $\angle QPX = \theta$ y $\angle YPR = \phi$. Como $PX = QX = 26$, el triángulo $PQX$ es isósceles con $\angle PQX = \angle QPX = \theta$, así que $PQ = 52\cos\theta$. Análogamente $PR = 52\cos\varphi$.

Como $PX = PY = XY = 26$, el triángulo $PXY$ es **equilátero**, con $\angle XPY = 60^\circ$. Con los rayos $PQ, PX, PY, PR$ en orden (X e Y son interiores):

$$\theta + 60^\circ + \varphi = 90^\circ \implies \theta + \varphi = 30^\circ.$$

## Condición sobre la hipotenusa

$$PQ^2 + PR^2 = QR^2 \implies 2704(\cos^2\theta + \cos^2\varphi) = 4816 \implies \cos^2\theta + \cos^2\varphi = \frac{301}{169}.$$

Con $\varphi = 30^\circ - \theta$ y $t = \tan\theta$, esto se reduce a:

$$1035t^2 - 338\sqrt{3}\,t + 21 = 0 \implies t = \frac{7\sqrt3}{23} \quad \text{o} \quad \frac{23\sqrt3}{1035}.$$

Las dos raíces son $\tan\theta$ y $\tan\varphi$ intercambiadas. Tomando $\tan\theta = \frac{7\sqrt3}{23}$:

$$\cos\theta = \frac{23}{26},\qquad \sin\theta = \frac{7\sqrt3}{26},\qquad \sin\varphi = \frac{1}{26},\qquad \cos\varphi = \frac{15\sqrt3}{26}.$$

(Efectivamente $PQ = 52\cdot\frac{23}{26} = 46$ y $PR = 52\cdot\frac{15\sqrt3}{26}=30\sqrt3$, y $46^2 + 2700 = 4816 = (4\sqrt{301})^2$ ✓)

## Área del cuadrilátero $QXYR$

El cuadrilátero es el triángulo $PQR$ menos los triángulos $PQX$, $PXY$ y $PRY$:

$$[QXYR] = [PQR] - [PQX] - [PXY] - [PRY].$$

- $[PQR] = \tfrac12 \cdot 46 \cdot 30\sqrt3 = 690\sqrt3$
- $[PQX] = \tfrac12(26)(26)\sin(\angle PXQ) = 338\sin 2\theta = 161\sqrt3$
- $[PXY] = \tfrac{\sqrt3}{4}(26)^2 = 169\sqrt3$
- $[PRY] = 338\sin 2\varphi = 15\sqrt3$

$$[QXYR] = 690\sqrt3 - (161 + 169 + 15)\sqrt3 = 690\sqrt3 - 345\sqrt3 = 345\sqrt3.$$

Por lo tanto $n = 345$.

$$\boxed{345}$$