Observemos primero que

\[
f(x)=x^4-4x^2+2=(x^2-2)^2-2.
\]

Como

\[
\frac{n^2+1}{n}=n+\frac1n,
\]

se cumple

\[
f\left(n+\frac1n\right)
=\left(\left(n+\frac1n\right)^2-2\right)^2-2
=\left(n^2+\frac1{n^2}\right)^2-2
=n^4+\frac1{n^4}.
\]

Por inducción,

\[
f^k\left(n+\frac1n\right)=n^{2^k}+n^{-2^k}.
\]

Sea \(m=2^k\). Entonces

\[
f^k\left(\frac{n^2+1}{n}\right)=n^m+n^{-m}.
\]

Para \(n=1\) no hay solución, pues \(f^k(2)=2\) y ningún \(c^{144}\) está a distancia menor que \(1/100\) de \(2\). Tomemos pues \(n\ge 2\).

Escribimos \(A=n^m\in\mathbb N\) y \(B=n^{-m}\). Como \(n\ge 2\) y \(m\ge 2\), se tiene

\[
0<B\le \frac14.
\]

Sea \(d=c^{144}\in\mathbb N\) y pongamos \(D=d-A\in\mathbb Z\). La condición es

\[
|A+B-d|=|B-D|<\frac1{100}.
\]

Si \(D\neq 0\), como \(D\in\mathbb Z\),

\[
|B-D|\ge 1-B\ge \frac34>\frac1{100},
\]

lo cual es imposible. Luego \(D=0\), es decir,

\[
c^{144}=n^m.
\]

Por tanto, \(n^m\) es una potencia \(144\)-ésima perfecta. Si \(p^a\mid n\), entonces \(144\mid ma\). Como \(m=2^k\),

\[
\gcd(144,m)\le 16.
\]

Así,

\[
a\ge \frac{144}{\gcd(144,m)}\ge \frac{144}{16}=9.
\]

Luego todo factor primo de \(n\) aparece con exponente al menos \(9\), de modo que

\[
n\ge 2^9=512.
\]

Finalmente, \(n=512\) sí funciona: tomando \(k=4\), tenemos \(m=16\), y

\[
f^4\left(512+\frac1{512}\right)
=512^{16}+512^{-16}
=2^{144}+2^{-144}.
\]

Con \(c=2\), la diferencia es

\[
2^{-144}<\frac1{100}.
\]

Por lo tanto, el menor natural es

\[
\boxed{512}.
\]