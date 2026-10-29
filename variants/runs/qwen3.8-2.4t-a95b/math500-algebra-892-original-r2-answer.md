

Para que la gráfica de \(y=f(x)\) interseque toda recta horizontal al menos una vez, el rango de \(f\) debe ser todo \(\mathbb{R}\).

Analizamos según el signo de \(a\).

**Caso 1: \(a>0\).**

- Para \(x\ge a\), tenemos \(f(x)=ax^2\). Como \(a>0\) y \(x\ge a>0\), esta rama es creciente y su valor mínimo está en \(x=a\):
  \[
  f(a)=a\cdot a^2=a^3.
  \]
  Así, su rango es \([a^3,\infty)\).

- Para \(x<a\), tenemos \(f(x)=ax+2a\). Como la pendiente es positiva y \(x<a\), su rango es
  \[
  (-\infty, a^2+2a).
  \]

Para cubrir todo \(\mathbb{R}\), no puede haber hueco entre ambos rangos, así que necesitamos
\[
a^3\le a^2+2a.
\]
Como \(a>0\), dividimos entre \(a\):
\[
a^2\le a+2,
\]
\[
a^2-a-2\le 0,
\]
\[
(a-2)(a+1)\le 0.
\]
Con \(a>0\), esto da
\[
0<a\le 2.
\]

**Caso 2: \(a<0\).**

- Para \(x\ge a\), la parábola \(ax^2\) abre hacia abajo. Como \(0\ge a\), el máximo ocurre en \(x=0\), con valor \(0\). Su rango es \((-\infty,0]\).

- Para \(x<a\), la recta \(ax+2a\) tiene pendiente negativa. Cuando \(x\to -\infty\), tiende a \(+\infty\), y cuando \(x\to a^-\), tiende a \(a^2+2a\). Su rango es
  \[
  (a^2+2a,\infty).
  \]

Para cubrir todo \(\mathbb{R}\), necesitamos
\[
a^2+2a\le 0,
\]
\[
a(a+2)\le 0,
\]
lo cual, con \(a<0\), implica
\[
-2\le a<0.
\]

Juntando ambos casos, los valores posibles son
\[
[-2,0)\cup(0,2].
\]

El mayor valor posible de \(a\) es \(2\).

\[
\boxed{2}
\]