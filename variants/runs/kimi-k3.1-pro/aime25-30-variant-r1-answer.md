Sea
\[
P(x)=(x-8)(x-50)(x-72)(x-k),
\]
de modo que \(g(x)=P(x)/x\). Supongamos que \(g\) alcanza su mínimo \(m\) en exactamente dos puntos positivos \(u,v\). Entonces \(P(x)-mx\) tiene raíces dobles en \(u,v\). Como es un polinomio mónico de cuarto grado,
\[
P(x)-mx=(x-u)^2(x-v)^2.
\]

Escribamos \(A=u+v\) y \(B=uv\). Por tanto,
\[
P(x)=(x^2-Ax+B)^2+mx.
\]
Comparando los coeficientes de \(x^3\), \(x^2\) y el término constante, obtenemos
\[
2A=130+k,\qquad A^2+2B=4576+130k,\qquad B^2=28800k.
\]
Como \(B>0\), \(B=120\sqrt{2k}\). Sustituyendo \(A=(130+k)/2\):
\[
\frac{(130+k)^2}{4}+240\sqrt{2k}=4576+130k,
\]
o equivalentemente,
\[
k^2-260k-1404+960\sqrt{2k}=0.
\]

Hacemos \(t=\sqrt{2k}>0\), así que \(k=t^2/2\). La ecuación se convierte en
\[
t^4-520t^2+3840t-5616=0,
\]
que se factoriza como
\[
(t-2)(t-6)(t-18)(t+26)=0.
\]
Las raíces positivas \(t=2,6,18\) dan
\[
k=2,\quad 18,\quad 162.
\]
En los tres casos \(A^2-4B>0\), por lo que \(u,v\) son positivos y distintos, y efectivamente hay exactamente dos minimizadores.

Por tanto, la suma pedida es
\[
\boxed{182}
\]