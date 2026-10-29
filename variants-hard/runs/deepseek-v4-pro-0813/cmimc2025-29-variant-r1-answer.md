Coloquemos coordenadas:

\[
S=(0,0),\quad R=(110,0),\quad P=(0,28),\quad Q=(20,28).
\]

La ecuación general de una cónica es

\[
Ax^2+Bxy+Cy^2+Dx+Ey+F=0.
\]

Al imponer que pase por los cuatro puntos:

- \(S=(0,0)\) da \(F=0\).
- \(R=(110,0)\) da \(D=-110A\).
- \(P=(0,28)\) da \(E=-28C\).
- \(Q=(20,28)\) da \(-1800A+560B=0\), luego

\[
B=\frac{45}{14}A.
\]

Dividiendo entre \(A\), la familia de cónicas queda

\[
x^2+\frac{45}{14}xy+ky^2-110x-28ky=0,
\]

donde \(k=\frac CA\).

La parte cuadrática tiene matriz

\[
M=\begin{pmatrix}
1 & \frac{45}{28}\\[2mm]
\frac{45}{28} & k
\end{pmatrix}.
\]

Sea

\[
h=\frac{45}{28}.
\]

Los eigenvalores de \(M\) son

\[
\lambda_\pm=\frac{1+k\pm\sqrt{(k-1)^2+4h^2}}2.
\]

La razón entre el eje mayor y el eje menor es

\[
r=\sqrt{\frac{\lambda_+}{\lambda_-}}.
\]

Para minimizar

\[
f(k)=\frac{1+k+\sqrt{(k-1)^2+4h^2}}{1+k-\sqrt{(k-1)^2+4h^2}},
\]

se deriva y se obtiene

\[
k=1+2h^2.
\]

Sustituyendo este valor:

\[
r=\sqrt{1+h^2}+h.
\]

Como

\[
\sqrt{1+h^2}=\sqrt{1+\left(\frac{45}{28}\right)^2}
=\sqrt{\frac{2809}{784}}
=\frac{53}{28},
\]

entonces

\[
r=\frac{53}{28}+\frac{45}{28}
=\frac{98}{28}
=\frac72.
\]

\[
\boxed{\frac{7}{2}}
\]