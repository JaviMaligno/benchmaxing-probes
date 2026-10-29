Contamos según el número de lados rojos **interiores**. Cada lado interior rojo satisface simultáneamente la condición de los dos cuadrados que lo comparten.

- **0 lados interiores rojos:** cada cuadrado debe tener rojo uno de sus 2 lados exteriores. Hay \(2^4=16\) coloraciones.
- **1 lado interior rojo:** hay 4 opciones para ese lado. Cada uno de los otros dos cuadrados tiene 2 lados exteriores disponibles, lo que da \(4\cdot2^2=16\) coloraciones.
- **2 lados interiores rojos:** deben ser disjuntos y cubrir los cuatro cuadrados. Solo hay 2 posibilidades: ambos horizontales o ambos verticales.

No pueden existir más de 2 lados interiores rojos. Por tanto, el total es
\[
16+16+2=\boxed{34}.
\]