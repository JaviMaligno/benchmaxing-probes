

Para que una terna de enteros positivos \((a,b,c)\) forme un triángulo, se debe cumplir la desigualdad triangular estricta:

\[
|b-c|<a<b+c.
\]

Así, fijados \(b,c\ge 1\), los valores posibles de \(a\) son

\[
a=|b-c|+1,\ |b-c|+2,\ \dots,\ b+c-1.
\]

Entonces

\[
\sum_{a=|b-c|+1}^{b+c-1}2^a
=2^{b+c}-2^{|b-c|+1}.
\]

Por tanto, la suma pedida es

\[
S=\sum_{b,c\ge 1}\frac{2^{b+c}-2^{|b-c|+1}}{3^b5^c}
= \sum_{b,c\ge 1}\frac{2^{b+c}}{3^b5^c}
-\sum_{b,c\ge 1}\frac{2^{|b-c|+1}}{3^b5^c}.
\]

La primera suma se factoriza:

\[
\sum_{b,c\ge 1}\frac{2^{b+c}}{3^b5^c}
=
\left(\sum_{b\ge 1}\left(\frac23\right)^b\right)
\left(\sum_{c\ge 1}\left(\frac25\right)^c\right)
=2\cdot \frac23=\frac43.
\]

Para la segunda suma, separamos en dos casos.

Si \(b\ge c\), escribimos \(d=b-c\ge 0\) y \(n=c\ge 1\):

\[
\sum_{b\ge c\ge 1}\frac{2^{|b-c|+1}}{3^b5^c}
=
\sum_{n\ge 1}\sum_{d\ge 0}
\frac{2^{d+1}}{3^{n+d}5^n}
=
2\left(\sum_{d\ge 0}\left(\frac23\right)^d\right)
\left(\sum_{n\ge 1}\left(\frac1{15}\right)^n\right).
\]

\[
=2\cdot 3\cdot \frac1{14}=\frac37.
\]

Si \(c>b\), escribimos \(d=c-b\ge 1\) y \(n=b\ge 1\):

\[
\sum_{c>b\ge 1}\frac{2^{|b-c|+1}}{3^b5^c}
=
\sum_{n\ge 1}\sum_{d\ge 1}
\frac{2^{d+1}}{3^n5^{n+d}}
=
2\left(\sum_{d\ge 1}\left(\frac25\right)^d\right)
\left(\sum_{n\ge 1}\left(\frac1{15}\right)^n\right).
\]

\[
=2\cdot \frac23\cdot \frac1{14}=\frac2{21}.
\]

Así, la segunda suma total es

\[
\frac37+\frac2{21}=\frac{11}{21}.
\]

Finalmente,

\[
S=\frac43-\frac{11}{21}
=\frac{28}{21}-\frac{11}{21}
=\frac{17}{21}.
\]

\[
\boxed{\frac{17}{21}}
\]