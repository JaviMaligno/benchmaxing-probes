La sucesión está definida por la recurrencia

\[
b_{k+1} = -\frac{1}{1+b_k}.
\]

Aplicamos la recurrencia dos veces para relacionar \(b_3\) con \(b_1\):

\[
b_2 = -\frac{1}{1+b_1}.
\]

\[
b_3 = -\frac{1}{1+b_2}
     = -\frac{1}{1 - \frac{1}{1+b_1}}.
\]

Simplificamos el denominador:

\[
1 - \frac{1}{1+b_1}
= \frac{(1+b_1)-1}{1+b_1}
= \frac{b_1}{1+b_1}.
\]

Por lo tanto,

\[
b_3 = -\frac{1}{\frac{b_1}{1+b_1}}
     = -\frac{1+b_1}{b_1}
     = -1 - \frac{1}{b_1}.
\]

La condición es \(b_3 = b_1\), así que:

\[
-1 - \frac{1}{b_1} = b_1.
\]

Multiplicamos por \(b_1\):

\[
-b_1 - 1 = b_1^2.
\]

Es decir,

\[
b_1^2 + b_1 + 1 = 0.
\]

Por tanto,

\[
b_1 = \frac{-1 \pm i\sqrt{3}}{2}.
\]

Además, \(b_1^3 = 1\) porque \(b_1\) es una raíz cúbica primitiva de la unidad.

Por otro lado, la recurrencia tiene periodo \(3\). En efecto:

\[
b_4 = b_1,\qquad b_5 = b_2,\qquad b_6 = b_3,
\]

y así sucesivamente. Por lo tanto \(b_k = b_{k+3}\) para todo \(k\), de modo que

\[
b_9 = b_6 = b_3 = b_1.
\]

Entonces,

\[
(b_9)^9 = (b_1)^9 = (b_1^3)^3 = 1^3 = 1.
\]

Por lo tanto, la respuesta es:

\[
\boxed{1}
\]