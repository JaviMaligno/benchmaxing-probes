

Sea \(p(x)=ax^2+bx+c\). Por la hipótesis,

\[
|p(x)|\le 1 \quad \text{para todo } x\in[0,1].
\]

Evaluamos en tres puntos:

\[
p(0)=c,\qquad p\!\left(\frac12\right)=\frac a4+\frac b2+c,\qquad p(1)=a+b+c.
\]

Llamemos

\[
u=p(0),\quad v=p\!\left(\frac12\right),\quad w=p(1).
\]

Entonces \(|u|,|v|,|w|\le 1\). Resolviendo para \(a,b,c\) en términos de \(u,v,w\):

\[
c=u,
\]

\[
a=2u-4v+2w,
\]

\[
b=-3u+4v-w.
\]

Por tanto,

\[
|a|+|b|+|c|
=
|2u-4v+2w|+|-3u+4v-w|+|u|.
\]

Usando la desigualdad triangular y que \(|u|,|v|,|w|\le 1\),

\[
|a|\le 2|u|+4|v|+2|w|\le 8,
\]

\[
|b|\le 3|u|+4|v|+|w|\le 8,
\]

\[
|c|\le 1.
\]

Así,

\[
|a|+|b|+|c|\le 8+8+1=17.
\]

Esta cota se alcanza con

\[
p(x)=8x^2-8x+1=2(2x-1)^2-1.
\]

Como \(2x-1\in[-1,1]\), se tiene \(|p(x)|\le 1\) en \([0,1]\), y

\[
|8|+|-8|+|1|=17.
\]

\[
\boxed{17}
\]