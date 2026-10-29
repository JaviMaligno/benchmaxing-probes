Para que \(y^3\) sea un divisor positivo de \(12!\), primero factorizamos \(12!\):

\[
12! = 2^{10}\cdot 3^5\cdot 5^2\cdot 7^1\cdot 11^1
\]

Si

\[
y = 2^a 3^b 5^c 7^d 11^e,
\]

entonces

\[
y^3 = 2^{3a}3^{3b}5^{3c}7^{3d}11^{3e}.
\]

Para que \(y^3\mid 12!\), cada exponente debe cumplir:

\[
3a \le 10,\quad 3b \le 5,\quad 3c \le 2,\quad 3d \le 1,\quad 3e \le 1.
\]

Así:

- \(a\) puede ser \(0,1,2,3\): \(4\) opciones.
- \(b\) puede ser \(0,1\): \(2\) opciones.
- \(c\) solo puede ser \(0\): \(1\) opción.
- \(d\) solo puede ser \(0\): \(1\) opción.
- \(e\) solo puede ser \(0\): \(1\) opción.

El número total de valores posibles de \(y\) es

\[
4\cdot 2\cdot 1\cdot 1\cdot 1 = 8.
\]

\[
\boxed{8}
\]