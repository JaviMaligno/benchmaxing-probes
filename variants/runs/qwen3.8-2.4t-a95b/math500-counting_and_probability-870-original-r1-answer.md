

Fijamos los puntos \(A\) y \(B\). Estos dividen la circunferencia en dos arcos. Como \(A\) y \(B\) son aleatorios, podemos suponer que la longitud fraccional de uno de los arcos es \(x\), con \(x\) uniforme en \([0,1]\), y la del otro arco es \(1-x\).

Los segmentos \(AB\) y \(CD\) se intersecan si y solo si \(C\) y \(D\) caen en arcos diferentes determinados por \(A\) y \(B\). Dado \(x\), la probabilidad de eso es

\[
2x(1-x),
\]

porque \(C\) puede caer en el primer arco y \(D\) en el segundo, o viceversa.

Ahora promediamos sobre \(x\):

\[
\int_0^1 2x(1-x)\,dx
=2\int_0^1 (x-x^2)\,dx
=2\left(\frac12-\frac13\right)
=\frac13.
\]

Por lo tanto, la probabilidad es

\[
\boxed{\frac{1}{3}}
\]