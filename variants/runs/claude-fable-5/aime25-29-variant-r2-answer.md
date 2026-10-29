## Planteamiento

Coloco $P$ en el origen, $Q=(q,0)$, $R=(0,r)$, con $q^2+r^2 = (4\sqrt{301})^2 = 4816$.

**Ángulos en $P$.** Como $PX=PY=XY=26$, el triángulo $PXY$ es equilátero, así que $\angle XPY = 60^\circ$. Sean $\alpha = \angle QPX$ y $\beta = \angle RPY$. Entonces
$$\alpha + 60^\circ + \beta = 90^\circ \implies \alpha+\beta = 30^\circ.$$

**Lados.** El triángulo $PQX$ es isósceles con $PX=QX=26$, de modo que $q = 2\cdot 26\cos\alpha = 52\cos\alpha$. Análogamente $r = 52\cos\beta$.

De $q^2+r^2 = 4816$:
$$\cos^2\alpha + \cos^2\beta = \frac{4816}{2704} = \frac{301}{169}.$$

Usando $\cos^2\alpha+\cos^2\beta = 1 + \tfrac12\big(\cos 2\alpha + \cos 2\beta\big) = 1 + \tfrac{\sqrt3}{2}\cos(2\alpha-30^\circ)$ (pues $2\alpha+2\beta = 60^\circ$):
$$\frac{\sqrt3}{2}\cos(2\alpha-30^\circ) = \frac{301}{169}-1 = \frac{132}{169} \implies \cos(2\alpha-30^\circ) = \frac{88\sqrt3}{169}.$$

Nótese que $\alpha-\beta = 2\alpha - 30^\circ$, así que $\cos(\alpha-\beta) = \dfrac{88\sqrt3}{169}$.

## Área de $QXYR$

$$[QXYR] = [PQR] - [PQX] - [PRY] - [PXY].$$

- $[PQR] = \tfrac12 qr = 1352\cos\alpha\cos\beta = 676\big(\cos(\alpha-\beta) + \cos 30^\circ\big)$.
- $[PQX] = \tfrac12\cdot PX\cdot PQ\cdot\sin\alpha = 338\sin 2\alpha$, y $[PRY] = 338\sin 2\beta$. Su suma es $338\cdot 2\sin 30^\circ\cos(\alpha-\beta) = 338\cos(\alpha-\beta)$.
- $[PXY] = \tfrac{\sqrt3}{4}\cdot 26^2 = 169\sqrt3$.

Entonces:
$$[QXYR] = 676\cos(\alpha-\beta) + 338\sqrt3 - 338\cos(\alpha-\beta) - 169\sqrt3 = 338\cos(\alpha-\beta) + 169\sqrt3.$$

Sustituyendo $\cos(\alpha-\beta) = \frac{88\sqrt3}{169}$:
$$[QXYR] = 338\cdot\frac{88\sqrt3}{169} + 169\sqrt3 = 176\sqrt3 + 169\sqrt3 = 345\sqrt3.$$

$$\boxed{345}$$