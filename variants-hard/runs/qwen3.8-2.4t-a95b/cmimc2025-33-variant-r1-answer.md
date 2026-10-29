

Sea

\[
g(x)=x^3-3x,\qquad x_0=\frac{n^2+1}{n}=n+\frac1n.
\]

Usamos la identidad clave: si \(x=t+t^{-1}\), entonces

\[
g(x)=(t+t^{-1})^3-3(t+t^{-1})=t^3+t^{-3}.
\]

Por inducción,

\[
g^k\!\left(n+\frac1n\right)=n^{3^k}+n^{-3^k}.
\]

Llamemos \(A=3^k\). Entonces queremos

\[
\left|n^A+n^{-A}-c^{72}\right|<\frac1{100}.
\]

Si \(n=1\), la expresión vale siempre \(2\), y no hay ningún \(c^{72}\) a distancia menor que \(1/100\). Así que \(n\ge 2\).

Como \(c^{72}\) y \(n^A\) son enteros, sea

\[
M=c^{72}-n^A\in \mathbb Z.
\]

La desigualdad se convierte en

\[
\left|n^{-A}-M\right|<\frac1{100}.
\]

Pero \(0<n^{-A}\le \frac12\), por lo que el único entero que puede estar a menos de \(1/100\) de \(n^{-A}\) es \(M=0\). Entonces necesariamente

\[
c^{72}=n^A=n^{3^k}.
\]

Ahora analizamos cuándo \(n^{3^k}\) es una potencia \(72\)-ésima. Si

\[
n=\prod p^{e_p},
\]

necesitamos que para cada primo \(p\),

\[
72 \mid 3^k e_p.
\]

Como \(72=2^3\cdot 3^2\):

- Si \(k=1\), se necesita \(24\mid e_p\), así que \(n\) es una potencia \(24\)-ésima. La menor posible mayor que \(1\) es \(2^{24}\).
- Si \(k\ge 2\), como \(\gcd(3^k,72)=9\), se necesita \(8\mid e_p\), así que \(n\) es una potencia octava. La menor posible mayor que \(1\) es

\[
2^8=256.
\]

Con \(n=256\), tomamos \(k=2\) y \(c=2\). Entonces

\[
g^2\!\left(\frac{256^2+1}{256}\right)
=256^9+256^{-9}
=2^{72}+2^{-72}.
\]

Por tanto,

\[
\left|g^2\!\left(\frac{256^2+1}{256}\right)-2^{72}\right|
=2^{-72}<\frac1{100}.
\]

Así que el menor \(n\) posible es

\[
\boxed{256}
\]