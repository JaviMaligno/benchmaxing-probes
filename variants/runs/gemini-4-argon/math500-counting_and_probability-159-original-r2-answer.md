Para resolver este problema paso a paso, podemos tratar a cada partido como un bloque individual dado que todos los miembros de cada partido deben sentarse juntos.

1. **Agrupar por partidos:**
   Tenemos 3 bloques:
   - Un bloque de 5 Demócratas.
   - Un bloque de 5 Republicanos.
   - Un bloque de 1 Independiente.

2. **Ordenar los bloques alrededor de la mesa circular:**
   El número de maneras de ordenar $n$ objetos alrededor de un círculo (donde las rotaciones se consideran equivalentes) es $(n-1)!$. 
   Para nuestros 3 bloques, hay $(3-1)! = 2! = 2$ maneras de colocarlos alrededor de la mesa (por ejemplo, fijando la posición del Independiente, los Demócratas pueden ir a su izquierda y los Republicanos a su derecha, o viceversa).

3. **Ordenar a los miembros dentro de cada bloque:**
   - Los 5 Demócratas pueden sentarse entre sí de $5! = 120$ maneras diferentes.
   - Los 5 Republicanos pueden sentarse entre sí de $5! = 120$ maneras diferentes.
   - El único Independiente puede sentarse de $1! = 1$ manera.

4. **Calcular el total de combinaciones:**
   Multiplicamos las formas de ordenar los bloques por las permutaciones internas de cada grupo:
   $$\text{Total} = 2 \times 5! \times 5! \times 1! = 2 \times 120 \times 120 \times 1 = 28800$$

\boxed{28800}