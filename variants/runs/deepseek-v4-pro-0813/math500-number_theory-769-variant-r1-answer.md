Vamos a reducir cada base módulo \(11\):

- \(117 = 11\cdot 10 + 7\), así que
  \[
  117^{36} \equiv 7^{36} \pmod{11}.
  \]
- \(194 = 11\cdot 17 + 7\), así que
  \[
  194^{38} \equiv 7^{38} \pmod{11}.
  \]

Por lo tanto,

\[
117^{36}+194^{38} \equiv 7^{36}+7^{38} \pmod{11}.
\]

Factorizamos:

\[
7^{36}+7^{38}=7^{36}(1+7^2)=7^{36}(1+49)=7^{36}\cdot 50.
\]

Reducimos módulo \(11\):

\[
50 \equiv 6 \pmod{11}.
\]

Ahora usamos el pequeño teorema de Fermat. Como \(11\) es primo y \(7\nmid 11\),

\[
7^{10}\equiv 1 \pmod{11}.
\]

Entonces,

\[
7^{36}=7^{30}\cdot 7^6 \equiv 1\cdot 7^6 \pmod{11}.
\]

Calculamos \(7^6\pmod{11}\):

\[
7^2=49\equiv 5,
\]
\[
7^4\equiv 5^2=25\equiv 3,
\]
\[
7^6=7^4\cdot 7^2\equiv 3\cdot 5=15\equiv 4 \pmod{11}.
\]

Por tanto,

\[
7^{36}\equiv 4 \pmod{11},
\]

y

\[
7^{36}\cdot 50 \equiv 4\cdot 6=24\equiv 2 \pmod{11}.
\]

El residuo es:

\[
\boxed{2}
\]