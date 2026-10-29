Consideremos una recta vertical genérica, que no coincida con ningún borde vertical de las piezas. Las piezas que atraviesa la dividen en segmentos de longitudes \(4\) o \(5\). Si hay \(a\) segmentos de longitud \(4\) y \(b\) de longitud \(5\), entonces
\[
4a+5b=20.
\]
Las únicas soluciones no negativas son
\[
(a,b)=(5,0)\qquad\text{y}\qquad(a,b)=(0,4).
\]
Por tanto, a lo largo de cada recta vertical todas las piezas tienen la misma orientación. En consecuencia, los cambios de orientación producen cortes verticales completos: el rectángulo se divide en franjas verticales, cada una con una sola orientación.

- Una franja de ancho \(4\) se rellena de forma única con cuatro piezas de \(5\times4\), apiladas verticalmente.
- Una franja de ancho \(5\) se rellena de forma única con cinco piezas de \(4\times5\), apiladas verticalmente.

Además, toda franja más ancha se subdivide necesariamente en estas franjas elementales. Así, basta contar las sucesiones ordenadas de anchos \(4\) y \(5\) cuya suma sea \(28\):
\[
4a+5b=28.
\]
Hay dos posibilidades:

1. \(a=7,\ b=0\): da \(1\) disposición.
2. \(a=2,\ b=4\): las dos franjas de ancho \(4\) y las cuatro de ancho \(5\) pueden ordenarse de
   \[
   \binom{6}{2}=15
   \]
   maneras.

Como las reflexiones y rotaciones se consideran distintas, no identificamos ninguna de estas disposiciones. El total es \(1+15=16\).

\[
\boxed{16}
\]