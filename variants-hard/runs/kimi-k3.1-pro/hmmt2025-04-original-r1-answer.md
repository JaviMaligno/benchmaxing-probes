Agrupamos los términos \(j\) y \(-j-1\) para \(j=0,\dots,999\). Cada par tiene la forma
\[
\left\lfloor x\right\rfloor+\left\lfloor -x\right\rfloor
=\begin{cases}
0,&x\in\mathbb Z,\\
-1,&x\notin\mathbb Z.
\end{cases}
\]
Aquí \(x=\frac{4050}{2j+1}\). Es entero para \(14\) valores de \(j\), correspondientes a los divisores impares de \(4050\) menores que \(2000\). Así, los \(1000\) pares suman
\[
-1000-14=-1014.
\]
Falta el término \(j=1000\), que vale
\[
\left\lfloor\frac{2025}{1000.5}\right\rfloor=2.
\]
Por tanto, la suma es \(-1014+2\).

\[
\boxed{-1012}
\]