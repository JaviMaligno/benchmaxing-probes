## Solución paso a paso

**Planteamiento:** Maya elige 7 muffins de 3 tipos (arándano, plátano y salvado), donde solo importa cuántos elige de cada tipo. Si llamamos $x_1, x_2, x_3$ a las cantidades de cada tipo, necesitamos contar las soluciones enteras no negativas de:

$$x_1 + x_2 + x_3 = 7$$

Como la vitrina tiene al menos 7 muffins de cada tipo, la única restricción es que cada $x_i \geq 0$.

**Método (estrellas y barras):** Este es un problema clásico de combinaciones con repetición. Repartir 7 objetos idénticos entre 3 categorías equivale a colocar 7 "estrellas" en 3 grupos, separadas por 2 "barras":

$$\underbrace{\star\star\cdots\star}_{7} \quad \text{con} \quad \underbrace{| \ |}_{2 \text{ barras}}$$

El número de ordenamientos distintos de 7 estrellas y 2 barras es elegir las posiciones de las barras entre 9 posiciones totales:

$$\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

**Verificación por enumeración:** Si $x_1 = 7,6,5,\dots,0$, las cantidades de soluciones para cada caso son $1, 2, 3, 4, 5, 6, 7, 8$, que suman $36$. ✓

$$\boxed{36}$$