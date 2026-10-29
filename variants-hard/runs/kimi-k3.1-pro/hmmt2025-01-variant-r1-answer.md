La factorización prima de \(11!\) es
\[
11!=2^8\cdot 3^4\cdot 5^2\cdot 7\cdot 11.
\]

Un divisor con unidades \(3\) no puede ser divisible por \(2\) ni por \(5\). Por tanto, tiene la forma
\[
d=3^b7^e11^f,\qquad 0\le b\le4,\quad e,f\in\{0,1\}.
\]

Como \(11^f\equiv1\pmod{10}\), solo debemos considerar \(3^b7^e\). Las potencias de \(3\) módulo \(10\), para \(b=0,1,2,3,4\), son \(1,3,9,7,1\).

- Si \(e=0\), necesitamos \(3^b\equiv3\pmod{10}\), así que \(b=1\).
- Si \(e=1\), necesitamos \(7\cdot3^b\equiv3\pmod{10}\), así que \(b=2\).

El factor \(11\) es opcional, por lo que los divisores buscados son
\[
3,\quad 33,\quad 63,\quad 693.
\]
Su suma es \(3+33+63+693=\boxed{792}\).