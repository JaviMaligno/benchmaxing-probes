

Sea

\[
S=\sum_{(a,b,c)\in T}\frac{2^a}{3^b5^c}.
\]

Para \(b,c\) fijos, las desigualdades triangulares equivalen a

\[
|b-c|<a<b+c.
\]

Como \(a\) es entero positivo,

\[
a=|b-c|+1,\ |b-c|+2,\dots,b+c-1.
\]

Entonces

\[
S=\sum_{b=1}^\infty\sum_{c=1}^\infty \frac1{3^b5^c}
\sum_{a=|b-c|+1}^{b+c-1}2^a.
\]

La suma interior es geométrica:

\[
\sum_{a=|b-c|+1}^{b+c-1}2^a
=2^{b+c}-2^{|b-c|+1}.
\]

Por tanto,

\[
S=\sum_{b,c\ge1}\frac{2^{b+c}}{3^b5^c}
-\sum_{b,c\ge1}\frac{2^{|b-c|+1}}{3^b5^c}.
\]

La primera suma se factoriza:

\[
\sum_{b,c\ge1}\frac{2^{b+c}}{3^b5^c}
=\left(\sum_{b=1}^\infty \left(\frac23\right)^b\right)
\left(\sum_{c=1}^\infty \left(\frac25\right)^c\right)
=2\cdot \frac23=\frac43.
\]

Para la segunda suma, separamos en \(b\ge c\) y \(c>b\).

Si \(b\ge c\), escribimos \(b=c+d\) con \(d\ge0\):

\[
\sum_{d=0}^\infty\sum_{c=1}^\infty
\frac{2^{d+1}}{3^{c+d}5^c}
=
\left(\sum_{c=1}^\infty\frac1{15^c}\right)
\left(\sum_{d=0}^\infty 2\left(\frac23\right)^d\right)
=
\frac1{14}\cdot 6=\frac37.
\]

Si \(c>b\), escribimos \(c=b+d\) con \(d\ge1\):

\[
\sum_{d=1}^\infty\sum_{b=1}^\infty
\frac{2^{d+1}}{3^b5^{b+d}}
=
\left(\sum_{b=1}^\infty\frac1{15^b}\right)
\left(\sum_{d=1}^\infty 2\left(\frac25\right)^d\right)
=
\frac1{14}\cdot \frac43=\frac2{21}.
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