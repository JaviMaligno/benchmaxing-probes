Aplicar una misma permutación de los números \(1,\dots,6\) a todas las casillas no cambia la validez del tablero. Fijemos entonces la primera fila como

\[
1,2 \mid 3,4 \mid 5,6,
\]

y al final multiplicaremos por \(6!\).

Con esa primera fila, las filas \(2\) y \(3\) en cada bloque deben usar los números complementarios de la primera fila:

\[
S_1=\{3,4,5,6\},\quad
S_2=\{1,2,5,6\},\quad
S_3=\{1,2,3,4\}.
\]

Sea \(T_i\) el conjunto de los dos números que van en la fila \(2\) del bloque \(i\). Los conjuntos \(T_1,T_2,T_3\) deben formar una partición de \(\{1,\dots,6\}\), con \(T_1\subset S_1\), \(T_2\subset S_2\), \(T_3\subset S_3\).

Contamos esas particiones según \(T_1\):

- Si \(T_1=\{3,4\}\), entonces forzosamente \(T_2=\{5,6\}\) y \(T_3=\{1,2\}\): \(1\) caso.
- Si \(T_1=\{5,6\}\), entonces \(T_2=\{1,2\}\) y \(T_3=\{3,4\}\): \(1\) caso.
- Si \(T_1\) tiene un elemento de \(\{3,4\}\) y uno de \(\{5,6\}\), hay \(2\cdot2=4\) elecciones. El número restante de \(\{3,4\}\) va al bloque \(3\), el restante de \(\{5,6\}\) al bloque \(2\), y \(1,2\) se reparten entre los bloques \(2\) y \(3\) de \(2\) maneras. Esto da \(4\cdot2=8\) casos.

Así hay

\[
1+1+8=10
\]

particiones válidas.

Para cada partición, en cada bloque la fila \(2\) puede ordenar sus dos números de \(2\) maneras y la fila \(3\) también, luego hay \(2\cdot2=4\) ordenes por bloque. En total,

\[
10\cdot 4^3=10\cdot64=640
\]

tableros normalizados. Multiplicando por las \(6!\) posibles primeras filas,

\[
6!\cdot640=720\cdot640=460800.
\]

Su factorización es

\[
460800=2^{11}\cdot 3^2\cdot 5^2.
\]

Por lo tanto,

\[
2\cdot 11+3\cdot 2+5\cdot 2=38.
\]

\[
\boxed{38}
\]