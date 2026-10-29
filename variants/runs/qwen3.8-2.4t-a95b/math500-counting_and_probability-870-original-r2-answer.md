

Fijamos \(A\) en un punto de la circunferencia. Como \(B\) se elige uniformemente, la longitud fraccional \(x\) del arco desde \(A\) hasta \(B\) en un sentido es uniforme en \([0,1]\).

Los puntos \(A\) y \(B\) dividen la circunferencia en dos arcos, de tamaños \(x\) y \(1-x\). Los segmentos \(AB\) y \(CD\) se intersecan si y solo si \(C\) y \(D\) caen en arcos distintos.

Dado \(x\), la probabilidad de que \(C\) y \(D\) estén en arcos distintos es

\[
x(1-x)+(1-x)x=2x(1-x).
\]

Promediando sobre \(x\sim \mathrm{Uniform}(0,1)\):

\[
\int_0^1 2x(1-x)\,dx
=
2\int_0^1 (x-x^2)\,dx
=
2\left(\frac12-\frac13\right)
=
\frac13.
\]

\[
\boxed{\frac{1}{3}}
\]