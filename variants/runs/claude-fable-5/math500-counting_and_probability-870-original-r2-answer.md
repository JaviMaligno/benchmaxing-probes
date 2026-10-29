Fijemos primero las posiciones de los cuatro puntos en el círculo y pensemos solo en cómo se etiquetan.

**Paso 1.** Elegir cuatro puntos aleatorios e independientes en la circunferencia equivale a elegir cuatro posiciones y luego asignarles las etiquetas $A$, $B$, $C$, $D$ de manera uniforme al azar. Por simetría, todas las asignaciones de etiquetas son igualmente probables.

**Paso 2.** Los segmentos $AB$ y $CD$ se cortan si y solo si los puntos $A$ y $B$ **separan** a $C$ y $D$ en el círculo, es decir, si al recorrer la circunferencia los puntos aparecen alternados (por ejemplo, $A, C, B, D$).

**Paso 3.** Hay exactamente tres maneras de dividir los cuatro puntos en dos parejas:
- $\{A,B\}$ con $\{C,D\}$,
- $\{A,C\}$ con $\{B,D\}$,
- $\{A,D\}$ con $\{B,C\}$.

Para cualquier configuración de cuatro puntos en posición genérica sobre el círculo, exactamente **una** de estas tres formas de emparejar produce cuerdas que se cruzan (la que empareja puntos "opuestos" en el orden cíclico). Como el etiquetado es uniforme, cada uno de los tres emparejamientos tiene la misma probabilidad de ser el que se cruza.

**Paso 4.** Por lo tanto, la probabilidad de que precisamente el emparejamiento $\{A,B\}$–$\{C,D\}$ sea el que se cruza es $\frac{1}{3}$.

$$\boxed{\dfrac{1}{3}}$$