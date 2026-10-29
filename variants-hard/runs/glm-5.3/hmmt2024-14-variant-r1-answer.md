Los puntos forman un grafo de \(3\) filas y \(20\) columnas, con movimientos horizontales o verticales. Un recorrido válido es un camino hamiltoniano: sus dos extremos tienen grado \(1\), y todos los demás vértices tienen grado \(2\).

**1. Primera columna.**  
El vértice inicial \((2,1)\) debe tener grado \(1\). Si el primer movimiento fuera hacia \((2,2)\), entonces \((1,1)\) y \((3,1)\) también quedarían con grado \(1\), dando tres extremos; imposible. Así que el primer movimiento es vertical.

Si sube a \((1,1)\), las aristas \((1,1)-(1,2)\) y \((3,1)-(3,2)\) quedan forzadas, y el otro extremo es \((3,1)\). Al quitar la primera columna, las columnas restantes forman un camino hamiltoniano en una rejilla \(3\times 19\), con extremos \((1,2)\) y \((3,2)\). El caso de bajar es simétrico, así que la respuesta es \(2C_{19}\), donde \(C_m\) cuenta caminos en \(3\times m\) con extremos \((1,1)\) y \((3,1)\).

**2. Recurrencia.**  
Sean \(T_m\), \(C_m\), \(B_m\) los números de caminos con extremos arriba-medio, arriba-abajo y medio-abajo en la primera columna. Al quitar una columna:

\[
T_m=C_{m-1},\qquad B_m=C_{m-1},\qquad C_m=T_{m-1}+B_{m-1}.
\]

Con base \(C_1=1\), \(T_1=B_1=0\). Por simetría \(T_m=B_m\), luego

\[
C_{2k+1}=2C_{2k-1}.
\]

Por tanto \(C_{19}=C_{2\cdot 9+1}=2^9=512\).

Finalmente,

\[
\boxed{1024}
\]