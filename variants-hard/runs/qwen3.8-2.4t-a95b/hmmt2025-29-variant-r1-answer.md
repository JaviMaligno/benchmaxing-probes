

Sea \(L=PQ\) y sea \(\theta=\angle QPY\). Como \(\angle PYQ=90^\circ\), el triángulo \(\triangle PQY\) es rectángulo en \(Y\), así que

\[
PY=L\cos\theta,\qquad QY=L\sin\theta.
\]

En el triángulo \(\triangle PYS\), el lado \(PS=30\) es opuesto al ángulo \(\alpha=\angle PYS\). Su circunradio es \(17\), por lo que

\[
30=2\cdot 17\sin\alpha \implies \sin\alpha=\frac{15}{17}.
\]

Como \(\triangle PYS\) es acutángulo, \(\cos\alpha=\frac{8}{17}\).

Además, \(\angle YPS=90^\circ-\theta\), pues \(PS\perp PQ\). Entonces

\[
\angle PSY=180^\circ-\alpha-(90^\circ-\theta)=90^\circ+\theta-\alpha.
\]

Por la ley de senos,

\[
PY=34\sin(90^\circ+\theta-\alpha)=34\cos(\theta-\alpha).
\]

Expandiendo,

\[
PY=34(\cos\theta\cos\alpha+\sin\theta\sin\alpha)
=34\left(\frac{8}{17}\cos\theta+\frac{15}{17}\sin\theta\right)
=16\cos\theta+30\sin\theta.
\]

Como \(PY=L\cos\theta\),

\[
L\cos\theta=16\cos\theta+30\sin\theta
\implies (L-16)\cos\theta=30\sin\theta. \tag{1}
\]

Ahora, en \(\triangle QYR\), sea \(\beta=\angle QYR\). El lado \(QR=30\) es opuesto a \(\beta\), y su circunradio es \(25\), así que

\[
30=2\cdot 25\sin\beta \implies \sin\beta=\frac35.
\]

Como \(\triangle QYR\) es acutángulo, \(\cos\beta=\frac45\).

El ángulo en \(Q\) del triángulo \(\triangle QYR\) es \(\theta\), porque \(QY\) divide el ángulo recto del rectángulo en \(Q\) y \(\angle PQY=90^\circ-\theta\). Entonces el ángulo en \(R\) es \(180^\circ-\theta-\beta\). Por la ley de senos,

\[
QY=50\sin(180^\circ-\theta-\beta)=50\sin(\theta+\beta).
\]

Expandiendo,

\[
QY=50(\sin\theta\cos\beta+\cos\theta\sin\beta)
=50\left(\frac45\sin\theta+\frac35\cos\theta\right)
=40\sin\theta+30\cos\theta.
\]

Como \(QY=L\sin\theta\),

\[
L\sin\theta=40\sin\theta+30\cos\theta
\implies (L-40)\sin\theta=30\cos\theta. \tag{2}
\]

Multiplicando \((1)\) y \((2)\),

\[
(L-16)(L-40)\sin\theta\cos\theta=900\sin\theta\cos\theta.
\]

Como \(0<\theta<90^\circ\), cancelamos \(\sin\theta\cos\theta\):

\[
(L-16)(L-40)=900.
\]

\[
L^2-56L+640=900
\]

\[
L^2-56L-260=0.
\]

Resolviendo,

\[
L=\frac{56\pm\sqrt{56^2+4\cdot260}}{2}
=\frac{56\pm\sqrt{4176}}{2}
=28\pm 6\sqrt{29}.
\]

La solución válida es la positiva, y además \(L>40\), por lo que

\[
\boxed{28+6\sqrt{29}}
\]