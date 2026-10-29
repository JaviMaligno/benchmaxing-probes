Queremos que la gráfica de

\[
g(x)=\begin{cases}
bx^2, & x\ge b,\\
bx+6b, & x<b
\end{cases}
\]

corte toda recta horizontal al menos una vez. Es decir, el rango de \(g\) debe ser todo \(\mathbb R\).

Analicemos ambos trozos.

## Caso 1: \(x\ge b\)

Aquí \(g(x)=bx^2\), con dominio \(x\ge b\).

- Si \(b>0\), este trozo produce valores \(bx^2\), que van desde \(b^3\) (cuando \(x=b\), si \(b\ge b\)) hasta \(+\infty\). Como \(x^2\ge 0\), solo da valores no negativos.
- Si \(b<0\), el dominio \(x\ge b\) incluye \(x=0\) (pues \(b<0\)), así que \(bx^2\le 0\) y además cuando \(x\) crece hacia \(+\infty\), \(bx^2\to -\infty\). En \(x=0\), \(g=0\). Así este trozo cubre desde \(-\infty\) hasta un máximo en el borde del dominio.

## Caso 2: \(x<b\)

Aquí \(g(x)=bx+6b=b(x+6)\), con dominio \(x<b\).

- Si \(b>0\), conforme \(x\to b^{-}\), \(g(x)\to b^2+6b\). Como \(x\) puede ir hacia \(-\infty\), \(bx+6b\to -\infty\). Luego este trozo cubre \((-\infty,\ b^2+6b)\) (sin incluir necesariamente el extremo si hay discontinuidad).
- Si \(b<0\), conforme \(x\to b^{-}\), \(g(x)\to b^2+6b\), y conforme \(x\to-\infty\), \(bx+6b\to +\infty\). Este trozo cubre \((b^2+6b,\ +\infty)\) aproximadamente.

Intuición clave: para cubrir todo \(\mathbb R\), es natural que **un trozo cubra los negativos/positivos** según el signo de \(b\).

## Probemos con \(b>0\)

- Trozo \(x<b\): cubre \((-\infty,\ b^2+6b)\).
- Trozo \(x\ge b\): cubre \([b^3,\ +\infty)\).

Para cubrir todo \(\mathbb R\), necesitamos que no haya hueco entre \(b^2+6b\) y \(b^3\). Además el extremo izquierdo del primer trozo ya es \(-\infty\), así que necesitamos:

\[
b^2+6b \ge b^3.
\]

Además, hay que verificar los valores intermedios con cuidado porque hay posible discontinuidad en \(x=b\).

En \(x=b\):
- Valor del segundo trozo (límite por la izquierda): \(b^2+6b\).
- Valor del primer trozo: \(b^3\).

Para \(b>0\), el primer trozo empieza exactamente en \(b^3\) (lo incluye) y va a \(+\infty\). Entonces solo falta que el primer trozo comience a más tardar donde termina el segundo:

\[
b^3 \le b^2+6b.
\]

Dividiendo por \(b>0\):

\[
b^2 \le b+6
\]

\[
b^2-b-6\le 0.
\]

Resolvemos \(b^2-b-6=0\), cuyas raíces son \(3\) y \(-2\). Como la parábola abre hacia arriba, la desigualdad se cumple para

\[
-2\le b\le 3.
\]

Con \(b>0\), obtenemos:

\[
0<b\le 3.
\]

El mayor valor en esta rama sería \(b=3\).

## Probemos con \(b<0\)

- Trozo \(x<b\): como \(b<0\), el dominio es \(x<b<0\). Aquí \(bx+6b=b(x+6)\). Dado que \(x\) está a la izquierda de \(b\), y \(b<0\), los valores van desde \(b^2+6b\) (en \(x\to b^{-}\)) hasta \(+\infty\) (cuando \(x\to-\infty\)). Así este trozo cubre aproximadamente \((b^2+6b,\ +\infty)\).
- Trozo \(x\ge b\): como \(b<0\), este dominio incluye desde un número negativo hasta \(+\infty\). La parábola \(bx^2\) abre hacia abajo. En \(x=b\), vale \(b^3<0\). El máximo de esta parábola en el dominio \(x\ge b\) ocurre en \(x=0\) y vale \(0\). Luego este trozo cubre \((-\infty,\ 0]\) (con certeza: en \(0\) vale \(0\), y al crecer \(x\) va a \(-\infty\), y el resto de la parábola entre \(b\) y \(0\) da valores de \(b^3\) a \(0\), todos \(\le 0\)).

Entonces para cubrir todo \(\mathbb R\), el trozo izquierdo debe cubrir desde un valor suficientemente bajo hasta \(+\infty\), y el derecho cubre \((-\infty,0]\). El hueco posible está entre \(0\) y el inicio del trozo izquierdo \(b^2+6b\).

Necesitamos que el trozo izquierdo empiece a más tardar en \(0\):

\[
b^2+6b \le 0.
\]

Resolvemos:

\[
b(b+6)\le 0.
\]

Las raíces son \(0\) y \(-6\). Como la parábola abre hacia arriba, la desigualdad se cumple para

\[
-6\le b\le 0.
\]

Con \(b<0\), obtenemos:

\[
-6\le b<0.
\]

Como pedimos el mayor valor de \(b\), los candidatos son \(b=3\) (rama positiva) y los negativos hasta \(-6\). Claramente el mayor es \(b=3\).

## Verificación en \(b=3\)

Para \(b=3\):

\[
g(x)=
\begin{cases}
3x^2, & x\ge 3,\\
3x+18, & x<3.
\end{cases}
\]

- Si \(x<3\), \(g(x)=3x+18\), que va de \(-\infty\) hasta acercarse a \(27\) cuando \(x\to 3^{-}\).
- Si \(x\ge 3\), \(g(x)=3x^2\), que en \(x=3\) vale \(27\) y crece hasta \(+\infty\).

No hay hueco: en \(27\) ambos trozos coinciden. Por tanto la gráfica corta toda recta horizontal.

\[
\boxed{3}
\]