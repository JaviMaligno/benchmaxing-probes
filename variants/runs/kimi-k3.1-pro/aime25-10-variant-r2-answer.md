Fijemos la primera fila como \(1,2,3,4,5,6\); al final multiplicaremos por \(6!\), pues cualquier permutación inicial es equivalente. Definimos
\[
A=\{1,2\},\qquad B=\{3,4\},\qquad C=\{5,6\}.
\]

En la segunda fila, los pares colocados en los tres bloques deben elegirse, respectivamente, de
\[
B\cup C,\qquad A\cup C,\qquad A\cup B,
\]
y entre los tres deben usar cada cifra exactamente una vez.

Sea \(k\) el número de elementos de \(A\) colocados en el segundo bloque. Las demás distribuciones quedan determinadas por esta elección, y para cada grupo hay \(\binom{2}{k}\) maneras de elegir las cifras. Por tanto, el número de distribuciones posibles es
\[
\sum_{k=0}^{2}\binom{2}{k}^3
=1+8+1=10.
\]

Dentro de cada bloque, el par de la segunda fila puede ordenarse de \(2\) maneras. El par correspondiente de la tercera fila queda determinado como conjunto, pero también admite \(2\) ordenaciones. Así, hay \(2^6\) ordenaciones internas.

El total es
\[
6!\cdot 10\cdot 2^6=460800
=2^{11}\cdot 3^2\cdot 5^2.
\]
En consecuencia,
\[
p a+q b+r c=2\cdot11+3\cdot2+5\cdot2
=\boxed{38}.
\]