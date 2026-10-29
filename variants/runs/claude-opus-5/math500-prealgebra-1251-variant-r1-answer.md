## Planteamiento

La suma de todos los ángulos interiores de un polígono convexo de $n$ lados es:

$$S = (n-2)\cdot 180^\circ$$

Si llamamos $x$ al ángulo omitido, entonces:

$$(n-2)\cdot 180^\circ - x = 1550^\circ \quad\Longrightarrow\quad x = (n-2)\cdot 180^\circ - 1550^\circ$$

## Restricción de convexidad

Al ser convexo, cada ángulo interior cumple $0^\circ < x < 180^\circ$.

**Cota inferior** ($x > 0$):
$$(n-2)\cdot 180 > 1550 \;\Longrightarrow\; n-2 > 8{,}61\ldots \;\Longrightarrow\; n-2 \geq 9$$

**Cota superior** ($x < 180$):
$$(n-2)\cdot 180 < 1730 \;\Longrightarrow\; n-2 < 9{,}61\ldots \;\Longrightarrow\; n-2 \leq 9$$

Por tanto $n-2 = 9$, es decir $n = 11$.

## Verificación

Para $n = 11$: la suma total es $9 \cdot 180^\circ = 1620^\circ$, y el ángulo omitido vale $1620^\circ - 1550^\circ = 70^\circ$, que efectivamente cumple $0^\circ < 70^\circ < 180^\circ$. ✓

(Si fuera $n = 12$, el ángulo omitido sería $1800^\circ - 1550^\circ = 250^\circ > 180^\circ$, imposible en un polígono convexo.)

\boxed{11}