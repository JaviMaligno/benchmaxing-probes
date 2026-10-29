Sea \(z=e^{i\theta}\), con \(\theta\in\mathbb{R}\). Entonces

\[
|1+z|=\left|e^{i\theta/2}\left(e^{-i\theta/2}+e^{i\theta/2}\right)\right|
=2\left|\cos\frac{\theta}{2}\right|.
\]

Además,

\[
1-z+z^2
= e^{i\theta}\left(e^{-i\theta}-1+e^{i\theta}\right)
= e^{i\theta}(2\cos\theta-1),
\]

por lo que

\[
|1-z+z^2|=|2\cos\theta-1|.
\]

Sea

\[
x=\left|\cos\frac{\theta}{2}\right|,\qquad 0\le x\le 1.
\]

Como \(\cos\theta=2\cos^2(\theta/2)-1=2x^2-1\), la expresión a maximizar es

\[
2x+|2(2x^2-1)-1|
=2x+|4x^2-3|.
\]

Consideramos dos casos.

Si \(0\le x\le \frac{\sqrt3}{2}\), entonces \(4x^2-3\le 0\), y

\[
f(x)=2x+3-4x^2.
\]

Esta parábola cóncava tiene su máximo en

\[
f'(x)=2-8x=0 \implies x=\frac14.
\]

Allí,

\[
f\left(\frac14\right)=2\cdot\frac14+3-4\cdot\frac1{16}
=\frac12+3-\frac14
=\frac{13}{4}.
\]

Si \(\frac{\sqrt3}{2}\le x\le 1\), entonces

\[
f(x)=2x+4x^2-3,
\]

que es creciente en ese intervalo, así que su máximo es

\[
f(1)=2+4-3=3.
\]

Por lo tanto, el valor máximo global es

\[
\boxed{\frac{13}{4}}
\]