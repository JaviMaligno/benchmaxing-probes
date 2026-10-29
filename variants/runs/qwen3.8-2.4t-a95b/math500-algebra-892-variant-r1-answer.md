

Para que la gráfica de \(y=g(x)\) corte a toda recta horizontal, el rango de \(g\) debe ser todo \(\mathbb{R}\).

Analicemos según el signo de \(b\).

### Caso 1: \(b>0\)

- Para \(x\ge b\), \(g(x)=bx^2\). Como \(b>0\) y \(x\ge b>0\), esta rama es creciente y su valor mínimo ocurre en \(x=b\):
  \[
  g(b)=b\cdot b^2=b^3.
  \]
  Por tanto, su rango es
  \[
  [b^3,\infty).
  \]

- Para \(x<b\), \(g(x)=bx+6b\). Como \(b>0\), es una recta creciente. Cuando \(x\to-\infty\), \(g(x)\to-\infty\), y cuando \(x\to b^-\),
  \[
  g(x)\to b^2+6b,
  \]
  sin alcanzar ese valor. Así, su rango es
  \[
  (-\infty,b^2+6b).
  \]

La unión de ambos rangos cubre todo \(\mathbb{R}\) si no hay hueco entre ellos, es decir, si
\[
b^3\le b^2+6b.
\]
Como \(b>0\), dividimos entre \(b\):
\[
b^2\le b+6,
\]
\[
b^2-b-6\le 0,
\]
\[
(b-3)(b+2)\le 0.
\]
Con \(b>0\), esto da
\[
0<b\le 3.
\]

### Caso 2: \(b=0\)

Entonces \(g(x)=0\) para todo \(x\), así que el rango es solo \(\{0\}\). No sirve.

### Caso 3: \(b<0\)

- Para \(x\ge b\), \(g(x)=bx^2\) es una parábola que abre hacia abajo. Como el dominio incluye \(x=0\), alcanza su máximo \(0\), y tiende a \(-\infty\). Su rango es
  \[
  (-\infty,0].
  \]

- Para \(x<b\), \(g(x)=bx+6b\) es decreciente. Cuando \(x\to-\infty\), \(g(x)\to+\infty\), y cuando \(x\to b^-\),
  \[
  g(x)\to b^2+6b.
  \]
  Su rango es
  \[
  (b^2+6b,\infty).
  \]

Para cubrir todo \(\mathbb{R}\), necesitamos
\[
b^2+6b\le 0,
\]
es decir,
\[
b(b+6)\le 0.
\]
Como \(b<0\), esto implica \(-6\le b<0\). Estos valores funcionan, pero son menores que \(3\).

Por tanto, el mayor valor posible de \(b\) es

\[
\boxed{3}
\]