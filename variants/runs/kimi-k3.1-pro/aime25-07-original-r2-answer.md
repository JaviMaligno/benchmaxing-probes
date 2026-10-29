Sea \(XY\) la última palabra, con \(X<Y\). Cada una de las otras cinco parejas debe contener una letra anterior a \(X\); de lo contrario, alguna tendría su primera letra después de \(X\). Por tanto, deben existir al menos cinco letras anteriores a \(X\), así que \(X\ge F\).

En consecuencia, si la última palabra contiene \(G\), solo hay dos casos:

1. **La última palabra es \(FG\).**  
   Las cinco letras \(A,B,C,D,E\) deben emparejarse con \(H,I,J,K,L\), una en cada pareja. Esto puede hacerse de
   \[
   5!=120
   \]
   maneras.

2. **La última palabra es \(GY\), con \(Y\in\{H,I,J,K,L\}\).**  
   Hay \(5\) opciones para \(Y\). Quedan seis letras anteriores a \(G\), namely \(A,\dots,F\), y cuatro posteriores. Cada una de estas cuatro debe emparejarse con una letra distinta de \(A,\dots,F\); las dos letras restantes forman la última pareja. El número de emparejamientos es
   \[
   5\cdot(6\cdot5\cdot4\cdot3)=1800.
   \]

El número total de emparejamientos de las doce letras es
\[
11!!=10395.
\]
Por tanto, la probabilidad buscada es
\[
\frac{120+1800}{10395}
=\frac{1920}{10395}
=\frac{128}{693}.
\]
Como la fracción ya es irreducible, \(m+n=128+693\).

\[
\boxed{821}
\]