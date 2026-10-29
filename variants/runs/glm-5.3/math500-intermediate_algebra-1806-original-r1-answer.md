Sea \(z=e^{i\theta}\) y \(u=\cos\theta\), con \(-1\le u\le 1\).

\[
|1+z|^2=(1+z)(1+\bar z)=2+2u,
\]
así que
\[
|1+z|=\sqrt{2+2u}.
\]

Además,
\[
1-z+z^2=z\left(z^{-1}-1+z\right)=z(2\cos\theta-1)=z(2u-1),
\]
por lo que
\[
|1-z+z^2|=|2u-1|.
\]

Por lo tanto hay que maximizar
\[
f(u)=\sqrt{2+2u}+|2u-1|.
\]

**Caso 1:** \(u\le \frac12\). Entonces
\[
f(u)=\sqrt{2+2u}+1-2u.
\]
Sea \(s=\sqrt{2+2u}\), de modo que \(u=\frac{s^2-2}{2}\) y \(0\le s\le \sqrt3\). Entonces
\[
f=s+1-(s^2-2)=3+s-s^2.
\]
Esta parábola tiene máximo en \(s=\frac12\), con valor
\[
3+\frac12-\frac14=\frac{13}{4}.
\]

**Caso 2:** \(u\ge \frac12\). Entonces
\[
f(u)=\sqrt{2+2u}+2u-1.
\]
Con \(s=\sqrt{2+2u}\), donde \(\sqrt3\le s\le 2\),
\[
f=s+s^2-3,
\]
que es creciente en el intervalo, por lo que su máximo es
\[
2+4-3=3.
\]

Comparando ambos casos, el máximo es \(\frac{13}{4}\), alcanzado por ejemplo cuando
\[
\cos\theta=-\frac78.
\]

\[
\boxed{\frac{13}{4}}
\]