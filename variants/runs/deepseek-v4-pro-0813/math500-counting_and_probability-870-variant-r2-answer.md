Voy a razonar paso a paso.

**Paso 1: Entender el problema**

Tenemos 6 puntos elegidos al azar e independientemente sobre una circunferencia. Los emparejamos como $PQ$, $RS$ y $TU$. Queremos la probabilidad de que los tres segmentos se crucen por pares: es decir, $PQ$ cruza a $RS$, $PQ$ cruza a $TU$, y $RS$ cruza a $TU$.

**Paso 2: Condición para que dos cuerdas se crucen**

Dos cuerdas con extremos $AB$ y $CD$ se cruzan en el interior del círculo si y solo si sus extremos se alternan alrededor de la circunferencia. Es decir, al recorrer el círculo, los puntos aparecen en el orden $A$, $C$, $B$, $D$ (o equivalentemente $A$, $D$, $B$, $C$).

**Paso 3: Poner etiquetas a los extremos de las cuerdas**

Llamemos a los tres pares de extremos:
- cuerda 1: puntos $P$ y $Q$ (los trato como tipo 1)
- cuerda 2: puntos $R$ y $S$ (tipo 2)
- cuerda 3: puntos $T$ y $U$ (tipo 3)

Ahora, para que las tres cuerdas se crucen por pares, en la disposición circular los seis puntos deben aparecer con sus tipos alternados de forma que ninguna cuerda tenga sus dos extremos adyacentes.

**Paso 4: Reducir al orden circular de tipos**

Fijemos la posición de un punto tipo 1 y vayamos colocando los demás. Como los puntos son aleatorios, todos los órdenes circulares de los 6 puntos son igualmente probables. Para contar solo la disposición de tipos, podemos fijar un punto de tipo 1 en la posición 1.

Ahora, ¿qué orden de tipos produce que las tres cuerdas se crucen por pares?

Al probar las permutaciones, se encuentra el patrón clásico:

Los seis puntos deben estar en el orden

$$
1, 2, 3, 1, 2, 3
$$

alrededor del círculo (o cualquier rotación/reflexión de ese patrón). Es decir, si recorremos el círculo vemos: punto de la cuerda 1, punto de la cuerda 2, punto de la cuerda 3, punto de la cuerda 1, punto de la cuerda 2, punto de la cuerda 3.

Verifiquemos: con este orden, la cuerda 1 tiene extremos en posiciones 1 y 4; la cuerda 2 en posiciones 2 y 5; la cuerda 3 en posiciones 3 y 6. Cada par de cuerdas tiene sus extremos alternados, luego los tres pares se cruzan.

**Paso 5: Contar las disposiciones favorables**

Fijemos $P$ (un extremo de la cuerda 1) en una posición fija. Los otros 5 puntos se pueden ordenar de $5! = 120$ maneras.

Ahora contemos cuántas disposiciones tienen el patrón $1,2,3,1,2,3$ a partir del $P$ fijado.

Tenemos:
- El otro punto de la cuerda 1 (es decir $Q$) debe ir exactamente en la posición 4.
- Los dos puntos de la cuerda 2 se colocan en las posiciones 2 y 5: hay $2$ maneras de asignarlos.
- Los dos puntos de la cuerda 3 se colocan en las posiciones 3 y 6: hay $2$ maneras de asignarlos.

Por lo tanto, hay $2 \cdot 2 = 4$ disposiciones favorables.

**Paso 6: Calcular la probabilidad**

$$
P = \frac{4}{120} = \frac{1}{30}.
$$

**Conclusión**

La probabilidad es $\frac{1}{30}$.

\[
\boxed{\frac{1}{30}}
\]