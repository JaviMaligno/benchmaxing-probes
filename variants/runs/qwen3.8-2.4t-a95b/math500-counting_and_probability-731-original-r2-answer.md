

Coloca el centro en \(O=(0,0)\). Como \(AB/AD=k\), podemos tomar

\[
A=(-k,1),\quad B=(k,1),\quad C=(k,-1),\quad D=(-k,-1).
\]

El área del rectángulo es

\[
(2k)(2)=4k.
\]

Para un punto \(P=(x,y)\), estar más cerca de \(O\) que del vértice \(B=(k,1)\) significa

\[
x^2+y^2 \le (x-k)^2+(y-1)^2.
\]

Simplificando:

\[
kx+y \le \frac{k^2+1}{2}.
\]

Aplicando las cuatro condiciones para los cuatro vértices, obtenemos

\[
|kx|+|y|\le \frac{k^2+1}{2}.
\]

Por simetría, basta calcular el área en el primer cuadrante y multiplicar por \(4\). En el primer cuadrante:

\[
0\le x\le k,\qquad 0\le y\le 1,\qquad kx+y\le \frac{k^2+1}{2}.
\]

Haz el cambio \(u=kx\), \(v=y\). Entonces el primer cuadrante se convierte en el rectángulo

\[
0\le u\le k^2,\qquad 0\le v\le 1,
\]

y la recta límite es

\[
u+v=\frac{k^2+1}{2}.
\]

Esta recta pasa por el centro del rectángulo \(\left(\frac{k^2}{2},\frac12\right)\), así que por simetría central divide ese rectángulo en dos áreas iguales. Por tanto, el área admisible en coordenadas \((u,v)\) es

\[
\frac12\cdot k^2\cdot 1=\frac{k^2}{2}.
\]

Como \(dx\,dy=\frac1k\,du\,dv\), el área admisible en el primer cuadrante es

\[
\frac1k\cdot \frac{k^2}{2}=\frac{k}{2}.
\]

El área total favorable es

\[
4\cdot \frac{k}{2}=2k.
\]

Por tanto, la probabilidad pedida es

\[
\frac{2k}{4k}=\frac12.
\]

\[
\boxed{\frac12}
\]