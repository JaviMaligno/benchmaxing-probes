Sea \(r_i = A_1A_i\) para \(i=2,\dots,11\).

Como \(\cos(\angle A_iA_1A_{i+1})=\frac{12}{13}\), tenemos

\[
\sin(\angle A_iA_1A_{i+1})=\frac{5}{13}.
\]

El área de cada triángulo es \(1\), así que

\[
1=\frac12 r_i r_{i+1}\cdot \frac{5}{13}
\]

y por tanto

\[
r_i r_{i+1}=\frac{26}{5}.
\]

Esto implica que las longitudes \(r_i\) se alternan. Si \(r_2=x\), entonces

\[
r_3=\frac{26/5}{x},\quad r_4=x,\quad r_5=\frac{26/5}{x},\dots
\]

En particular,

\[
A_1A_2 + A_1A_{11}=x+\frac{26/5}{x}.
\]

Llamemos

\[
S=x+\frac{26/5}{x}.
\]

Para cada lado \(A_iA_{i+1}\) con \(2\le i\le 10\), por la ley de cosenos,

\[
A_iA_{i+1}^2=r_i^2+r_{i+1}^2-2r_ir_{i+1}\cdot \frac{12}{13}.
\]

Como \(r_i+r_{i+1}=S\) y \(r_ir_{i+1}=\frac{26}{5}\),

\[
r_i^2+r_{i+1}^2=S^2-2\cdot \frac{26}{5}.
\]

Entonces

\[
A_iA_{i+1}^2
=S^2-2\cdot \frac{26}{5}-2\cdot \frac{26}{5}\cdot \frac{12}{13}.
\]

Calculando el término constante:

\[
2\cdot \frac{26}{5}\left(1+\frac{12}{13}\right)
=2\cdot \frac{26}{5}\cdot \frac{25}{13}
=20.
\]

Por eso cada uno de los \(9\) lados intermedios mide

\[
\sqrt{S^2-20}.
\]

El perímetro total es \(20\):

\[
S+9\sqrt{S^2-20}=20.
\]

Así,

\[
\sqrt{S^2-20}=\frac{20-S}{9}.
\]

Elevando al cuadrado:

\[
S^2-20=\frac{(20-S)^2}{81}.
\]

Multiplicando por \(81\):

\[
81S^2-1620=S^2-40S+400.
\]

\[
80S^2+40S-2020=0.
\]

Dividiendo entre \(20\):

\[
4S^2+2S-101=0.
\]

Resolviendo:

\[
S=\frac{-2+\sqrt{4+1616}}{8}
=\frac{-2+\sqrt{1620}}{8}
=\frac{-2+18\sqrt5}{8}
=\frac{9\sqrt5-1}{4}.
\]

Por tanto,

\[
A_1A_2+A_1A_{11}=\frac{9\sqrt5-1}{4}.
\]

Entonces \(m=9\), \(n=5\), \(p=1\), \(q=4\), y

\[
m+n+p+q=9+5+1+4=19.
\]

\[
\boxed{19}
\]