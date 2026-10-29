Sea \(H\) el subgrupo de \(\mathbb F_2^n\) generado por los vectores de peso \(k\). Como el grafo es una unión de clases laterales de \(H\),

\[
d_{n,k}=\frac{2^n}{|H|}.
\]

Analicemos \(H\):

- Si \(k<n\), para cada par \(i\neq j\) podemos elegir un vector \(v\) de peso \(k\) que tenga un \(1\) en la posición \(i\) y un \(0\) en la posición \(j\). Cambiando ese \(1\) por un \(0\) y ese \(0\) por un \(1\) se obtiene otro vector \(v'\) de peso \(k\), y

\[
v+v'=e_i+e_j.
\]

Así, \(H\) contiene todos los vectores de peso \(2\), es decir, contiene el subespacio de los vectores de peso par.

- Si \(k\) es par y \(k<n\), todos los generadores tienen peso par, luego \(H\) es exactamente el subespacio de peso par, de dimensión \(n-1\). Entonces

\[
d_{n,k}=2.
\]

- Si \(k\) es impar y \(k<n\), además del subespacio de peso par hay un generador de peso impar, así que \(H=\mathbb F_2^n\) y

\[
d_{n,k}=1.
\]

- Si \(k=n\), el único vector de peso \(n\) es \((1,1,\dots,1)\), luego \(H=\{0,(1,\dots,1)\}\), y

\[
d_{n,k}=2^{n-1}.
\]

Para cada \(n\), la suma interna es:

- Si \(n=2m\):

\[
m\cdot 1+(m-1)\cdot 2+2^{2m-1}=3m-2+2^{2m-1}.
\]

- Si \(n=2m+1\):

\[
m\cdot 1+m\cdot 2+2^{2m}=3m+2^{2m}.
\]

Calculando para \(n=1,\dots,12\):

\[
1,3,7,12,22,39,73,138,268,525,1039,2064.
\]

Sumando:

\[
1+3+7+12+22+39+73+138+268+525+1039+2064=4191.
\]

\[
\boxed{4191}
\]