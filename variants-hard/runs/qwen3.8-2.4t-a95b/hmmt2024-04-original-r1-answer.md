

Sea

\[
f(x)=\frac{P(x)}{Q(x)},
\]

donde \(P\) y \(Q\) son polinomios cuadráticos. Como \(f(n)=n^3\) para \(n=1,2,3,4,5\), tenemos

\[
P(n)=n^3Q(n).
\]

Definamos

\[
H(x)=P(x)-x^3Q(x).
\]

Como \(P\) y \(Q\) son cuadráticos, \(H\) tiene grado a lo más \(5\), y además

\[
H(1)=H(2)=H(3)=H(4)=H(5)=0.
\]

Por tanto,

\[
H(x)=C(x-1)(x-2)(x-3)(x-4)(x-5)
\]

para alguna constante \(C\neq 0\).

Ahora,

\[
(x-1)(x-2)(x-3)(x-4)(x-5)
=x^5-15x^4+85x^3-225x^2+274x-120.
\]

Entonces

\[
P(x)-x^3Q(x)=C(x^5-15x^4+85x^3-225x^2+274x-120).
\]

Si \(Q(x)=ax^2+bx+c\), los términos de grado \(5,4,3\) del lado izquierdo provienen solo de \(-x^3Q(x)\). Comparando coeficientes:

\[
-a=C,\qquad -b=-15C,\qquad -c=85C.
\]

Así,

\[
Q(x)=C(-x^2+15x-85).
\]

Luego

\[
P(x)=C(-225x^2+274x-120).
\]

Por lo tanto,

\[
f(x)=\frac{-225x^2+274x-120}{-x^2+15x-85}
=\frac{225x^2-274x+120}{x^2-15x+85}.
\]

Finalmente,

\[
f(0)=\frac{120}{85}=\frac{24}{17}.
\]

\[
\boxed{\frac{24}{17}}
\]