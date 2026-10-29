Para hallar el área del cuadrilátero convexo formado por los circuncentros de los triángulos $\triangle ABC$, $\triangle BCD$, $\triangle CDA$ y $\triangle DAB$, podemos situar el trapecio $ABCD$ en un sistema de coordenadas cartesianas.

### Paso 1: Coordenadas de los vértices del trapecio
Colocamos el vértice $D$ en el origen $(0,0)$ y el lado $CD$ sobre el eje positivo de las $x$, de modo que $C = (19,0)$. Como $AB \parallel CD$ y $AB = 11$, los vértices $A$ y $B$ tienen la misma ordenada $h > 0$, pudiendo escribirse como $A = (x_A, h)$ y $B = (x_A + 11, h)$.

Usando las longitudes de los lados $DA = 4$ y $BC = 8$:
1. $DA^2 = x_A^2 + h^2 = 4^2 = 16$
2. $BC^2 = (19 - (x_A + 11))^2 + h^2 = (8 - x_A)^2 + h^2 = 8^2 = 64$

Restando la primera ecuación de la segunda:
$$(8 - x_A)^2 - x_A^2 = 64 - 16$$
$$64 - 16x_A = 48 \implies 16x_A = 16 \implies x_A = 1$$

Sustituyendo $x_A = 1$ en la primera ecuación obtenemos la altura $h$:
$$1^2 + h^2 = 16 \implies h = \sqrt{15}$$

Así, las coordenadas de los vértices son:
- $D = (0, 0)$
- $C = (19, 0)$
- $A = (1, \sqrt{15})$
- $B = (12, \sqrt{15})$

---

### Paso 2: Ecuaciones de las mediatrices de los lados
El circuncentro de un triángulo es la intersección de las mediatrices de sus lados. Observemos cómo se obtienen los cuatro circuncentros:
- El circuncentro de $\triangle DAB$ ($O_C$) es la intersección de las mediatrices de $AB$ y $DA$.
- El circuncentro de $\triangle ABC$ ($O_D$) es la intersección de las mediatrices de $AB$ y $BC$.
- El circuncentro de $\triangle BCD$ ($O_A$) es la intersección de las mediatrices de $CD$ y $BC$.
- El circuncentro de $\triangle CDA$ ($O_B$) es la intersección de las mediatrices de $CD$ y $DA$.

Por lo tanto, el cuadrilátero $O_C O_D O_A O_B$ tiene sus vértices exactamente en las intersecciones de las mediatrices de $AB$ y $CD$ con las mediatrices de $DA$ y $BC$.

Calculamos las ecuaciones de estas cuatro mediatrices:
1. **Mediatriz de $AB$ ($L_{AB}$):** Como $A=(1, \sqrt{15})$ y $B=(12, \sqrt{15})$, es la recta vertical:
   $$x = \frac{1 + 12}{2} = \frac{13}{2}$$

2. **Mediatriz de $CD$ ($L_{CD}$):** Como $D=(0,0)$ y $C=(19,0)$, es la recta vertical:
   $$x = \frac{0 + 19}{2} = \frac{19}{2}$$

3. **Mediatriz de $DA$ ($L_{DA}$):** El conjunto de puntos equidistantes de $D=(0,0)$ y $A=(1, \sqrt{15})$ cumple:
   $$x^2 + y^2 = (x - 1)^2 + (y - \sqrt{15})^2 \implies 2x + 2\sqrt{15}y = 16 \implies y = \frac{8 - x}{\sqrt{15}}$$

4. **Mediatriz de $BC$ ($L_{BC}$):** El conjunto de puntos equidistantes de $B=(12, \sqrt{15})$ y $C=(19, 0)$ cumple:
   $$(x - 12)^2 + (y - \sqrt{15})^2 = (x - 19)^2 + y^2$$
   $$-24x + 144 - 2\sqrt{15}y + 15 = -38x + 361 \implies 14x - 2\sqrt{15}y = 202 \implies y = \frac{7x - 101}{\sqrt{15}}$$

---

### Paso 3: Cálculo del área del cuadrilátero de circuncentros
Como $L_{AB}$ y $L_{CD}$ son dos rectas verticales paralelas ($x = \frac{13}{2}$ y $x = \frac{19}{2}$), el cuadrilátero formado por los cuatro circuncentros es un trapecio cuyas bases son los segmentos verticales determinados por $L_{DA}$ y $L_{BC}$ sobre dichas rectas.

Para un valor dado de $x$, la distancia vertical entre $L_{DA}$ y $L_{BC}$ es:
$$\Delta y(x) = \frac{8 - x}{\sqrt{15}} - \frac{7x - 101}{\sqrt{15}} = \frac{109 - 8x}{\sqrt{15}}$$

Evaluamos esta longitud en las dos rectas verticales:
- En $x = \frac{13}{2}$:
  $$b_1 = \Delta y\left(\frac{13}{2}\right) = \frac{109 - 8\left(\frac{13}{2}\right)}{\sqrt{15}} = \frac{109 - 52}{\sqrt{15}} = \frac{57}{\sqrt{15}}$$
- En $x = \frac{19}{2}$:
  $$b_2 = \Delta y\left(\frac{19}{2}\right) = \frac{109 - 8\left(\frac{19}{2}\right)}{\sqrt{15}} = \frac{109 - 76}{\sqrt{15}} = \frac{33}{\sqrt{15}}$$

La altura de este trapecio (la distancia horizontal entre las rectas verticales $x = \frac{13}{2}$ y $x = \frac{19}{2}$) es:
$$\Delta x = \frac{19}{2} - \frac{13}{2} = 3$$

Finalmente, el área del trapecio es:
$$\text{Área} = \frac{b_1 + b_2}{2} \cdot \Delta x = \frac{\frac{57}{\sqrt{15}} + \frac{33}{\sqrt{15}}}{2} \cdot 3 = \frac{90}{2\sqrt{15}} \cdot 3 = \frac{135}{\sqrt{15}} = 9\sqrt{15}$$

\boxed{9\sqrt{15}}