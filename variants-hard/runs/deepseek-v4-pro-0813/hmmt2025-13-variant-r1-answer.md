Cada frasco debe contener un conjunto de 4 etiquetas sin elementos aislados respecto a la recta \(1,2,\dots,20\). Así, dentro de un frasco solo hay dos tipos posibles:

- **Tipo A:** 4 etiquetas consecutivas (1 tramo de longitud 4).
- **Tipo B:** dos pares de etiquetas consecutivas, separados (2 tramos de longitud 2).

Sea \(b\) el número de frascos de tipo B y \(a=5-b\) los de tipo A. El número total de tramos consecutivos es

\[
a+2b=5+b.
\]

Además, dos tramos adyacentes pertenecen siempre a frascos distintos.

Contamos primero etiquetando los frascos y luego dividimos entre \(5!\).

Para \(b\) fijo, elegimos cuáles \(b\) colores son de tipo B: \(\binom{5}{b}\). Ahora contamos las palabras de longitud \(5+b\) donde \(b\) letras aparecen dos veces y las otras \(5-b\) aparecen una vez, sin letras iguales adyacentes.

Por inclusión-exclusión sobre los pares cuyas dos copias quedan juntas:

\[
W_b=\sum_{j=0}^{b}(-1)^j\binom{b}{j}\frac{(5+b-j)!}{2^{\,b-j}}.
\]

Obtenemos:

\[
\begin{aligned}
W_0&=120,\\
W_1&=240,\\
W_2&=660,\\
W_3&=2220,\\
W_4&=8760,\\
W_5&=39480.
\end{aligned}
\]

Entonces el número de formas con frascos etiquetados es

\[
\sum_{b=0}^{5}\binom{5}{b}W_b
=120+5\cdot240+10\cdot660+10\cdot2220+5\cdot8760+39480
=113400.
\]

Como los frascos son indistinguibles, dividimos entre \(5!\):

\[
\frac{113400}{5!}=\frac{113400}{120}=945.
\]

\[
\boxed{945}
\]