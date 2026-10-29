Sea

\[
A=\arccos x,\quad B=\arccos 2x,\quad C=\arccos 3x,
\]

de modo que \(A+B+C=\pi\), con \(\cos A=x,\ \cos B=2x,\ \cos C=3x\).

Como \(A+B=\pi-C\),

\[
\cos(A+B)=\cos(\pi-C)=-\cos C=-3x.
\]

Usando la identidad de la suma:

\[
\cos(A+B)=\cos A\cos B-\sin A\sin B=2x^2-\sin A\sin B.
\]

Igualando:

\[
2x^2-\sin A\sin B=-3x
\]

\[
\sin A\sin B=2x^2+3x.
\]

Como \(A,B\in[0,\pi]\), se tiene \(\sin A,\sin B\ge 0\), así que \(2x^2+3x\ge0\), lo cual fuerza \(x\ge0\) (pues \(x\in[-1/3,1/3]\)).

Ahora elevamos al cuadrado:

\[
\sin^2 A\sin^2 B=(2x^2+3x)^2.
\]

Como \(\sin^2 A=1-x^2\) y \(\sin^2 B=1-4x^2\),

\[
(1-x^2)(1-4x^2)=(2x^2+3x)^2.
\]

Expandimos ambos lados:

\[
1-5x^2+4x^4=4x^4+12x^3+9x^2.
\]

Cancelando \(4x^4\):

\[
1-5x^2=12x^3+9x^2
\]

\[
12x^3+14x^2-1=0.
\]

Este cúbico no tiene raíces racionales (se comprueba con el criterio de la raíz racional), luego es irreducible sobre \(\mathbb{Q}\). Por tanto, es el polinomio mínimo de \(x\), y cualquier polinomio cúbico con coeficientes enteros que tenga a \(x\) como raíz debe ser un múltiplo entero de este (o de su negativo).

Así, el polinomio con menor suma de valores absolutos de coeficientes es

\[
12x^3+14x^2+0x-1=0,
\]

con

\[
|a|+|b|+|c|+|d|=12+14+0+1=27.
\]

\[
\boxed{27}
\]