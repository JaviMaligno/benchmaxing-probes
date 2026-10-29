El problema pide el mayor entero menor que \(3000\) que cumpla:

\[
x \equiv 2 \pmod{7}
\]
\[
x \equiv 8 \pmod{11}
\]
\[
x \equiv 8 \pmod{13}
\]

**Paso 1: combinar las dos últimas congruencias.**

Como \(\text{mcd}(11,13)=1\), las condiciones \(x \equiv 8 \pmod{11}\) y \(x \equiv 8 \pmod{13}\) equivalen a:

\[
x \equiv 8 \pmod{11\cdot 13}
\]

es decir,

\[
x \equiv 8 \pmod{143}.
\]

**Paso 2: resolver el sistema con la primera congruencia.**

Ahora tenemos:

\[
x \equiv 2 \pmod{7}
\]
\[
x \equiv 8 \pmod{143}.
\]

Escribimos \(x = 8 + 143k\). Como debe cumplir \(x \equiv 2 \pmod{7}\):

\[
8 + 143k \equiv 2 \pmod{7}.
\]

Como \(8 \equiv 1 \pmod{7}\), la congruencia queda:

\[
1 + k \equiv 2 \pmod{7},
\]

por lo tanto:

\[
k \equiv 1 \pmod{7}.
\]

Entonces \(k = 1 + 7t\), y:

\[
x = 8 + 143(1 + 7t) = 151 + 1001t.
\]

**Paso 3: hallar la solución general.**

Así,

\[
x \equiv 151 \pmod{1001}.
\]

**Paso 4: encontrar el mayor valor menor que \(3000\).**

Buscamos el mayor \(t\) tal que:

\[
151 + 1001t < 3000.
\]

Probamos valores:

- \(t = 2\): \(151 + 2002 = 2153\),
- \(t = 3\): \(151 + 3003 = 3154\), que supera \(3000\).

Por lo tanto, el mayor valor válido es \(2153\).

Final:

\[
\boxed{2153}
\]