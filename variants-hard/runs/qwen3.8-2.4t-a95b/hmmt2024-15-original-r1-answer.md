

Modelamos el país como un grafo simple de \(8\) vértices (ciudades distinguibles), donde las carreteras son aristas. Cada vértice tiene grado \(3\), y para cualquier par de vértices distintos \(u,v\), el número de vecinos comunes \(|N(u)\cap N(v)|\) es \(0\) o \(2\).

### 1. Clasificación de los grafos posibles

**Si hay un triángulo.**  
Supongamos que \(a,b,c\) forman un triángulo. La arista \(ab\) ya tiene a \(c\) como vecino común, así que por la condición debe tener exactamente \(2\) vecinos comunes. Entonces existe un vértice \(d\) adyacente a \(a\) y \(b\).

Como \(a\) tiene grado \(3\), sus vecinos son \(b,c,d\). Para la arista \(ac\), ya \(b\) es vecino común, y el único otro candidato posible es \(d\), así que \(d\) también es adyacente a \(c\). Por tanto \(a,b,c,d\) forman un \(K_4\). Cada uno tiene grado \(3\), así que este \(K_4\) es una componente conexa. Con \(8\) vértices, la otra componente también debe ser \(K_4\).

Esto da el grafo:

\[
K_4 \sqcup K_4.
\]

Este grafo cumple la condición: dos ciudades dentro del mismo \(K_4\) tienen \(2\) vecinos comunes, y dos ciudades en componentes distintas tienen \(0\).

---

**Si no hay triángulos.**  
Entonces dos ciudades adyacentes tienen \(0\) vecinos comunes.

Fijemos un vértice \(v\). Sus \(3\) vecinos tienen cada uno otros \(2\) vecinos, y como no hay triángulos, ninguno de esos vecinos adicionales es vecino de \(v\). Así que hay

\[
3\cdot 2=6
\]

caminos de longitud \(2\) desde \(v\), contados por vecinos comunes con los no vecinos de \(v\).

Hay \(4\) no vecinos de \(v\), y cada uno puede tener \(0\) o \(2\) vecinos comunes con \(v\). Como la suma debe ser \(6\), exactamente tres no vecinos tienen \(2\) vecinos comunes con \(v\), y exactamente uno tiene \(0\). Llamemos \(f(v)\) a ese único no vecino con \(0\) vecinos comunes.

La relación es simétrica, así que \(f\) es una involución sin puntos fijos: las ciudades se agrupan en \(4\) pares “antípodas”.

Para un par \(\{v,f(v)\}\), sean

\[
A=N(v), \qquad B=N(f(v)).
\]

Como \(v\) y \(f(v)\) no tienen vecinos comunes, \(A\) y \(B\) son conjuntos disjuntos de tamaño \(3\). Además, cada vértice de \(A\) es adyacente a exactamente \(2\) vértices de \(B\), y viceversa. Por tanto, entre \(A\) y \(B\) hay un grafo bipartito \(2\)-regular con \(3+3\) vértices, es decir, un ciclo \(C_6\).

Esa estructura es exactamente el grao cubo \(Q_3\). Recíprocamente, el cubo cumple la condición: vértices adyacentes tienen \(0\) vecinos comunes, vértices a distancia \(2\) tienen \(2\), y vértices opuestos tienen \(0\).

Así que los únicos tipos de grafos son:

1. \(K_4 \sqcup K_4\),
2. el cubo \(Q_3\).

---

### 2. Conteo con ciudades distinguibles

**Caso \(K_4 \sqcup K_4\).**  
Solo hay que particionar las \(8\) ciudades en dos conjuntos de \(4\):

\[
\frac{1}{2}\binom{8}{4}=35.
\]

---

**Caso cubo.**  
Los \(4\) pares opuestos del cubo forman un emparejamiento perfecto. El número de emparejamientos perfectos en \(8\) ciudades es

\[
\frac{8!}{2^4 4!}=105.
\]

Fijado un emparejamiento, tomemos una ciudad fija, digamos la ciudad \(1\). Sus tres vecinos deben ser uno de cada uno de los otros tres pares, y hay \(2^3=8\) formas de elegirlos. Una vez elegidos, todas las demás aristas quedan forzadas.

Por tanto, hay

\[
105\cdot 8=840
\]

cubos etiquetados.

---

Sumando ambos casos:

\[
35+840=875.
\]

\[
\boxed{875}
\]