Consideremos primero los **cuatro segmentos interiores**, que concurren en el vértice central. Cada cuadrado tiene dos de estos segmentos y dos segmentos exteriores.

Fijada la coloración de los segmentos interiores:

- Si un cuadrado ya tiene \(0\) o \(2\) lados interiores rojos, sus dos lados exteriores quedan determinados.
- Si tiene exactamente \(1\) lado interior rojo, necesita exactamente un lado exterior rojo, lo cual puede hacerse de \(2\) maneras.

Clasificamos según el número de segmentos interiores rojos:

\[
\begin{array}{c|c|c|c}
\text{Segmentos interiores rojos}&\text{Disposición}&\text{Casos}&\text{Coloraciones por caso}\\ \hline
0&-&1&1\\
1&-&4&2^2=4\\
2&\text{Opuestos}&2&2^4=16\\
2&\text{Adyacentes}&4&2^2=4\\
3&-&4&2^2=4\\
4&-&1&1
\end{array}
\]

Por tanto, el número total es
\[
1+4\cdot4+2\cdot16+4\cdot4+4\cdot4+1
=1+16+32+16+16+1
=82.
\]

\[
\boxed{82}
\]