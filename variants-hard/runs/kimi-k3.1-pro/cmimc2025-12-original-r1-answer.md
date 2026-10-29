Sea \(p_n\) la probabilidad de que Pinky alcance en algún momento un total de exactamente \(n\) camarones. Para no enfermarse el día en que su piel se vuelve rosa, debe alcanzar exactamente \(10\); si pasa de \(9\) a \(11\), se enfermará.

El último día antes de llegar a \(n\), Pinky estaba en \(n-1\) y comió \(1\), o estaba en \(n-2\) y comió \(2\). Por tanto,
\[
p_n=\frac12p_{n-1}+\frac12p_{n-2},
\qquad p_0=1,\quad p_1=\frac12.
\]

La solución de esta recurrencia es
\[
p_n=\frac23+\frac13\left(-\frac12\right)^n.
\]
Así,
\[
p_{10}=\frac23+\frac{1}{3\cdot 2^{10}}
=\frac{2048+1}{3072}
=\frac{683}{1024}.
\]

\[
\boxed{\frac{683}{1024}}
\]