

Sean los puntos del arreglo

\[
(x,y),\qquad x=0,1,\dots,n-1,\quad y=0,1,2.
\]

La altura total disponible es \(2\) unidades.

Cualquier cuadrado con vértices en puntos de la retícula tiene un lado dado por un vector entero \((a,b)\), y el lado perpendicular \((-b,a)\). Su extensión vertical es

\[
|a|+|b|.
\]

Como el arreglo solo tiene altura \(2\), debemos tener

\[
|a|+|b|\le 2.
\]

Las posibilidades, salvo simetrías, son:

1. \((1,0)\): cuadrados de lado \(1\).
2. \((2,0)\): cuadrados de lado \(2\).
3. \((1,1)\): cuadrados inclinados de lado \(\sqrt{2}\).

Estos son exactamente los tres tamaños mencionados.

Ahora contamos cuántos hay de cada tipo.

**Cuadrados de lado \(1\):**  
Hay \(n-1\) posiciones horizontales y \(2\) posiciones verticales:

\[
2(n-1).
\]

**Cuadrados de lado \(2\):**  
Ocupan una caja \(2\times 2\), así que hay \(n-2\) posiciones horizontales y solo \(1\) vertical:

\[
n-2.
\]

**Cuadrados inclinados de lado \(\sqrt{2}\):**  
Cada uno ocupa también una caja \(2\times 2\), con los vértices en los puntos medios de los lados de esa caja. Hay uno por cada caja \(2\times 2\), es decir:

\[
n-2.
\]

Por tanto, el número total de cuadrados es

\[
2(n-1)+(n-2)+(n-2)=4n-6.
\]

Nos dicen que este total es \(86\):

\[
4n-6=86.
\]

Entonces

\[
4n=92 \quad\Rightarrow\quad n=23.
\]

\[
\boxed{23}
\]