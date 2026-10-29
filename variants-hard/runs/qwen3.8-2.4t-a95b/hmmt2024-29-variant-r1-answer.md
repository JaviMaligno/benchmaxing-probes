

Coloquemos \(P=(0,0)\) y \(R=(8,0)\), de modo que \(\overline{PR}\) esté sobre el eje \(x\). Por simetría, podemos suponer que \(Q\) está por encima del eje \(x\).

Sea \(\mathbf u=(\cos\theta,\sin\theta)\) el vector unitario en la dirección de \(P\) a \(Q\). Como \(PQ=6\),

\[
Q=6\mathbf u.
\]

Como \(Y\) está sobre \(\overline{PQ}\) y \(T\) está sobre \(\overline{RY}\), la coordenada \(y\) de \(T\) está entre \(0\) y la coordenada \(y\) de \(Y\), la cual no supera la de \(Q\). Además, \(QT\perp PR\), así que \(QT\) es vertical, y como \(QT=3\), \(T\) está 3 unidades debajo de \(Q\):

\[
T=6\mathbf u-3\mathbf j,
\]

donde \(\mathbf j=(0,1)\).

Sea \(d=RT\). Entonces

\[
\overrightarrow{TR}=R-T=(8,0)-6\mathbf u+3\mathbf j.
\]

Como \(T\) está en \(\overline{RY}\), el vector \(\overrightarrow{TR}\) tiene la misma dirección que \(\overrightarrow{YR}\). Además, \(\overrightarrow{YQ}\) es paralelo a \(\mathbf u\). Dado que \(\angle QYR=60^\circ\), el ángulo entre \(\mathbf u\) y \(\overrightarrow{TR}\) es \(60^\circ\). Por tanto,

\[
\mathbf u\cdot \overrightarrow{TR}=d\cos 60^\circ=\frac d2.
\]

Calculamos ese producto escalar:

\[
\mathbf u\cdot(8\mathbf i-6\mathbf u+3\mathbf j)
=8\cos\theta-6+3\sin\theta.
\]

Así,

\[
8\cos\theta+3\sin\theta-6=\frac d2.
\]

Multiplicando por \(12\),

\[
96\cos\theta+36\sin\theta=72+6d.
\]

Por otro lado,

\[
d^2=|\overrightarrow{TR}|^2
=(8-6\cos\theta)^2+(3-6\sin\theta)^2.
\]

Expandiendo y usando \(\cos^2\theta+\sin^2\theta=1\),

\[
d^2=109-96\cos\theta-36\sin\theta.
\]

Sustituyendo \(96\cos\theta+36\sin\theta=72+6d\),

\[
d^2=109-(72+6d)=37-6d.
\]

Entonces

\[
d^2+6d-37=0.
\]

Resolviendo,

\[
d=-3\pm\sqrt{46}.
\]

Como \(d>0\), tomamos la raíz positiva:

\[
\boxed{\sqrt{46}-3}
\]