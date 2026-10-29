

Numeramos los vértices del polígono como \(0,1,\dots,27\) módulo \(28\).

En un polígono regular, dos segmentos entre vértices tienen la misma longitud si y solo si la distancia cíclica entre sus extremos es la misma. Así, fijamos una distancia \(d\), con \(1\le d\le 14\).

Para \(d<14\), los segmentos permitidos unen cada vértice \(i\) con \(i\pm d\). Este grafo se descompone en

\[
g=\gcd(28,d)
\]

ciclos, cada uno de longitud \(28/g\).

Un ciclo impar no puede tener emparejamiento perfecto. Un ciclo par tiene exactamente \(2\) emparejamientos perfectos. Por tanto, si \(28/g\) es par y \(d<14\), el número de configuraciones es \(2^g\).

Analizamos los casos:

- \(d=1,3,5,9,11,13\): \(\gcd(28,d)=1\). Hay un solo ciclo de longitud \(28\), dando \(2\) configuraciones por cada \(d\).  
  Total: \(6\cdot 2=12\).

- \(d=2,6,10\): \(\gcd(28,d)=2\). Hay dos ciclos de longitud \(14\), dando \(2^2=4\) configuraciones por cada \(d\).  
  Total: \(3\cdot 4=12\).

- \(d=4,8,12\): \(\gcd(28,d)=4\). Hay cuatro ciclos de longitud \(7\), que son impares, así que no hay configuraciones.  
  Total: \(0\).

- \(d=7\): \(\gcd(28,7)=7\). Hay siete ciclos de longitud \(4\), dando \(2^7=128\) configuraciones.

- \(d=14\): los segmentos son los \(14\) diámetros. Para cubrir todos los vértices, deben usarse todos, así que hay \(1\) configuración.

Sumando:

\[
12+12+0+128+1=153.
\]

\[
\boxed{153}
\]