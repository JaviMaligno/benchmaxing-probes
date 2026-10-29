Modelamos las 16 sillas como una secuencia binaria de longitud 16, con 8 sillas seleccionadas (1) y 8 no seleccionadas (0).

La condición «ninguna persona se sienta junto a otras dos personas» prohíbe que haya **tres sillas seleccionadas consecutivas**, es decir, evita el bloque `111`.

Colocamos primero las 8 sillas no seleccionadas:

\[
\_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_
\]

Esto crea **9 huecos** (incluidos los extremos). Las 8 sillas seleccionadas deben repartirse entre esos 9 huecos, con a lo sumo **2 sillas por hueco**, para evitar tres seleccionadas seguidas.

Debemos contar las soluciones de

\[
x_0+x_1+\cdots+x_8=8,\qquad 0\le x_i\le 2.
\]

El número de soluciones es el coeficiente de \(x^8\) en

\[
(1+x+x^2)^9.
\]

Elegimos \(j\) huecos con 2 sillas y \(8-2j\) huecos con 1 silla:

\[
\sum_{j=0}^{4} \frac{9!}{j!(8-2j)!(1+j)!}
= 9+252+1260+1260+126
= 2907.
\]

Por lo tanto, \(N=2907\), y su resto al dividir entre \(1000\) es

\[
\boxed{907}
\]