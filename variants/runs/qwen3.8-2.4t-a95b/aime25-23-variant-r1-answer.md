

Sea \(N=24q+r\), con \(0\le r<24\). El algoritmo voraz toma \(q\) monedas de \(24\) y luego completa \(r\) usando monedas de \(10\) y \(1\).

Para monedas de \(1\) y \(10\), el mínimo número de monedas para formar \(m\) es

\[
c(m)=\left\lfloor \frac m{10}\right\rfloor+(m\bmod 10).
\]

Así, el número de monedas del algoritmo voraz es

\[
G=q+c(r).
\]

Cualquier otra colección debe usar \(q-k\) monedas de \(24\), para algún \(k\ge 0\), y luego formar \(r+24k\) con monedas de \(10\) y \(1\). Su número de monedas es

\[
C_k=q-k+c(r+24k).
\]

Queremos saber cuándo \(C_k\ge C_0\) para todo \(k\le q\).

Al pasar de \(k-1\) a \(k\), añadimos \(24\) al resto y quitamos una moneda de \(24\). Si el último dígito decimal del resto es \(0,1,2,3,4,5\), entonces \(c\) aumenta en \(6\), por lo que la diferencia neta es \(+5\). Si el último dígito es \(6,7,8,9\), entonces \(c\) disminuye en \(3\), por lo que la diferencia neta es \(-4\).

Como el último dígito aumenta en \(4\) módulo \(10\) en cada paso, basta revisar los primeros cinco pasos. Si \(s=r\bmod 10\), las diferencias acumuladas \(D_k=C_k-C_0\) para \(k=1,\dots,5\) son:

\[
\begin{array}{c|c}
s & D_1,D_2,D_3,D_4,D_5\\ \hline
0,1 & 5,10,6,11,7\\
2,3 & 5,1,6,11,7\\
4,5 & 5,1,6,2,7\\
6,7 & -4,1,6,2,7\\
8,9 & -4,1,-3,2,7
\end{array}
\]

Además, cada 5 pasos se añaden \(120\) centavos, es decir, \(12\) monedas de \(10\), mientras que se quitan \(5\) monedas de \(24\), así que

\[
D_{k+5}=D_k+7.
\]

Por tanto:

- Si \(r\bmod 10\in\{0,1,2,3,4,5\}\), todas las diferencias son no negativas: el algoritmo voraz tiene éxito.
- Si \(r\bmod 10\in\{6,7,8,9\}\) y \(q\ge 1\), ya \(D_1=-4<0\): el algoritmo voraz falla.

Para \(q=0\), es decir \(N<24\), no hay monedas de \(24\) disponibles, así que todos esos casos tienen éxito.

Los residuos malos en un bloque completo de \(24\) son

\[
r\in\{6,7,8,9,16,17,18,19\},
\]

es decir, \(8\) fallos por bloque.

Ahora contamos entre \(1\) y \(1000\). Como

\[
1000=24\cdot 41+16,
\]

hay \(40\) bloques completos con \(q=1,\dots,40\), aportando

\[
40\cdot 8=320
\]

fallos. En el bloque parcial \(q=41\), con \(r=0,\dots,16\), los residuos malos son \(6,7,8,9,16\), aportando \(5\) fallos más.

Total de fallos:

\[
320+5=325.
\]

Por tanto, el número de valores de \(N\) para los cuales el algoritmo voraz tiene éxito es

\[
1000-325=675.
\]

\[
\boxed{675}
\]