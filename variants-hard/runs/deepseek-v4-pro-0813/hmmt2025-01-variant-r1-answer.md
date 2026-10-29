Voy a factorizar \(11!\) en primos.

\[
11! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7 \cdot 11
\]

Un divisor de \(11!\) tiene la forma

\[
d = 2^a\,3^b\,5^c\,7^d\,11^e
\]

con

\[
0\le a\le 8,\quad 0\le b\le 4,\quad 0\le c\le 2,\quad 0\le d\le 1,\quad 0\le e\le 1.
\]

Queremos que su dígito de las unidades sea \(3\). Como \(11!\) es divisible por \(2\) y por \(5\), un divisor termina en \(3\) exactamente cuando es impar y no es divisible por \(5\), y su residuo módulo \(10\) es \(3\).

Por tanto, debe cumplirse:

\[
a=0,\qquad c=0.
\]

Así, el divisor tiene la forma

\[
d = 3^b\,7^d\,11^e.
\]

Las posibilidades son:

\[
3^b \quad (b=0,\dots,4),
\]
\[
3^b\cdot 7,
\]
\[
3^b\cdot 11,
\]
\[
3^b\cdot 7\cdot 11.
\]

Calculamos los dígitos de las unidades.

Los valores de \(3^b\) módulo \(10\) son:

\[
3^0=1,\quad 3^1=3,\quad 3^2=9,\quad 3^3=7,\quad 3^4=1.
\]

Como \(7\equiv -3\pmod{10}\) y \(11\equiv 1\pmod{10}\), conviene trabajar módulo \(10\):

- \(3^b\cdot 1\) termina en \(3\) solo para \(b=1\).
- \(3^b\cdot 7 \equiv 3^b\cdot (-3)\equiv -3^{b+1}\pmod{10}\).  
  Para que termine en \(3\), necesitamos \(3^{b+1}\equiv 7\pmod{10}\), lo que ocurre para \(b+1\equiv 3\pmod 4\), es decir \(b=2\).
- \(3^b\cdot 11 \equiv 3^b\pmod{10}\), igual que el primer caso: \(b=1\).
- \(3^b\cdot 7\cdot 11 \equiv 3^b\cdot 7\pmod{10}\), igual que el segundo caso: \(b=2\).

Así, los divisores que terminan en \(3\) son:

\[
3,\quad 3\cdot 11=33,
\]
\[
3^2\cdot 7=63,
\]
\[
3^2\cdot 7\cdot 11=693.
\]

Su suma es:

\[
3+33+63+693 = 792.
\]

\[
\boxed{792}
\]