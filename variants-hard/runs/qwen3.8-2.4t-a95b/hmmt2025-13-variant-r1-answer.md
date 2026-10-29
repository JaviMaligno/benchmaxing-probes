En una distribución válida, miremos los **segmentos maximales consecutivos** de canicas que están en el mismo frasco.

1. Un segmento maximal de longitud \(1\) sería una canica sin ninguna canica adyacente en su frasco, lo cual está prohibido.

2. Cada frasco tiene exactamente \(4\) canicas. Para un frasco fijo, sus segmentos maximales tienen longitud al menos \(2\) y suman \(4\). Las únicas posibilidades son:
   - un segmento de longitud \(4\), o
   - dos segmentos de longitud \(2\).

   Por tanto, **todos los segmentos maximales tienen longitud par**.

3. Como empezamos en la canica \(1\) y todos los segmentos maximales tienen longitud par, las fronteras entre segmentos ocurren siempre después de una canica par. Así, las parejas
   \[
   \{1,2\},\{3,4\},\ldots,\{19,20\}
   \]
   quedan siempre dentro del mismo frasco.

4. Entonces el problema equivale a tomar estas \(10\) parejas distinguibles y agruparlas en \(5\) grupos de \(2\) parejas, pues cada frasco contiene \(4\) canicas. Recíprocamente, cualquier agrupación así es válida: cada canica tiene a su pareja adyacente, y si dos parejas consecutivas quedan en el mismo frasco, simplemente forman cuatro canicas consecutivas.

5. Como los frascos son indistinguibles, contamos emparejamientos no ordenados de \(10\) objetos distinguibles:
   \[
   \frac{10!}{2^5\,5!}=9\cdot 7\cdot 5\cdot 3\cdot 1=945.
   \]

\[
\boxed{945}
\]