## Planteamiento

Sea $\alpha = \angle QPR$ y sea $F$ el pie de la perpendicular desde $Q$ a $\overline{PR}$ (la recta $QT$ es justamente $QF$).

**Triángulo $QYT$:**
- $\angle QYT = \angle QYR = 60^\circ$ (pues $T\in\overline{YR}$).
- $\angle YQT = \angle PQF = 90^\circ-\alpha$ (triángulo rectángulo $PFQ$).
- Luego $\angle QTY = 30^\circ+\alpha$.

Por el teorema del seno con $QT=3$:
$$QY=\frac{3\sin(30^\circ+\alpha)}{\sin 60^\circ},\qquad YT=\frac{3\cos\alpha}{\sin 60^\circ}$$

**Triángulo $PYR$:** $\angle P=\alpha$, $\angle PYR=120^\circ$, $\angle PRY=60^\circ-\alpha$, con $PR=8$:
$$PY=\frac{8\sin(60^\circ-\alpha)}{\sin 60^\circ},\qquad RY=\frac{8\sin\alpha}{\sin 60^\circ}$$

## Condición $PQ=6$

$PY+YQ=6$ da
$$8\sin(60^\circ-\alpha)+3\sin(30^\circ+\alpha)=6\sin 60^\circ=3\sqrt3$$

Desarrollando: $\left(\tfrac32+4\sqrt3\right)\cos\alpha+\left(\tfrac{3\sqrt3}{2}-4\right)\sin\alpha=3\sqrt3$.

## Cálculo de $RT$

$$RT=RY-YT=\frac{8\sin\alpha-3\cos\alpha}{\sin 60^\circ}=\frac{2u}{\sqrt3},\qquad u:=8\sin\alpha-3\cos\alpha$$

El vector de coeficientes de la condición es $\left(\tfrac32+4\sqrt3,\ \tfrac{3\sqrt3}{2}-4\right)=R_{60^\circ}(3,-8)$, de módulo $\sqrt{73}$. Escribiendo $\psi$ como el ángulo entre $(3,-8)$ y $(\cos\alpha,\sin\alpha)$:
$$\sqrt{73}\cos\psi=-u,\qquad \sqrt{73}\cos(\psi-60^\circ)=3\sqrt3\ \Longrightarrow\ \sqrt{73}\sin\psi=6+\frac{u}{\sqrt3}$$

Sumando cuadrados:
$$u^2+\left(6+\frac{u}{\sqrt3}\right)^2=73\ \Longrightarrow\ \frac43u^2+4\sqrt3\,u-37=0\ \Longrightarrow\ u^2+3\sqrt3\,u-\frac{111}{4}=0$$

La raíz positiva es $u=\dfrac{\sqrt{138}-3\sqrt3}{2}$, de donde
$$RT=\frac{2u}{\sqrt3}=\frac{\sqrt{138}-3\sqrt3}{\sqrt3}=\sqrt{46}-3$$

**Verificación numérica:** $\alpha\approx 43.09^\circ$ da $Q\approx(4.381,4.100)$, $T\approx(4.381,1.100)$, $Y\approx(1.960,1.836)$, con $\angle QYR=60.00^\circ$, $PQ=6$, $QT=3$ y $RT\approx 3.7823=\sqrt{46}-3$. ✓

$$\boxed{\sqrt{46}-3}$$