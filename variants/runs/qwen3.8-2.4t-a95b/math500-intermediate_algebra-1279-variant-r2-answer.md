

Sea  
\[
P(t)=(t-1)(t-2)(t-3)(t-4).
\]
Entonces
\[
\frac{P'(t)}{P(t)}=\sum_{k=1}^4 \frac{1}{t-k}.
\]

Además,
\[
\frac{k}{x^2-k}=\frac{x^2}{x^2-k}-1,
\]
por lo que
\[
\sum_{k=1}^4 \frac{k}{x^2-k}
= x^2\sum_{k=1}^4 \frac{1}{x^2-k}-4
= x^2\frac{P'(x^2)}{P(x^2)}-4.
\]

La ecuación dada es
\[
\sum_{k=1}^4 \frac{k}{x^2-k}=2022x-4,
\]
así que
\[
x^2\frac{P'(x^2)}{P(x^2)}-4=2022x-4,
\]
y por tanto
\[
x^2\frac{P'(x^2)}{P(x^2)}=2022x.
\]

Multiplicando por \(P(x^2)\), obtenemos el polinomio
\[
x^2P'(x^2)-2022xP(x^2)=0.
\]

Como
\[
P(t)=t^4-10t^3+35t^2-50t+24,
\]
entonces
\[
P'(t)=4t^3-30t^2+70t-50.
\]

Los términos principales del polinomio son
\[
x^2P'(x^2)-2022xP(x^2)
=4x^8+\cdots-2022x(x^8+\cdots)
=-2022x^9+4x^8+\cdots.
\]

Por lo tanto, es un polinomio de grado \(9\) con coeficiente principal \(-2022\) y coeficiente de \(x^8\) igual a \(4\).

Por las fórmulas de Vieta, la suma de todas las raíces complejas es
\[
-\frac{4}{-2022}=\frac{4}{2022}=\frac{2}{1011}.
\]

\[
\boxed{\frac{2}{1011}}
\]