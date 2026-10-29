

Definamos \(F_i\) como la función \(j \mapsto f(i,j)\). Entonces:

- \(F_0(j)=\operatorname{mod}_5(j+1)\), es decir  
  \[
  F_0=(1,2,3,4,0).
  \]

- Para \(i\ge 1\), la recursión dice:
  \[
  F_i(0)=F_{i-1}(1),
  \qquad
  F_i(j)=F_{i-1}(F_i(j-1)) \quad (1\le j\le 4).
  \]
  Así, la fila \(F_i\) se obtiene iterando \(F_{i-1}\) empezando en \(1\):
  \[
  F_i=(F_{i-1}(1), F_{i-1}^2(1), F_{i-1}^3(1), F_{i-1}^4(1), F_{i-1}^5(1)).
  \]

Calculemos las primeras filas:

\[
F_0=(1,2,3,4,0)
\]

\[
F_1=(2,3,4,0,1)
\]

\[
F_2=(3,0,2,4,1)
\]

\[
F_3=(0,3,4,1,0)
\]

\[
F_4=(3,1,3,1,3)
\]

\[
F_5=(1,1,1,1,1)
\]

A partir de aquí, si \(F_i\) es constante igual a \(1\), entonces \(F_{i+1}\) también es constante igual a \(1\). Por tanto, para todo \(i\ge 5\),

\[
f(i,j)=1.
\]

Como \(2015\ge 5\), tenemos

\[
f(2015,2)=1.
\]

\[
\boxed{1}
\]