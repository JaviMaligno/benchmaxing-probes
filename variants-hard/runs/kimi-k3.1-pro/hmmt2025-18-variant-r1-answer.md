Sea \(L=2\cdot 60+1=121\). Tras 60 minutos, cada valor es el máximo de una ventana de \(L\) valores iniciales consecutivos. Por tanto, un valor inicial sigue apareciendo exactamente cuando es el máximo de al menos una de esas ventanas.

Fijemos un valor \(x_j\), y sean \(a\) y \(b\) las distancias a los valores más grandes más cercanos a su izquierda y a su derecha. Una ventana de longitud \(L\) que contiene a \(x_j\) puede extenderse \(p\) posiciones a la izquierda y \(L-1-p\) a la derecha. Para que \(x_j\) sea su máximo, debe cumplirse
\[
p\le a-1,\qquad L-1-p\le b-1.
\]
Tal \(p\) existe si y solo si \(a+b\ge L+1\).

Para \(a,b\) fijos, los \(a+b-2\) valores intermedios deben ser menores que \(x_j\), y los dos extremos, mayores. Condicionando a \(x_j=u\), obtenemos
\[
\Pr(a,b)=\int_0^1u^{a+b-2}(1-u)^2\,du
=\frac{2}{(a+b-1)(a+b)(a+b+1)}.
\]
Así, la probabilidad de que \(x_j\) desaparezca es
\[
\sum_{s=2}^{L}(s-1)\frac{2}{(s-1)s(s+1)}
=\sum_{s=2}^{L}\left(\frac2s-\frac2{s+1}\right)
=1-\frac2{L+1}.
\]
Por ello, sobrevive con probabilidad \(2/(L+1)=1/61\). Por linealidad de la esperanza, el número esperado de valores distintos es
\[
\boxed{\frac{1011}{61}}.
\]