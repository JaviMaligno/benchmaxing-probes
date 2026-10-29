

Dividimos las 6 columnas en los tres bloques \(B_1,B_2,B_3\), cada uno de tamaño \(3\times 2\). Cada fila debe ser una permutación de \(\{1,2,3,4,5,6\}\).

**1. Primera fila.**  
La primera fila puede elegirse de

\[
6! = 720
\]

formas.

**2. Segunda fila, fijada la primera.**  
Supongamos que en la primera fila los tres bloques contienen las parejas

\[
P_1,\;P_2,\;P_3,
\]

donde \(P_i\) está en el bloque \(B_i\). Para que cada bloque tenga 6 números distintos, la segunda fila no puede poner en \(B_i\) ningún número de \(P_i\). Además, la segunda fila debe usar cada número una vez.

Contemos primero solo cómo asignar los 6 números a los tres bloques, con 2 números por bloque:

- Los números de \(P_1\) pueden ir a \(B_2\) o \(B_3\).
- Los números de \(P_2\) pueden ir a \(B_1\) o \(B_3\).
- Los números de \(P_3\) pueden ir a \(B_1\) o \(B_2\).

Sea \(t\) el número de elementos de \(P_3\) que van a \(B_1\). Entonces:

- \(B_1\) recibe \(t\) elementos de \(P_3\), así que necesita \(2-t\) elementos de \(P_2\).
- \(B_2\) recibe los \(2-t\) elementos restantes de \(P_3\), así que necesita \(t\) elementos de \(P_1\).
- \(B_3\) recibe automáticamente los elementos restantes.

Para cada \(t\in\{0,1,2\}\), hay

\[
\binom{2}{t}^3
\]

formas de elegir esos elementos. Por tanto, el número de asignaciones por bloques es

\[
\sum_{t=0}^2 \binom{2}{t}^3 = 1^3+2^3+1^3 = 10.
\]

Dentro de cada bloque, los 2 números pueden ordenarse en las 2 columnas de \(2!\) formas. Así que la segunda fila tiene

\[
10\cdot 2^3 = 80
\]

posibilidades.

**3. Tercera fila.**  
Dadas las dos primeras filas, en cada bloque quedan exactamente 2 números ausentes; la tercera fila debe colocarlos allí. En cada bloque hay \(2!\) órdenes posibles, así que hay

\[
2^3 = 8
\]

formas para la tercera fila.

Además, la tercera fila automáticamente contiene los 6 números una vez cada uno: cada número aparece en la primera fila en un bloque y en la segunda fila en un bloque distinto, por lo que falta exactamente en el tercer bloque.

**4. Total.**

\[
720\cdot 80\cdot 8 = 460800.
\]

Factorizando:

\[
460800 = 2^{11}\cdot 3^2\cdot 5^2.
\]

Entonces

\[
p\cdot a+q\cdot b+r\cdot c
=2\cdot 11+3\cdot 2+5\cdot 2
=22+6+10=38.
\]

\[
\boxed{38}
\]