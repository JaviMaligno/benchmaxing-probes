Vamos a calcular paso a paso.

Primero reducimos cada base módulo \(11\):

- \(129 \div 11 = 11\) con resto \(8\), así que
  \[
  129 \equiv 8 \pmod{11}.
  \]

- \(96 \div 11 = 8\) con resto \(8\), así que
  \[
  96 \equiv 8 \pmod{11}.
  \]

Por lo tanto,
\[
129^{34}+96^{38} \equiv 8^{34}+8^{38} \pmod{11}.
\]

Sacamos factor común:
\[
8^{34}+8^{38}=8^{34}(1+8^4).
\]

Calculamos \(8^4 \pmod{11}\):
\[
8^2=64 \equiv 9 \pmod{11},
\]
\[
8^4=(8^2)^2 \equiv 9^2=81 \equiv 4 \pmod{11}.
\]

Entonces
\[
1+8^4 \equiv 1+4=5 \pmod{11}.
\]

Ahora falta \(8^{34} \pmod{11}\). Por el pequeño teorema de Fermat, como \(11\) es primo y \(11\nmid 8\),
\[
8^{10}\equiv 1 \pmod{11}.
\]

Entonces
\[
8^{34}=8^{30}\cdot 8^4=(8^{10})^3\cdot 8^4 \equiv 1^3\cdot 4=4 \pmod{11}.
\]

Finalmente,
\[
8^{34}(1+8^4)\equiv 4\cdot 5=20\equiv 9 \pmod{11}.
\]

Por lo tanto, el residuo es:

\[
\boxed{9}
\]