

Con probabilidad \(1\), los seis puntos son distintos, así que solo importa su orden cíclico alrededor de la circunferencia.

Numeremos las seis posiciones del orden cíclico como \(1,2,\dots,6\). Como los puntos son independientes y uniformes, cada asignación de las etiquetas \(P,Q,R,S,T,U\) a esas posición es igualmente probable. Hay

\[
6! = 720
\]

asignaciones posibles.

Dos cuerdas se cruzan si y solo si sus extremos se alternan en el orden cíclico.

Para que la cuerda \(PQ\) sea cruzada por \(RS\) y por \(TU\), cada una de estas dos cuerdas debe tener un extremo en cada uno de los dos arcos en que \(P\) y \(Q\) dividen la circunferencia. Por tanto, cada arco debe contener exactamente dos de los puntos restantes. Eso significa que \(P\) y \(Q\) deben estar en posiciones opuestas del orden cíclico, es decir, separadas por tres posiciones.

Lo mismo debe ocurrir para \(RS\) y para \(TU\). Así, las tres cuerdas deben ocupar exactamente los tres pares de posiciones opuestas:

\[
\{1,4\},\quad \{2,5\},\quad \{3,6\}.
\]

Recíprocamente, si las tres cuerdas ocupan esos tres pares de posiciones opuestas, entonces cualquier par de cuerdas tiene extremos alternados y, por tanto, se cruzan.

Contemos las asignaciones favorables:

- Asignar las cuerdas \(PQ, RS, TU\) a los tres pares opuestos: \(3!\) maneras.
- Elegir, para cada cuerda, cuál extremo va en cuál de sus dos posiciones: \(2^3\) maneras.

Por tanto, hay

\[
3!\cdot 2^3 = 6\cdot 8 = 48
\]

asignaciones favorables.

La probabilidad es

\[
\frac{48}{720}=\frac{1}{15}.
\]

\[
\boxed{\frac{1}{15}}
\]