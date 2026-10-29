

Sea \(m=2n+3\). Como \(m\) es impar, \(\gcd(2,m)=1\). Si \(d=\operatorname{ord}_m(2)\), entonces

\[
m\mid 2^{n!}-1 \quad\Longleftrightarrow\quad d\mid n!.
\]

### 1. Cuando \(m\) es compuesto

Escribamos \(m=\prod \ell_i^{a_i}\). Para cada potencia prima \(\ell^a\Vert m\), como \(m\) es impar compuesto, el cofactor de \(\ell\) es al menos \(3\), luego

\[
\ell \le \frac{m}{3}=\frac{2n+3}{3}\le n
\]

para \(n\ge 50\). Además,

\[
\ell^{a-1}\le \frac{m}{\ell}\le \frac{m}{3}\le n.
\]

Así, \(\ell^{a-1}\mid n!\) y \(\ell-1\mid n!\). Como \(\gcd(\ell^{a-1},\ell-1)=1\),

\[
\varphi(\ell^a)=\ell^{a-1}(\ell-1)\mid n!.
\]

Por tanto, \(\operatorname{ord}_{\ell^a}(2)\mid n!\), y el orden módulo \(m\), que es el mcm de estos órdenes, también divide a \(n!\). Entonces, si \(m\) es compuesto, siempre se cumple

\[
2n+3\mid 2^{n!}-1.
\]

### 2. Cuando \(m=p\) es primo

Aquí

\[
\operatorname{ord}_p(2)\mid p-1=2n+2=2(n+1).
\]

Sea \(q=n+1\), con \(51\le q\le 101\).

- Si \(q\) es compuesto, entonces \(q>4\), por lo que \(q\mid (q-1)!=n!\). Además, \(2q\le 202\), así que la potencia de \(2\) en \(2q\) es como mucho \(2^7\), mientras que \(n!\) con \(n\ge 50\) tiene factores de \(2\) de sobra. Luego \(2q\mid n!\), y por tanto \(\operatorname{ord}_p(2)\mid n!\). En este caso sí divide.

- Si \(q\) es primo, entonces \(p=2q+1\). El orden de \(2\) módulo \(p\) divide a \(2q\), y como \(p>3\), no puede ser \(1\) ni \(2\). Así que el orden es \(q\) o \(2q\), en ambos casos múltiplo de \(q=n+1>n\). Como \(q\) es primo y mayor que \(n\), \(q\nmid n!\), luego el orden no divide a \(n!\). Entonces

\[
2n+3\nmid 2^{n!}-1.
\]

Por tanto, los \(n\) buscados son exactamente aquellos para los cuales \(q=n+1\) y \(2q+1\) son ambos primos.

Los primos \(q\) entre \(51\) y \(101\) son:

\[
53,59,61,67,71,73,79,83,89,97,101.
\]

Comprobamos \(2q+1\):

\[
\begin{aligned}
53&\mapsto 107 \text{ primo},\\
59&\mapsto 119=7\cdot 17,\\
61&\mapsto 123=3\cdot 41,\\
67&\mapsto 135,\\
71&\mapsto 143=11\cdot 13,\\
73&\mapsto 147,\\
79&\mapsto 159=3\cdot 53,\\
83&\mapsto 167 \text{ primo},\\
89&\mapsto 179 \text{ primo},\\
97&\mapsto 195,\\
101&\mapsto 203=7\cdot 29.
\end{aligned}
\]

Los casos que fallan son entonces

\[
n=q-1=52,\;82,\;88.
\]

Su suma es

\[
52+82+88=222.
\]

\[
\boxed{222}
\]