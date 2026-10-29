Sea \(f(x)=ax^2+bx+c\). Como \(|f(x)|\le 1\) para todo \(x\in[0,1]\), en particular:

\[
|f(0)|=|c|\le 1,
\]
\[
|f(1)|=|a+b+c|\le 1,
\]
\[
|f(1/2)|=\left|\frac a4+\frac b2+c\right|\le 1.
\]

De estas tres condiciones se despejan los coeficientes:

\[
a=2f(0)-4f(1/2)+2f(1),
\]
\[
b=-3f(0)+4f(1/2)-f(1),
\]
\[
c=f(0).
\]

Por tanto,

\[
|a|\le 2+4+2=8,
\]
\[
|b|\le 3+4+1=8,
\]
\[
|c|\le 1.
\]

Luego

\[
|a|+|b|+|c|\le 8+8+1=17.
\]

Este valor se alcanza con

\[
f(x)=8x^2-8x+1=8\left(x-\frac12\right)^2-1,
\]

que cumple \(|f(x)|\le 1\) en \([0,1]\), y da

\[
|a|+|b|+|c|=8+8+1=17.
\]

\[
\boxed{17}
\]