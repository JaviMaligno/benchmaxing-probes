

Primero identifiquemos los pares prohibidos, es decir, aquellos cuyo producto excede 20.

Entre los números \(1,2,3,4,5,6,7\), los pares prohibidos son:

\[
(3,7),\ (4,6),\ (4,7),\ (5,6),\ (5,7),\ (6,7).
\]

En particular, el \(7\) solo puede ser adyacente a \(1\) y \(2\), porque

\[
7\cdot 3=21>20.
\]

Como en el círculo cada número tiene exactamente dos vecinos, el \(7\) debe estar entre el \(1\) y el \(2\).

Quitemos momentáneamente al \(7\). Entonces los números restantes deben formar un camino desde \(1\) hasta \(2\) usando \(3,4,5,6\) en algún orden:

\[
1,\ \_,\ \_,\ \_,\ \_,\ 2.
\]

Como \(1\) y \(2\) pueden ser adyacentes a cualquier número, la única restricción está en el orden interno de \(3,4,5,6\).

Entre \(3,4,5,6\), el \(6\) solo puede ser adyacente al \(3\), pues

\[
6\cdot 4=24>20,\qquad 6\cdot 5=30>20.
\]

Por tanto, en el bloque interno, el \(6\) no puede estar en medio; debe estar en un extremo, junto a \(1\) o \(2\), y al lado del \(3\).

Las posibilidades internas son:

\[
6,3,4,5;\qquad 6,3,5,4;\qquad 4,5,3,6;\qquad 5,4,3,6.
\]

Hay \(4\) caminos válidos de \(1\) a \(2\).

Ahora contemos considerando rotaciones y reflexiones como distintas:

- Posición del \(7\): \(7\) maneras.
- Elegir cuáles de sus dos lados ocupan \(1\) y \(2\): \(2\) maneras.
- Orden interno válido entre ellos: \(4\) maneras.

Por lo tanto, el número total de arreglos es

\[
7\cdot 2\cdot 4=56.
\]

\[
\boxed{56}
\]