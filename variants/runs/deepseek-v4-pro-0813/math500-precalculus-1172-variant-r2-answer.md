Las dos rectas son paralelas porque sus vectores directores son proporcionales:

\[
\begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}
\quad\text{y}\quad
\begin{pmatrix} -6 \\ 20 \\ -8 \end{pmatrix}
= -2 \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}.
\]

Un punto de la primera recta es \(P = (1,5,-2)\) y uno de la segunda es \(Q = (8,-1,9)\). Formamos el vector que los une:

\[
Q - P = \begin{pmatrix} 8-1 \\ -1-5 \\ 9-(-2) \end{pmatrix}
= \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}.
\]

La distancia entre dos rectas paralelas es la longitud de la componente de \(Q-P\) perpendicular al vector director común \(\vec v = (3,-10,4)\):

\[
d = \frac{\lVert (Q-P) \times \vec v \rVert}{\lVert \vec v \rVert}.
\]

Calculamos el producto cruz:

\[
(Q-P) \times \vec v
=
\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k \\
7 & -6 & 11 \\
3 & -10 & 4
\end{vmatrix}.
\]

Componentes:

\[
\mathbf i:\ (-6)(4) - 11(-10) = -24 + 110 = 86,
\]
\[
\mathbf j:\ -(7\cdot 4 - 11\cdot 3) = -(28 - 33) = 5,
\]
\[
\mathbf k:\ 7(-10) - (-6)(3) = -70 + 18 = -52.
\]

Entonces,

\[
(Q-P) \times \vec v = (86, 5, -52).
\]

Ahora su norma:

\[
\lVert (86,5,-52) \rVert
= \sqrt{86^2 + 5^2 + (-52)^2}
= \sqrt{7396 + 25 + 2704}
= \sqrt{10125}.
\]

Además,

\[
\lVert \vec v \rVert
= \sqrt{3^2 + (-10)^2 + 4^2}
= \sqrt{9 + 100 + 16}
= \sqrt{125}.
\]

Por lo tanto, la distancia es:

\[
d = \frac{\sqrt{10125}}{\sqrt{125}}
= \sqrt{\frac{10125}{125}}
= \sqrt{81}
= 9.
\]

\[
\boxed{9}
\]