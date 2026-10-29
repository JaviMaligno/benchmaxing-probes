

Sea

\[
P(w)=w^{10}-w^9+w^8-w^7+w^6-w^5+w^4-w^3+w^2-w+1.
\]

Multiplicando por \(w+1\),

\[
(w+1)P(w)=w^{11}+1.
\]

Si \(P(w)=0\), entonces \(w^{11}=-1\), salvo el posible caso \(w=-1\). Pero

\[
P(-1)=11\neq 0,
\]

así que \(w=-1\) no es solución.

Las soluciones de \(w^{11}=-1\) son

\[
w=e^{i(2m+1)\pi/11},\qquad m=0,1,\dots,10.
\]

Están todas sobre la circunferencia unitaria, por lo que \(\rho=1\). Excluimos \(w=-1\), que corresponde a

\[
\frac{(2m+1)\pi}{11}=\pi \implies m=5.
\]

Por tanto, los posibles valores de \(\varphi\) son

\[
\varphi=\frac{(2m+1)\pi}{11},\qquad m=0,1,\dots,10,\quad m\neq 5.
\]

Su suma es

\[
\sum_{\substack{m=0\\ m\neq 5}}^{10}\frac{(2m+1)\pi}{11}
=
\frac{\pi}{11}\left(\sum_{m=0}^{10}(2m+1)-11\right).
\]

Como

\[
\sum_{m=0}^{10}(2m+1)=1+3+\cdots+21=121,
\]

obtenemos

\[
\frac{\pi}{11}(121-11)=\frac{110\pi}{11}=10\pi.
\]

\[
\boxed{10\pi}
\]