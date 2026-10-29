

Sea \(t=a-b\). Como el denominador \(a^4+b^4+96\) es siempre positivo, si \(t\le 0\) la expresión es \(\le 0\), mientras que tomando por ejemplo \(a=1,b=0\) es positiva. Así que el máximo se alcanza con \(t>0\).

Primero acotamos el denominador en términos de \(t\). Tenemos

\[
(a-b)^2 \le 2(a^2+b^2)
\]

y además

\[
(a^2+b^2)^2 \le 2(a^4+b^4).
\]

Elevando al cuadrado la primera desigualdad y usando la segunda,

\[
(a-b)^4 \le 4(a^2+b^2)^2 \le 8(a^4+b^4).
\]

Por tanto,

\[
a^4+b^4 \ge \frac{(a-b)^4}{8}=\frac{t^4}{8}.
\]

Entonces, como \(t>0\),

\[
\frac{a-b}{a^4+b^4+96}
\le
\frac{t}{\frac{t^4}{8}+96}.
\]

Ahora aplicamos AM-GM:

\[
\frac{t^4}{8}+96
=
\frac{t^4}{8}+32+32+32
\ge
4\sqrt[4]{\frac{t^4}{8}\cdot 32^3}.
\]

Como

\[
\frac{32^3}{8}=4096=8^4,
\]

se obtiene

\[
\frac{t^4}{8}+96 \ge 4\sqrt[4]{4096t^4}=32t.
\]

Luego

\[
\frac{t}{\frac{t^4}{8}+96}\le \frac{t}{32t}=\frac1{32}.
\]

La igualdad ocurre cuando \(a=-b\) y \(t=4\), es decir, \(a=2\), \(b=-2\). En efecto,

\[
\frac{2-(-2)}{2^4+(-2)^4+96}
=
\frac{4}{16+16+96}
=
\frac{4}{128}
=
\frac1{32}.
\]

\[
\boxed{\frac{1}{32}}
\]