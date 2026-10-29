

Sea \(N_k\) el número de subconjuntos de \(\{1,2,\dots,18\}\) cuyo tamaño es congruente con \(k \pmod 5\). Como cada subconjunto es igualmente probable,

\[
p(k)=\frac{N_k}{2^{18}}.
\]

Los coeficientes binomiales para \(n=18\) son

\[
1,18,153,816,3060,8568,18564,31824,43758,48620,
\]
\[
43758,31824,18564,8568,3060,816,153,18,1.
\]

Agrupamos según el índice módulo \(5\):

\[
\begin{aligned}
N_0&=\binom{18}{0}+\binom{18}{5}+\binom{18}{10}+\binom{18}{15}
=1+8568+43758+816=53143,\\
N_1&=\binom{18}{1}+\binom{18}{6}+\binom{18}{11}+\binom{18}{16}
=18+18564+31824+153=50559,\\
N_2&=\binom{18}{2}+\binom{18}{7}+\binom{18}{12}+\binom{18}{17}
=153+31824+18564+18=50559,\\
N_3&=\binom{18}{3}+\binom{18}{8}+\binom{18}{13}+\binom{18}{18}
=816+43758+8568+1=53143,\\
N_4&=\binom{18}{4}+\binom{18}{9}+\binom{18}{14}
=3060+48620+3060=54740.
\end{aligned}
\]

Además, \(2^{18}=262144\). Entonces

\[
\sum_{k=0}^4 \left|p(k)-\frac15\right|
=
\frac{1}{262144}\sum_{k=0}^4 \left|N_k-\frac{262144}{5}\right|.
\]

Multiplicando numerador y denominador por \(5\),

\[
=
\frac{1}{5\cdot 262144}
\sum_{k=0}^4 |5N_k-262144|.
\]

Calculamos:

\[
\begin{aligned}
|5\cdot 53143-262144|&=3571,\\
|5\cdot 50559-262144|&=9349,\\
|5\cdot 50559-262144|&=9349,\\
|5\cdot 53143-262144|&=3571,\\
|5\cdot 54740-262144|&=11556.
\end{aligned}
\]

Por tanto,

\[
\sum_{k=0}^4 \left|p(k)-\frac15\right|
=
\frac{3571+9349+9349+3571+11556}{5\cdot 262144}
=
\frac{37396}{1310720}
=
\frac{9349}{327680}.
\]

\[
\boxed{\frac{9349}{327680}}
\]