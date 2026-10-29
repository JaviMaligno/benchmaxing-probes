

Sea \(z=e^{i\theta}\), con \(\theta\in\mathbb{R}\). Entonces

\[
|1+z|=\left|1+e^{i\theta}\right|=\sqrt{2+2\cos\theta}.
\]

Para el segundo término, usando \(|z|=1\),

\[
|1-z+z^2|^2=(1-z+z^2)(1-z^{-1}+z^{-2}).
\]

Expandiendo y agrupando:

\[
|1-z+z^2|^2
=3-2(z+z^{-1})+(z^2+z^{-2})
=3-4\cos\theta+2\cos 2\theta.
\]

Como \(\cos 2\theta=2\cos^2\theta-1\),

\[
|1-z+z^2|^2
=3-4\cos\theta+4\cos^2\theta-2
=(2\cos\theta-1)^2.
\]

Por tanto,

\[
|1-z+z^2|=|2\cos\theta-1|.
\]

Sea \(u=\cos\theta\in[-1,1]\). Queremos maximizar

\[
f(u)=\sqrt{2+2u}+|2u-1|.
\]

Hagamos

\[
x=\sqrt{2+2u},\qquad x\in[0,2].
\]

Entonces

\[
u=\frac{x^2}{2}-1,
\]

y

\[
2u-1=x^2-3.
\]

Así, la expresión se convierte en

\[
g(x)=x+|x^2-3|,\qquad 0\le x\le 2.
\]

Si \(0\le x\le \sqrt{3}\), entonces

\[
g(x)=x+3-x^2=3+x-x^2.
\]

Esta cuadrática cóncava tiene su máximo en

\[
1-2x=0\implies x=\frac12,
\]

donde

\[
g\left(\frac12\right)=3+\frac12-\frac14=\frac{13}{4}.
\]

Si \(\sqrt{3}\le x\le 2\), entonces

\[
g(x)=x+x^2-3,
\]

que es creciente en ese intervalo, así que su máximo está en \(x=2\):

\[
g(2)=2+4-3=3.
\]

Comparando, el valor máximo global es

\[
\frac{13}{4}.
\]

Este se alcanza cuando \(x=\frac12\), es decir, cuando \(\cos\theta=-\frac78\).

\[
\boxed{\frac{13}{4}}
\]