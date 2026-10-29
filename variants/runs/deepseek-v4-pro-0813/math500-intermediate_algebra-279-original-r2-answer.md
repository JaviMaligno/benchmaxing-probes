Paso a paso:

1. Sea \(P(x)=x^8+3x^4-4\). Observamos que solo aparecen potencias de \(x^4\), así que sustituimos \(y=x^4\):

\[
P(x)=y^2+3y-4.
\]

2. Factorizamos el polinomio en \(y\):

\[
y^2+3y-4=(y+4)(y-1).
\]

3. Volvemos a \(x\):

\[
x^8+3x^4-4=(x^4+4)(x^4-1).
\]

4. Factorizamos cada factor sobre los enteros.

- \(x^4-1=(x^2-1)(x^2+1)=(x-1)(x+1)(x^2+1)\).

- \(x^4+4\) se puede factorizar mediante la identidad de Sophie Germain:

\[
x^4+4=x^4+4x^2+4-4x^2=(x^2+2)^2-(2x)^2
=(x^2-2x+2)(x^2+2x+2).
\]

5. Por lo tanto, la factorización completa sobre los enteros es:

\[
P(x)=(x-1)(x+1)(x^2+1)(x^2-2x+2)(x^2+2x+2).
\]

Todos esos factores son monicos y ya no se pueden factorizar más sobre los enteros.

6. Ahora evaluamos cada factor en \(x=1\):

\[
x-1 \to 0,
\]
\[
x+1 \to 2,
\]
\[
x^2+1 \to 2,
\]
\[
x^2-2x+2 \to 1-2+2=1,
\]
\[
x^2+2x+2 \to 1+2+2=5.
\]

7. La suma pedida es:

\[
0+2+2+1+5=10.
\]

\[
\boxed{10}
\]