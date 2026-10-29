Sea \(S(c)\) el conjunto de caras del cubo grande en las que se ve una celda roja \(c\). Contamos pares no ordenados de posiciones para los dos cubos rojos, ya que los cubos rojos son idénticos.

En un cubo \(3\times 3\times 3\), las celdas se clasifican así:

\[
\begin{array}{c|c|c}
\text{Tipo de celda} & |S(c)| & \text{Número}\\
\hline
\text{interior} & 0 & 1\\
\text{centro de cara} & 1 & 6\\
\text{centro de arista} & 2 & 12\\
\text{esquina} & 3 & 8
\end{array}
\]

Necesitamos que las dos celdas rojas tengan conjuntos de caras visibles cuya unión tenga tamaño exactamente \(4\). Como una sola celda tiene a lo más \(3\) caras visibles, ambas celdas rojas deben estar en la frontera.

Contamos por casos:

1. **Esquina-esquina:** se necesita intersección \(2\). Dos esquinas que comparten exactamente dos caras corresponden a vértices unidos por una arista del cubo, así que hay \(12\).

2. **Esquina-centro de arista:** se necesita intersección \(1\). Para cada esquina hay \(6\) celdas de arista que comparten exactamente una de sus tres caras, hence \(8\cdot 6=48\).

3. **Esquina-centro de cara:** se necesita intersección \(0\). Para cada esquina sirven las \(3\) caras opuestas a sus tres caras, hence \(8\cdot 3=24\).

4. **Centro de arista-centro de arista:** se necesita intersección \(0\). Para una arista fija, \(5\) de las otras \(11\) aristas tienen pares de caras disjuntos, hence
\[
\frac{12\cdot 5}{2}=30.
\]

Las demás combinaciones no pueden producir \(4\) caras visibles.

Por lo tanto,
\[
12+48+24+30=114.
\]

\[
\boxed{114}
\]