Sea \(i\) el número de lados rojos interiores (compartidos por dos cuadrados) y \(b\) el número de lados rojos del borde.

Cada lado interior rojo cuenta para \(2\) cuadrados, mientras que cada lado de borde rojo cuenta para \(1\). Como hay \(4\) cuadrados y cada uno debe tener exactamente \(1\) lado rojo:

\[
2i+b=4
\]

Entonces \(i\) puede ser \(0,1,2\).

- \(i=0\): todos los lados rojos están en el borde. Cada cuadrado tiene \(2\) lados de borde y debe elegir exactamente uno. Hay
  \[
  2^4=16
  \]
  coloraciones.

- \(i=1\): hay \(4\) opciones para elegir el lado interior rojo. Este lado satisface a sus dos cuadrados adyacentes; los otros dos cuadrados deben elegir uno de sus \(2\) lados de borde cada uno. Hay
  \[
  4\cdot 2^2=16
  \]
  coloraciones.

- \(i=2\): los dos lados rojos deben ser interiores y no pueden compartir un cuadrado. Las únicas posibilidades son los dos lados interiores verticales o los dos horizontales. Hay
  \[
  2
  \]
  coloraciones.

Total:

\[
16+16+2=34
\]

\[
\boxed{34}
\]