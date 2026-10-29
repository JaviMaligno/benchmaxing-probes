

Sea

\[
f(x)=2\prod_{i=1}^n (x-r_i),
\]

donde \(r_1,\dots,r_n\) son las raíces enteras distintas.

Por las fórmulas de Vieta,

\[
a_0 = 2(-1)^n \prod_{i=1}^n r_i = 66,
\]

así que

\[
\prod_{i=1}^n r_i = 33(-1)^n.
\]

En particular,

\[
\left|\prod_{i=1}^n r_i\right|=33=3\cdot 11.
\]

Además,

\[
a_{n-1}=-2\sum_{i=1}^n r_i,
\]

por lo que queremos minimizar

\[
|a_{n-1}|=2\left|\sum_{i=1}^n r_i\right|.
\]

Como el producto de los valores absolutos de las raíces es \(33\), los valores absolutos posibles de las raíces solo pueden provenir de \(1,3,11,33\). Además, como las raíces son distintas, a lo más podemos incluir \(1\) y \(-1\).

Consideramos los casos.

### Caso 1: aparece \(33\)

Las raíces pueden ser \(\pm 33\), posiblemente junto con alguno de \(1,-1\). Las sumas posibles tienen valor absoluto mínimo \(33\), lo que da

\[
|a_{n-1}|\ge 66.
\]

### Caso 2: aparecen \(3\) y \(11\)

Las raíces incluyen uno de \(\pm 3\) y uno de \(\pm 11\), posiblemente con \(1\) o \(-1\).

- Sin \(1\) ni \(-1\): \(n=2\). El producto debe ser positivo, así que las raíces son \(\{3,11\}\) o \(\{-3,-11\}\). La suma tiene valor absoluto \(14\), dando

\[
|a_{n-1}|=28.
\]

- Con exactamente uno de \(1,-1\): \(n=3\). El producto debe ser negativo. Las combinaciones válidas dan sumas

\[
3-11+1=-7,\qquad -3+11+1=9,
\]
\[
3+11-1=13,\qquad -3-11-1=-15.
\]

El menor valor absoluto de la suma es \(7\), por lo que

\[
|a_{n-1}|=2\cdot 7=14.
\]

- Con \(1\) y \(-1\): \(n=4\). Las sumas posibles tienen valor absoluto mínimo \(8\), dando

\[
|a_{n-1}|=16.
\]

El mínimo global es \(14\). Se alcanza, por ejemplo, con

\[
f(x)=2(x-3)(x+11)(x-1)=2x^3+14x^2-82x+66.
\]

\[
\boxed{14}
\]