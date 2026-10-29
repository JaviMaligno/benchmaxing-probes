## Planteamiento

Etiquetemos los segmentos: los **verticales** están en las tres líneas $x=0,1,2$ (dos en cada una), y los **horizontales** en las tres líneas $y=0,1,2$ (dos en cada una).

Uso una matriz de transferencia recorriendo las líneas verticales de izquierda a derecha. El **estado** de la línea $x=c$ es el par de colores de sus dos segmentos verticales $(v_0,v_1)$, con $1=$ rojo: hay 4 estados.

## Peso de una columna de cuadrados

Dadas las verticales izquierdas $a=(a_0,a_1)$ y derechas $b=(b_0,b_1)$ de una columna, sean $s_0=a_0+b_0$ y $s_1=a_1+b_1$ los rojos verticales de cada cuadrado. Los tres horizontales $h_0,h_1,h_2$ de esa columna deben cumplir
$$h_0+h_1=2-s_0,\qquad h_1+h_2=2-s_1.$$

Con $t=2-s$, el conjunto de valores admisibles de $h_1$ es $S(0)=\{0\}$, $S(1)=\{0,1\}$, $S(2)=\{1\}$, y el número de soluciones es $|S(t_0)\cap S(t_1)|$:

- $2$ si $s_0=s_1=1$,
- $0$ si $\{s_0,s_1\}=\{0,2\}$,
- $1$ en los demás casos.

Con el orden de estados $00,01,10,11$:
$$W=\begin{pmatrix}1&1&1&2\\1&0&2&1\\1&2&0&1\\2&1&1&1\end{pmatrix}$$

## Conteo

El total es $\sum_{a,b,c} W[a,b]\,W[b,c]=\sum_b(\text{suma de columna }b)(\text{suma de fila }b)$.

Sumas de fila: $5,4,4,5$. Sumas de columna: $5,4,4,5$.

$$5\cdot5+4\cdot4+4\cdot4+5\cdot5=25+16+16+25=82$$

\boxed{82}