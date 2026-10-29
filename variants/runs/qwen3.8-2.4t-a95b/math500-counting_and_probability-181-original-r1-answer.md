

En una retícula rectangular de \(3\) filas y \(n\) columnas de puntos, solo hay tres tamaños posibles de cuadrados:

1. **Cuadrados de lado \(1\)** (orientados con la retícula):  
   Hay \(2\) filas de cuadrados unitarios y \(n-1\) posiciones horizontales:
   \[
   2(n-1)
   \]

2. **Cuadrados de lado \(2\)** (orientados con la retícula):  
   Solo cabe verticalmente una posición, y hay \(n-2\) posiciones horizontales:
   \[
   n-2
   \]

3. **Cuadrados inclinados de lado \(\sqrt{2}\)**:  
   Cada uno ocupa un bloque de \(3\) columnas consecutivas, con vértices del tipo
   \[
   (i,1),\ (i+1,0),\ (i+2,1),\ (i+1,2)
   \]
   Así que también hay
   \[
   n-2
   \]

El total de cuadrados es
\[
2(n-1)+(n-2)+(n-2)=4n-6.
\]

Dado que el total es \(70\),
\[
4n-6=70
\]
\[
4n=76
\]
\[
n=19.
\]

\[
\boxed{19}
\]