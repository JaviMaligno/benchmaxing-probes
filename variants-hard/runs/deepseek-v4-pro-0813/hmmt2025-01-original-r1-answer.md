Vamos a resolverlo paso a paso.

Sea \(9!=362880\). Primero factorizamos:

\[
9!=2^7\cdot 3^4\cdot 5\cdot 7
\]

Queremos los divisores positivos de \(9!\) cuyo dígito de las unidades sea \(1\).

Un divisor tiene la forma:

\[
d=2^a3^b5^c7^d
\]

con \(0\le a\le 7\), \(0\le b\le 4\), \(0\le c\le 1\), \(0\le d\le 1\).

Para que el dígito de las unidades sea \(1\), \(d\equiv 1\pmod{10}\). Como \(10=2\cdot 5\), analizamos módulo \(2\) y módulo \(5\).

Como \(d\) debe ser impar, no puede contener factor \(2\), así que \(a=0\). Además, para que no termine en \(5\), tampoco debe contener factor \(5\), así que \(c=0\).

Por lo tanto, los divisores buscados son de la forma:

\[
d=3^b7^d
\]

con \(0\le b\le 4\), \(0\le d\le 1\), y \(d\equiv 1\pmod{10}\).

Ahora enumeramos:

- Si \(d=0\): \(1,3,9,27,81\). Terminan en \(1\): \(1\) y \(81\).
- Si \(d=1\): \(7,21,63,189,567\). Terminan en \(1\): \(21\).

Los divisores son \(1,81,21\).

\[
1+81+21=103
\]

\[
\boxed{103}
\]