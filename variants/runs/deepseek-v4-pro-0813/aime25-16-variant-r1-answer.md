Voy a resolver el problema paso a paso.

**Paso 1: Nombrar las posiciones.**

Los seis puntos están en una recta en el orden \(P, Q, R, S, T, U\). Pongamos coordenadas en esta recta (eje \(x\)):

\[
P = p,\quad Q = q,\quad R = r,\quad S = s,\quad T = t,\quad U = u
\]

con

\[
p < q < r < s < t < u.
\]

**Paso 2: Traducir las longitudes dadas.**

- \(PR = 24 \Rightarrow r - p = 24\)
- \(QS = 30 \Rightarrow s - q = 30\)
- \(RT = 37 \Rightarrow t - r = 37\)
- \(SU = 29 \Rightarrow u - s = 29\)
- \(PU = 74 \Rightarrow u - p = 74\)

**Paso 3: Expresar todo en función de \(r\) y \(s\).**

De \(r-p=24\): \(p = r - 24\).

De \(t-r=37\): \(t = r + 37\).

De \(u-s=29\): \(u = s + 29\).

De \(u-p=74\):

\[
(s+29) - (r-24) = 74.
\]

\[
s + 29 - r + 24 = 74.
\]

\[
s - r + 53 = 74.
\]

\[
s - r = 21.
\]

Por tanto:

\[
s = r + 21.
\]

Además, sabíamos que \(QS = 30\), es decir \(s - q = 30\):

\[
q = s - 30 = (r+21) - 30 = r - 9.
\]

Comprobemos el orden:

\[
p = r - 24,\quad q = r - 9,\quad r = r,\quad s = r + 21,\quad t = r + 37,\quad u = s + 29 = r + 50.
\]

El orden es correcto:

\[
p < q < r < s < t < u.
\]

Además, \(PU = u - p = (r+50) - (r-24) = 74\), correcto.

**Paso 4: Coordenadas del punto \(X\).**

Sea \(X = (r, h)\) o, mejor, tomemos un sistema de coordenadas. Como \(RX = 17\) y \(SX = 10\), si situamos la recta como eje \(x\) y ponemos \(R\) y \(S\) sobre él, el punto \(X\) está en la intersección de dos circunferencias centradas en \(R\) y \(S\).

Tomemos \(R = (0,0)\) y \(S = (21,0)\), ya que \(s - r = 21\).

Si \(X = (x, y)\), entonces:

\[
RX = 17 \Rightarrow x^2 + y^2 = 17^2 = 289.
\]

\[
SX = 10 \Rightarrow (x-21)^2 + y^2 = 10^2 = 100.
\]

**Paso 5: Hallar \(x\) e \(y\).**

Restamos la segunda ecuación de la primera:

\[
x^2 + y^2 - \big((x-21)^2 + y^2\big) = 289 - 100.
\]

\[
x^2 - (x^2 - 42x + 441) = 189.
\]

\[
42x - 441 = 189.
\]

\[
42x = 630.
\]

\[
x = 15.
\]

Sustituimos \(x=15\) en \(x^2 + y^2 = 289\):

\[
225 + y^2 = 289.
\]

\[
y^2 = 64.
\]

\[
y = \pm 8.
\]

Tomemos \(y = 8\) (el área no depende del signo). Por tanto:

\[
X = (15, 8)
\]

respecto a \(R=(0,0)\), \(S=(21,0)\).

**Paso 6: Coordenadas de \(Q\) y \(T\) en este sistema.**

Como \(q = r - 9\), y \(r=0\) en este sistema, entonces:

\[
Q = (-9, 0).
\]

Como \(t = r + 37\):

\[
T = (37, 0).
\]

**Paso 7: Calcular el área de \(\triangle QXT\).**

Los vértices son:

\[
Q = (-9,0),\quad X = (15,8),\quad T = (37,0).
\]

La base \(QT\) está sobre el eje \(x\) y mide:

\[
QT = 37 - (-9) = 46.
\]

La altura desde \(X\) hasta la recta \(QT\) (eje \(x\)) es:

\[
h = |y_X| = 8.
\]

Por tanto, el área es:

\[
A = \frac{1}{2} \cdot QT \cdot h = \frac{1}{2} \cdot 46 \cdot 8 = 184.
\]

\[
\boxed{184}
\]