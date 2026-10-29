Interpretamos cada subconjunto posible como una cadena binaria de longitud \(17\), con \(9\) unos (asientos ocupados) y \(8\) ceros (asientos vacíos).

La condición “ningún invitado está sentado junto a otros dos invitados” equivale a prohibir tres asientos ocupados consecutivos. En efecto, si hubiera tres ocupados seguidos, el del medio estaría junto a otros dos invitados.

Primero colocamos los \(8\) asientos vacíos. Estos crean \(9\) espacios o huecos: antes del primer vacío, entre vacíos consecutivos, y después del último vacío.

En cada hueco podemos colocar \(0\), \(1\) o \(2\) asientos ocupados; no podemos colocar \(3\), porque formarían tres ocupados consecutivos. Así, debemos repartir \(9\) asientos ocupados entre \(9\) huecos, con capacidad máxima \(2\) por hueco.

El número pedido es el coeficiente de \(x^9\) en

\[
(1+x+x^2)^9.
\]

Usamos inclusión-exclusión. Sin el límite superior, el número de soluciones no negativas de

\[
a_1+\cdots+a_9=9
\]

es

\[
\binom{17}{8}.
\]

Restamos los casos donde algún \(a_i\ge 3\), sumamos los casos donde dos variables son \(\ge 3\), etc.:

\[
N=\binom{17}{8}-\binom{9}{1}\binom{14}{8}
+\binom{9}{2}\binom{11}{8}
-\binom{9}{3}\binom{8}{8}.
\]

Calculamos:

\[
\binom{17}{8}=24310,
\]

\[
\binom{9}{1}\binom{14}{8}=9\cdot 3003=27027,
\]

\[
\binom{9}{2}\binom{11}{8}=36\cdot 165=5940,
\]

\[
\binom{9}{3}\binom{8}{8}=84\cdot 1=84.
\]

Entonces

\[
N=24310-27027+5940-84=3139.
\]

Finalmente,

\[
3139 \equiv 139 \pmod{1000}.
\]

\[
\boxed{139}
\]