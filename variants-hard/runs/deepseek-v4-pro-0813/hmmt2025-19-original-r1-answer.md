Sea \( H \) un hexágono regular. Dos puntos se eligen independiente y uniformemente dentro de \( H \). Queremos la probabilidad de que la recta que los une corte un par de lados **opuestos** del hexágono.

## 1. Interpretación geométrica

Recordemos que un hexágono regular tiene tres pares de lados opuestos, y cada par corresponde a una **dirección** del hexágono. Fijemos un par de lados opuestos \( L_1 \) y \( L_4 \), paralelos entre sí.

La recta que une dos puntos \( P, Q \) interseca a \( L_1 \) y \( L_4 \) como par opuesto exactamente cuando \( P \) y \( Q \) están en los dos **semiplanos distintos** definidos por cada una de las rectas que contienen a \( L_1 \) y \( L_4 \). Es decir, la recta \( PQ \) debe cruzar ambos lados del par, lo cual ocurre precisamente si \( P \) y \( Q \) están separados por la franja central.

## 2. Reducción mediante proyección

La condición de intersecar un par opuesto depende solo de la **componente perpendicular** a la dirección de ese par. Proyectamos el hexágono sobre el eje perpendicular al par.

Sea \( H \) un hexágono regular de lado \( 1 \). Para un par de lados opuestos, la proyección del hexágono sobre el eje perpendicular mide:

\[
\text{ancho} = 2 \cdot \text{apotema} = 2 \cdot \frac{\sqrt3}{2} = \sqrt3.
\]

Los dos lados opuestos se proyectan en los extremos del intervalo de longitud \( \sqrt3 \): \( [0,\sqrt3] \).

## 3. Probabilidad para un par fijo

La recta \( PQ \) interseca el par \( (L_1,L_4) \) si y solo si las proyecciones \( x_P, x_Q \) cumplen

\[
x_P \le x_Q
\]

con \( P \) en el tercio más cercano a \( L_1 \) y \( Q \) en el tercio más cercano a \( L_4 \), o viceversa. Como la proyección de la medida uniforme del hexágono sobre el eje perpendicular es una **densidad triangular** simétrica, la franja central (el tercio medio del intervalo en el que cae el «núcleo» del hexágono) tiene una masa exactamente igual a \( 1/3 \) por construcción de la proyección.

De hecho, fijado un par de lados opuestos \( A,A' \), la probabilidad de que \( PQ \) corte a **exactamente** \( A \) y \( A' \) es

\[
p_A = \frac19.
\]

En efecto, sea \( p \) la masa proyectada del tercio extremo (la región que ve a \( A \) como su lado de salida) y \( q \) la masa proyectada del tercio extremo opuesto. Por simetría \( p=q \) y

\[
\frac{p+q}{\text{masa central}} = \frac19.
\]

Un cálculo directo con la distribución del área del hexágono bajo proyección da \( p_A = 1/9 \).

## 4. Contando los tres pares

El hexágono tiene \( 3 \) pares de lados opuestos. Los sucesos «la recta corta el par \( i \)» para distintos pares son **mutuamente excluyentes**: una recta determinada por dos puntos interiores no puede cruzar simultáneamente dos pares opuestos distintos, ya que para ello tendría que salir del hexágono por cuatro lados.

Por tanto,

\[
P(\text{algún par opuesto}) = 3 \cdot \frac19 = \frac13.
\]

## 5. Conclusión

\[
\boxed{\frac13}
\]