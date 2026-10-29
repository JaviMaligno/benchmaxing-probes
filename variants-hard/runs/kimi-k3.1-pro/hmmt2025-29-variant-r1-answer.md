Sea \(w=PQ\) y \(\theta=\angle YPQ\). Como \(\triangle PYQ\) es rectángulo en \(Y\),
\[
PY=w\cos\theta,\qquad QY=w\sin\theta.
\]
Además, \(\angle YPS=90^\circ-\theta\) y \(\angle YQR=\theta\).

Definimos \(\alpha=\angle PYS\) y \(\beta=\angle QYR\). Por la ley de senos, usando \(PS=QR=30\),
\[
\sen\alpha=\frac{30}{2\cdot17}=\frac{15}{17},\qquad
\sen\beta=\frac{30}{2\cdot25}=\frac35.
\]
Como ambos triángulos son agudos,
\[
\cos\alpha=\frac8{17},\qquad \cos\beta=\frac45.
\]

En \(\triangle PYS\), el tercer ángulo es \(90^\circ+\theta-\alpha\). Por tanto,
\[
PY=34\sen(90^\circ+\theta-\alpha)=34\cos(\theta-\alpha).
\]
Sustituyendo \(PY=w\cos\theta\),
\[
w=34(\cos\alpha+\tan\theta\sen\alpha)
=16+30\tan\theta.
\]

Análogamente, en \(\triangle QYR\),
\[
QY=50\sen(180^\circ-\beta-\theta)=50\sen(\beta+\theta),
\]
de donde
\[
w=50(\cos\beta+\cot\theta\sen\beta)
=40+30\cot\theta.
\]

Sea \(t=\tan\theta>0\). Igualando ambas expresiones:
\[
16+30t=40+\frac{30}{t}
\quad\Longrightarrow\quad
5t^2-4t-5=0.
\]
La raíz positiva es \(t=\frac{2+\sqrt{29}}5\). Así,
\[
PQ=16+30t=\boxed{28+6\sqrt{29}}.
\]