

Coloquemos los puntos del grid en coordenadas  
\[
(x,y)\quad\text{con }x=0,1,\dots,n-1,\quad y=0,1,2.
\]

Como solo hay 3 filas de puntos, la altura disponible es 2 unidades.

Los cuadrados posibles se clasifican según su lado:

1. **Cuadrados de lado 1**  
   Son los cuadrados alineados con la cuadrícula de tamaño \(1\times 1\).  
   Hay \(n-1\) posiciones horizontales y 2 posiciones verticales:
   \[
   2(n-1).
   \]

2. **Cuadrados de lado \(\sqrt{2}\)**  
   Son los cuadrados inclinados formados dentro de un bloque \(2\times 2\) de puntos.  
   Cada bloque de 3 columnas consecutivas aporta 1 cuadrado de este tipo.  
   Hay \(n-2\) bloques así:
   \[
   n-2.
   \]

3. **Cuadrados de lado 2**  
   Son los cuadrados alineados de tamaño \(2\times 2\).  
   Hay \(n-2\) posiciones horizontales y solo 1 vertical:
   \[
   n-2.
   \]

Por lo tanto, el número total de cuadrados es
\[
2(n-1)+(n-2)+(n-2)=4n-6.
\]

Nos dicen que el total es 70:
\[
4n-6=70.
\]

Entonces
\[
4n=76 \quad\Rightarrow\quad n=19.
\]

\[
\boxed{19}
\]