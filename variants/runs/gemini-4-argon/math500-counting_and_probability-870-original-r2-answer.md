Para encontrar la probabilidad de que los segmentos $AB$ y $CD$ se intersequen, podemos razonar paso a paso utilizando la simetría del problema:

1. **Elección de los puntos:** Dado que los cuatro puntos $A$, $B$, $C$ y $D$ se eligen al azar y de manera independiente sobre la circunferencia de un círculo (una distribución continua), la probabilidad de que dos o más puntos coincidan es $0$. Por lo tanto, podemos asumir que los cuatro puntos son distintos.

2. **Formación de pares de segmentos:** Con cualesquiera cuatro puntos distintos sobre una circunferencia, podemos formar un cuadrilátero convexo. Existen exactamente $\frac{1}{2}\binom{4}{2} = 3$ maneras distintas de dividir estos cuatro puntos en dos pares para formar dos segmentos (cuerdas):
   - $AB$ y $CD$
   - $AC$ y $BD$
   - $AD$ y $BC$

3. **Condición de intersección:** En cualquier cuadrilátero convexo inscrito en un círculo, dos de estas agrupaciones corresponden a lados opuestos (que no se intersecan) y exactamente **una** agrupación corresponde a las dos diagonales del cuadrilátero (las cuales sí se intersecan en el interior del círculo).

4. **Simetría:** Como los puntos $A$, $B$, $C$ y $D$ se eligen de forma independiente e idénticamente distribuida, cualquier ordenamiento cíclico de las etiquetas es igualmente probable. En consecuencia, cada una de las $3$ formas de emparejar los puntos tiene la misma probabilidad de ser el par de diagonales que se cruzan.

Por lo tanto, la probabilidad de que específicamente los segmentos $AB$ y $CD$ se intersequen es $1$ de $3$.

\boxed{\frac{1}{3}}