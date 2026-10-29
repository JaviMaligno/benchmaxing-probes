Primero, aplicamos la restricción \(xyz=2\).

Queremos minimizar

\[
x^4+4y^2+4z^4.
\]

Una estrategia es usar la desigualdad entre media aritmética y geométrica (AM–GM), pero hay que elegir bien los términos para que el producto dependa de \(xyz\) y se pueda igualar a una constante.

Escribimos

\[
x^4+4y^2+4z^4
= x^4+2y^2+2y^2+4z^4.
\]

Aplicamos AM–GM a estos cuatro términos:

\[
x^4+2y^2+2y^2+4z^4
\ge 4\sqrt[4]{x^4\cdot 2y^2\cdot 2y^2\cdot 4z^4}.
\]

Simplificamos el producto:

\[
x^4\cdot 2y^2\cdot 2y^2\cdot 4z^4
=16x^4y^4z^4.
\]

Por tanto,

\[
x^4+4y^2+4z^4
\ge 4\sqrt[4]{16x^4y^4z^4}
=4\cdot 2xyz
=8xyz.
\]

Como \(xyz=2\),

\[
x^4+4y^2+4z^4\ge 8\cdot 2=16.
\]

La igualdad en AM–GM se da cuando

\[
x^4=2y^2=2y^2=4z^4.
\]

Entonces

\[
x^4=2y^2=4z^4.
\]

Llamemos \(k=x^4=2y^2=4z^4\). Así,

\[
x=k^{1/4},\qquad y=\sqrt{\frac k2},\qquad z=\left(\frac k4\right)^{1/4}.
\]

Usamos \(xyz=2\):

\[
k^{1/4}\cdot \left(\frac k2\right)^{1/2}\cdot \left(\frac k4\right)^{1/4}=2.
\]

Escribimos en potencias:

\[
k^{1/4+\frac12+\frac14}\cdot 2^{-1/2}\cdot 4^{-1/4}=2.
\]

Los exponentes de \(k\) suman \(1\):

\[
k\cdot 2^{-1/2}\cdot 4^{-1/4}=2.
\]

Pero \(4^{-1/4}=2^{-1/2}\), luego

\[
k\cdot 2^{-1/2}\cdot 2^{-1/2}=2,
\]

es decir,

\[
k\cdot 2^{-1}=2.
\]

Por tanto,

\[
k=4.
\]

Así, el mínimo es \(16\), alcanzado cuando

\[
x=4^{1/4}=\sqrt2,\qquad y=\sqrt{\frac42}=\sqrt2,\qquad z=\left(\frac44\right)^{1/4}=1.
\]

Verificamos: \(xyz=\sqrt2\cdot\sqrt2\cdot1=2\), y

\[
x^4+4y^2+4z^4
=(\sqrt2)^4+4(\sqrt2)^2+4(1)^4
=4+8+4=16.
\]

Por lo tanto, el valor mínimo es

\[
\boxed{16}.
\]