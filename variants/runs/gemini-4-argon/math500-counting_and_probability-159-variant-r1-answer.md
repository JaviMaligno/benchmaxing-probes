Para resolver este problema paso a paso, podemos tratar a cada grupo como una sola unidad o bloque, ya que todos los miembros de cada partido deben sentarse juntos:

1. **Agrupar a los miembros en bloques:**
   Tenemos 3 bloques en total:
   - El bloque de los 6 miembros del partido Verde (*Greens*).
   - El bloque de los 4 miembros del partido Liberal (*Liberals*).
   - El bloque de 1 miembro no afiliado.

2. **Permutar los bloques alrededor de la mesa circular:**
   El número de formas de organizar $n$ objetos distintos alrededor de un círculo (donde las rotaciones son equivalentes) es $(n - 1)!$. Para nuestros 3 bloques:
   $$(3 - 1)! = 2! = 2 \text{ formas}$$

3. **Permutar a los miembros dentro de cada bloque:**
   - Los 6 miembros Verdes pueden sentarse entre sí de $6! = 720$ formas.
   - Los 4 miembros Liberales pueden sentarse entre sí de $4! = 24$ formas.
   - El miembro no afiliado solo tiene $1! = 1$ forma.

4. **Calcular el total de combinaciones:**
   Multiplicamos las formas de organizar los bloques por las permutaciones internas de cada bloque:
   $$\text{Total} = 2 \times 720 \times 24 \times 1 = 34560$$

\boxed{34560}