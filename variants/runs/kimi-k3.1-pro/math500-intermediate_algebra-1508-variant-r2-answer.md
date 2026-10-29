Sea \(x=b_1\). Aplicando la recurrencia:
\[
b_2=-\frac1{1+x},\qquad
b_3=-\frac1{1+b_2}=-\frac{1+x}{x}.
\]
Como \(b_3=b_1=x\),
\[
-\frac{1+x}{x}=x
\quad\Longrightarrow\quad
x^2+x+1=0.
\]
Multiplicando por \(x-1\), obtenemos \(x^3-1=0\), así que \(x^3=1\).

Además, la recurrencia tiene período \(3\), pues \(b_{k+3}=b_k\). Por tanto,
\[
b_9=b_3=b_1=x.
\]
Finalmente,
\[
(b_9)^9=x^9=(x^3)^3=1.
\]

\[
\boxed{1}
\]