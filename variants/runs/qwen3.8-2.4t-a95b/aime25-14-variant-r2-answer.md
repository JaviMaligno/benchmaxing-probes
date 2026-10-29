

Determinemos primero la configuración del pentágono.

En el triángulo \(PQR\), por ley de cosenos,

\[
PR^2=38^2+19^2-2(38)(19)\cos 60^\circ
=1444+361-722=1083=3\cdot 19^2,
\]

así que

\[
PR=19\sqrt3.
\]

Además,

\[
PR^2+QR^2=1083+361=1444=PQ^2,
\]

por lo que \(\triangle PQR\) es rectángulo en \(R\). De manera análoga, en \(\triangle PTS\),

\[
PS=19\sqrt3
\]

y el triángulo es rectángulo en \(S\).

Como \(PR=PS\), el triángulo \(PRS\) es isósceles. Sea \(M\) el punto medio de \(RS\). Entonces \(RM=24\), y

\[
PM=\sqrt{(19\sqrt3)^2-24^2}
=\sqrt{1083-576}
=\sqrt{507}=13\sqrt3.
\]

Coloquemos coordenadas con \(P=(0,0)\), \(M=(13\sqrt3,0)\), de modo que

\[
R=(13\sqrt3,-24),\qquad S=(13\sqrt3,24).
\]

Como \(QR\perp PR\) y \(QR=19\), el vector \(RQ\) debe ser perpendicular a \((13\sqrt3,-24)\) y tener longitud \(19\). La elección compatible con la convexidad es

\[
RQ=(-8\sqrt3,-13),
\]

por lo que

\[
Q=(13\sqrt3,-24)+(-8\sqrt3,-13)=(5\sqrt3,-37).
\]

Análogamente,

\[
T=(5\sqrt3,37).
\]

Así, el pentágono es simétrico respecto al eje \(x\).

Para cualquier punto \(Y\), si \(Y'\) es su reflejo respecto al eje \(x\), entonces \(g(Y')=g(Y)\). Como la suma de distancias es una función convexa,

\[
g\!\left(\frac{Y+Y'}2\right)\le \frac{g(Y)+g(Y')}{2}=g(Y).
\]

Por lo tanto, el mínimo se alcanza sobre el eje \(x\). Sea \(Y=(x,0)\). Entonces

\[
g(Y)=|x|
+2\sqrt{(x-5\sqrt3)^2+37^2}
+2\sqrt{(x-13\sqrt3)^2+24^2}.
\]

Esta función es convexa. Para \(x>0\), su derivada es

\[
g'(x)=1
+2\frac{x-5\sqrt3}{\sqrt{(x-5\sqrt3)^2+37^2}}
+2\frac{x-13\sqrt3}{\sqrt{(x-13\sqrt3)^2+24^2}}.
\]

Evaluando en \(x=5\sqrt3\),

\[
g'(5\sqrt3)
=
1+0
+2\frac{-8\sqrt3}{\sqrt{(-8\sqrt3)^2+24^2}}.
\]

Pero

\[
\sqrt{(-8\sqrt3)^2+24^2}
=\sqrt{192+576}
=\sqrt{768}=16\sqrt3,
\]

así que

\[
g'(5\sqrt3)=1+2\frac{-8\sqrt3}{16\sqrt3}=1-1=0.
\]

Como la función es convexa, este punto da el mínimo global.

Finalmente, en \(Y=(5\sqrt3,0)\),

\[
PY=5\sqrt3,
\]

\[
QY=TY=37,
\]

y

\[
RY=SY=\sqrt{(8\sqrt3)^2+24^2}=16\sqrt3.
\]

Por tanto,

\[
g_{\min}=5\sqrt3+2(37)+2(16\sqrt3)
=74+37\sqrt3.
\]

Así,

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