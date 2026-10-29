

Sea \(n=25\). Para un \(x\) fijo, definimos \(Z_x=f(f(x))\).

Como \(f\) es una función aleatoria uniforme, los valores \(f(1),\dots,f(n)\) son independientes y uniformes en \(\{1,\dots,n\}\).

Para \(z\neq x\), el evento \(f(f(x))=z\) ocurre si existe algún \(y\neq x\) tal que \(f(x)=y\) y \(f(y)=z\). Hay \(n-1\) elecciones posibles para \(y\), y cada par de valores tiene probabilidad \(1/n^2\). Por tanto,

\[
\Pr(f(f(x))=z)=\frac{n-1}{n^2},\qquad z\neq x.
\]

El caso \(z=x\) no contribuye al cuadrado, pues \((x-x)^2=0\). Entonces,

\[
\mathbb{E}\bigl[(f(f(x))-x)^2\bigr]
=
\frac{n-1}{n^2}\sum_{z\neq x}(z-x)^2.
\]

Por linealidad de la esperanza,

\[
\mathbb{E}\left[\sum_{x=1}^{n}(f(f(x))-x)^2\right]
=
\frac{n-1}{n^2}\sum_{x=1}^{n}\sum_{z\neq x}(z-x)^2.
\]

Los términos diagonales son cero, así que podemos sumar sobre todos los pares ordenados:

\[
\sum_{x=1}^{n}\sum_{z=1}^{n}(z-x)^2
=
2n\sum_{k=1}^{n}k^2-2\left(\sum_{k=1}^{n}k\right)^2.
\]

Para \(n=25\),

\[
\sum_{k=1}^{25}k=325,\qquad \sum_{k=1}^{25}k^2=5525.
\]

Por tanto,

\[
\sum_{x=1}^{25}\sum_{z=1}^{25}(z-x)^2
=
2\cdot 25\cdot 5525-2\cdot 325^2
=
276250-211250
=
65000.
\]

Finalmente,

\[
\mathbb{E}\left[\sum_{x=1}^{25}(f(f(x))-x)^2\right]
=
\frac{24}{625}\cdot 65000
=
24\cdot 104
=
2496.
\]

\[
\boxed{2496}
\]