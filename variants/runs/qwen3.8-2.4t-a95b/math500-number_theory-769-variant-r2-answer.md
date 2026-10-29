

Calculamos módulo \(11\):

\[
117 \equiv 7 \pmod{11}, \qquad 194 \equiv 7 \pmod{11}
\]

Entonces:

\[
117^{36}+194^{38} \equiv 7^{36}+7^{38} \pmod{11}
\]

Factorizamos:

\[
7^{36}+7^{38}=7^{36}(1+7^2)
\]

Como \(7^2=49\equiv 5\pmod{11}\), tenemos:

\[
1+7^2 \equiv 1+5=6 \pmod{11}
\]

Ahora calculamos \(7^{36}\pmod{11}\). Por el pequeño teorema de Fermat, \(7^{10}\equiv 1\pmod{11}\). Como \(36\equiv 6\pmod{10}\),

\[
7^{36}\equiv 7^6\pmod{11}
\]

Calculamos:

\[
7^2\equiv 5,\quad 7^4\equiv 5^2=25\equiv 3,\quad 7^6\equiv 7^4\cdot 7^2\equiv 3\cdot 5=15\equiv 4
\]

Por tanto:

\[
7^{36}+7^{38}\equiv 4\cdot 6=24\equiv 2\pmod{11}
\]

\[
\boxed{2}
\]