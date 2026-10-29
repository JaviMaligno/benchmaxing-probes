Los cuatro puntos elegidos al azar en la circunferencia determinan cuatro posiciones. Por simetría, podemos fijar primero las cuatro posiciones en el círculo y luego preguntarnos cómo se asignan las etiquetas $A$, $B$, $C$, $D$ a esas posiciones.

**Paso 1: Reducir el problema a las formas de emparejar los puntos.**
Dadas cuatro posiciones fijas en el círculo, lo único que importa es cómo se dividen en dos parejas: una pareja forma el segmento $AB$ y la otra el segmento $CD$. Hay exactamente 3 maneras de partir cuatro puntos en dos parejas, y por simetría de la elección aleatoria e independiente, las tres particiones son igualmente probables.

**Paso 2: Determinar cuántas particiones producen intersección.**
Si llamamos $P_1, P_2, P_3, P_4$ a las cuatro posiciones en orden alrededor del círculo, las dos cuerdas se cortan si y solo si las parejas se "entrelazan", es decir, si los extremos de una cuerda separan a los extremos de la otra sobre la circunferencia. De las tres particiones posibles:

- $\{P_1,P_2\}$ con $\{P_3,P_4\}$: las cuerdas no se cortan (puntos adyacentes).
- $\{P_1,P_4\}$ con $\{P_2,P_3\}$: las cuerdas no se cortan (puntos adyacentes).
- $\{P_1,P_3\}$ con $\{P_2,P_4\}$: las cuerdas sí se cortan (puntos alternados).

**Paso 3: Calcular la probabilidad.**
Solo 1 de las 3 particiones igualmente probables produce segmentos que se intersecan, así que la probabilidad es $\frac{1}{3}$.

$$\boxed{\dfrac{1}{3}}$$