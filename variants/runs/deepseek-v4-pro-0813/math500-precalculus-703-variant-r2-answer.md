El polinomio es

\[
w^{10}-w^9+w^8-w^7+w^6-w^5+w^4-w^3+w^2-w+1.
\]

Se trata de una progresión geométrica de razón \(-w\). Su suma es

\[
\frac{1-(-w)^{11}}{1-(-w)}=\frac{1+w^{11}}{1+w}.
\]

Como debe anularse, y \(w\neq -1\), se tiene

\[
1+w^{11}=0 \implies w^{11}=-1.
\]

Las soluciones son las raíces undécimas de \(-1\), es decir,

\[
w=e^{i\frac{(2k+1)\pi}{11}},\qquad k=0,1,\dots,10.
\]

Ahora, el enunciado pide la suma de todos los posibles valores de \(\varphi\), con \(0\le \varphi<2\pi\). Por tanto, los ángulos son

\[
\varphi_k=\frac{(2k+1)\pi}{11},\qquad k=0,1,\dots,10.
\]

Su suma es

\[
\sum_{k=0}^{10}\frac{(2k+1)\pi}{11}
=\frac{\pi}{11}\left[\sum_{k=0}^{10}(2k+1)\right].
\]

La suma interior es la de los once primeros impares:

\[
1+3+5+\cdots+21=11^2=121.
\]

Luego

\[
\frac{\pi}{11}\cdot 121=11\pi.
\]

Por lo tanto, la suma de todos los posibles valores de \(\varphi\) es

\[
\boxed{11\pi}
\]