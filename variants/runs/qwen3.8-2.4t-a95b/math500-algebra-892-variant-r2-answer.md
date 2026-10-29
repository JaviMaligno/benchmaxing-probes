

Para que la gráfica de \(y=g(x)\) corte a toda recta horizontal, el rango de \(g\) debe ser todo \(\mathbb{R}\).

Analizamos según el signo de \(b\).

**Caso \(b=0\):**  
\(g(x)=0\) para todo \(x\), así que el rango es \(\{0\}\). No sirve.

**Caso \(b>0\):**  
- Para \(x\ge b\), \(g(x)=bx^2\) es creciente en \(x\ge b>0\), con valor mínimo  
  \[
  g(b)=b^3.
  \]
  Su rango es \([b^3,\infty)\).
- Para \(x<b\), \(g(x)=bx+6b\) es una recta de pendiente positiva, con rango  
  \[
  (-\infty, b^2+6b).
  \]

Para cubrir todo \(\mathbb{R}\), necesitamos que no haya hueco entre ambos rangos:
\[
b^3 \le b^2+6b.
\]
Como \(b>0\), dividimos entre \(b\):
\[
b^2 \le b+6 \quad\Longleftrightarrow\quad b^2-b-6\le 0.
\]
Factorizando:
\[
(b-3)(b+2)\le 0,
\]
lo cual da \(0<b\le 3\).

**Caso \(b<0\):**  
- Para \(x\ge b\), \(g(x)=bx^2\) abre hacia abajo y alcanza máximo \(0\) en \(x=0\), así que su rango es \((-\infty,0]\).
- Para \(x<b\), \(g(x)=bx+6b\) tiene rango \((b^2+6b,\infty)\).

Para cubrir todo \(\mathbb{R}\), se necesita
\[
b^2+6b\le 0 \quad\Longleftrightarrow\quad b(b+6)\le 0,
\]
es decir, \(-6\le b<0\).

Por tanto, los valores válidos son
\[
[-6,0)\cup(0,3].
\]

El mayor valor de \(b\) es \(\boxed{3}\).