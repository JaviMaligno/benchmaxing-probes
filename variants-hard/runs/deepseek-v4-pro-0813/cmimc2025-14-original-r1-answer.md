Representamos cada cadena como un vector en \(\mathbb F_2^n\). En este grafo, \(x\sim y\) sii \(x+y\) tiene peso de Hamming \(k\). Por tanto, la componente conexa del vector cero es el subgrupo generado por los vectores de peso \(k\), y

\[
c_{n,k}=2^{\,n-\dim H_k}.
\]

Sea \(H_k=\langle v\in\mathbb F_2^n: \operatorname{wt}(v)=k\rangle\).

- Si \(1\le k<n\):
  - Si \(k\) es par, todo generador tiene peso par, así que \(H_k\) es el subespacio de vectores de peso par, de dimensión \(n-1\). Luego \(c_{n,k}=2\).
  - Si \(k\) es impar, \(H_k\) contiene ese subespacio par y además un vector de peso impar, así que \(H_k=\mathbb F_2^n\). Luego \(c_{n,k}=1\).

- Si \(k=n\), solo hay el vector \(111\dots1\), así que \(\dim H_k=1\), y \(c_{n,n}=2^{n-1}\).

Entonces, para cada \(n\):

\[
\begin{array}{c|c}
n & \displaystyle\sum_{k=1}^n c_{n,k}\\ \hline
1 & 1\\
2 & 3\\
3 & 7\\
4 & 12\\
5 & 22\\
6 & 39\\
7 & 73\\
8 & 138\\
9 & 268\\
10 & 525
\end{array}
\]

Sumando:

\[
1+3+7+12+22+39+73+138+268+525=1088.
\]

\[
\boxed{1088}
\]