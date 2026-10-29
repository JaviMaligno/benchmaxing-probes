Voy a resolver el problema paso a paso.

Queremos encontrar los valores de \(x\) donde

\[
f(x)=g(x).
\]

Las funciones son:

\[
f(x)=e^{3x^2-|\lfloor x \rfloor|!}+\binom{22+735235|\lfloor x \rfloor |}{2356}+\phi(|\lfloor x \rfloor|+1)+72x^4+3x^3-6x^2+2x+1
\]

\[
g(x)=e^{3x^2-|\lfloor x \rfloor|!}+\binom{22+735235|\lfloor x \rfloor |}{2356}+\phi(|\lfloor x \rfloor|+1)+72x^4+4x^3-11x^2-6x+13
\]

Observa que los tres primeros términos (los que dependen del suelo \(\lfloor x\rfloor\)) son idénticos. Entonces, al igualar \(f(x)=g(x)\), esos términos se cancelan. Queda:

\[
72x^4+3x^3-6x^2+2x+1=72x^4+4x^3-11x^2-6x+13
\]

Cancelamos \(72x^4\) en ambos lados:

\[
3x^3-6x^2+2x+1=4x^3-11x^2-6x+13
\]

Movemos todo a un lado:

\[
3x^3-6x^2+2x+1-4x^3+11x^2+6x-13=0
\]

\[
-x^3+5x^2+8x-12=0
\]

Multiplicamos por \(-1\):

\[
x^3-5x^2-8x+12=0.
\]

Buscamos raíces de

\[
P(x)=x^3-5x^2-8x+12=0.
\]

Probamos divisores de \(12\): \(x=1\):

\[
1-5-8+12=0.
\]

Así que \(x=1\) es raíz. Factorizamos:

\[
x^3-5x^2-8x+12=(x-1)(x^2-4x-12).
\]

Resolvemos

\[
x^2-4x-12=0.
\]

\[
x=\frac{4\pm\sqrt{16+48}}{2}=\frac{4\pm 8}{2}.
\]

Entonces

\[
x=\frac{4+8}{2}=6,\qquad x=\frac{4-8}{2}=-2.
\]

Las raíces son:

\[
x=-2,\quad x=1,\quad x=6.
\]

El mayor valor de \(x\) es \(6\).

\[
\boxed{6}
\]