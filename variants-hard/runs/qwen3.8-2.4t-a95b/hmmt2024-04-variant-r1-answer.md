

Sea \(g(x)=\dfrac{P(x)}{Q(x)}\), donde \(P\) y \(Q\) son polinomios cuadráticos. Definamos

\[
H(x)=P(x)-x^{3}Q(x).
\]

Como \(g(k)=k^{3}\) para \(k\in\{1,2,3,4,6\}\), tenemos

\[
P(k)-k^{3}Q(k)=0,
\]

así que \(H(x)\) tiene raíces \(1,2,3,4,6\). Además, \(H\) tiene grado a lo sumo \(5\). Por tanto,

\[
H(x)=A(x-1)(x-2)(x-3)(x-4)(x-6)
\]

para alguna constante \(A\neq 0\).

Sea

\[
F(x)=(x-1)(x-2)(x-3)(x-4)(x-6).
\]

Queremos \(g(0)=\dfrac{P(0)}{Q(0)}\). Como \(P\) es cuadrático, el término constante de \(H=P-x^{3}Q\) es simplemente \(P(0)\). Además, el coeficiente de \(x^{3}\) en \(H\) es \(-Q(0)\), porque el término \(x^{3}Q(x)\) aporta \(Q(0)x^{3}\).

Así,

\[
g(0)=\frac{H(0)}{-[x^{3}]H}
=\frac{F(0)}{-[x^{3}]F}.
\]

Calculamos:

\[
F(0)=(-1)(-2)(-3)(-4)(-6)=-144.
\]

El coeficiente de \(x^{3}\) en \(F\) es la suma de los productos de las raíces tomadas de dos en dos:

\[
[x^{3}]F=\sum_{i<j} r_ir_j.
\]

Con raíces \(1,2,3,4,6\),

\[
\sum r_i = 16,\qquad \sum r_i^2=1+4+9+16+36=66.
\]

Entonces

\[
\sum_{i<j} r_ir_j=\frac{16^{2}-66}{2}=\frac{190}{2}=95.
\]

Por lo tanto,

\[
g(0)=\frac{-144}{-95}=\frac{144}{95}.
\]

\[
\boxed{\frac{144}{95}}
\]