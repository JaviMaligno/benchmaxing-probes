

Coloquemos coordenadas:

\[
S=(0,0),\quad R=(110,0),\quad P=(0,28).
\]

Como \(PQ\parallel SR\) y \(PQ=20\), tenemos

\[
Q=(20,28).
\]

Sea una cónica general

\[
Ax^2+Bxy+Cy^2+Dx+Ey+F=0.
\]

Como pasa por \(S=(0,0)\), se tiene \(F=0\).

Al pasar por \(R=(110,0)\):

\[
12100A+110D=0 \implies D=-110A.
\]

Al pasar por \(P=(0,28)\):

\[
784C+28E=0 \implies E=-28C.
\]

Al pasar por \(Q=(20,28)\):

\[
400A+560B+784C+20D+28E=0.
\]

Sustituyendo \(D=-110A\) y \(E=-28C\):

\[
400A+560B+784C-2200A-784C=0,
\]

\[
-1800A+560B=0 \implies B=\frac{45}{14}A.
\]

Si \(A=0\), entonces \(B=0\) y la cónica se degenera en dos rectas, así que para una elipse \(A\neq 0\). Escalando para tomar \(A=1\), la parte cuadrática de la cónica es

\[
M(t)=
\begin{pmatrix}
1 & \frac{45}{28}\\[2mm]
\frac{45}{28} & t
\end{pmatrix},
\]

donde \(t=C/A\). Para que sea una elipse, \(M(t)\) debe ser definida positiva, es decir,

\[
t>\left(\frac{45}{28}\right)^2.
\]

Si los valores propios de \(M(t)\) son \(\lambda_1,\lambda_2\), la razón de los ejes de la elipse es

\[
r=\sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}.
\]

Entonces

\[
r+\frac1r=\frac{\operatorname{tr}M}{\sqrt{\det M}}
=\frac{1+t}{\sqrt{t-\left(\frac{45}{28}\right)^2}}.
\]

Sea

\[
m=\frac{45}{28}.
\]

Minimizamos

\[
g(t)=\frac{(1+t)^2}{t-m^2}.
\]

Derivando,

\[
g'(t)=\frac{(1+t)\bigl(t-(1+2m^2)\bigr)}{(t-m^2)^2},
\]

por lo que el mínimo ocurre en

\[
t=1+2m^2.
\]

En ese punto,

\[
r+\frac1r
=
\frac{2+2m^2}{\sqrt{1+m^2}}
=
2\sqrt{1+m^2}.
\]

Como \(r\ge 1\), la solución es

\[
r=\sqrt{1+m^2}+m.
\]

Ahora

\[
\sqrt{1+m^2}
=
\sqrt{1+\left(\frac{45}{28}\right)^2}
=
\sqrt{\frac{2809}{784}}
=
\frac{53}{28}.
\]

Por tanto,

\[
r=\frac{53}{28}+\frac{45}{28}
=
\frac{98}{28}
=
\frac72.
\]

\[
\boxed{\frac{7}{2}}
\]