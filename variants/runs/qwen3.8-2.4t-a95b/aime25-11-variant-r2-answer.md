

Como \(y=g(x)\in[-1,1]\), cualquier intersección con la parábola

\[
x=66y^2
\]

debe cumplir \(0\le x\le 66\).

La función \(g\) es una onda triangular. En cada intervalo de longitud \(2\), centrado en un entero par \(m\), tenemos

\[
g(x)=\sigma(x-m),\qquad x\in[m-1,m+1],
\]

donde

\[
\sigma=
\begin{cases}
+1, & m\equiv 0 \pmod 4,\\
-1, & m\equiv 2 \pmod 4.
\end{cases}
\]

Así, si \(y=g(x)\), entonces

\[
y=\sigma(x-m)\quad\Longrightarrow\quad x=m+\sigma y.
\]

Al intersectar con \(x=66y^2\), obtenemos

\[
66y^2=m+\sigma y,
\]

o sea

\[
66y^2-\sigma y-m=0.
\]

Los intervalos que pueden importar para \(0\le x\le 66\) corresponden a

\[
m=0,2,4,\dots,66.
\]

Para \(0\le m\le 64\), las dos raíces de la ecuación cuadrática están dentro de \([-1,1]\), por lo que ambas dan intersecciones válidas. Por Vieta, la suma de esas dos raíces es

\[
\frac{\sigma}{66}.
\]

Hay \(17\) valores con \(\sigma=+1\):

\[
m=0,4,8,\dots,64,
\]

y \(16\) valores con \(\sigma=-1\):

\[
m=2,6,10,\dots,62.
\]

Por tanto, la contribución total de estos segmentos es

\[
17\cdot\frac{1}{66}+16\cdot\left(-\frac{1}{66}\right)=\frac{1}{66}.
\]

Falta el segmento centrado en \(m=66\), donde \(\sigma=-1\). La ecuación es

\[
66y^2+y-66=0.
\]

Sus raíces son

\[
y=\frac{-1\pm\sqrt{1+4\cdot 66^2}}{132}
=\frac{-1\pm\sqrt{17425}}{132}.
\]

La raíz negativa es menor que \(-1\), así que no pertenece al segmento. Solo cuenta la raíz positiva:

\[
y=\frac{-1+\sqrt{17425}}{132}.
\]

Entonces la suma total de coordenadas \(y\) es

\[
\frac{1}{66}+\frac{-1+\sqrt{17425}}{132}
=\frac{2}{132}+\frac{-1+\sqrt{17425}}{132}
=\frac{1+\sqrt{17425}}{132}.
\]

Como

\[
17425=25\cdot 697,
\]

y \(697=17\cdot 41\) es libre de cuadrados,

\[
\frac{1+\sqrt{17425}}{132}
=\frac{1+5\sqrt{697}}{132}.
\]

Así,

\[
a=1,\qquad b=5,\qquad c=697,\qquad d=132.
\]

Por lo tanto,

\[
a+b+c+d=1+5+697+132=835.
\]

\[
\boxed{835}
\]