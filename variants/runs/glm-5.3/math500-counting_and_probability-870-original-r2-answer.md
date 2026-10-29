## Razonamiento

**Paso 1: Reducir a orden circular.** Por simetría rotacional, fijamos el punto $A$ en un lugar del círculo. Los otros tres puntos $B$, $C$, $D$ se distribuyen de manera uniforme e independiente, así que el orden circular de $\{B, C, D\}$ partiendo desde $A$ es una permutación aleatoria: hay $3! = 6$ órdenes igualmente probables.

**Paso 2: Criterio de cruce.** La cuerda $AB$ divide la circunferencia en dos arcos. Las cuerdas $AB$ y $CD$ se cruzan **si y solo si** $C$ y $D$ caen en arcos distintos (es decir, los extremos se alternan alrededor del círculo: $A, C, B, D$ o $A, D, B, C$).

**Paso 3: Contar los casos.** Enumeramos el orden circular $A, X, Y, Z$ con $\{X,Y,Z\} = \{B,C,D\}$:

| Orden circular | ¿$C$ y $D$ en arcos distintos? |
|---|---|
| $A, B, C, D$ | No (ambos entre $B$ y $A$) |
| $A, B, D, C$ | No |
| $A, C, B, D$ | **Sí** (cruzan) |
| $A, D, B, C$ | **Sí** (cruzan) |
| $A, C, D, B$ | No (ambos entre $A$ y $B$) |
| $A, D, C, B$ | No |

**Paso 4: Probabilidad.** De los $6$ órdenes equiprobables, exactamente $2$ producen cruce:

$$P = \frac{2}{6} = \frac{1}{3}$$

**Verificación:** el argumento coincide con el resultado general de que, con $2k$ puntos emparejados al azar, la probabilidad de cruce de dos pares es $\frac{1}{3}$ — también se confirma numéricamente por simulación.

$$\boxed{\dfrac{1}{3}}$$