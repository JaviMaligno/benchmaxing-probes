Sea el número \(d_1d_2\cdots d_9\), usando cada dígito del \(1\) al \(9\) exactamente una vez.

Como \(22=2\cdot 11\), el número debe ser divisible entre \(2\) y entre \(11\).

1. **Divisibilidad entre \(2\):** el último dígito \(d_9\) debe ser par.

2. **Divisibilidad entre \(11\):** la suma alternada
\[
(d_1+d_3+d_5+d_7+d_9)-(d_2+d_4+d_6+d_8)
\]
debe ser múltiplo de \(11\).

Definamos
\[
O=\{d_1,d_3,d_5,d_7,d_9\},\qquad E=\{d_2,d_4,d_6,d_8\}.
\]
Sea \(A=\sum_{d\in O}d\). Entonces \(\sum_{d\in E}d=45-A\), y la diferencia alternada es
\[
A-(45-A)=2A-45.
\]
Necesitamos que \(2A-45\) sea múltiplo de \(11\). Como \(A\) es la suma de cinco dígitos distintos, \(15\le A\le 35\). Los únicos valores posibles son
\[
A=17,\qquad A=28.
\]

Para cada conjunto posible \(O\), el dígito final \(d_9\) debe ser un dígito par de \(O\). Si \(O\) tiene \(k\) dígitos pares, entonces hay
\[
k\cdot 4!\cdot 4!
\]
números: \(k\) opciones para \(d_9\), luego \(4!\) ordenamientos en las demás posiciones impares y \(4!\) en las posiciones pares.

Para \(A=17\), los conjuntos posibles son
\[
\{1,2,3,4,7\},\qquad \{1,2,3,5,6\},
\]
cada uno con \(k=2\). Así,
\[
\sum k=4.
\]

Para \(A=28\), la enumeración da los conjuntos
\[
\begin{aligned}
&\{3,4,6,7,8\},\{3,4,5,7,9\},\{2,5,6,7,8\},\\
&\{2,4,6,7,9\},\{2,4,5,8,9\},\{2,3,6,8,9\},\\
&\{1,5,6,7,9\},\{1,4,6,8,9\},\{1,3,7,8,9\}.
\end{aligned}
\]
Los valores de \(k\) son
\[
3,1,3,3,3,3,1,3,1,
\]
cuya suma es \(21\).

Por lo tanto,
\[
N=(4+21)\cdot 4!\cdot 4!
=25\cdot 576
=14400.
\]
La diferencia pedida es
\[
14400-14025=375.
\]

\[
\boxed{375}
\]