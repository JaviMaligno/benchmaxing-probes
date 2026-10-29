El área de un paralelogramo delimitado por las rectas \(y=px+a\), \(y=px+b\), \(y=qx+c\), \(y=qx+d\) (con \(p\ne q\)) está dada por:

\[
\text{Área}=\frac{|a-b|\,|c-d|}{|p-q|}.
\]

Para el primer paralelogramo tenemos:

\[
\frac{|(r)-(s)|\,|(r)-(s)|}{|p-q|}
=\frac{(s-r)^2}{|p-q|}=8.
\]

Para el segundo:

\[
\frac{|r-(-s)|\,|r-(-s)|}{|p-q|}
=\frac{(r+s)^2}{|p-q|}=50.
\]

Como \(p,q,r,s\) son enteros positivos y las áreas son distintas, \(p\ne q\); supongamos \(p>q\), de modo que \(|p-q|=p-q\). Entonces:

\[
(s-r)^2=8(p-q),\qquad (r+s)^2=50(p-q).
\]

Dividiendo ambas igualdades:

\[
\frac{(r+s)^2}{(s-r)^2}=\frac{50}{8}=\frac{25}{4},
\]

y tomando raíces cuadradas positivas:

\[
\frac{r+s}{s-r}=\frac{5}{2}.
\]

Despejando:

\[
2(r+s)=5(s-r)\implies 2r+2s=5s-5r\implies 7r=3s.
\]

Así:

\[
r=\frac{3s}{7}.
\]

Para que \(r\) sea entero positivo, \(s\) debe ser múltiplo de \(7\). Sea \(s=7k\), entonces \(r=3k\), con \(k\) entero positivo.

Tenemos:

\[
s-r=4k,\qquad r+s=10k.
\]

Entonces:

\[
(4k)^2=8(p-q)\implies 16k^2=8(p-q)\implies p-q=2k^2.
\]

Además:

\[
(10k)^2=50(p-q)\implies 100k^2=50(p-q)\implies p-q=2k^2,
\]

que coincide. Por tanto, la condición es \(p-q=2k^2\).

Queremos minimizar

\[
p+q+r+s=p+q+3k+7k=p+q+10k.
\]

Con \(p-q=2k^2\) y \(p,q\) enteros positivos. Para \(k=1\):

\[
p-q=2.
\]

El mínimo de \(p+q\) con \(p,q>0\) y \(p-q=2\) se da con \(q=1\), \(p=3\), lo que da \(p+q=4\). Así:

\[
p+q+r+s=4+10=14.
\]

Por lo tanto, el menor valor posible es:

\[
\boxed{14}
\]