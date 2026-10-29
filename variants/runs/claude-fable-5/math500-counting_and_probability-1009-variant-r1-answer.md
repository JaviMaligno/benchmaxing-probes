Es un problema de combinaciones con repetición (barras y estrellas): hay que contar las soluciones enteras no negativas de $x_1 + x_2 + x_3 = 7$, donde cada variable representa cuántos muffins elige de cada tipo (arándano, plátano y salvado).

La fórmula es $\binom{n + k - 1}{k - 1}$ con $n = 7$ muffins y $k = 3$ tipos:

$$\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

Como el mostrador tiene al menos siete de cada tipo, ninguna combinación queda excluida por falta de existencias.

$$\boxed{36}$$