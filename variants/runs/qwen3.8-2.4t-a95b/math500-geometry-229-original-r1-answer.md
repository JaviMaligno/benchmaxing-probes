

Sea \(D=|a-b|\). Para un paralelogramo formado por las rectas

\[
y=ax+u,\quad y=ax+v,\quad y=bx+u,\quad y=bx+v,
\]

el área es

\[
\frac{|u-v|^2}{|a-b|}.
\]

Esto se puede ver usando el cambio de variables \((s,t)=(y-ax,y-bx)\), donde la región es un rectángulo de lados \(|u-v|\) y \(|u-v|\), y el jacobiano aporta el factor \(|a-b|\).

Para el primer paralelogramo:

\[
\frac{(c-d)^2}{D}=18.
\]

Para el segundo:

\[
\frac{(c+d)^2}{D}=72.
\]

Dividiendo ambas ecuaciones:

\[
\left(\frac{c+d}{c-d}\right)^2=4,
\]

por lo que

\[
c+d=2|c-d|.
\]

Si \(d>c\), entonces \(c+d=2(d-c)\), de donde \(d=3c\). Análogamente si \(c>d\), se obtiene \(c=3d\). Así, \(\{c,d\}=\{m,3m\}\) para algún entero positivo \(m\).

Entonces

\[
|c-d|=2m,
\]

y usando la primera área:

\[
\frac{(2m)^2}{D}=18
\]

\[
\frac{4m^2}{D}=18
\]

\[
D=\frac{2m^2}{9}.
\]

Como \(D\) es entero, \(m\) debe ser múltiplo de \(3\). Escribamos \(m=3k\). Entonces

\[
D=2k^2,
\]

y

\[
c+d=4m=12k.
\]

Para minimizar \(a+b\) dado que \(|a-b|=2k^2\) y \(a,b\) son enteros positivos, el mínimo es

\[
a+b=2k^2+2.
\]

Por tanto,

\[
a+b+c+d=2k^2+2+12k.
\]

Esta expresión es mínima para \(k=1\), dando

\[
2+2+12=16.
\]

Un ejemplo que lo logra es \(a=1\), \(b=3\), \(c=3\), \(d=9\).

\[
\boxed{16}
\]