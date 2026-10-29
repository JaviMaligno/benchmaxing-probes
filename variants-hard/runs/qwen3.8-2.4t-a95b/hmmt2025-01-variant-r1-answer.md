

Primero factorizamos:

\[
11! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7 \cdot 11
\]

Un divisor cuya cifra de unidades sea \(3\) debe ser impar y no múltiplo de \(5\), así que no puede incluir factores \(2\) ni \(5\). Por tanto, solo puede dividir

\[
3^4 \cdot 7 \cdot 11
\]

Trabajamos módulo \(10\). Como \(11 \equiv 1 \pmod{10}\), el factor \(11\) no cambia la cifra de unidades.

Los divisores tienen la forma

\[
3^a \cdot 7^b \cdot 11^c
\]

con \(0 \le a \le 4\), \(b,c \in \{0,1\}\).

- Si \(b=0\), necesitamos \(3^a \equiv 3 \pmod{10}\), lo cual ocurre para \(a=1\).
- Si \(b=1\), necesitamos \(3^a \cdot 7 \equiv 3 \pmod{10}\). Como \(7^{-1} \equiv 3 \pmod{10}\), esto da \(3^a \equiv 9 \pmod{10}\), lo cual ocurre para \(a=2\).

Así, los divisores son:

\[
3,\quad 3\cdot 11=33,\quad 3^2\cdot 7=63,\quad 3^2\cdot 7\cdot 11=693
\]

Su suma es

\[
3+33+63+693=792
\]

\[
\boxed{792}
\]