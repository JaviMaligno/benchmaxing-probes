## Planteamiento

Hay que repartir 7 muffins entre 3 tipos (arándano, plátano, salvado), donde solo importa cuántos de cada tipo. Es decir, contar las soluciones enteras no negativas de:

$$x_1 + x_2 + x_3 = 7, \qquad x_i \ge 0$$

El enunciado garantiza que hay al menos 7 muffins de cada tipo, así que ninguna variable tiene cota superior efectiva.

## Cálculo

Por el método de "estrellas y barras": 7 estrellas y 2 barras, en total 9 posiciones de las cuales elegimos 2 para las barras:

$$\binom{7+3-1}{3-1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

## Verificación

Fijando el número de muffins de arándano $x_1 = k$, quedan $7-k$ para repartir entre dos tipos, lo que da $8-k$ opciones:

$$8+7+6+5+4+3+2+1 = 36$$

Ambos métodos coinciden.

\boxed{36}