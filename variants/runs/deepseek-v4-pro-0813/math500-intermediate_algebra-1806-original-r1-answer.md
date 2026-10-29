Sea $z$ un número complejo con $|z|=1$. Escribimos $z=e^{i\theta}$. Entonces:

- $|1+z|=|1+e^{i\theta}|=\sqrt{(1+\cos\theta)^2+\sin^2\theta}=\sqrt{2+2\cos\theta}=2\left|\cos\frac{\theta}{2}\right|$.

Para el segundo término, observamos que
\[
1-z+z^2 = 1 - e^{i\theta} + e^{2i\theta}.
\]
Multiplicando por $e^{-i\theta}$ (que tiene módulo 1), obtenemos
\[
|1-z+z^2| = |e^{-i\theta} - 1 + e^{i\theta}| = |2\cos\theta - 1|.
\]
Por tanto,
\[
|1-z+z^2| = |2\cos\theta - 1|.
\]

Ahora, usando $\cos\theta = 2\cos^2\frac{\theta}{2}-1$, la expresión a maximizar es
\[
f(\theta) = 2\left|\cos\frac{\theta}{2}\right| + \left|2\cos\theta - 1\right|.
\]
Sea $t=\cos\frac{\theta}{2}$, con $t\in[-1,1]$. Entonces $\cos\theta=2t^2-1$ y
\[
f(t)=2|t| + |4t^2-3|.
\]

**Caso 1:** $|t|\le\frac{\sqrt3}{2}$. Entonces $4t^2-3\le0$ y
\[
f(t)=2|t|+3-4t^2.
\]
Sea $x=|t|\in[0,\frac{\sqrt3}{2}]$. Maximizamos
\[
g(x)=2x+3-4x^2 = 3+2x-4x^2.
\]
El vértice está en $x=\frac14$, y
\[
g\left(\frac14\right)=3+\frac12-\frac14=3.25=\frac{13}{4}.
\]
En los extremos:
\[
g(0)=3,\qquad g\left(\frac{\sqrt3}{2}\right)=2\cdot\frac{\sqrt3}{2}+3-4\cdot\frac34
=\sqrt3+0=\sqrt3\approx1.732.
\]
Así que el máximo en este caso es $\frac{13}{4}$, alcanzado cuando $t=\pm\frac14$.

**Caso 2:** $|t|\ge\frac{\sqrt3}{2}$. Entonces $4t^2-3\ge0$ y
\[
f(t)=2|t|+4t^2-3.
\]
Sea $x=|t|\in[\frac{\sqrt3}{2},1]$. Maximizamos
\[
h(x)=4x^2+2x-3,
\]
que es creciente en $x\in[\frac{\sqrt3}{2},1]$, pues su derivada $8x+2>0$. Su máximo está en $x=1$:
\[
h(1)=4+2-3=3.
\]

Comparando ambos casos, el máximo es
\[
\frac{13}{4}.
\]

Por lo tanto, el valor máximo es
\[
\boxed{\frac{13}{4}}.
\]