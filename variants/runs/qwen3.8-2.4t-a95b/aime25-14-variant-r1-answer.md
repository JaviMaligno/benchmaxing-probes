

Primero determinamos la forma del pentágono.

En el triángulo \(PQR\), por ley de cosenos:

\[
PR^2=38^2+19^2-2(38)(19)\cos 60^\circ
=1444+361-722=1083.
\]

Así,

\[
PR=19\sqrt3.
\]

Además, los lados \(19,19\sqrt3,38\) forman un triángulo \(30^\circ\)-\(60^\circ\)-\(90^\circ\), por lo que \(\angle R=90^\circ\). Análogamente, en el triángulo \(PTS\),

\[
PS=19\sqrt3
\]

y \(\angle S=90^\circ\).

Coloquemos ahora

\[
R=(-24,0),\qquad S=(24,0),
\]

de modo que \(RS=48\). Como \(PR=PS=19\sqrt3\), el punto \(P\) está sobre el eje de simetría:

\[
P=(0,h),\qquad h^2+24^2=(19\sqrt3)^2=1083.
\]

Entonces

\[
h^2=507=169\cdot 3 \implies h=13\sqrt3.
\]

Así,

\[
P=(0,13\sqrt3).
\]

Como \(QR\perp PR\) y \(QR=19\), un vector perpendicular a \(RP=(24,13\sqrt3)\) de longitud \(19\) es \((-13,8\sqrt3)\). Por convexidad, \(Q\) queda del lado opuesto a \(S\) respecto de \(PR\), así que

\[
Q=(-37,8\sqrt3).
\]

Por simetría,

\[
T=(37,8\sqrt3).
\]

Ahora consideremos el punto

\[
F=(0,8\sqrt3),
\]

que es el punto medio de \(QT\). Sus distancias a los vértices son:

\[
PF=13\sqrt3-8\sqrt3=5\sqrt3,
\]

\[
RF=SF=\sqrt{24^2+(8\sqrt3)^2}
=\sqrt{576+192}
=\sqrt{768}=16\sqrt3,
\]

\[
QF=TF=37.
\]

Por tanto,

\[
g(F)=5\sqrt3+2(16\sqrt3)+2(37)=74+37\sqrt3.
\]

Para ver que este es el mínimo global:

- Para cualquier punto \(Y\),

\[
QY+TY\ge QT=74,
\]

con igualdad si \(Y\) está sobre el segmento \(QT\).

- Para los puntos \(P,R,S\), tomemos los vectores unitarios

\[
u_P=(0,1),\qquad 
u_R=\left(-\frac{\sqrt3}{2},-\frac12\right),\qquad
u_S=\left(\frac{\sqrt3}{2},-\frac12\right).
\]

Se cumple \(u_P+u_R+u_S=0\). Por Cauchy-Schwarz, para cualquier \(Y\),

\[
PY\ge u_P\cdot(P-Y),\quad
RY\ge u_R\cdot(R-Y),\quad
SY\ge u_S\cdot(S-Y).
\]

Sumando,

\[
PY+RY+SY
\ge u_P\cdot P+u_R\cdot R+u_S\cdot S.
\]

Calculamos:

\[
u_P\cdot P=13\sqrt3,
\]

\[
u_R\cdot R=12\sqrt3,\qquad
u_S\cdot S=12\sqrt3.
\]

Así,

\[
PY+RY+SY\ge 37\sqrt3.
\]

La igualdad se alcanza precisamente en \(F\). Como además \(F\) está sobre el segmento \(QT\), también se alcanza la igualdad en \(QY+TY\ge 74\).

Por lo tanto, el valor mínimo de \(g(Y)\) es

\[
74+37\sqrt3.
\]

Entonces

\[
m=74,\qquad n=37,\qquad p=3,
\]

y

\[
m+n+p=74+37+3=114.
\]

\[
\boxed{114}
\]