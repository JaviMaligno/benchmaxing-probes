

Como \(g(x)\in[-1,1]\), cualquier punto de intersección tiene

\[
y\in[-1,1],\qquad x=66y^2\in[0,66].
\]

La función \(g\) es una zigzag de periodo \(4\). En cada periodo hay dos tipos de ramas.

### 1. Ramas ascendentes

En los intervalos de la forma \([4k-1,4k+1)\), se tiene

\[
g(x)=x-4k.
\]

Si \(y=g(x)\), entonces \(x=4k+y\). Combinando con \(x=66y^2\),

\[
66y^2=4k+y
\]

o sea

\[
66y^2-y-4k=0.
\]

Como \(0\le x\le 66\), las ramas ascendentes relevantes corresponden a \(k=0,1,\dots,16\).

Para cada \(k\), la suma de las raíces es

\[
\frac{1}{66}.
\]

Además, para \(k=0,1,\dots,16\), ambas raíces están en \([-1,1]\). Por lo tanto, la contribución total de las ramas ascendentes es

\[
17\cdot \frac{1}{66}=\frac{17}{66}.
\]

### 2. Ramas descendentes

En los intervalos de la forma \([4k+1,4k+3)\), se tiene

\[
g(x)=4k+2-x.
\]

Si \(y=g(x)\), entonces \(x=4k+2-y\). Combinando con \(x=66y^2\),

\[
66y^2=4k+2-y
\]

o sea

\[
66y^2+y-(4k+2)=0.
\]

Para \(k=0,1,\dots,15\), ambas raíces están en \([-1,1]\). La suma de raíces en cada caso es

\[
-\frac{1}{66}.
\]

Así, estas 16 ramas contribuyen con

\[
16\cdot\left(-\frac{1}{66}\right)=-\frac{16}{66}.
\]

Para \(k=16\), la ecuación es

\[
66y^2+y-66=0.
\]

Sus raíces son

\[
y=\frac{-1\pm\sqrt{1+4\cdot 66\cdot 66}}{132}
=\frac{-1\pm\sqrt{17425}}{132}.
\]

Como

\[
17425=25\cdot 697,
\]

tenemos \(\sqrt{17425}=5\sqrt{697}\). Solo la raíz positiva está en \([-1,1]\), así que la contribución final de la rama descendente \(k=16\) es

\[
\frac{-1+5\sqrt{697}}{132}.
\]

### 3. Suma total

\[
S=\frac{17}{66}-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}.
\]

\[
S=\frac{1}{66}+\frac{-1+5\sqrt{697}}{132}
=\frac{2}{132}+\frac{-1+5\sqrt{697}}{132}
=\frac{1+5\sqrt{697}}{132}.
\]

Así,

\[
a=1,\qquad b=5,\qquad c=697,\qquad d=132.
\]

Además, \(697=17\cdot 41\), que es libre de cuadrados, y \(\gcd(1,5,132)=1\).

Por lo tanto,

\[
a+b+c+d=1+5+697+132=835.
\]

\[
\boxed{835}
\]