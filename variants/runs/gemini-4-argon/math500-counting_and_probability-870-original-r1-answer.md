Para encontrar la probabilidad de que los segmentos $AB$ y $CD$ se intersecan cuando se eligen cuatro puntos $A$, $B$, $C$ y $D$ de forma aleatoria e independiente sobre la circunferencia de un círculo, podemos razonar paso a paso utilizando la simetría del problema:

1. **Puntos distintos:** Dado que la distribución sobre la circunferencia es continua, la probabilidad de que dos o más puntos coincidan en la misma posición es $0$. Por lo tanto, con probabilidad $1$, los cuatro puntos $A$, $B$, $C$ y $D$ son distintos.

2. **Cuadrilátero cíclico:** Cuatro puntos distintos cualesquiera sobre una circunferencia forman los vértices de un único cuadrilátero convexo inscrito en el círculo.

3. **Emparejamientos posibles:** Existen exactamente $3$ formas distintas de dividir estos cuatro puntos en dos pares para formar dos cuerdas (segmentos):
   - $\{AB, CD\}$
   - $\{AC, BD\}$
   - $\{AD, BC\}$

4. **Condición de intersección:** De estas $3$ maneras de emparejar los puntos, dos corresponden a lados opuestos del cuadrilátero convexo (que no se intersecan) y exactamente **una** corresponde a las dos diagonales del cuadrilátero, las cuales se cruzan en el interior del círculo.

5. **Simetría:** Como los puntos $A$, $B$, $C$ y $D$ se eligen de manera independiente e idénticamente distribuida, todas las permutaciones del orden de los puntos alrededor del círculo son igualmente probables. Esto significa que cada uno de los $3$ emparejamientos posibles tiene la misma probabilidad de ser el que corresponde a las diagonales.

Por lo tanto, la probabilidad de que los segmentos $AB$ y $CD$ se intersequen es de $1$ entre $3$.

\boxed{\frac{1}{3}}