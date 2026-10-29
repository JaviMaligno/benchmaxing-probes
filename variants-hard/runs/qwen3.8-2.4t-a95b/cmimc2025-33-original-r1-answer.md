

Sea \(f^k\) la \(k\)-ésima iteración de \(f\). Observamos que

\[
f(x)=x^4-4x^2+2=(x^2-2)^2-2.
\]

Si \(x=u+u^{-1}\), entonces

\[
x^2-2=u^2+u^{-2},
\]

por lo que

\[
f(x)=(u^2+u^{-2})^2-2=u^4+u^{-4}.
\]

Como

\[
\frac{n^2+1}{n}=n+\frac1n,
\]

por inducción se obtiene

\[
f^k\!\left(\frac{n^2+1}{n}\right)=n^{4^k}+n^{-4^k}.
\]

Para \(n=1\), esto vale siempre \(2\), que no está a menos de \(1/100\) de ninguna potencia \(c^{144}\) entera.

Supongamos \(n\ge 2\) y \(k\ge 1\). Sea

\[
A=n^{4^k}\in\mathbb{Z},\qquad r=n^{-4^k}\le \frac1{16}.
\]

Entonces

\[
f^k\!\left(\frac{n^2+1}{n}\right)=A+r.
\]

Como \(c^{144}\) es entero, si \(c^{144}\neq A\), la distancia entre \(A+r\) y \(c^{144}\) es al menos

\[
1-r\ge 1-\frac1{16}=\frac{15}{16}>\frac1{100}.
\]

Por tanto, necesariamente debe ocurrir

\[
n^{4^k}=c^{144}
\]

y además \(n^{-4^k}<1/100\).

Escribamos \(n=\prod p^{a_p}\). La igualdad \(n^{4^k}=c^{144}\) implica que, para cada primo \(p\),

\[
144 \mid a_p 4^k.
\]

Como \(4^k=2^{2k}\) no aporta factores \(3\), y

\[
144=2^4\cdot 3^2,
\]

es necesario que

\[
9\mid a_p
\]

para todo \(p\). Así, \(n\) debe ser una novena potencia perfecta.

La menor novena potencia perfecta mayor que \(1\) es

\[
2^9=512.
\]

Con \(n=512\), tomando \(k=2\),

\[
f^2\!\left(\frac{512^2+1}{512}\right)
=512^{16}+512^{-16}
=(2^9)^{16}+2^{-144}
=2^{144}+2^{-144}.
\]

Eligiendo \(c=2\), la diferencia es

\[
\left|2^{144}+2^{-144}-2^{144}\right|=2^{-144}<\frac1{100}.
\]

Por tanto, el menor \(n\) posible es

\[
\boxed{512}
\]