Razonemos por partes.

En una cuadrícula \(2\times2\) hay \(4\) segmentos interiores y \(8\) segmentos exteriores. Cada cuadrado tiene exactamente \(2\) segmentos interiores y \(2\) exteriores.

Si un cuadrado tiene:
- \(0\) segmentos interiores rojos, entonces exactamente uno de sus dos segmentos exteriores debe ser rojo: \(2\) opciones.
- \(1\) segmento interior rojo, sus dos segmentos exteriores deben ser azules: \(1\) opción.
- \(2\) segmentos interiores rojos, ya tendría dos lados rojos, imposible.

Por tanto, los segmentos interiores rojos no pueden compartir cuadrado; forman un apareamiento en el ciclo de los cuatro cuadrados.

Contamos por el número de segmentos interiores rojos:

1. Ninguno rojo:  
   Cada uno de los cuatro cuadrados necesita uno de sus dos lados exteriores rojo, así que hay  
   \[
   2^4
   \]
   coloraciones.

2. Exactamente uno rojo:  
   Hay \(4\) formas de elegirlo. Los dos cuadrados que lo tocan ya tienen su lado rojo, y los otros dos cuadrados tienen \(2\) opciones cada uno. Luego hay  
   \[
   4\cdot 2^2
   \]
   coloraciones.

3. Dos rojos:  
   Deben ser segmentos interiores opuestos para no compartir cuadrado. Hay \(2\) pares opuestos, y entonces todos los lados exteriores son azules. Esto da  
   \[
   2
   \]
   coloraciones.

Sumando los casos:
\[
\boxed{34}
\]