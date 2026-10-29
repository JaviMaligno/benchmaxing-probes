Un número racional tiene desarrollo decimal finito si y solo si, en su forma irreducible, el denominador es de la forma \(2^a 5^b\) con \(a,b\ge 0\).

Aquí, \(\frac{1}{k}\) ya está en forma irreducible para cualquier entero positivo \(k\), así que su recíproco tiene expansión decimal finita exactamente cuando \(k\) no tiene factores primos distintos de \(2\) y \(5\).

Debemos contar los enteros positivos impares menores que \(4000\) de la forma \(5^b\), pues al ser impares no pueden contener factor \(2\).

Los enteros impares positivos menores que \(4000\) son:
\[
1, 3, 5, 7, \dots, 3999.
\]
Su cantidad es
\[
\frac{3999-1}{2}+1=2000.
\]

Entre ellos, los de la forma \(5^b\) menores que \(4000\) son:
\[
5^0=1,\quad 5^1=5,\quad 5^2=25,\quad 5^3=125,\quad 5^4=625,\quad 5^5=3125.
\]
\(5^6=15625\) ya supera \(4000\). Por tanto hay \(6\) números favorables.

La probabilidad es
\[
\frac{6}{2000}=\frac{3}{1000}.
\]

Aquí \(m=3\) y \(n=1000\), que son primos relativos, así que
\[
m+n=1003.
\]

\[
\boxed{1003}
\]