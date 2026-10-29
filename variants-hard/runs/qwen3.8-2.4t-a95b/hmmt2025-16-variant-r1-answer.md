

Numeremos las líneas de la cuadrícula de \(0\) a \(6\) en cada dirección. Cada rectángulo queda determinado por elegir 2 líneas verticales y 2 horizontales, así que hay

\[
\binom{7}{2}^2 = 21^2 = 441
\]

rectángulos posibles.

Dos rectángulos alineados con la cuadrícula no comparten ningún punto si y solo si están estrictamente separados en la dirección horizontal o en la vertical.

Sea \(H\) el conjunto de pares no ordenados separados horizontalmente. Para que un rectángulo esté estrictamente a la izquierda del otro, sus intervalos en \(x\) deben ser

\[
a<b<e<f,
\]

lo cual equivale a elegir 4 líneas verticales entre las 7 disponibles:

\[
\binom{7}{4}=35.
\]

Para cada elección horizontal, los intervalos en \(y\) de ambos rectángulos pueden ser cualesquiera: \(21\cdot 21=441\) opciones. Como el par no ordenado tiene una única orientación izquierda/derecha,

\[
|H|=35\cdot 441=15435.
\]

Por simetría, si \(V\) es el conjunto de pares separados verticalmente,

\[
|V|=15435.
\]

Ahora contamos \(H\cap V\): pares separados tanto horizontal como verticalmente. Elegimos 4 líneas verticales y 4 horizontales:

\[
\binom{7}{4}\binom{7}{4}=35^2.
\]

Dados los intervalos izquierda/derecha y abajo/arriba, hay 2 formas de asignar los intervalos verticales a los rectángulos izquierdo y derecho. Por tanto,

\[
|H\cap V|=2\cdot 35^2=2450.
\]

Por inclusión-exclusión, el número de pares no ordenados válidos es

\[
|H\cup V|=15435+15435-2450=28420.
\]

\[
\boxed{28420}
\]