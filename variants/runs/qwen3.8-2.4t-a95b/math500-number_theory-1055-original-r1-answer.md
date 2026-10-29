Sea \(n\) el número de monedas en cada una de las 7 bolsas originales. Entonces, antes de encontrar la bolsa extra, tengo \(7n\) monedas.

**Condición 1: redistribución equitativa en 8 bolsas**

Tras encontrar la bolsa de 53 monedas, el total es \(7n + 53\), y debe repartirse en partes iguales entre 8 bolsas:

\[
7n + 53 \equiv 0 \pmod{8}
\]

Como \(53 \equiv 5 \pmod{8}\) y \(7 \equiv -1 \pmod{8}\):

\[
-n + 5 \equiv 0 \pmod{8} \implies n \equiv 5 \pmod{8}
\]

Así que \(n \in \{5, 13, 21, 29, 37, \dots\}\).

**Condición 2: más de 200 monedas en total**

\[
7n + 53 > 200 \implies 7n > 147 \implies n > 21
\]

**Combinando ambas condiciones**

El menor \(n \geq 22\) con \(n \equiv 5 \pmod{8}\) es \(n = 29\) (notemos que \(n = 21\) cumple la congruencia, pero daría exactamente \(7\cdot21 + 53 = 200\), que **no** es mayor que 200).

**Verificación con \(n = 29\):**
- Monedas originales: \(7 \cdot 29 = 203\).
- Tras encontrar la bolsa: \(203 + 53 = 256\).
- Reparto en 8 bolsas: \(256 / 8 = 32\) monedas por bolsa. ✓
- \(256 > 200\). ✓

Por tanto, el menor número de monedas que podía tener antes de encontrar la bolsa es

\[
\boxed{203}
\]