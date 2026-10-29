

Sea \(n\) el entero buscado. Las condiciones son:

\[
n \equiv 2 \pmod{7}, \qquad n \equiv 8 \pmod{11}, \qquad n \equiv 8 \pmod{13}.
\]

Como \(n\) deja resto \(8\) al dividirlo entre \(11\) y entre \(13\), y \(11\) y \(13\) son coprimos, tenemos

\[
n \equiv 8 \pmod{11\cdot 13} = 8 \pmod{143}.
\]

Entonces \(n = 8 + 143k\) para algún entero \(k\).

Ahora imponemos la condición módulo \(7\):

\[
8 + 143k \equiv 2 \pmod{7}.
\]

Como \(8 \equiv 1 \pmod{7}\) y \(143 \equiv 3 \pmod{7}\), queda

\[
1 + 3k \equiv 2 \pmod{7},
\]

\[
3k \equiv 1 \pmod{7}.
\]

El inverso de \(3\) módulo \(7\) es \(5\), así que

\[
k \equiv 5 \pmod{7}.
\]

Por tanto, \(k = 5 + 7t\), y

\[
n = 8 + 143(5 + 7t) = 723 + 1001t.
\]

Queremos el mayor \(n < 3000\). Probando valores de \(t\):

\[
t=2 \implies n = 723 + 2002 = 2725,
\]

\[
t=3 \implies n = 3726 > 3000.
\]

Así que el mayor entero menor que \(3000\) que cumple las condiciones es

\[
\boxed{2725}
\]