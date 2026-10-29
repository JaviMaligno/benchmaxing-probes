Es un problema clásico de permutaciones circulares con bloques.

**Paso 1: Tratar cada partido como un bloque.** Tenemos 3 bloques (Demócratas, Republicanos, Independiente). Alrededor de una mesa circular, el número de formas de ordenar 3 bloques, considerando rotaciones como equivalentes, es (3−1)! = 2.

**Paso 2: Ordenar dentro de cada bloque.** Los 5 demócratas pueden ordenarse entre sí de 5! = 120 maneras, los 5 republicanos de 5! = 120 maneras, y el independiente de 1! = 1 manera.

**Paso 3: Multiplicar.**

$$2 \cdot 120 \cdot 120 \cdot 1 = 28800$$

$$\boxed{28800}$$