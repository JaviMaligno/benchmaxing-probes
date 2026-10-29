Sea \(D=|p-q|\). Mediante el cambio de variables

\[
u=y-px,\qquad v=y-qx,
\]

el paralelogramo se convierte en un rectángulo en coordenadas \((u,v)\). El jacobiano de la transformación tiene determinante \(|p-q|=D\), por lo que el área en el plano \((x,y)\) es el área del rectángulo dividida entre \(D\).

Para el primer paralelogramo, los valores de \(u\) y \(v\) están entre \(r\) y \(s\), así que

\[
\frac{(s-r)^2}{D}=8.
\]

Para el segundo paralelogramo, los valores son \(r\) y \(-s\), así que la longitud del lado es \(r+s\), y

\[
\frac{(r+s)^2}{D}=50.
\]

Dividiendo ambas ecuaciones:

\[
\frac{(r+s)^2}{(s-r)^2}=\frac{50}{8}=\frac{25}{4},
\]

de modo que

\[
\frac{r+s}{|s-r|}=\frac{5}{2}.
\]

Como \(r+s\) y \(|s-r|\) tienen la misma paridad, el menor caso entero posible es

\[
r+s=10,\qquad |s-r|=4,
\]

lo que da \(\{r,s\}=\{3,7\}\). Entonces

\[
D=\frac{(s-r)^2}{8}=\frac{16}{8}=2.
\]

Por tanto, \(|p-q|=2\). Como \(p\) y \(q\) son enteros positivos, la menor suma posible es

\[
p+q=1+3=4.
\]

Así,

\[
p+q+r+s=4+10=14.
\]

Esto se alcanza, por ejemplo, con \(p=1,q=3,r=3,s=7\).

\[
\boxed{14}
\]