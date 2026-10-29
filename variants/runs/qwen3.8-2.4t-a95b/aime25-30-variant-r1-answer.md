

Sea \(m\) el valor mínimo de \(g\) sobre \(x>0\). Para \(k>0\), se tiene \(g(x)\to+\infty\) cuando \(x\to0^+\) y cuando \(x\to\infty\), así que el mínimo existe.

Supongamos que ese mínimo se alcanza exactamente en dos números positivos distintos \(a\) y \(b\). Como \(x>0\), podemos multiplicar por \(x\) sin cambiar desigualdades:

\[
P(x)=x(g(x)-m)=(x-8)(x-50)(x-72)(x-k)-mx.
\]

Entonces \(P(x)\ge 0\) para todo \(x>0\), y \(P(a)=P(b)=0\). Cada cero interior de un polinomio no negativo tiene multiplicidad par. Como \(P\) tiene grado \(4\), necesariamente

\[
P(x)=(x-a)^2(x-b)^2.
\]

Escribamos \(s=a+b\) y \(p=ab\), con \(p>0\). Entonces

\[
(x-a)^2(x-b)^2=(x^2-sx+p)^2
=x^4-2sx^3+(s^2+2p)x^2-2spx+p^2.
\]

Por otro lado,

\[
(x-8)(x-50)(x-72)=x^3-130x^2+4576x-28800,
\]

así que

\[
P(x)=x^4-(130+k)x^3+(4576+130k)x^2-(28800+4576k+m)x+28800k.
\]

Igualando coeficientes:

\[
2s=130+k,
\]
\[
s^2+2p=4576+130k,
\]
\[
p^2=28800k.
\]

Como \(p>0\),

\[
p=\sqrt{28800k}=120\sqrt{2k}.
\]

Sustituyendo \(s=\frac{130+k}{2}\) en la segunda ecuación:

\[
\left(\frac{130+k}{2}\right)^2+240\sqrt{2k}=4576+130k.
\]

Simplificando:

\[
\frac{k^2}{4}-65k-351+240\sqrt{2k}=0.
\]

Sea \(y=\sqrt{2k}>0\), de modo que \(k=y^2/2\). Multiplicando por \(16\):

\[
y^4-520y^2+3840y-5616=0.
\]

Factorizando:

\[
y^4-520y^2+3840y-5616=(y-2)(y-6)(y-18)(y+26).
\]

Como \(y>0\), las soluciones son

\[
y=2,\quad y=6,\quad y=18.
\]

Por tanto,

\[
k=\frac{y^2}{2}\in\{2,18,162\}.
\]

Para cada uno de estos valores, \(s=(130+k)/2\) y \(p=120\sqrt{2k}\) dan un discriminante \(s^2-4p>0\), así que hay dos raíces positivas distintas \(a,b\). El coeficiente lineal determina \(m\), y entonces \(P(x)=(x-a)^2(x-b)^2\ge0\), con igualdad solo en \(a\) y \(b\). Así, cada uno funciona y no hay más.

La suma pedida es

\[
2+18+162=182.
\]

\[
\boxed{182}
\]