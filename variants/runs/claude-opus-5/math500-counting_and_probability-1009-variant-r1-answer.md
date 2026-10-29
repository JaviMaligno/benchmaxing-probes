## Razonamiento

Se trata de contar cuántas soluciones enteras no negativas tiene la ecuación

$$b_1 + b_2 + b_3 = 7$$

donde $b_1$ es el número de muffins de arándano, $b_2$ de banana y $b_3$ de bran. Como el expositor tiene al menos siete de cada tipo, ninguna variable está acotada por arriba (cualquier valor de 0 a 7 es posible), así que no hay restricciones adicionales.

Este es el problema clásico de **combinaciones con repetición**: distribuir 7 unidades idénticas entre 3 categorías distinguibles. Por el método de "barras y estrellas", colocamos 7 estrellas y 2 barras en fila, y cada ordenamiento determina un reparto único:

$$\binom{n+k-1}{k-1} = \binom{7+3-1}{3-1} = \binom{9}{2}$$

$$\binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

**Verificación** fijando el número de muffins de arándano $b_1$: para cada valor de $b_1 = 0,1,\dots,7$, quedan $7 - b_1$ muffins a repartir entre banana y bran, lo cual admite $7 - b_1 + 1 = 8 - b_1$ formas. Sumando:

$$8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 36$$

Ambos métodos coinciden.

\boxed{36}