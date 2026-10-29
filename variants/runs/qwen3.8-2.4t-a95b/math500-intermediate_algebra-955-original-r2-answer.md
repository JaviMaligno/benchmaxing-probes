

Sea \(p(x)=ax^2+bx+c\). Como \(|p(x)|\le 1\) para todo \(x\in[0,1]\), en particular

\[
|p(0)|\le 1,\qquad \left|p\left(\frac12\right)\right|\le 1,\qquad |p(1)|\le 1.
\]

Definamos

\[
y_0=p(0),\qquad y_1=p\left(\frac12\right),\qquad y_2=p(1).
\]

Entonces \(|y_0|,|y_1|,|y_2|\le 1\). Además,

\[
y_0=c,
\]
\[
y_1=\frac a4+\frac b2+c,
\]
\[
y_2=a+b+c.
\]

Resolviendo para \(a,b,c\) en términos de \(y_0,y_1,y_2\), se obtiene

\[
a=2y_0-4y_1+2y_2,
\]
\[
b=-3y_0+4y_1-y_2,
\]
\[
c=y_0.
\]

Por la desigualdad triangular,

\[
|a|\le 2|y_0|+4|y_1|+2|y_2|,
\]
\[
|b|\le 3|y_0|+4|y_1|+|y_2|,
\]
\[
|c|\le |y_0|.
\]

Sumando,

\[
|a|+|b|+|c|
\le (2+3+1)|y_0|+(4+4)|y_1|+(2+1)|y_2|.
\]

Como \(|y_i|\le 1\),

\[
|a|+|b|+|c|\le 6+8+3=17.
\]

Este valor se alcanza con

\[
p(x)=8x^2-8x+1=8\left(x-\frac12\right)^2-1,
\]

que satisface \(-1\le p(x)\le 1\) en \([0,1]\). Para este polinomio,

\[
|a|+|b|+|c|=8+8+1=17.
\]

\[
\boxed{17}
\]