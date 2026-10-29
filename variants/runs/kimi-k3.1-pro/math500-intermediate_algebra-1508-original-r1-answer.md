La recurrencia tiene periodo \(3\), pues
\[
a_2=\frac1{1-a_1},\qquad
a_3=\frac{a_1-1}{a_1},\qquad
a_4=a_1.
\]
Por tanto, \(a_9=a_3=a_1\).

De \(a_3=a_1\) obtenemos
\[
a_1=\frac{a_1-1}{a_1}
\quad\Longrightarrow\quad
a_1^2-a_1+1=0.
\]
Multiplicando por \(a_1+1\):
\[
(a_1+1)(a_1^2-a_1+1)=a_1^3+1=0,
\]
así que \(a_1^3=-1\). Finalmente,
\[
(a_9)^9=a_1^9=(a_1^3)^3=(-1)^3=\boxed{-1}.
\]