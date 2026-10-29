

Sea \(p\) la probabilidad de la cara \(F\), y sea \(q\) la probabilidad de su cara opuesta. Como las otras cuatro caras tienen probabilidad \(1/6\),

\[
p+q+4\cdot \frac16=1 \implies p+q=\frac13.
\]

Escribamos

\[
p=\frac16+a,\qquad q=\frac16-a,
\]

con \(a>0\), porque \(p>1/6\) y \(q<1/6\).

Al lanzar dos dados iguales e independientes, la probabilidad de que la suma sea \(7\) se obtiene de los tres pares opuestos:

- Para el par sesgado \((F,\text{opuesta})\), la contribución es

\[
2pq=2\left(\frac16+a\right)\left(\frac16-a\right)
=2\left(\frac1{36}-a^2\right).
\]

- Para cada uno de los otros dos pares, ambas caras tienen probabilidad \(1/6\), así que cada par contribuye

\[
2\cdot \frac16\cdot \frac16=\frac1{18}.
\]

Por tanto, la probabilidad total de sumar \(7\) es

\[
2\left(\frac1{36}-a^2\right)+2\cdot \frac1{18}
=\frac16-2a^2.
\]

Nos dicen que esto es igual a \(\frac{71}{450}\). Como

\[
\frac16=\frac{75}{450},
\]

tenemos

\[
\frac{75}{450}-2a^2=\frac{71}{450}
\]

\[
2a^2=\frac{4}{450}=\frac{2}{225}
\]

\[
a^2=\frac1{225}
\]

\[
a=\frac1{15}.
\]

Entonces

\[
p=\frac16+\frac1{15}=\frac5{30}+\frac2{30}=\frac7{30}.
\]

Así, \(m=7\) y \(n=30\), por lo que

\[
m+n=37.
\]

\[
\boxed{37}
\]