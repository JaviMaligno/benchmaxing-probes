

Sea

\[
F(a,b)=\sqrt{a^2+225}+\sqrt{b^2+400}+\sqrt{a^2+b^2-70a-80b+2825}.
\]

Notemos que

\[
a^2+b^2-70a-80b+2825=(35-a)^2+(40-b)^2.
\]

Como \(0\le a\le 35\) y \(0\le b\le 40\), tenemos \(35-a\ge 0\) y \(40-b\ge 0\).

Usamos la desigualdad

\[
\sqrt{x^2+y^2}\ge \frac{x+y}{\sqrt2}
\]

para \(x,y\ge 0\), que se sigue de

\[
2(x^2+y^2)-(x+y)^2=(x-y)^2\ge 0.
\]

Aplicándola a cada término:

\[
\sqrt{a^2+15^2}\ge \frac{a+15}{\sqrt2},
\]

\[
\sqrt{b^2+20^2}\ge \frac{b+20}{\sqrt2},
\]

y

\[
\sqrt{(35-a)^2+(40-b)^2}\ge \frac{(35-a)+(40-b)}{\sqrt2}
=\frac{75-a-b}{\sqrt2}.
\]

Sumando las tres desigualdades:

\[
F(a,b)\ge \frac{a+15+b+20+75-a-b}{\sqrt2}
=\frac{110}{\sqrt2}=55\sqrt2.
\]

La igualdad ocurre cuando

\[
a=15,\qquad b=20,\qquad 35-a=40-b,
\]

lo cual se cumple para \((a,b)=(15,20)\), que está dentro del dominio.

Por lo tanto, el valor mínimo es

\[
\boxed{55\sqrt2}
\]