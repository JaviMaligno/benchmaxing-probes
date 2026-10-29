Factorizamos la expresión:

\[
12x^2-xy-6y^2=(4x-3y)(3x+2y).
\]

Como \(x\) y \(y\) son enteros, el producto es cero si y solo si uno de los factores es cero.

**Caso 1:** \(4x-3y=0\)

Entonces \(4x=3y\), de modo que las soluciones enteras son

\[
x=3k,\qquad y=4k
\]

para algún entero \(k\). Necesitamos

\[
-100\le 3k\le 100,\qquad -100\le 4k\le 100.
\]

La restricción más fuerte es \(|4k|\le 100\), así que

\[
|k|\le 25.
\]

Hay \(51\) valores posibles de \(k\): \(-25,-24,\dots,25\).

**Caso 2:** \(3x+2y=0\)

Entonces \(3x=-2y\), de modo que las soluciones enteras son

\[
x=-2k,\qquad y=3k
\]

para algún entero \(k\). Necesitamos

\[
-100\le 2k\le 100,\qquad -100\le 3k\le 100.
\]

La restricción más fuerte es \(|3k|\le 100\), así que

\[
|k|\le 33.
\]

Hay \(67\) valores posibles de \(k\): \(-33,-32,\dots,33\).

Ambos casos incluyen el par \((0,0)\), así que lo contamos dos veces. Por lo tanto, el número total de pares ordenados es

\[
51+67-1=117.
\]

\[
\boxed{117}
\]