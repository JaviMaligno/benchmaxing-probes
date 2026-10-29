

Supongamos que el orden de la baraja es uniformemente aleatorio. Los palos no importan: solo importa la secuencia de valores, con cuatro cartas de cada valor \(2,3,4\).

Llamemos **racha** a un bloque consecutivo maximal de cartas del mismo valor. En una racha de longitud \(L\), el proceso produce exactamente \(\lfloor L/2\rfloor\) retiros: el primer doble se forma entre las cartas 1 y 2 de la racha, el siguiente posible entre las cartas 3 y 4, etc. Una carta impar sobrante no produce un retiro extra.

Como cada valor aparece 4 veces, las longitudes posibles de racha son \(1,2,3,4\).

Sea \(D\) el número total de pares adyacentes iguales en la baraja original. En una racha de longitud \(L\), hay \(L-1\) pares adyacentes iguales. Comparando con los retiros:

\[
\begin{array}{c|cccc}
L & 1 & 2 & 3 & 4\\
\hline
L-1 & 0 & 1 & 2 & 3\\
\lfloor L/2\rfloor & 0 & 1 & 1 & 2
\end{array}
\]

La diferencia es \(1\) exactamente cuando la racha tiene longitud \(3\) o \(4\). Si \(R\) es el número de rachas de longitud al menos \(3\), entonces

\[
N = D - R.
\]

Ahora calculamos las esperanzas.

Para cualquier par de posiciones adyacentes, la probabilidad de que tengan el mismo valor es

\[
\frac{3}{11},
\]

pues fijada la primera carta, quedan \(3\) cartas de su mismo valor entre las \(11\) restantes. Hay \(11\) pares adyacentes, así que

\[
\mathbb{E}[D]=11\cdot \frac{3}{11}=3.
\]

Para \(\mathbb{E}[R]\), fijemos un valor, por ejemplo el \(2\). Sus cuatro posiciones forman un subconjunto uniforme de tamaño \(4\) entre las \(12\) posiciones; hay \(\binom{12}{4}=495\) posibilidades.

Una racha de \(2\)’s de longitud al menos \(3\) comienza en \(i\in\{1,\dots,10\}\) si las posiciones \(i,i+1,i+2\) son \(2\)’s y, si \(i>1\), la posición \(i-1\) no lo es.

- Si \(i=1\), la cuarta carta de valor \(2\) puede estar en cualquiera de las posiciones \(4,\dots,12\): \(9\) opciones.
- Si \(i=2,\dots,10\), la posición \(i-1\) está prohibida y las posiciones \(i,i+1,i+2\) están ocupadas; quedan \(8\) opciones para la cuarta carta. Hay \(9\) tales valores de \(i\).

Por tanto, para un valor fijo,

\[
\mathbb{E}[\text{rachas de longitud }\ge 3]
=
\frac{9+9\cdot 8}{495}
=
\frac{81}{495}
=
\frac{9}{55}.
\]

Como hay tres valores,

\[
\mathbb{E}[R]=3\cdot \frac{9}{55}=\frac{27}{55}.
\]

Finalmente,

\[
\mathbb{E}[N]
=
\mathbb{E}[D]-\mathbb{E}[R]
=
3-\frac{27}{55}
=
\frac{138}{55}.
\]

\[
\boxed{\frac{138}{55}}
\]