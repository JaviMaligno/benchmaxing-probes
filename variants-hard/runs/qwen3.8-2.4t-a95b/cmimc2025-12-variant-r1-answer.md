

Sea \(p_n\) la probabilidad de que Coral llegue exactamente a \(n\) peces en total.

El día en que sus plumas se vuelven naranjas es el primer día en que el total es \(\ge 8\). Como cada día come 1 o 2 peces, ese día puede terminar con total \(8\) o \(9\). Se enferma ese día si termina con \(9\) o más. Por tanto, no enfermarse ese día equivale a llegar exactamente a \(8\).

Para \(n\ge 2\), llegar exactamente a \(n\) requiere haber estado antes en \(n-1\) y comer 1 pez, o en \(n-2\) y comer 2 peces:

\[
p_n=\frac23 p_{n-1}+\frac13 p_{n-2}.
\]

Con

\[
p_0=1,\qquad p_1=\frac23.
\]

La recurrencia tiene solución cerrada. Su ecuación característica es

\[
r^2=\frac23 r+\frac13,
\]

con raíces \(r=1\) y \(r=-\frac13\). Por tanto,

\[
p_n=A+B\left(-\frac13\right)^n.
\]

Usando \(p_0=1\) y \(p_1=\frac23\), se obtiene

\[
p_n=\frac34+\frac14\left(-\frac13\right)^n.
\]

Entonces

\[
p_8=\frac34+\frac14\cdot\frac1{6561}
=\frac{19684}{26244}
=\frac{4921}{6561}.
\]

\[
\boxed{\frac{4921}{6561}}
\]