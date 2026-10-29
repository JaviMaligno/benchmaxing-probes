Por Vieta, si las raíces enteras distintas son \(r_1,\dots,r_n\), entonces

\[
g(x)=2\prod_{i=1}^n (x-r_i).
\]

Además,

\[
c_0=g(0)=2(-1)^n\prod_{i=1}^n r_i=78
\]

así que

\[
\left|\prod_{i=1}^n r_i\right|=39=3\cdot 13.
\]

Ninguna raíz es \(0\). Aparte de las posibles raíces \(1\) y \(-1\), las demás raíces deben tener valores absolutos que multipliquen \(39\). Por ser \(39\) libre de cuadrados, las raíces no unitarias solo pueden ser:

- dos raíces con valores absolutos \(3\) y \(13\), o
- una raíz con valor absoluto \(39\).

Sea \(S=\sum r_i\) la suma de las raíces. La parte no unitaria de la suma tiene valor absoluto mínimo \(10\) cuando las raíces son \(3\) y \(-13\) (o \(-3\) y \(13\)). Las raíces \(1\) y \(-1\) solo pueden aportar en total \(-1,0\) o \(1\). Por lo tanto,

\[
|S|\ge 10-1=9.
\]

Como

\[
c_{n-1}=-2S,
\]

se tiene

\[
|c_{n-1}|=2|S|\ge 18.
\]

El valor se alcanza con raíces \(1,3,-13\):

\[
g(x)=2(x-1)(x-3)(x+13)=2x^3+18x^2-98x+78,
\]

donde \(c_{n-1}=c_2=18\).

\[
\boxed{18}
\]