El rango de la función debe cubrir todos los reales para que toda recta horizontal corte la gráfica al menos una vez.

**Caso 1: \(b=0\)**

Entonces \(g(x)=0\) para todo \(x\), y su rango es solo \(\{0\}\). No sirve.

**Caso 2: \(b>0\)**

Para \(x\ge b\): \(g(x)=bx^2\). Su mínimo en ese trozo ocurre en \(x=b\), dando \(b^3>0\). Así que este trozo tiene rango \([b^3,\infty)\).

Para \(x<b\): \(g(x)=bx+6b=b(x+6)\). Como \(x<b\), el trozo cubre \((-\infty, b^2+6b)\).

La unión debe cubrir toda la recta real. Por lo tanto, no debe haber huecos:

\[
b^3 \le b^2+6b.
\]

Como \(b>0\), dividimos por \(b\):

\[
b^2 \le b+6 \quad\Rightarrow\quad b^2-b-6\le 0.
\]

Las raíces son \(3\) y \(-2\), así que:

\[
-2\le b\le 3.
\]

Con \(b>0\), se obtiene \(0<b\le 3\).

**Caso 3: \(b<0\)**

Para \(x\ge b\): \(g(x)=bx^2\le 0\), con máximo \(0\) (cuando \(x=0\); como \(b<0\), el punto \(x=0\) está en este trozo) y tiende a \(-\infty\). El rango es \((-\infty,0]\).

Para \(x<b\): \(g(x)=b(x+6)\). Como \(b<0\), este trozo decrece con \(x\). Con \(x<b\), el mayor valor se da cuando \(x\to b^-\), tendiendo a \(b^2+6b\).

Para cubrir toda la recta, la unión debe llegar a \(+\infty\), lo cual no ocurre: ambos trozos están acotados superiormente. Además hay un salto desde \(0\) hasta \(b^2+6b\) que deja valores sin cubrir. Por tanto, \(b<0\) no sirve.

El mayor valor es el del caso \(b>0\):

\[
\boxed{3}
\]