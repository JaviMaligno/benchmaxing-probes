Sea \(n\) el número de monedas en cada una de las siete bolsas originales. Antes de encontrar la bolsa adicional, tenías \(7n\) monedas; después, \(7n+53\).

Para repartirlas equitativamente entre ocho bolsas:
\[
7n+53\equiv 0\pmod 8.
\]
Como \(53\equiv5\pmod8\) y \(7\equiv-1\pmod8\), obtenemos \(n\equiv5\pmod8\). Así, los totales posibles son:
\[
88,\quad144,\quad200,\quad256,\ldots
\]
El primer total estrictamente mayor que \(200\) es \(256\), que permite ocho bolsas de \(32\) monedas. Por tanto, inicialmente tenías:
\[
256-53=\boxed{203}
\]