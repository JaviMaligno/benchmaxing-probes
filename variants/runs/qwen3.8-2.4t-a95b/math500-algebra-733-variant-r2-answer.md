

Para cualquier valor fijo de \(x\), los términos

\[
e^{2x^2-|\lfloor x\rfloor|!},\qquad 
\binom{19+735235|\lfloor x\rfloor|}{2356},\qquad 
\phi(|\lfloor x\rfloor|+1)
\]

son exactamente iguales en \(p(x)\) y \(q(x)\), pues dependen de la misma \(x\). Por tanto, al resolver \(p(x)=q(x)\), esos términos se cancelan.

Queda comparar solo las partes polinomiales:

\[
51x^4+3x^3-4x^2+5x+2
=
51x^4+4x^3-7x^2-8x+17.
\]

Cancelamos \(51x^4\):

\[
3x^3-4x^2+5x+2=4x^3-7x^2-8x+17.
\]

Llevando todo a un lado:

\[
0=x^3-3x^2-13x+15.
\]

Factorizamos. Probando \(x=1\):

\[
1-3-13+15=0,
\]

así que \(x-1\) es un factor. Dividiendo:

\[
x^3-3x^2-13x+15=(x-1)(x^2-2x-15).
\]

Y

\[
x^2-2x-15=(x-5)(x+3).
\]

Entonces las intersecciones ocurren en

\[
x=-3,\;1,\;5.
\]

El mayor valor de \(x\) es \(5\).

\[
\boxed{5}
\]