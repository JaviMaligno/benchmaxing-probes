Para hallar el área del cuadrilátero convexo formado por los circuncentros de los triángulos $\triangle PQR$, $\triangle QRS$, $\triangle RSP$ y $\triangle SPQ$, podemos establecer un sistema de coordenadas cartesianas.

### Paso 1: Coordenadas de los vértices del trapecio
Colocamos la base $RS$ sobre el eje $x$ con $S$ en el origen:
$$S = (0, 0), \quad R = (18, 0)$$

Como $PQ \parallel RS$ y $PQ = 10$, sean $P = (x_P, h)$ y $Q = (x_P + 10, h)$, donde $h > 0$ es la altura del trapecio. Usando las longitudes de los lados laterales $SP = 5$ y $QR = 7$, tenemos:
$$SP^2 = x_P^2 + h^2 = 5^2 = 25$$
$$QR^2 = (18 - (x_P + 10))^2 + h^2 = (8 - x_P)^2 + h^2 = 7^2 = 49$$

Restando la primera ecuación de la segunda:
$$(8 - x_P)^2 - x_P^2 = 49 - 25 \implies 64 - 16x_P = 24 \implies 16x_P = 40 \implies x_P = \frac{5}{2}$$

Sustituyendo $x_P = \frac{5}{2}$ para hallar $h$:
$$h^2 = 25 - \left(\frac{5}{2}\right)^2 = \frac{75}{4} \implies h = \frac{5\sqrt{3}}{2}$$

Por lo tanto, los vértices $P$ y $Q$ son:
$$P = \left(\frac{5}{2}, \frac{5\sqrt{3}}{2}\right), \quad Q = \left(\frac{25}{2}, \frac{5\sqrt{3}}{2}\right)$$

---

### Paso 2: Ecuaciones de las mediatrices de los lados
Sean $O_1, O_2, O_3, O_4$ los circuncentros de $\triangle PQR$, $\triangle QRS$, $\triangle RSP$ y $\triangle SPQ$, respectivamente. Cada circuncentro se encuentra en la intersección de las mediatrices de los lados correspondientes:

1. **Mediatriz de $PQ$:** El punto medio de $PQ$ tiene abscisa $x = \frac{5/2 + 25/2}{2} = \frac{15}{2}$. Como $PQ$ es horizontal, su mediatriz es la recta vertical:
   $$x = \frac{15}{2}$$
   Tanto $O_1$ como $O_4$ pertenecen a esta recta.

2. **Mediatriz de $RS$:** El punto medio de $RS$ es $(9, 0)$, por lo que su mediatriz es la recta vertical:
   $$x = 9$$
   Tanto $O_2$ como $O_3$ pertenecen a esta recta.

3. **Mediatriz de $SP$:** Un punto $(x, y)$ equidista de $S(0,0)$ y $P\left(\frac{5}{2}, \frac{5\sqrt{3}}{2}\right)$ si y solo si:
   $$x^2 + y^2 = \left(x - \frac{5}{2}\right)^2 + \left(y - \frac{5\sqrt{3}}{2}\right)^2$$
   $$0 = -5x - 5\sqrt{3}y + \frac{25}{4} + \frac{75}{4} \implies 5x + 5\sqrt{3}y = 25 \implies y = \frac{5 - x}{\sqrt{3}}$$
   Tanto $O_3$ como $O_4$ pertenecen a esta recta.

4. **Mediatriz de $QR$:** Un punto $(x, y)$ equidista de $R(18,0)$ y $Q\left(\frac{25}{2}, \frac{5\sqrt{3}}{2}\right)$ si y solo si:
   $$(x - 18)^2 + y^2 = \left(x - \frac{25}{2}\right)^2 + \left(y - \frac{5\sqrt{3}}{2}\right)^2$$
   $$-36x + 324 = -25x - 5\sqrt{3}y + \frac{625}{4} + \frac{75}{4}$$
   $$-11x + 324 = -5\sqrt{3}y + 175 \implies 5\sqrt{3}y = 11x - 149 \implies y = \frac{11x - 149}{5\sqrt{3}}$$
   Tanto $O_1$ como $O_2$ pertenecen a esta recta.

---

### Paso 3: Coordenadas de los circuncentros y área del cuadrilátero
Evaluamos las ordenadas de los cuatro circuncentros en las rectas verticales $x = \frac{15}{2}$ y $x = 9$:

- En la recta $x = \frac{15}{2}$:
  $$y(O_4) = \frac{5 - 15/2}{\sqrt{3}} = -\frac{5}{2\sqrt{3}} = -\frac{25}{10\sqrt{3}}$$
  $$y(O_1) = \frac{11(15/2) - 149}{5\sqrt{3}} = \frac{165/2 - 298/2}{5\sqrt{3}} = -\frac{133}{10\sqrt{3}}$$
  La longitud del segmento vertical $O_1O_4$ es:
  $$L_1 = y(O_4) - y(O_1) = \frac{-25 - (-133)}{10\sqrt{3}} = \frac{108}{10\sqrt{3}} = \frac{54}{5\sqrt{3}}$$

- En la recta $x = 9$:
  $$y(O_3) = \frac{5 - 9}{\sqrt{3}} = -\frac{4}{\sqrt{3}}$$
  $$y(O_2) = \frac{11(9) - 149}{5\sqrt{3}} = \frac{-50}{5\sqrt{3}} = -\frac{10}{\sqrt{3}}$$
  La longitud del segmento vertical $O_2O_3$ es:
  $$L_2 = y(O_3) - y(O_2) = \frac{-4 - (-10)}{\sqrt{3}} = \frac{6}{\sqrt{3}} = \frac{30}{5\sqrt{3}}$$

El cuadrilátero $O_1O_2O_3O_4$ es un trapecio cuyas bases paralelas son los segmentos verticales $O_1O_4$ y $O_2O_3$, y cuya altura es la distancia horizontal entre las rectas $x = \frac{15}{2}$ y $x = 9$:
$$d = 9 - \frac{15}{2} = \frac{3}{2}$$

Finalmente, calculamos el área del trapecio $O_1O_2O_3O_4$:
$$\text{Área} = \frac{L_1 + L_2}{2} \cdot d = \frac{\frac{54}{5\sqrt{3}} + \frac{30}{5\sqrt{3}}}{2} \cdot \frac{3}{2} = \frac{84}{10\sqrt{3}} \cdot \frac{3}{2} = \frac{63}{5\sqrt{3}} = \frac{21\sqrt{3}}{5}$$

\boxed{\frac{21\sqrt{3}}{5}}