Es un problema de combinaciones con repetición (estrellas y barras).

Buscamos el número de soluciones enteras no negativas de:

$$x_1 + x_2 + x_3 = 7$$

donde $x_1, x_2, x_3$ son las cantidades de muffins de arándano, plátano y salvado. Como hay al menos 7 de cada tipo, no hay restricciones adicionales.

Por la fórmula de estrellas y barras, el número de soluciones es:

$$\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

$$\boxed{36}$$