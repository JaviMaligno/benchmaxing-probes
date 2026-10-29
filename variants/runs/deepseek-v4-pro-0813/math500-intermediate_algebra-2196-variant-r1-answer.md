Necesitamos maximizar

\[
f(a,b)=\frac{a-b}{a^4+b^4+96}.
\]

Como el denominador es siempre positivo, el máximo se alcanzará para \(a-b>0\), es decir \(a>b\). Si cambiamos \((a,b)\mapsto(-b,-a)\), el numerador \(a-b\) se transforma en \((-b)-(-a)=a-b\), y el denominador no cambia, así que la expresión es invariante bajo esa transformación. Por ello, es natural probar con \(b=-a\).

Si \(b=-a\), entonces:

\[
a-b = 2a,\qquad a^4+b^4 = 2a^4,
\]

y la expresión queda

\[
\frac{2a}{2a^4+96}=\frac{a}{a^4+48}.
\]

Maximicemos \(g(a)=\dfrac{a}{a^4+48}\) para \(a>0\). Derivando:

\[
g'(a)=\frac{(a^4+48)-a(4a^3)}{(a^4+48)^2}
=\frac{48-3a^4}{(a^4+48)^2}.
\]

Igualamos a cero:

\[
48-3a^4=0 \implies a^4=16 \implies a=2.
\]

Entonces \(b=-2\), y el valor es

\[
g(2)=\frac{2}{16+48}=\frac{2}{64}=\frac{1}{32}.
\]

Por tanto, el máximo es

\[
\boxed{\frac{1}{32}}.
\]

*Justificación adicional de optimalidad:* se puede demostrar mediante la desigualdad

\[
a-b\le \frac{a^4+b^4+96}{32},
\]

equivalente a

\[
32(a-b)\le a^4+b^4+96.
\]

Esta desigualdad puede escribirse como

\[
(a^4-32a+64)+(b^4+32b+32)\ge 0,
\]

o, completando factores, se verifica que su mínimo se alcanza justamente en \(a=2,\, b=-2\). Por lo tanto, el valor máximo global es efectivamente \(\frac{1}{32}\).