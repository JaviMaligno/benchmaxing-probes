Para resolver este problema paso a paso, podemos tratar a cada grupo de miembros del mismo partido como un único bloque:

1. **Agrupar por bloques:** 
   Dado que todos los miembros de cada partido deben sentarse juntos, podemos considerar tres unidades o bloques:
   - Un bloque de 6 Verdes (*Greens*).
   - Un bloque de 4 Liberales (*Liberals*).
   - El miembro no afiliado (1 persona).

2. **Permutar los bloques alrededor de la mesa circular:**
   El número de formas de organizar $n$ objetos distintos alrededor de una mesa circular (considerando equivalentes las rotaciones) es $(n - 1)!$. Para nuestros 3 bloques, hay:
   $$(3 - 1)! = 2! = 2 \text{ formas}$$

3. **Permutar a los miembros dentro de cada bloque:**
   - Los 6 miembros Verdes pueden sentarse entre sí de $6!$ formas distintas.
   - Los 4 miembros Liberales pueden sentarse entre sí de $4!$ formas distintas.
   - El miembro no afiliado solo tiene $1! = 1$ forma.

4. **Calcular el total de combinaciones:**
   Multiplicamos las formas de organizar los bloques por las permutaciones internas de cada bloque:
   $$\text{Total} = 2! \times 6! \times 4! = 2 \times 720 \times 24 = 34560$$

\boxed{34560}