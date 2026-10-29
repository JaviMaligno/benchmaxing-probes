

Sea \(w=e^{i\theta}\), con \(\theta\in\mathbb{R}\). Entonces

\[
|1+w|=\left|1+e^{i\theta}\right|
=\left|e^{i\theta/2}\left(e^{-i\theta/2}+e^{i\theta/2}\right)\right|
=2\left|\cos\frac{\theta}{2}\right|.
\]

Para el segundo término,

\[
|2-2w+2w^2|=2|1-w+w^2|.
\]

Como

\[
1-w+w^2
=1-e^{i\theta}+e^{2i\theta}
=e^{i\theta}\left(e^{-i\theta}-1+e^{i\theta}\right)
=e^{i\theta}(2\cos\theta-1),
\]

tenemos

\[
|1-w+w^2|=|2\cos\theta-1|.
\]

Por tanto, la expresión a maximizar es

\[
2\left|\cos\frac{\theta}{2}\right|+2|2\cos\theta-1|.
\]

Sea

\[
t=\left|\cos\frac{\theta}{2}\right|,\qquad 0\le t\le 1.
\]

Entonces

\[
\cos\theta=2\cos^2\frac{\theta}{2}-1=2t^2-1.
\]

Así, debemos maximizar

\[
f(t)=2t+2|2(2t^2-1)-1|
=2t+2|4t^2-3|.
\]

Consideramos dos casos.

Si \(0\le t\le \frac{\sqrt3}{2}\), entonces \(4t^2-3\le 0\), y

\[
f(t)=2t+2(3-4t^2)=6+2t-8t^2.
\]

Esta cuadrática cóncava tiene su máximo donde

\[
f'(t)=2-16t=0 \implies t=\frac18.
\]

El valor es

\[
f\left(\frac18\right)
=6+2\cdot\frac18-8\cdot\frac1{64}
=6+\frac14-\frac18
=\frac{49}{8}.
\]

Si \(\frac{\sqrt3}{2}\le t\le 1\), entonces \(4t^2-3\ge 0\), y

\[
f(t)=2t+2(4t^2-3)=8t^2+2t-6,
\]

que es creciente en ese intervalo, por lo que su máximo está en \(t=1\):

\[
f(1)=8+2-6=4.
\]

Comparando, el máximo global es

\[
\boxed{\frac{49}{8}}
\]