## Razonamiento

**Paso 1: Reducir por simetría.** Por simetría rotacional, fijamos el punto $A$ en una posición cualquiera del círculo. Los otros tres puntos ($B$, $C$, $D$) caen independientemente en el resto de la circunferencia, y sus $3! = 6$ órdenes posibles al recorrer el círculo desde $A$ son equiprobables.

**Paso 2: Criterio de intersección.** Los segmentos $AB$ y $CD$ se cruzan en el interior del círculo si y solo si los cuatro puntos **alternan** alrededor de la circunferencia; es decir, al recorrerla desde $A$ encontramos algo como $A, C, B, D$ (o $A, D, B, C$). Si en cambio $A$ y $B$ son adyacentes en el orden, ambos quedan en el mismo arco y los segmentos no se cruzan.

**Paso 3: Contar casos favorables.** Los 6 órdenes posibles desde $A$ son:

$$A,B,C,D \quad A,B,D,C \quad A,C,B,D \quad A,C,D,B \quad A,D,B,C \quad A,D,C,B$$

Los órdenes alternados son solo $A,C,B,D$ y $A,D,B,C$: exactamente **2 casos**.

**Paso 4: Calcular la probabilidad.**

$$P(\text{intersección}) = \frac{2}{6} = \frac{1}{3}$$

$$\boxed{\dfrac{1}{3}}$$