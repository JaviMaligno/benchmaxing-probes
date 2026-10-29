Denotemos \(r_i=A_1A_i\) y sea \(\theta=\angle A_iA_1A_{i+1}\). Como \(\cos\theta=\frac{12}{13}\), se tiene \(\sin\theta=\frac{5}{13}\).

Para cada \(2\le i\le 10\), el área del triángulo es \(1\), así que

\[
1=\frac12 r_i r_{i+1}\sin\theta
=\frac12 r_i r_{i+1}\cdot \frac{5}{13}.
\]

Por lo tanto,

\[
r_i r_{i+1}=\frac{26}{5}.
\]

Esto hace que las distancias desde \(A_1\) alternen entre dos valores:

\[
r_2=r_4=\cdots=r_{10}=x,\qquad
r_3=r_5=\cdots=r_{11}=y,
\]

con

\[
xy=\frac{26}{5}.
\]

Cada lado \(A_iA_{i+1}\), para \(2\le i\le 10\), tiene la misma longitud \(L\). Por la ley de los cosenos,

\[
L^2=x^2+y^2-2xy\cdot \frac{12}{13}
=x^2+y^2-\frac{48}{5}.
\]

Sea \(t=x+y\). Entonces

\[
x^2+y^2=t^2-2xy=t^2-\frac{52}{5},
\]

de modo que

\[
L^2=t^2-\frac{52}{5}-\frac{48}{5}=t^2-20.
\]

El perímetro es \(20\), y consta de los dos lados \(A_1A_2\) y \(A_1A_{11}\), que suman \(x+y=t\), más los nueve lados intermedios de longitud \(L\):

\[
20=t+9L.
\]

Así,

\[
L=\frac{20-t}{9},
\]

y sustituyendo en \(L^2=t^2-20\),

\[
t^2-20=\frac{(20-t)^2}{81}.
\]

Esto se simplifica a

\[
4t^2+2t-101=0.
\]

La raíz positiva es

\[
t=\frac{9\sqrt5-1}{4}.
\]

Por lo tanto,

\[
m=9,\quad n=5,\quad p=1,\quad q=4,
\]

y

\[
m+n+p+q=9+5+1+4=19.
\]

\[
\boxed{19}
\]