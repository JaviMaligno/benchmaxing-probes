

Sea \(n=|\lfloor x\rfloor|\). Los tres primeros términos de \(f(x)\) y \(g(x)\) son idénticos:

\[
e^{3x^2-n!},\qquad \binom{22+735235n}{2356},\qquad \phi(n+1),
\]

así que se cancelan al igualar \(f(x)=g(x)\). Solo queda comparar los polinomios:

\[
72x^4+3x^3-6x^2+2x+1
=
72x^4+4x^3-11x^2-6x+13.
\]

Cancelando \(72x^4\) y llevando todo a un lado:

\[
0=(4-3)x^3+(-11+6)x^2+(-6-2)x+(13-1)
\]

\[
0=x^3-5x^2-8x+12.
\]

Factorizamos. Probando \(x=1\):

\[
1-5-8+12=0,
\]

entonces \(x-1\) es factor. Dividiendo:

\[
x^3-5x^2-8x+12=(x-1)(x^2-4x-12).
\]

Y

\[
x^2-4x-12=(x-6)(x+2).
\]

Por tanto,

\[
(x-1)(x-6)(x+2)=0,
\]

cuyas raíces son

\[
x=-2,\quad x=1,\quad x=6.
\]

En \(x=6\), \(\lfloor x\rfloor=6\), por lo que todos los términos originales están definidos. Así, el mayor valor de \(x\) donde se intersecan es

\[
\boxed{6}
\]