Sea \( x \) el número de monedas en cada una de las siete bolsas originales. Entonces, antes de encontrar la bolsa de 53 monedas, tenías \( 7x \) monedas.

Después de encontrar la bolsa, tienes un total de \( 7x + 53 \) monedas. Al redistribuirlas en ocho bolsas con la misma cantidad, esa cantidad debe ser un número entero, por lo que:

\[
7x + 53 \equiv 0 \pmod{8}
\]

Como \( 7 \equiv -1 \pmod{8} \) y \( 53 \equiv 5 \pmod{8} \), tenemos:

\[
-x + 5 \equiv 0 \pmod{8} \implies x \equiv 5 \pmod{8}
\]

Además, el total debe ser mayor que 200:

\[
7x + 53 > 200 \implies 7x > 147 \implies x > 21
\]

Buscamos el menor \( x > 21 \) tal que \( x \equiv 5 \pmod{8} \).

Probando valores: \( x = 29 \) cumple, pues \( 29 \equiv 5 \pmod{8} \) y \( 29 > 21 \).

Por lo tanto, antes de encontrar la bolsa tenías:

\[
7x = 7 \cdot 29 = 203
\]

Comprobación: \( 203 + 53 = 256 = 8 \cdot 32 \), y \( 203 > 200 \).

\[
\boxed{203}
\]