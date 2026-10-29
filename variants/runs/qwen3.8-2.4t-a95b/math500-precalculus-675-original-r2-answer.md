

Sea \(A=\begin{pmatrix}2&3\\0&-2\end{pmatrix}\) y \(\mathbf v=(x,y)\). La menor constante \(C\) que cumple

\[
\|A\mathbf v\|\le C\|\mathbf v\|
\]

para todo \(\mathbf v\) es la norma espectral de \(A\).

Calculamos directamente:

\[
A\mathbf v=\begin{pmatrix}2x+3y\\-2y\end{pmatrix}.
\]

Entonces

\[
\|A\mathbf v\|^2=(2x+3y)^2+(-2y)^2
=4x^2+12xy+9y^2+4y^2
=4x^2+12xy+13y^2.
\]

Queremos el máximo de

\[
\frac{\|A\mathbf v\|^2}{\|\mathbf v\|^2}
=\frac{4x^2+12xy+13y^2}{x^2+y^2}.
\]

Si \(C=4\), comprobamos:

\[
16(x^2+y^2)-(4x^2+12xy+13y^2)
=12x^2-12xy+3y^2
=3(2x-y)^2\ge 0.
\]

Por lo tanto,

\[
\|A\mathbf v\|^2\le 16\|\mathbf v\|^2,
\]

así que \(\|A\mathbf v\|\le 4\|\mathbf v\|\).

La igualdad ocurre cuando \(2x-y=0\), por ejemplo con \(\mathbf v=(1,2)\), de modo que no se puede usar una constante menor.

\[
\boxed{4}
\]