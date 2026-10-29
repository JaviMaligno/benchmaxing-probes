## Solución

**Planteamiento.** Coloco $P$ en el origen, con $Q=(0,q)$ en el eje $y$ y $R=(r,0)$ en el eje $x$, de modo que $q^2+r^2 = QR^2 = (4\sqrt{301})^2 = 4816$.

Como $PX=PY=XY=26$, el triángulo $PXY$ es equilátero, así que $X$ e $Y$ están en la circunferencia de radio 26 centrada en $P$ y el ángulo $\angle XPY = 60^\circ$. Escribo
$$X = 26(\cos\theta_1,\sin\theta_1), \qquad Y = 26(\cos\theta_2,\sin\theta_2), \qquad \theta_1 = \theta_2 + 60^\circ.$$

**Condiciones de equidistancia.** $QX = PX$ implica que $X$ está en la mediatriz de $PQ$, es decir $X_y = q/2$, luego $q = 52\sin(\theta_2+60^\circ)$. Análogamente, $RY = PY$ da $Y_x = r/2$, luego $r = 52\cos\theta_2$.

**Usar la hipotenusa.** Sustituyendo en $q^2+r^2 = 4816$ con $\beta = \theta_2$:
$$\sin^2(\beta+60^\circ) + \cos^2\beta = \frac{4816}{2704} = \frac{301}{169}.$$
Con identidades de ángulo doble, el lado izquierdo es
$$1 + \tfrac{1}{2}\big[\cos 2\beta - \cos(2\beta+120^\circ)\big] = 1 + \tfrac{\sqrt3}{2}\sin(2\beta+60^\circ),$$
de donde
$$\sin(2\beta+60^\circ) = \frac{2}{\sqrt3}\cdot\frac{132}{169} = \frac{88\sqrt3}{169}.$$

**Área del cuadrilátero.** El triángulo $PQR$ se descompone como $[PQX] + [PXY] + [PRY] + [QXYR]$. Calculando cada pieza con $s = \sin(2\beta+60^\circ)$:

- $[PQR] = \tfrac12 qr = 1352\sin(\beta+60^\circ)\cos\beta = 676\,s + 338\sqrt3$,
- $[PQX] = \tfrac12 \cdot q \cdot X_x = 338\sin(2\beta+120^\circ)$,
- $[PRY] = \tfrac12 \cdot r \cdot Y_y = 338\sin 2\beta$,
- $[PQX]+[PRY] = 338\big[\sin(2\beta+120^\circ)+\sin 2\beta\big] = 338\,s$,
- $[PXY] = \tfrac{\sqrt3}{4}\cdot 26^2 = 169\sqrt3$.

Por lo tanto:
$$[QXYR] = (676s + 338\sqrt3) - 338s - 169\sqrt3 = 338s + 169\sqrt3 = 338\cdot\frac{88\sqrt3}{169} + 169\sqrt3 = 176\sqrt3 + 169\sqrt3 = 345\sqrt3.$$

$$\boxed{345}$$