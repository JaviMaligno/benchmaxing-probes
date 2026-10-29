Factorizamos \(12!\) en primos:

\[
12! = 2^{10}\cdot 3^5\cdot 5^2\cdot 7\cdot 11.
\]

Para que \(y^3\) sea divisor de \(12!\), cada exponente en \(y^3\) no puede superar al exponente correspondiente en \(12!\). Así:

\[
3v_p(y)\le v_p(12!).
\]

Entonces:

- Para \(p=2\): \(v_2(y)\le \left\lfloor \frac{10}{3}\right\rfloor=3\).
- Para \(p=3\): \(v_3(y)\le \left\lfloor \frac{5}{3}\right\rfloor=1\).
- Para \(p=5,7,11\): el exponente máximo es \(0\).

Por lo tanto, \(y\) debe tener la forma

\[
y=2^a\cdot 3^b,
\]

con \(0\le a\le 3\) y \(0\le b\le 1\).

El número de elecciones es

\[
(3+1)(1+1)=4\cdot 2=8.
\]

\[
\boxed{8}
\]