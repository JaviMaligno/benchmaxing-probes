Sea \(n\) el número de monedas en cada una de las nueve bolsas originales. Antes de encontrar la bolsa adicional, tenías \(9n\) monedas.

1. Después del hallazgo, el total es \(9n+47\).
2. Para repartirlas equitativamente entre diez bolsas, este total debe ser múltiplo de \(10\):
   \[
   9n+47\equiv 0\pmod{10}\implies n\equiv 7\pmod{10}.
   \]
   Así, \(n\) puede ser \(7,17,27,37,\ldots\)
3. Los totales correspondientes tras el hallazgo son \(110,200,290,380,\ldots\). El primero que supera \(300\) es \(380\), obtenido con \(n=37\).

Por tanto, antes del hallazgo tenías \(9\cdot37=\boxed{333}\).