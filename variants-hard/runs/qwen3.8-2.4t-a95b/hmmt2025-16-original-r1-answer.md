

Numera las líneas de la cuadrícula de \(0\) a \(5\) en cada dirección. Un rectángulo queda determinado al elegir 2 líneas verticales y 2 horizontales.

Dos rectángulos no comparten ningún punto (ni interior, ni bordes, ni vértices) si y solo si sus proyecciones en \(x\) son disjuntas o sus proyecciones en \(y\) son disjuntas.

Contemos los pares no ordenados:

1. **Separados horizontalmente**:  
   Para que un rectángulo esté estrictamente a la izquierda del otro, elegimos 4 líneas verticales distintas
   \[
   x_1<x_2<x_3<x_4,
   \]
   donde el rectángulo izquierdo usa \(x_1,x_2\) y el derecho usa \(x_3,x_4\).  
   Hay
   \[
   \binom{6}{4}=15
   \]
   formas.

   Para cada rectángulo, las líneas horizontales pueden elegirse libremente:
   \[
   \binom{6}{2}^2=15^2=225.
   \]

   Entonces hay
   \[
   15\cdot 225=3375
   \]
   pares separados horizontalmente.

2. **Separados verticalmente**:  
   Por simetría, también hay
   \[
   3375
   \]
   pares.

3. **Contados dos veces**:  
   Los pares separados tanto horizontal como verticalmente se contaron en ambos casos.  
   Elegimos 4 líneas verticales y 4 horizontales:
   \[
   \binom{6}{4}\binom{6}{4}=15\cdot 15=225.
   \]
   Con esas líneas, hay 2 formas de emparejar los rectángulos en diagonal. Así que hay
   \[
   225\cdot 2=450
   \]
   pares contados dos veces.

Por inclusión-exclusión, el total es
\[
3375+3375-450=6300.
\]

\[
\boxed{6300}
\]