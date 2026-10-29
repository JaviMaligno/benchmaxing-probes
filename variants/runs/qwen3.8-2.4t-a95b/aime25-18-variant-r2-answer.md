

Nombramos los cuatro cuadrados como \(A, B, C, D\) en forma de cuadrícula \(2\times 2\).

Hay \(4\) segmentos internos compartidos: \(AB\), \(BD\), \(DC\), \(CA\), que forman un ciclo de \(4\) aristas. Los otros \(8\) segmentos están en el borde exterior y pertenecen a un solo cuadrado.

Si un segmento interno se colorea rojo, entonces cuenta como lado rojo para los dos cuadrados que comparte. Por tanto, no podemos tener dos segmentos internos rojos que toquen el mismo cuadrado. Es decir, los segmentos internos rojos deben formar un matching en el ciclo \(C_4\).

Contamos según cuántos segmentos internos hay rojos:

- **0 internos rojos:** cada cuadrado debe tener exactamente uno de sus dos lados exteriores rojo.  
  Cada cuadrado tiene \(2\) opciones, independientes:  
  \[
  2^4 = 16.
  \]

- **1 interno rojo:** elegimos cuál de los \(4\) segmentos internos es rojo.  
  Los dos cuadrados que comparte ya quedan satisfechos.  
  Los otros dos cuadrados eligen uno de sus dos lados exteriores:  
  \[
  4 \cdot 2^2 = 16.
  \]

- **2 internos rojos:** para no compartir cuadrados, deben ser opuestos en el ciclo.  
  Hay \(2\) maneras, y todos los cuadrados quedan satisfechos:  
  \[
  2.
  \]

No puede haber \(3\) o más segmentos internos rojos, porque algún cuadrado tendría más de un lado rojo.

Total:

\[
16+16+2=34.
\]

\[
\boxed{34}
\]