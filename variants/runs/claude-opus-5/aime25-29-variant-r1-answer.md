## Planteamiento

Como $PX = PY = XY = 26$, el triángulo $PXY$ es equilátero (lado 26). Coloco $P$ en el origen y defino:

- $\alpha = \angle XPQ$, $\beta = \angle YPR$

Como $\angle P = 90°$ y el ángulo $\angle XPY = 60°$, se tiene $\alpha + \beta = 30°$.

## Lados del triángulo

El triángulo $PQX$ es isósceles con $PX = QX = 26$, así que la base vale $PQ = 52\cos\alpha$. Análogamente $PR = 52\cos\beta$.

De $PQ^2 + PR^2 = (4\sqrt{301})^2 = 4816$:

$$\cos^2\alpha + \cos^2\beta = \frac{4816}{2704} = \frac{301}{169}$$

Usando $\cos^2\alpha+\cos^2\beta = 1 + \cos(\alpha+\beta)\cos(\alpha-\beta)$:

$$\frac{\sqrt3}{2}\cos(\alpha-\beta) = \frac{301}{169}-1 = \frac{132}{169} \quad\Longrightarrow\quad \cos(\alpha-\beta) = \frac{88\sqrt3}{169}$$

## Áreas

**Triángulo completo:**
$$[PQR] = \tfrac12 \cdot 52\cos\alpha\cdot 52\cos\beta = 1352\cos\alpha\cos\beta$$
con $\cos\alpha\cos\beta = \tfrac12\left[\tfrac{88\sqrt3}{169} + \tfrac{\sqrt3}{2}\right]$, lo que da
$$[PQR] = 352\sqrt3 + 338\sqrt3 = 690\sqrt3$$

**Triángulos laterales:** $[PQX] = 338\sin 2\alpha$, $[PRY] = 338\sin 2\beta$, y
$$\sin2\alpha+\sin2\beta = 2\sin(\alpha+\beta)\cos(\alpha-\beta) = \frac{88\sqrt3}{169}$$
$$\Longrightarrow [PQX]+[PRY] = 176\sqrt3$$

**Triángulo equilátero:** $[PXY] = \tfrac{\sqrt3}{4}\cdot 676 = 169\sqrt3$

## Resultado

$$[QXYR] = 690\sqrt3 - 176\sqrt3 - 169\sqrt3 = 345\sqrt3$$

$$\boxed{345}$$