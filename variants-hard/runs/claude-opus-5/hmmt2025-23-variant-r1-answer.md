## Planteamiento

En un cuadrado, los triángulos formados por $Q$ con lados **opuestos** suman la mitad del área total:

$$[QWX]+[QYZ] = [QXY]+[QZW] = \tfrac{1}{2}[WXYZ]$$

El área total es $3+4+6+7=20$, así que cada par opuesto suma $10$: los pares deben ser $\{3,7\}$ y $\{4,6\}$. El lado es $s=\sqrt{20}=2\sqrt5$.

## Coordenadas

Tomo $W=(0,0)$, $X=(s,0)$, $Y=(s,s)$, $Z=(0,s)$, $Q=(x,y)$. Entonces:

$$[QWX]=\tfrac{s y}{2},\quad [QXY]=\tfrac{s(s-x)}{2},\quad [QYZ]=\tfrac{s(s-y)}{2},\quad [QZW]=\tfrac{s x}{2}$$

Con $[QWX]=3$, $[QYZ]=7$, $[QXY]=4$, $[QZW]=6$ y $s=\frac{10}{\sqrt5}$:

$$y=\frac{3}{\sqrt5},\quad s-y=\frac{7}{\sqrt5},\quad x=\frac{6}{\sqrt5},\quad s-x=\frac{4}{\sqrt5}$$

## Distancias

$$QW^2=\frac{36+9}{5}=9,\qquad QX^2=\frac{16+9}{5}=5,\qquad QY^2=\frac{16+49}{5}=13,\qquad QZ^2=\frac{36+49}{5}=17$$

Por tanto:

$$(QW\cdot QX\cdot QY\cdot QZ)^2 = 9\cdot 5\cdot 13\cdot 17 = 9945$$

$$QW\cdot QX\cdot QY\cdot QZ=\sqrt{9945}=3\sqrt{1105}\approx 99.73$$

Las demás asignaciones compatibles de las áreas solo permutan los cuatro valores $\{9,5,13,17\}$, así que el producto es el mismo.

\boxed{3\sqrt{1105}}