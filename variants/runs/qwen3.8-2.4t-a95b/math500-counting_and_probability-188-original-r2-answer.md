

Elegimos \(x,y\) de forma uniforme e independiente en \((0,3)\), así que el área total posible es

\[
3\cdot 3=9.
\]

Para que exista un triángulo de lados \(1,x,y\), se deben cumplir las desigualdades triangulares:

\[
x+y>1,\qquad x+1>y,\qquad y+1>x.
\]

Las dos últimas equivalen a

\[
|x-y|<1.
\]

Por tanto, la región favorable dentro del cuadrado \((0,3)\times(0,3)\) está dada por

\[
x+y>1 \quad \text{y} \quad |x-y|<1.
\]

Calculamos el área favorable.

La condición \(|x-y|<1\) describe una franja diagonal de ancho 1 alrededor de \(y=x\). Dentro del cuadrado de lado 3, el área fuera de esa franja son dos triángulos rectángulos de catetos 2, cada uno con área

\[
\frac{1}{2}\cdot 2\cdot 2=2.
\]

Así que el área donde \(|x-y|<1\) es

\[
9-2-2=5.
\]

Pero también debemos excluir la región donde \(x+y\le 1\). Esa región es un triángulo rectángulo de catetos 1, con área

\[
\frac{1}{2}\cdot 1\cdot 1=\frac12.
\]

Ese triángulo está completamente dentro de la franja \(|x-y|<1\), así que el área favorable total es

\[
5-\frac12=\frac92.
\]

Por tanto, la probabilidad es

\[
\frac{\frac92}{9}=\frac12.
\]

\[
\boxed{\frac12}
\]