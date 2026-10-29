

Tomemos el rectángulo con lado horizontal \(20\) y lado vertical \(28\). Cada pieza \(4\times 5\) puede colocarse en orientación \(5\times 4\) (horizontal) o \(4\times 5\) (vertical).

Consideremos una línea horizontal genérica, que no pase por ningún lado horizontal de las piezas pequeñas. Supongamos que corta \(h\) piezas horizontales \(5\times 4\) y \(v\) piezas verticales \(4\times 5\). Como la línea debe cubrir todo el ancho \(20\),

\[
5h+4v=20.
\]

Las únicas soluciones enteras no negativas son

\[
(h,v)=(4,0)\quad\text{o}\quad (0,5).
\]

Es decir, toda sección horizontal genérica está formada o bien por \(4\) rectángulos horizontales, o bien por \(5\) rectángulos verticales. No hay secciones mixtas.

Por tanto, la partición se organiza en capas horizontales:

- Una capa de tipo vertical consiste en \(5\) rectángulos \(4\times 5\) colocados lado a lado; su altura es \(5\).
- Una capa de tipo horizontal consiste en \(4\) rectángulos \(5\times 4\) colocados lado a lado; su altura es \(4\).

Además, la distribución interna de cada capa es única, porque partir el ancho \(20\) en \(5\) segmentos de longitud \(4\), o en \(4\) segmentos de longitud \(5\), no admite variaciones.

Sea \(r\) el número de capas verticales de altura \(5\), y \(s\) el número de capas horizontales de altura \(4\). Entonces

\[
5r+4s=28.
\]

Módulo \(4\), obtenemos \(r\equiv 0\pmod 4\). Como \(5r\le 28\), las posibilidades son:

1. \(r=0,\ s=7\): todas las capas son horizontales. Esto da \(1\) partición.
2. \(r=4,\ s=2\): hay \(6\) capas en total, de las cuales \(2\) son horizontales y \(4\) verticales. El número de ordenaciones posibles es

\[
\binom{6}{2}=15.
\]

Como las rotaciones y reflexiones se consideran distintas, contamos cada ordenación de capas por separado, sin identificar configuraciones simétricas.

En total,

\[
1+15=16.
\]

\[
\boxed{16}
\]