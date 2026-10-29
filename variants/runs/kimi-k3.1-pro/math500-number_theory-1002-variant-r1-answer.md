Como el número deja resto \(8\) al dividirlo tanto por \(11\) como por \(13\), debe cumplir
\[
n\equiv 8\pmod{143},
\]
porque \(11\cdot13=143\). Así, \(n=143k+8\).

Imponiendo la condición módulo \(7\):
\[
143k+8\equiv 3k+1\equiv2\pmod7
\quad\Rightarrow\quad
3k\equiv1\pmod7
\quad\Rightarrow\quad
k\equiv5\pmod7.
\]
Por tanto, \(k=7t+5\), y
\[
n=143(7t+5)+8=1001t+723.
\]

El mayor valor menor que \(3000\) se obtiene con \(t=2\):
\[
n=1001\cdot2+723=2725.
\]
Comprobación: \(2725\) deja restos \(2\), \(8\) y \(8\) al dividirlo por \(7\), \(11\) y \(13\), respectivamente.

\[
\boxed{2725}
\]