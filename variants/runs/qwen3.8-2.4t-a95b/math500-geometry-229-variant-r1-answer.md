

Sea \(D=|p-q|\). Para un paralelogramo formado por las rectas

\[
y=px+\alpha,\quad y=px+\beta,\quad y=qx+\gamma,\quad y=qx+\delta,
\]

el área es

\[
\frac{|\alpha-\beta|\,|\gamma-\delta|}{|p-q|}.
\]

Esto se puede ver con el cambio de variables \(u=y-px\), \(v=y-qx\), cuyo Jacobiano aporta el factor \(1/|p-q|\).

Para el primer paralelogramo, las diferencias de ordenadas al origen son \(|s-r|\) en ambas familias, así que

\[
\frac{(s-r)^2}{D}=8.
\]

Para el segundo paralelogramo, las diferencias son \(r-(-s)=r+s\), así que

\[
\frac{(r+s)^2}{D}=50.
\]

Dividiendo ambas ecuaciones:

\[
\frac{(r+s)^2}{(s-r)^2}=\frac{50}{8}=\frac{25}{4},
\]

por lo tanto

\[
\frac{r+s}{|s-r|}=\frac52.
\]

Supongamos sin pérdida de generalidad que \(s>r\). Entonces

\[
2(r+s)=5(s-r),
\]

\[
2r+2s=5s-5r,
\]

\[
7r=3s.
\]

Así que \(r=3k\) y \(s=7k\) para algún entero positivo \(k\). Entonces

\[
r+s=10k,\qquad |s-r|=4k.
\]

Usando la primera área:

\[
\frac{(4k)^2}{D}=8
\]

\[
\frac{16k^2}{D}=8
\]

\[
D=2k^2.
\]

Por tanto, \(|p-q|=2k^2\). Para minimizar \(p+q\) con enteros positivos y diferencia \(2k^2\), tomamos los valores más pequeños posibles:

\[
\{p,q\}=\{1,1+2k^2\},
\]

de modo que

\[
p+q=2k^2+2.
\]

La suma total es

\[
p+q+r+s=2k^2+2+10k.
\]

Como \(k\ge 1\), el mínimo ocurre en \(k=1\):

\[
2(1)^2+2+10(1)=14.
\]

Esto es alcanzable, por ejemplo con \(p=1\), \(q=3\), \(r=3\), \(s=7\).

\[
\boxed{14}
\]