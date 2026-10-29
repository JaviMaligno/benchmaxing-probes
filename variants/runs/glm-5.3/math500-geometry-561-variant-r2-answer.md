## Planteamiento

Un octógono equiangulador tiene ángulos de 135°, así que cada lado gira 45° respecto al anterior. Como las longitudes alternan 3, √2, 3, √2, …, los lados opuestos son paralelos e iguales, y el octógono cierra bien.

**Vectores de los lados** (girando 45° cada vez):

$$(3,0),\ (1,1),\ (0,3),\ (-1,1),\ (-3,0),\ (-1,-1),\ (0,-3),\ (1,-1)$$

pues $\sqrt{2}(\cos 45^\circ, \sin 45^\circ) = (1,1)$, etc. La suma es $(0,0)$: la figura cierra.

**Vértices** (partiendo del origen):

$$(0,0),\ (3,0),\ (4,1),\ (4,4),\ (3,5),\ (0,5),\ (-1,4),\ (-1,1)$$

**Fórmula del shoelace:**

$$\sum x_i y_{i+1} = 0+3+16+20+15+0-1+0 = 53$$
$$\sum y_i x_{i+1} = 0+0+4+12+0-5-4+0 = 7$$

$$\text{Área} = \frac{53-7}{2} = 23$$

**Verificación geométrica:** el octógono está inscrito en el cuadrado $x\in[-1,4]$, $y\in[0,5]$, de área $25$, y le faltan exactamente cuatro triángulos rectos isósceles de catetos $1$ (uno en cada esquina), es decir $4\cdot\tfrac12 = 2$:

$$25 - 2 = 23 \checkmark$$

$$\boxed{23}$$