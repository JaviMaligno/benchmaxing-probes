

Sea \(y=x^4\). Entonces

\[
x^8+63x^4-64 = y^2+63y-64.
\]

Factorizamos el polinomio cuadrático:

\[
y^2+63y-64=(y-1)(y+64),
\]

pues \(1\cdot(-64)=-64\) y \(1+(-64)=-63\), así que con signo ajustado se obtiene \(+63y\).

Volviendo a \(x\):

\[
x^8+63x^4-64=(x^4-1)(x^4+64).
\]

Ahora factorizamos cada parte sobre los enteros.

Primero,

\[
x^4-1=(x^2-1)(x^2+1)=(x-1)(x+1)(x^2+1),
\]

y \(x^2+1\) es irreducible sobre los enteros.

Luego,

\[
x^4+64=x^4+4\cdot 2^4.
\]

Usamos la identidad de Sophie Germain:

\[
a^4+4b^4=(a^2-2ab+2b^2)(a^2+2ab+2b^2).
\]

Con \(a=x\) y \(b=2\):

\[
x^4+64=(x^2-4x+8)(x^2+4x+8).
\]

Ambos cuadráticos son irreducibles sobre los enteros, pues sus discriminantes son negativos:

\[
(-4)^2-4(1)(8)=-16,
\]
\[
4^2-4(1)(8)=-16.
\]

Por tanto, la factorización en factores mónicos irreducibles es

\[
x^8+63x^4-64=(x-1)(x+1)(x^2+1)(x^2-4x+8)(x^2+4x+8).
\]

Evaluamos cada factor en \(x=1\):

\[
(x-1)(1)=0,
\]
\[
(x+1)(1)=2,
\]
\[
(x^2+1)(1)=2,
\]
\[
(x^2-4x+8)(1)=1-4+8=5,
\]
\[
(x^2+4x+8)(1)=1+4+8=13.
\]

La suma pedida es

\[
0+2+2+5+13=22.
\]

\[
\boxed{22}
\]