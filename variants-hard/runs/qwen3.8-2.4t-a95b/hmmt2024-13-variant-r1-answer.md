

Clasificamos las posiciones de un cubo unitario dentro del cubo \(3\times 3\times 3\) según el número de caras del cubo grande en las que queda visible:

- **Esquina:** visible en \(3\) caras. Hay \(8\) posiciones.
- **Arista:** visible en \(2\) caras. Hay \(12\) posiciones.
- **Centro de cara:** visible en \(1\) cara. Hay \(6\) posiciones.
- **Interior:** visible en \(0\) caras. Hay \(1\) posición.

Queremos que las dos piezas azules hagan que el color azul sea visible en exactamente \(3\) de las \(6\) caras del cubo grande. Como las rotaciones y reflexiones se consideran distintas, contamos posiciones fijas.

### Caso 1: Un cubo azul está en una esquina

Una esquina ya aporta \(3\) caras visibles. Para no añadir más caras, el segundo cubo azul debe estar en una posición cuyas caras visibles estén entre esas mismas \(3\) caras.

Para una esquina dada, tales posiciones son:

- las \(3\) aristas que tocan esa esquina,
- los \(3\) centros de cara en las caras de esa esquina,
- la posición interior.

En total, \(3+3+1=7\) opciones por cada esquina.

\[
8\cdot 7=56
\]

### Caso 2: Ningún cubo azul está en una esquina

Entonces, para conseguir \(3\) caras visibles, las opciones son:

#### a) Dos cubos azules en aristas

Cada arista aporta \(2\) caras. Para que la unión tenga exactamente \(3\) caras, las dos aristas deben compartir exactamente una cara. Eso equivale a elegir dos aristas dentro de una misma cara del cubo grande.

Cada cara tiene \(4\) aristas, así que aporta

\[
\binom{4}{2}=6
\]

pares de aristas. Como hay \(6\) caras:

\[
6\cdot 6=36
\]

#### b) Un cubo azul en una arista y otro en un centro de cara

La arista aporta \(2\) caras. El centro de cara debe estar en una cara diferente de esas dos. Para cada arista, hay \(4\) centros de cara posibles.

\[
12\cdot 4=48
\]

No hay otros casos: dos centros de cara dan como máximo \(2\) caras visibles, y usar el interior no aumenta el número de caras visibles.

Sumando todo:

\[
56+36+48=140
\]

\[
\boxed{140}
\]