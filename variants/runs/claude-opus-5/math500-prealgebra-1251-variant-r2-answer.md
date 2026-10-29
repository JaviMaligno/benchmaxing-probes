## Planteamiento

La suma de los ángulos interiores de un polígono convexo de $n$ lados es $(n-2)\cdot 180^\circ$.

Si llamamos $x$ al ángulo omitido, entonces:
$$(n-2)\cdot 180^\circ - x = 1550^\circ$$

## Restricción de convexidad

En un polígono convexo, cada ángulo interior cumple $0^\circ < x < 180^\circ$. Por tanto:
$$1550^\circ < (n-2)\cdot 180^\circ < 1730^\circ$$

## Resolución

Dividiendo entre 180:
$$8{,}61\ldots < n-2 < 9{,}61\ldots$$

El único entero en ese intervalo es $n-2 = 9$, es decir $n = 11$.

## Verificación

Para $n = 11$: la suma total es $9 \cdot 180^\circ = 1620^\circ$, y el ángulo omitido vale $1620^\circ - 1550^\circ = 70^\circ$, que efectivamente cumple $0^\circ < 70^\circ < 180^\circ$. ✓

(Con $n = 12$ el ángulo faltante sería $1800^\circ - 1550^\circ = 250^\circ > 180^\circ$, imposible en un polígono convexo.)

\boxed{11}