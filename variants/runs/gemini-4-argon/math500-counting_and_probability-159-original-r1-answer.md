Para resolver este problema paso a paso, podemos tratar a cada partido como un único bloque, ya que todos los miembros de cada partido deben sentarse juntos:

1. **Agrupar por partidos:** Tenemos 3 bloques distintos: el bloque de 5 demócratas, el bloque de 5 republicanos y el bloque de 1 independiente.
2. **Permutación circular de los bloques:** El número de formas de organizar $n$ bloques alrededor de una mesa circular (considerando equivalentes las rotaciones) es $(n - 1)!$. Para nuestros $3$ bloques, hay $(3 - 1)! = 2! = 2$ formas de ubicarlos alrededor de la mesa (por ejemplo, fijando al independiente, los demócratas pueden ir a su izquierda y los republicanos a su derecha, o viceversa).
3. **Permutaciones internas de cada partido:**
   - Los 5 demócratas pueden sentarse dentro de su propio bloque de $5! = 120$ formas distintas.
   - Los 5 republicanos pueden sentarse dentro de su propio bloque de $5! = 120$ formas distintas.
   - El único independiente puede sentarse de $1! = 1$ forma.

4. **Total de combinaciones:** Multiplicamos las formas de organizar los bloques por las permutaciones internas de cada bloque:
   $$\text{Total} = 2! \times 5! \times 5! \times 1! = 2 \times 120 \times 120 \times 1 = 28800$$

\boxed{28800}