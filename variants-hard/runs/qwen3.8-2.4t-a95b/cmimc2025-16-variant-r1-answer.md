

Voy a verificar el conteo con un pequeño cálculo por transferencia de columnas y, si es posible, una comprobación rápida por fuerza bruta.

Representa cada columna por el conjunto de filas ocupadas. Como no puede haber fichas verticalmente adyacentes, los estados permitidos para una columna de altura 4 son:

\[
\varnothing,\{1\},\{2\},\{3\},\{4\},\{1,3\},\{1,4\},\{2,4\}.
\]

Para dos columnas consecutivas \(A,B\), necesitamos:

1. \(A\cap B=\varnothing\), para que no haya fichas horizontalmente adyacentes.
2. Cada bloque \(2\times2\) formado por esas dos columnas debe tener al menos una ficha. Esto equivale a que \(A\cup B\) contenga al menos una fila en cada par consecutivo \(\{1,2\},\{2,3\},\{3,4\}\).

Las transiciones válidas son:

\[
\begin{aligned}
\varnothing &\leftrightarrow \{1,3\},\{2,4\},\\
\{1\} &\leftrightarrow \{3\},\{2,4\},\\
\{2\} &\leftrightarrow \{3\},\{4\},\{1,3\},\{1,4\},\\
\{3\} &\leftrightarrow \{1\},\{2\},\{1,4\},\{2,4\},\\
\{4\} &\leftrightarrow \{2\},\{1,3\},\\
\{1,3\} &\leftrightarrow \varnothing,\{2\},\{4\},\{2,4\},\\
\{1,4\} &\leftrightarrow \{2\},\{3\},\\
\{2,4\} &\leftrightarrow \varnothing,\{1\},\{3\},\{1,3\}.
\end{aligned}
\]

Sea \(N_k(s)\) el número de configuraciones de las primeras \(k\) columnas que terminan en el estado \(s\). Inicialmente \(N_1(s)=1\) para cada estado. Iterando con las transiciones anteriores:

\[
\begin{array}{c|cccccccc|c}
k & \varnothing & \{1\} & \{2\} & \{3\} & \{4\} & \{1,3\} & \{1,4\} & \{2,4\} & \text{Total}\\
\hline
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 8\\
2 & 2 & 2 & 4 & 4 & 2 & 4 & 2 & 4 & 24\\
3 & 8 & 8 & 12 & 12 & 8 & 12 & 8 & 12 & 80\\
4 & 24 & 24 & 40 & 40 & 24 & 40 & 24 & 40 & 256\\
5 & 80 & 80 & 128 & 128 & 80 & 128 & 80 & 128 & 832
\end{array}
\]

Por lo tanto, el número total de colocaciones válidas en la cuadrícula \(4\times5\) es

\[
\boxed{832}
\]