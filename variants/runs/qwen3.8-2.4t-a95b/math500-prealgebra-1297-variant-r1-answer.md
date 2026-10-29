

Los ceros al final de un factorial provienen de los factores \(10 = 2 \cdot 5\). En \(47!\) hay más factores de \(2\) que de \(5\), así que basta contar cuántas veces aparece el factor \(5\).

Contamos los múltiplos de \(5\) hasta \(47\):

\[
\left\lfloor \frac{47}{5} \right\rfloor = 9
\]

También contamos los múltiplos de \(25\), porque aportan un factor \(5\) extra:

\[
\left\lfloor \frac{47}{25} \right\rfloor = 1
\]

Total de factores \(5\):

\[
9 + 1 = 10
\]

Por lo tanto, el número de ceros al final de \(47!\) es

\[
\boxed{10}
\]