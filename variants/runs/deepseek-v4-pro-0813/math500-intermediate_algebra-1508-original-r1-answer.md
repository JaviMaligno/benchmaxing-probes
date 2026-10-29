Vamos a resolverlo paso a paso.

La recurrencia es

\[
a_{i+1} = \frac{1}{1 - a_i}.
\]

Queremos que \(a_3 = a_1\).

Primero calculemos las primeras iteraciones:

\[
a_2 = \frac{1}{1 - a_1}.
\]

\[
a_3 = \frac{1}{1 - a_2}
= \frac{1}{1 - \frac{1}{1 - a_1}}
= \frac{1 - a_1}{-a_1}
= \frac{a_1 - 1}{a_1}.
\]

La condición \(a_3 = a_1\) da

\[
\frac{a_1 - 1}{a_1} = a_1.
\]

Multiplicamos por \(a_1\):

\[
a_1 - 1 = a_1^2.
\]

Es decir,

\[
a_1^2 - a_1 + 1 = 0.
\]

Por tanto,

\[
a_1 = \frac{1 \pm i\sqrt{3}}{2}.
\]

Estos valores tienen la propiedad de que son raíces cúbicas de \(-1\), y satisfacen

\[
a_1^3 = -1.
\]

Como la recurrencia tiene periodo 3 cuando \(a_3 = a_1\), se cumple que

\[
a_9 = a_3 = a_1.
\]

Entonces:

\[
(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1.
\]

Por lo tanto,

\[
\boxed{-1}
\]