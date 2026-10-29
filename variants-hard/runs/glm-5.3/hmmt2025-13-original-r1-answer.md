Primero etiquetemos provisionalmente las cajas como \(A,B,C,D\).

Una colocación es entonces una palabra de longitud \(16\) en la que cada letra aparece \(4\) veces. La condición de vecinos dice que cada tramo maximal de letras consecutivas iguales tiene longitud al menos \(2\). Como cada letra aparece \(4\) veces, cada caja es de una de estas dos formas:

- un solo tramo de longitud \(4\), o
- dos tramos de longitud \(2\).

Sea \(k\) el número de letras que aparecen en dos tramos. Entonces hay \(4+k\) tramos en total. Elegimos esas \(k\) letras de \(4\) formas posibles en \(\binom{4}{k}\) maneras.

Para un valor fijo de \(k\), contamos las palabras de tramos en que \(k\) letras aparecen dos veces y \(4-k\) letras una vez, con tramos vecinos distintos. Por inclusión-exclusión, si forzamos \(j\) de las letras repetidas a quedar adyacentes, se fusionan en bloques, lo que da

\[
N_k=\sum_{j=0}^{k}(-1)^j\binom{k}{j}\frac{(4+k-j)!}{2!^{\,k-j}}.
\]

Los valores son:

\[
\begin{array}{c|c|c}
k & N_k & \binom{4}{k}N_k\\
\hline
0 & 24 & 24\\
1 & 36 & 144\\
2 & 84 & 504\\
3 & 246 & 984\\
4 & 864 & 864
\end{array}
\]

Sumando:

\[
24+144+504+984+864=2520.
\]

Estas son colocaciones con cajas etiquetadas. Como las cajas son indistinguibles, dividimos entre \(4!\):

\[
\frac{2520}{24}=105.
\]

\[
\boxed{105}
\]