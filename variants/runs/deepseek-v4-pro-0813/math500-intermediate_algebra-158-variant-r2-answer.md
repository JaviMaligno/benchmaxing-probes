El problema pide maximizar

\[
pq^2r^2s^3
\]

bajo la restricción

\[
p+q+r+s=16,
\]

con \(p,q,r,s>0\).

Aplicamos el método de los multiplicadores de Lagrange o la desigualdad de la media aritmética–geométrica ponderada (AM–GM). Aquí conviene usar AM–GM ponderada.

Los exponentes son \(1,2,2,3\) para \(p,q,r,s\), respectivamente. La suma de los exponentes es

\[
1+2+2+3=8.
\]

La desigualdad AM–GM ponderada dice que

\[
\frac{p+q+r+s}{8}
=
\frac{p+\frac{q}{2}+\frac{q}{2}+\frac{r}{2}+\frac{r}{2}+\frac{s}{3}+\frac{s}{3}+\frac{s}{3}}{8}
\]

no, mejor agrupamos de la forma correcta. Escribimos cada variable repetida según su exponente:

\[
p,\quad \frac{q}{2},\frac{q}{2},\quad \frac{r}{2},\frac{r}{2},\quad \frac{s}{3},\frac{s}{3},\frac{s}{3}.
\]

Hay en total \(1+2+2+3=8\) términos. Su media aritmética es

\[
\frac{p+\frac{q}{2}+\frac{q}{2}+\frac{r}{2}+\frac{r}{2}+\frac{s}{3}+\frac{s}{3}+\frac{s}{3}}{8}
=
\frac{p+q+r+s}{8}
=
\frac{16}{8}
=
2.
\]

Por AM–GM,

\[
\frac{p+\frac{q}{2}+\frac{q}{2}+\frac{r}{2}+\frac{r}{2}+\frac{s}{3}+\frac{s}{3}+\frac{s}{3}}{8}
\ge
\left(p\left(\frac{q}{2}\right)^2\left(\frac{r}{2}\right)^2\left(\frac{s}{3}\right)^3\right)^{1/8}.
\]

Es decir,

\[
2 \ge \left(\frac{pq^2r^2s^3}{2^2\cdot 2^2\cdot 3^3}\right)^{1/8}.
\]

Ahora,

\[
2^2\cdot 2^2\cdot 3^3 = 4\cdot 4\cdot 27 = 432.
\]

Entonces

\[
2 \ge \left(\frac{pq^2r^2s^3}{432}\right)^{1/8}.
\]

Elevando a la octava potencia:

\[
2^8 \ge \frac{pq^2r^2s^3}{432}.
\]

Por tanto,

\[
256 \ge \frac{pq^2r^2s^3}{432},
\]

así que

\[
pq^2r^2s^3 \le 256\cdot 432.
\]

Calculamos

\[
256\cdot 432 = 110592.
\]

La igualdad se da cuando todos los términos ponderados son iguales:

\[
p = \frac{q}{2} = \frac{r}{2} = \frac{s}{3}.
\]

Sea \(t\) ese valor común. Entonces

\[
p=t,\quad q=2t,\quad r=2t,\quad s=3t.
\]

La suma es

\[
t+2t+2t+3t=8t=16,
\]

de donde \(t=2\). Por tanto,

\[
p=2,\quad q=4,\quad r=4,\quad s=6.
\]

Verificamos:

\[
pq^2r^2s^3 = 2\cdot 4^2\cdot 4^2\cdot 6^3
= 2\cdot 16\cdot 16\cdot 216.
\]

Calculamos:

\[
2\cdot 16=32,\qquad 32\cdot 16=512,\qquad 512\cdot 216=110592.
\]

Por lo tanto, el valor máximo es

\[
\boxed{110592}.
\]