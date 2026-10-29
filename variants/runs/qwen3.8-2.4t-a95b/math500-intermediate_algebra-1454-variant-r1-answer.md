

Completamos el cuadrado en el tercer radical:

\[
a^2+b^2-70a-80b+2825=(35-a)^2+(40-b)^2.
\]

Así, la expresión es

\[
E=\sqrt{a^2+225}+\sqrt{b^2+400}+\sqrt{(35-a)^2+(40-b)^2}.
\]

Usamos la desigualdad \((x+y)^2\le 2(x^2+y^2)\), válida para números reales, y que aquí los términos son no negativos.

1. Para el primer radical:

\[
(a+15)^2\le 2(a^2+15^2)=2(a^2+225),
\]

de donde

\[
\sqrt{a^2+225}\ge \frac{a+15}{\sqrt2}.
\]

2. Para el segundo radical:

\[
(b+20)^2\le 2(b^2+20^2)=2(b^2+400),
\]

de donde

\[
\sqrt{b^2+400}\ge \frac{b+20}{\sqrt2}.
\]

3. Para el tercer radical, como \(0\le a\le 35\) y \(0\le b\le 40\), tenemos \(35-a\ge 0\) y \(40-b\ge 0\). Entonces

\[
\bigl((35-a)+(40-b)\bigr)^2\le 2\bigl((35-a)^2+(40-b)^2\bigr),
\]

por lo que

\[
\sqrt{(35-a)^2+(40-b)^2}\ge \frac{75-a-b}{\sqrt2}.
\]

Sumando las tres desigualdades:

\[
E\ge \frac{a+15}{\sqrt2}+\frac{b+20}{\sqrt2}+\frac{75-a-b}{\sqrt2}
=\frac{110}{\sqrt2}=55\sqrt2.
\]

La igualdad ocurre cuando

\[
a=15,\qquad b=20,\qquad 35-a=40-b,
\]

lo cual se cumple con \(a=15\), \(b=20\), dentro del dominio dado.

Por lo tanto, el valor mínimo es

\[
\boxed{55\sqrt{2}}
\]