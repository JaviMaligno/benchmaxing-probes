

Trabajamos módulo \(11\):

\[
117 \equiv 7 \pmod{11}, \qquad 194 \equiv 7 \pmod{11}
\]

Entonces:

\[
117^{36}+194^{38} \equiv 7^{36}+7^{38} \pmod{11}
\]

Por el pequeño teorema de Fermat, como \(11\) es primo y \(7\) no es múltiplo de \(11\):

\[
7^{10} \equiv 1 \pmod{11}
\]

Reducimos los exponentes módulo \(10\):

\[
36 \equiv 6 \pmod{10}, \qquad 38 \equiv 8 \pmod{10}
\]

Así que:

\[
7^{36} \equiv 7^6 \pmod{11}, \qquad 7^{38} \equiv 7^8 \pmod{11}
\]

Calculamos potencias:

\[
7^2 = 49 \equiv 5 \pmod{11}
\]

\[
7^4 \equiv 5^2 = 25 \equiv 3 \pmod{11}
\]

\[
7^6 = 7^4 \cdot 7^2 \equiv 3 \cdot 5 = 15 \equiv 4 \pmod{11}
\]

\[
7^8 = 7^6 \cdot 7^2 \equiv 4 \cdot 5 = 20 \equiv 9 \pmod{11}
\]

Finalmente:

\[
117^{36}+194^{38} \equiv 4+9 = 13 \equiv 2 \pmod{11}
\]

\[
\boxed{2}
\]