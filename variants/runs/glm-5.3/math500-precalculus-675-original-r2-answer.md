El menor \(C\) es el máximo de \(\dfrac{\|A\mathbf v\|}{\|\mathbf v\|}\) sobre todos los vectores \(\mathbf v\neq \mathbf 0\), es decir, la norma operatoria euclidiana de
\[
A=\begin{pmatrix}2&3\\0&-2\end{pmatrix}.
\]

Para \(\mathbf v=(x,y)\),
\[
A\mathbf v=(2x+3y,\,-2y),
\]
entonces
\[
\|A\mathbf v\|^2=(2x+3y)^2+(-2y)^2
=4x^2+12xy+13y^2.
\]
Esta forma cuadrática tiene matriz
\[
A^T A=\begin{pmatrix}4&6\\6&13\end{pmatrix}.
\]
Sus valores propios satisfacen
\[
\lambda^2-17\lambda+16=0,
\]
de donde
\[
\lambda=1,\ 16.
\]
Por lo tanto,
\[
\max_{\mathbf v\ne 0}\frac{\|A\mathbf v\|^2}{\|\mathbf v\|^2}=16,
\]
y así el máximo de \(\dfrac{\|A\mathbf v\|}{\|\mathbf v\|}\) es \(4\).

\[
\boxed{4}
\]