

Sean las rectas dadas por las transformaciones

\[
u=y-ax,\qquad v=y-bx.
\]

Entonces las rectas \(y=ax+\text{const}\) son \(u=\text{const}\), y las rectas \(y=bx+\text{const}\) son \(v=\text{const}\). El jacobiano de la transformación es

\[
\left|\frac{\partial(u,v)}{\partial(x,y)}\right|
=
\begin{vmatrix}
-a & 1\\
-b & 1
\end{vmatrix}
=|b-a|.
\]

Sea \(D=|a-b|\). Como el paralelogramo es acotado, \(D>0\).

Para el primer paralelogramo, en coordenadas \((u,v)\) tenemos el rectángulo con lados \(|d-c|\) y \(|d-c|\), así que

\[
\frac{(d-c)^2}{D}=18.
\]

Para el segundo paralelogramo, los valores de \(u\) y \(v\) van de \(-d\) a \(c\), por lo que cada lado mide \(c+d\). Así,

\[
\frac{(c+d)^2}{D}=72.
\]

Dividiendo ambas ecuaciones:

\[
\frac{(c+d)^2}{(d-c)^2}=4,
\]

por tanto

\[
c+d=2|d-c|.
\]

Si \(d>c\), entonces \(c+d=2(d-c)\), de donde \(d=3c\).  
Si \(c>d\), se obtiene análogamente \(c=3d\). En cualquier caso, uno es el triple del otro.

Supongamos \(d=3c\). Entonces \(c+d=4c\), y usando

\[
\frac{(c+d)^2}{D}=72
\]

obtenemos

\[
\frac{16c^2}{D}=72
\quad\Longrightarrow\quad
D=\frac{2c^2}{9}.
\]

Como \(D\) debe ser entero, \(c\) debe ser múltiplo de \(3\). Sea \(c=3k\). Entonces

\[
D=2k^2.
\]

Además,

\[
c+d=3k+9k=12k.
\]

Para minimizar \(a+b\) dado \(D=|a-b|\), tomamos los enteros positivos más pequeños con esa diferencia: \(1\) y \(D+1\), cuya suma es \(D+2\).

Así,

\[
a+b+c+d=(D+2)+12k=2k^2+12k+2.
\]

Esto es mínimo para \(k=1\), dando

\[
2(1)^2+12(1)+2=16.
\]

Esto se logra, por ejemplo, con \(a=1\), \(b=3\), \(c=3\), \(d=9\).

\[
\boxed{16}
\]