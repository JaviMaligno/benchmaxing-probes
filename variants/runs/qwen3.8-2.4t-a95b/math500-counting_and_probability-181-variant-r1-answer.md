

Coloquemos los puntos en coordenadas \((x,y)\) con \(x=0,1,\dots,n-1\) y \(y=0,1,2\). La altura total disponible es \(2\).

Si un cuadrado tiene vértices en la red, uno de sus lados puede representarse con un vector entero \((a,b)\). Su altura total es \(|a|+|b|\), así que necesitamos

\[
|a|+|b|\le 2.
\]

Por tanto, los únicos tamaños posibles son:

1. **Cuadrados de lado \(1\)**: vector \((1,0)\).  
   Hay \(2\) filas de celdas unitarias y \(n-1\) columnas de celdas:
   \[
   2(n-1).
   \]

2. **Cuadrados de lado \(2\)**: vector \((2,0)\).  
   Deben ocupar las 3 filas y 3 columnas de puntos, es decir, 2 unidades de ancho. Hay \(n-2\) posiciones horizontales:
   \[
   n-2.
   \]

3. **Cuadrados inclinados de lado \(\sqrt{2}\)**: vector \((1,1)\).  
   En cada bloque de \(3\times 3\) puntos hay exactamente uno de estos cuadrados, con vértices en los puntos medios de los lados del bloque. Hay \(n-2\) bloques horizontales:
   \[
   n-2.
   \]

El número total de cuadrados es

\[
2(n-1)+(n-2)+(n-2)=4n-6.
\]

Nos dicen que este total es \(86\):

\[
4n-6=86
\]

\[
4n=92
\]

\[
n=23.
\]

\[
\boxed{23}
\]