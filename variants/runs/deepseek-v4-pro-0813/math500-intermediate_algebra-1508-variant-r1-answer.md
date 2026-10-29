Sea \(b_1=x\). Aplicando la recurrencia:

\[
b_2=-\frac{1}{1+x},
\]

\[
b_3=-\frac{1}{1+b_2}
=-\frac{1}{1-\frac{1}{1+x}}
=-\frac{1+x}{x}.
\]

Como \(b_3=b_1\), se tiene

\[
-\frac{1+x}{x}=x
\]

\[
-(1+x)=x^2
\]

\[
x^2+x+1=0.
\]

Por tanto, \(x\) es una raíz cúbica primitiva de la unidad:

\[
x^3=1.
\]

Además:

\[
b_2=-\frac{1}{1+x}.
\]

Como \(x^2+x+1=0\), tenemos \(1+x=-x^2\), luego

\[
b_2=-\frac{1}{-x^2}=\frac{1}{x^2}=x,
\]

porque \(x^3=1\). Entonces \(b_2=b_1\), y por inducción todos los términos son iguales a \(x\). Por lo tanto,

\[
b_9=x
\]

y

\[
(b_9)^9=x^9=(x^3)^3=1.
\]

\[
\boxed{1}
\]