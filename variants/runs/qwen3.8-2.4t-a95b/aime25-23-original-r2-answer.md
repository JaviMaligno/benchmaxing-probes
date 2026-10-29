

Sea \(N=25q+r\), con \(0\le r<25\). El algoritmo codicioso toma \(q\) monedas de \(25\) centavos y luego forma el resto \(r\) usando monedas de \(10\) y \(1\) centavos.

Para una cantidad \(A\) usando solo monedas de \(10\) y \(1\), el número mínimo de monedas es

\[
h(A)=\left\lfloor \frac{A}{10}\right\rfloor+(A\bmod 10).
\]

Así, el número de monedas que da el algoritmo codicioso es

\[
C_0=q+h(r).
\]

Cualquier otra colección puede tener menos monedas de \(25\). Si quitamos \(k\) monedas de \(25\), entonces debemos formar \(25k+r\) con monedas de \(10\) y \(1\), dando

\[
C_k=q-k+h(25k+r).
\]

Comparamos \(C_{k+1}\) con \(C_k\). Al añadir \(25\) a una cantidad \(A\):

- Si \(A\bmod 10\in\{0,1,2,3,4\}\), entonces \(h(A+25)=h(A)+7\).
- Si \(A\bmod 10\in\{5,6,7,8,9\}\), entonces \(h(A+25)=h(A)-2\).

Por tanto,

\[
C_{k+1}-C_k=-1+\bigl(h(A+25)-h(A)\bigr),
\]

que vale \(+6\) en el primer caso y \(-3\) en el segundo.

Como \(25k\bmod 10\) alterna entre \(0\) y \(5\), hay dos casos:

1. Si \(r\bmod 10\in\{0,1,2,3,4\}\), los cambios alternan \(+6,-3,+6,-3,\dots\). La suma acumulada siempre es positiva para \(k\ge1\), así que el algoritmo codicioso siempre tiene éxito.

2. Si \(r\bmod 10\in\{5,6,7,8,9\}\), el primer cambio es \(-3\). Así, si \(q\ge1\), quitar una moneda de \(25\) reduce el número total de monedas en \(3\), por lo que el algoritmo codicioso falla. Si \(q=0\), no hay monedas de \(25\) que quitar, así que tiene éxito.

Entonces fallan exactamente los \(N=25q+r\) con \(q\ge1\) y

\[
r\in\{5,6,7,8,9,15,16,17,18,19\}.
\]

Entre \(1\) y \(1000\):

- De \(1\) a \(24\), todos tienen éxito: \(24\) valores.
- Desde \(25\) hasta \(999\) hay \(39\) bloques completos de \(25\). En cada bloque fallan \(10\) valores, así que tienen éxito \(15\) valores por bloque: \(39\cdot 15=585\).
- \(1000=25\cdot 40+0\) tiene éxito: \(1\) valor.

Total:

\[
24+585+1=610.
\]

\[
\boxed{610}
\]