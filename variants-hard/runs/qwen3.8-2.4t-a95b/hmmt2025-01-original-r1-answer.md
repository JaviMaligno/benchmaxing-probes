

Descomponemos en factores primos:

\[
9! = 2^7 \cdot 3^4 \cdot 5 \cdot 7
\]

Un divisor de \(9!\) tiene la forma

\[
2^a 3^b 5^c 7^d
\]

Para que termine en \(1\), debe ser impar y no múltiplo de \(5\), así que necesariamente \(a=0\) y \(c=0\). Entonces los divisores posibles son

\[
3^b 7^d,\quad 0\le b\le 4,\quad 0\le d\le 1
\]

Miramos la cifra de unidades:

- Potencias de \(3\) módulo \(10\):  
  \[
  3^0=1,\;3^1=3,\;3^2=9,\;3^3=27\equiv 7,\;3^4=81\equiv 1
  \]

- Si \(d=0\), necesitamos \(3^b\equiv 1\pmod{10}\), lo cual ocurre para \(b=0,4\).  
  Esto da los divisores \(1\) y \(81\).

- Si \(d=1\), necesitamos \(7\cdot 3^b\equiv 1\pmod{10}\). Como \(7\cdot 3=21\equiv 1\), se necesita \(3^b\equiv 3\pmod{10}\), lo cual ocurre para \(b=1\).  
  Esto da el divisor \(3\cdot 7=21\).

Los divisores de \(9!\) que terminan en \(1\) son entonces

\[
1,\;21,\;81
\]

Su suma es

\[
1+21+81=103
\]

\[
\boxed{103}
\]