

Sea \(n=23\). Para cada \(k\in\{1,\dots,n\}\), queremos

\[
\mathbb{E}\bigl[(g(g(k))-k)^2\bigr].
\]

Como \(g\) es una función aleatoria uniforme, los valores \(g(1),\dots,g(n)\) son independientes y uniformes en \(\{1,\dots,n\}\).

Fijemos \(k\). Sea \(Y=g(k)\). Entonces \(Y\) es uniforme en \(\{1,\dots,n\}\).

- Si \(Y=k\), entonces \(g(g(k))=g(k)=k\), por lo que la contribución es \(0\).
- Si \(Y=j\neq k\), entonces \(g(j)\) es independiente de \(g(k)\) y uniforme en \(\{1,\dots,n\}\).

Por tanto,

\[
\mathbb{E}\bigl[(g(g(k))-k)^2\bigr]
=
\frac{n-1}{n}\cdot \mathbb{E}\bigl[(U-k)^2\bigr],
\]

donde \(U\) es uniforme en \(\{1,\dots,n\}\).

Sumando sobre \(k\),

\[
\mathbb{E}\left[\sum_{k=1}^n (g(g(k))-k)^2\right]
=
\frac{n-1}{n}\sum_{k=1}^n \mathbb{E}\bigl[(U-k)^2\bigr].
\]

Ahora

\[
\sum_{k=1}^n \mathbb{E}\bigl[(U-k)^2\bigr]
=
\frac{1}{n}\sum_{u=1}^n\sum_{k=1}^n (u-k)^2.
\]

Para \(U,V\) independientes y uniformes en \(\{1,\dots,n\}\),

\[
\mathbb{E}[(U-V)^2]=2\operatorname{Var}(U)=2\cdot\frac{n^2-1}{12}
=\frac{n^2-1}{6}.
\]

Así,

\[
\frac{1}{n}\sum_{u,k}(u-k)^2
=
n\cdot \frac{n^2-1}{6}.
\]

Luego la esperanza total es

\[
\frac{n-1}{n}\cdot n\cdot \frac{n^2-1}{6}
=
\frac{(n-1)(n^2-1)}{6}.
\]

Con \(n=23\),

\[
\frac{22\cdot(23^2-1)}{6}
=
\frac{22\cdot 528}{6}
=
22\cdot 88
=
1936.
\]

\[
\boxed{1936}
\]