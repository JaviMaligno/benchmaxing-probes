

Sea \(n\) el entero buscado. Las condiciones son:

\[
n \equiv 5 \pmod{7}, \qquad n \equiv 10 \pmod{11}, \qquad n \equiv 10 \pmod{13}.
\]

Como \(11\) y \(13\) son coprimos, las dos últimas condiciones se combinan en

\[
n \equiv 10 \pmod{143}.
\]

Así, \(n = 10 + 143k\) para algún entero \(k\).

Ahora imponemos la condición módulo \(7\):

\[
10 + 143k \equiv 5 \pmod{7}.
\]

Como \(10 \equiv 3 \pmod{7}\) y \(143 \equiv 3 \pmod{7}\), tenemos

\[
3 + 3k \equiv 5 \pmod{7},
\]

\[
3k \equiv 2 \pmod{7}.
\]

El inverso de \(3\) módulo \(7\) es \(5\), así que

\[
k \equiv 2 \cdot 5 \equiv 10 \equiv 3 \pmod{7}.
\]

Por tanto, \(k = 3 + 7t\), y

\[
n = 10 + 143(3 + 7t) = 439 + 1001t.
\]

Queremos el mayor \(n < 2010\). Probando valores:

\[
t=1 \implies n = 439 + 1001 = 1440,
\]

\[
t=2 \implies n = 2441 > 2010.
\]

Por lo tanto, el mayor entero menor que \(2010\) que cumple las condiciones es

\[
\boxed{1440}
\]