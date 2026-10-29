

Sea

\[
N=\underline{a}\underline{b}\underline{c}=100a+10b+c
\]

un número de tres cifras, y sea su rotación cíclica

\[
R=\underline{b}\underline{c}\underline{a}=100b+10c+a.
\]

Observamos que

\[
10N=1000a+100b+10c,
\]

por lo que

\[
10N-R=999a,
\qquad\text{es decir,}\qquad
R=10N-999a.
\]

Si \(x\mid 999\), entonces siempre que \(x\mid N\),

\[
R=10N-999a
\]

también es divisible por \(x\). Así, todo divisor de \(999\) cumple la condición.

Recíprocamente, supongamos que \(x\) cumple la condición. Como \(x\) tiene dos cifras, existe un múltiplo de \(x\) entre \(110\) y \(199\):

- si \(x\ge 55\), entonces \(2x\in[110,198]\);
- si \(10\le x\le 54\), tomando \(k=\left\lceil \frac{110}{x}\right\rceil\), se tiene
  \[
  110\le kx<110+x\le 163<200.
  \]

Sea \(N\) ese múltiplo. Entonces \(N\) tiene cifra de centenas \(a=1\). Por la hipótesis, \(x\mid N\) y \(x\mid R\). Luego

\[
x\mid (10N-R)=999.
\]

Por tanto, los \(x\) válidos son exactamente los divisores de dos cifras de \(999\).

Factorizamos:

\[
999=3^3\cdot 37.
\]

Sus divisores de dos cifras son

\[
27,\;37.
\]

La suma pedida es

\[
27+37=64.
\]

\[
\boxed{64}
\]