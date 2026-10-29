Sea \(x\) una raíz. Como \(x=0\) no es raíz y \(11x-1=0\) tampoco, podemos escribir
\[
\left(\frac{x}{11x-1}\right)^{10}=-1.
\]
Definimos
\[
\omega=\frac{x}{11x-1},
\]
de modo que \(\omega^{10}=-1\) y \(|\omega|=1\). Además,
\[
x=\frac{\omega}{11\omega-1}.
\]
Entonces, para cada \(\omega\) en el círculo unidad,
\[
x\bar x
=\frac{\omega}{11\omega-1}\cdot\frac{\bar\omega}{11\bar\omega-1}
=\frac{1}{121-11(\omega+\bar\omega)+1}
=\frac{1}{122-22\operatorname{Re}\omega}.
\]
Por tanto,
\[
\frac{1}{x\bar x}=122-22\operatorname{Re}\omega.
\]

Las diez soluciones de \(\omega^{10}=-1\) son
\[
\omega_k=e^{i(2k+1)\pi/10},\qquad k=0,1,\dots,9.
\]
Al agruparlas en pares conjugados, los cinco valores distintos de \(\cos\theta\) son
\[
\cos\frac{\pi}{10},\quad \cos\frac{3\pi}{10},\quad 0,\quad -\cos\frac{3\pi}{10},\quad -\cos\frac{\pi}{10}.
\]
Su suma es \(0\). La suma pedida es
\[
\sum_{i=1}^{5}\frac{1}{s_i\overline{s_i}}
=\sum_{i=1}^{5}(122-22\cos\theta_i)
=5\cdot 122-22\cdot 0
=610.
\]

\[
\boxed{610}
\]