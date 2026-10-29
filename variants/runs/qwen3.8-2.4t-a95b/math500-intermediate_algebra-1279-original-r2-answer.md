

Sea
\[
P(t)=(t-1)(t-2)(t-3)(t-4)=t^4-10t^3+35t^2-50t+24.
\]

Para cada \(k\),
\[
\frac{k}{x^2-k}=\frac{x^2}{x^2-k}-1.
\]
Por tanto,
\[
\sum_{k=1}^4 \frac{k}{x^2-k}
=
x^2\sum_{k=1}^4\frac1{x^2-k}-4.
\]

La ecuación dada se convierte en
\[
x^2\sum_{k=1}^4\frac1{x^2-k}-4=2010x-4,
\]
es decir,
\[
x^2\sum_{k=1}^4\frac1{x^2-k}=2010x.
\]

Como
\[
\sum_{k=1}^4\frac1{t-k}=\frac{P'(t)}{P(t)},
\]
con \(t=x^2\) obtenemos
\[
\frac{x^2P'(x^2)}{P(x^2)}=2010x.
\]

Multiplicando por \(P(x^2)\),
\[
x^2P'(x^2)-2010xP(x^2)=0.
\]

Si \(x^2\in\{1,2,3,4\}\), entonces \(P(x^2)=0\), pero el polinomio anterior vale \(x^2P'(x^2)\neq 0\); así que no se introducen soluciones falsas en los polos.

Ahora calculamos los términos principales. Como
\[
P'(t)=4t^3-30t^2+70t-50,
\]
tenemos
\[
x^2P'(x^2)=4x^8+\cdots
\]
y
\[
2010xP(x^2)=2010x(x^8-10x^6+\cdots)=2010x^9+\cdots.
\]

Así, el polinomio resultante es
\[
-2010x^9+4x^8+\cdots=0.
\]

Por Vieta, la suma de todas las raíces complejas es
\[
-\frac{4}{-2010}=\frac{4}{2010}=\frac{2}{1005}.
\]

\[
\boxed{\frac{2}{1005}}
\]