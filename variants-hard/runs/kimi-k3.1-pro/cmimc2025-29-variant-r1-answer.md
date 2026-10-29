Coloco los vértices en
\[
S=(0,0),\quad R=(110,0),\quad P=(0,28),\quad Q=(20,28).
\]

Una cónica general que pasa por \(S\) tiene ecuación
\[
Ax^2+Bxy+Cy^2+Dx+Ey=0.
\]
Al imponer que pase por \(R\) y \(P\), se obtiene \(D=-110A\) y \(E=-28C\). Al imponer que pase por \(Q\), resulta \(B=\frac{45}{14}A\). Normalizando \(A=1\) y escribiendo \(c=C/A\), la familia de cónicas es
\[
x^2-110x+\frac{45}{14}xy+c(y^2-28y)=0.
\]

Su forma cuadrática tiene matriz
\[
M=\begin{pmatrix}1&k\\k&c\end{pmatrix},
\qquad k=\frac{45}{28}.
\]
Para que sea una elipse, \(c>k^2\). Si \(\lambda_{\min},\lambda_{\max}\) son los valores propios de \(M\), la razón entre los ejes mayor y menor es
\[
r=\sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}.
\]

Definiendo
\[
T=1+c,\qquad \Delta=\sqrt{(c-1)^2+4k^2},
\]
tenemos
\[
r^2=\frac{T+\Delta}{T-\Delta}.
\]
Por tanto, minimizar \(r\) equivale a maximizar
\[
\frac{\Delta^2}{T^2}
=\frac{(c-1)^2+4k^2}{(c+1)^2}.
\]
Su derivada se anula en \(c=1+2k^2\), donde se alcanza el máximo. En ese punto,
\[
\frac{\Delta}{T}=\frac{k}{\sqrt{1+k^2}},
\]
y, en consecuencia,
\[
r=\sqrt{\frac{1+k/\sqrt{1+k^2}}{1-k/\sqrt{1+k^2}}}
=\sqrt{1+k^2}+k.
\]
Finalmente,
\[
r=\sqrt{1+\left(\frac{45}{28}\right)^2}+\frac{45}{28}
=\frac{53}{28}+\frac{45}{28}
=\boxed{\frac72}.
\]