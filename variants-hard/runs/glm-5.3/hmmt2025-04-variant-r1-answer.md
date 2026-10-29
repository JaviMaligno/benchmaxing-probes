Paso a paso:

1. Sea \(x=k+\tfrac12\). Los valores de \(x\) son números de la forma \(\pm\frac{d}{2}\) con \(d\) impar.

2. Emparejamos \(x>0\) con \(-x\), es decir \(k\) con \(-k-1\). Esto cubre los \(1200\) pares \(x=\tfrac12,\tfrac32,\dots,\tfrac{2399}{2}\). El término \(x=1200.5\) (con \(k=1200\)) queda sin pareja.

3. Para un par, con \(t=\frac{3150}{x}>0\):
\[
\left\lfloor t\right\rfloor+\left\lfloor -t\right\rfloor
=
\begin{cases}
0,& t\in\mathbb Z,\\
-1,& t\notin\mathbb Z.
\end{cases}
\]

4. Para \(x=\frac{2m+1}{2}\), \(m=0,\dots,1199\):
\[
t=\frac{6300}{2m+1}.
\]
Esto es entero exactamente cuando el impar \(2m+1\) divide a \(6300\).

Como
\[
6300=2^2\cdot 3^2\cdot 5^2\cdot 7,
\]
tiene \((2+1)(2+1)(1+1)=18\) divisores impares, y todos son menores que \(2399\), así que los 18 aparecen.

5. De los \(1200\) pares, 18 contribuyen \(0\), y los demás contribuyen \(-1\):
\[
-(1200-18)=-1182.
\]

6. El término sin pareja es
\[
\left\lfloor \frac{3150}{1200.5}\right\rfloor
=
\left\lfloor \frac{6300}{2401}\right\rfloor=2.
\]

Por lo tanto:
\[
-1182+2=-1180.
\]

\[
\boxed{-1180}
\]