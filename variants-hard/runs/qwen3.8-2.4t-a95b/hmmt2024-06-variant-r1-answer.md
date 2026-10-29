

Sea  
\[
M=2n+3,\qquad N=n+1,
\]
de modo que \(M=2N+1\). Como \(M\) es impar, \(\gcd(2,M)=1\), y

\[
M\mid 2^{n!}-1 \iff \operatorname{ord}_M(2)\mid n!.
\]

### 1. Si \(M\) es compuesto

Sea \(p^a\) una potencia prima que divide a \(M\). Como \(M\) es impar compuesto y \(n\ge 60\), todo primo divisor \(p\) cumple \(p\le M/3<n\). Además,

\[
p^{a-1}\le \frac{M}{p}\le \frac{M}{3}<n.
\]

Por tanto, \(p^{a-1}\le n\) y \(p-1<n\). Como \(\gcd(p^{a-1},p-1)=1\), se tiene

\[
\varphi(p^a)=p^{a-1}(p-1)\mid n!.
\]

Luego \(\operatorname{ord}_{p^a}(2)\mid \varphi(p^a)\mid n!\). Por CRT, el orden módulo \(M\) también divide a \(n!\). Así, si \(M\) es compuesto, siempre se cumple la divisibilidad; esos \(n\) no aportan.

### 2. Si \(M\) es primo

Entonces \(M=2N+1\) es primo y

\[
\operatorname{ord}_M(2)\mid M-1=2N.
\]

- Si \(N=n+1\) es compuesto, como \(N>4\), se sabe que \(N\mid (N-1)!=n!\). Además, \(n!\) tiene factores de 2 de sobra para incluir el factor extra en \(2N\), así que \(2N\mid n!\). Por tanto, \(\operatorname{ord}_M(2)\mid n!\), y la divisibilidad sí se cumple.

- Si \(N=n+1\) es primo, los posibles órdenes de \(2\) módulo \(M\) son divisores de \(2N\): \(1,2,N,2N\). Como \(M>3\), el orden no es \(1\) ni \(2\), así que es \(N\) o \(2N\). En ambos casos es múltiplo de \(N=n+1\), que es un primo mayor que \(n\), por lo que no divide a \(n!\). Entonces la divisibilidad falla.

Por tanto, buscamos los \(n\) tales que \(n+1\) es primo y \(2(n+1)+1=2n+3\) también es primo.

Los primos \(N=n+1\) entre \(61\) y \(121\) son:

\[
61,67,71,73,79,83,89,97,101,103,107,109,113.
\]

Calculamos \(2N+1\):

\[
\begin{aligned}
61&\mapsto 123=3\cdot 41,\\
67&\mapsto 135,\\
71&\mapsto 143=11\cdot 13,\\
73&\mapsto 147,\\
79&\mapsto 159,\\
83&\mapsto 167\ \text{primo},\\
89&\mapsto 179\ \text{primo},\\
97&\mapsto 195,\\
101&\mapsto 203=7\cdot 29,\\
103&\mapsto 207,\\
107&\mapsto 215=5\cdot 43,\\
109&\mapsto 219,\\
113&\mapsto 227\ \text{primo}.
\end{aligned}
\]

Los casos válidos son \(N=83,89,113\), es decir,

\[
n=82,\ 88,\ 112.
\]

La suma pedida es

\[
82+88+112=282.
\]

\[
\boxed{282}
\]