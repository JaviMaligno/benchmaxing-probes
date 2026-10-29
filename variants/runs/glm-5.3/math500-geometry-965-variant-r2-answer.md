## Planteamiento

Coloco coordenadas: $P=(0,0)$ y $S$ sobre el eje $x$. Como $PS\parallel QR$, la base $QR$ es horizontal.

Sea $\angle QPR = \angle RPS = \alpha$ (la bisectriz). Entonces:
- $\vec{PR}$ tiene dirección $(\cos\alpha,\sin\alpha)$: escribo $R=(t\cos\alpha,\, t\sin\alpha)$,
- $\vec{PQ}$ tiene dirección $(\cos 2\alpha,\sin 2\alpha)$,
- $S=(a,0)$ para algún $a>0$.

**Condición $PR\perp RS$:** $\vec{RS}=(a-t\cos\alpha,\,-t\sin\alpha)$, y perpendicularidad con $(\cos\alpha,\sin\alpha)$ da
$$a\cos\alpha - t(\cos^2\alpha+\sin^2\alpha)=0 \;\Rightarrow\; t=a\cos\alpha.$$
Así que $R=(a\cos^2\alpha,\; a\cos\alpha\sin\alpha)$.

**Ubico $Q$:** está en la altura de $R$ (base paralela) y sobre el rayo de ángulo $2\alpha$:
$$Q=u(\cos2\alpha,\sin2\alpha),\qquad u\sin 2\alpha = a\cos\alpha\sin\alpha
\;\Rightarrow\; u=\frac{a\cos\alpha\sin\alpha}{2\sin\alpha\cos\alpha}=\frac a2.$$
Entonces $Q=\left(\tfrac a2\cos 2\alpha,\; a\cos\alpha\sin\alpha\right)$, y la base superior es
$$QR=a\cos^2\alpha-\tfrac a2\cos 2\alpha = a\cos^2\alpha-a\cos^2\alpha+\tfrac a2=\frac a2.$$

**Altura del trapecio:** $h=a\cos\alpha\sin\alpha$.

## Áreas

$$[PQRS]=\frac12\left(a+\frac a2\right)h=\frac{3a}{4}\cdot a\cos\alpha\sin\alpha=45
\;\Rightarrow\; a^2\cos\alpha\sin\alpha=60.$$

$$[\triangle PRS]=\frac12\cdot a\cdot h=\frac{a^2}{2}\cos\alpha\sin\alpha=\frac{60}{2}=30.$$

**Verificación:** $[PQR]=\frac12\cdot\frac a2\cdot h=\frac{a^2}{4}\cos\alpha\sin\alpha=15$, y $15+30=45$. ✓

$$\boxed{30}$$