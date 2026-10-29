## Planteamiento

Un octágono equiangular tiene ángulos interiores de $135°$, es decir, la dirección de cada lado gira $45°$ respecto al anterior. Como hay cuatro lados de $3$ y cuatro de $\sqrt{2}$ sin adyacentes iguales, las longitudes necesariamente **alternan**: $3, \sqrt{2}, 3, \sqrt{2}, \dots$

## Construcción de coordenadas

Coloco los lados sucesivamente en direcciones $0°, 45°, 90°, 135°, \dots$ (giros de $45°$). Entonces los lados de longitud $3$ van en direcciones cardinales y los de longitud $\sqrt{2}$ en diagonales.

**Clave:** cada lado de longitud $\sqrt{2}$ en dirección diagonal ($45°$, $135°$, etc.) tiene proyección $\sqrt{2}\cos 45° = \sqrt{2}\cdot\tfrac{\sqrt{2}}{2} = 1$ sobre cada eje.

Partiendo de $(0,0)$, los vértices son:
$$(0,0) \to (3,0) \to (4,1) \to (4,4) \to (3,5) \to (0,5) \to (-1,4) \to (-1,1) \to (0,0)$$

Verificación de longitudes: los desplazamientos son $(3,0)$, $(1,1)$, $(0,3)$, $(-1,1)$, $(-3,0)$, $(-1,-1)$, $(0,-3)$, $(1,-1)$, es decir, lados que alternan $3$ y $\sqrt{2}$ con giros de $45°$. ✓

## Cálculo del área

**Método de la caja:** el octágono queda inscrito en un cuadrado de lado $3 + \sqrt{2}\cdot\sqrt{2}/2 \cdot 2 = 5$ (va de $x=-1$ a $x=4$ y de $y=0$ a $y=5$).

Las cuatro esquinas recortadas son triángulos rectángulos isósceles de catetos $1$, cada uno de área $\tfrac{1}{2}$:

$$\text{Área} = 5^2 - 4\cdot\tfrac{1}{2} = 25 - 2 = 23$$

**Verificación (shoelace):** con los vértices $(0,0),(3,0),(4,1),(4,4),(3,5),(0,5),(-1,4),(-1,1)$:
$$\tfrac{1}{2}\big[3 + 12 + 8 + 15 + 5 + 3\big] = \tfrac{46}{2} = 23 ✓$$

(En general, el área es $a^2 + b^2 + 2ab\sqrt{2}$, que con $a=3$, $b=\sqrt{2}$ da $9+2+12=23$.)

\boxed{23}