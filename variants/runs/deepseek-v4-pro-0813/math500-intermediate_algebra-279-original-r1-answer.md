Sustituimos \(y=x^4\):

\[
x^8+3x^4-4 = y^2+3y-4 = (y+4)(y-1) = (x^4+4)(x^4-1).
\]

Factorizamos cada factor por completo:

\[
x^4-1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1),
\]

y usando la identidad de Sophie Germain,

\[
x^4+4 = (x^2+2x+2)(x^2-2x+2).
\]

Entonces

\[
x^8+3x^4-4 = (x-1)(x+1)(x^2+1)(x^2+2x+2)(x^2-2x+2).
\]

Todos los factores son mónicos, con coeficientes enteros e irreducibles sobre los enteros. Evaluando en \(x=1\):

\[
\begin{aligned}
(x-1)(1) &= 0,\\
(x+1)(1) &= 2,\\
(x^2+1)(1) &= 2,\\
(x^2+2x+2)(1) &= 1+2+2 = 5,\\
(x^2-2x+2)(1) &= 1-2+2 = 1.
\end{aligned}
\]

La suma es

\[
0+2+2+5+1 = 10.
\]

\[
\boxed{10}
\]