Para resolver el problema paso a paso, podemos establecer un sistema de coordenadas cartesianas con origen en el punto $A$:

1. **Ubicación de las circunferencias y los puntos $A, B, C, D$:**
   - Sea $A = (0, 0)$ el centro de $\omega_1$. Como su radio es $6$, la ecuación de $\omega_1$ es:
     $$x^2 + y^2 = 36$$
   - Situemos el diámetro $\overline{BC}$ de $\omega_2$ sobre el eje $x$, con el punto de tangencia en $B = (6, 0)$.
   - Como $\omega_1$ es tangente interiormente a $\omega_2$ en $B$ y el radio de $\omega_2$ es $15$, el centro de $\omega_2$ se encuentra en $O = (6 - 15, 0) = (-9, 0)$, y el otro extremo del diámetro es $C = (6 - 30, 0) = (-24, 0)$.
   - La ecuación de $\omega_2$ es:
     $$(x + 9)^2 + y^2 = 15^2 = 225$$
   - Dado que $\overline{AD} \perp \overline{BC}$ y $A = (0, 0)$, el punto $D$ se encuentra sobre el eje $y$, es decir, $D = (0, y_D)$. Tomando $y_D > 0$ (como se muestra en la figura) y sustituyendo $x = 0$ en la ecuación de $\omega_2$:
     $$(0 + 9)^2 + y_D^2 = 225 \implies 81 + y_D^2 = 225 \implies y_D^2 = 144 \implies y_D = 12$$
     Por lo tanto, $D = (0, 12)$.

2. **Coordenadas del rectángulo inscrito $EFGH$:**
   - Todo rectángulo inscrito en $\omega_1$ tiene su centro en el centro de la circunferencia, $A = (0, 0)$.
   - Como $\overline{EF} \perp \overline{BC}$, los lados $\overline{EF}$ y $\overline{GH}$ son verticales, mientras que $\overline{FG}$ y $\overline{EH}$ son horizontales.
   - Teniendo en cuenta que $C(-24, 0)$ está más cerca de $\overline{GH}$ que de $\overline{EF}$, y $D(0, 12)$ está más cerca de $\overline{FG}$ que de $\overline{EH}$, las coordenadas de los vértices para $x > 0$ e $y > 0$ con $x^2 + y^2 = 36$ son:
     $$E = (x, -y), \quad F = (x, y), \quad G = (-x, y), \quad H = (-x, -y)$$

3. **Áreas de los triángulos $\triangle DGF$ y $\triangle CHG$:**
   - Para $\triangle DGF$, la base horizontal $\overline{GF}$ mide $2x$ y la altura desde $D(0, 12)$ hasta la recta $GF$ ($y = \text{cte}$) es $12 - y$. Su área es:
     $$\text{Área}(\triangle DGF) = \frac{1}{2} (2x)(12 - y) = x(12 - y)$$
   - Para $\triangle CHG$, la base vertical $\overline{HG}$ mide $2y$ y la altura desde $C(-24, 0)$ hasta la recta $HG$ ($x = \text{cte}$) es $24 - x$. Su área es:
     $$\text{Área}(\triangle CHG) = \frac{1}{2} (2y)(24 - x) = y(24 - x)$$

4. **Igualación de áreas y cálculo del área de $EFGH$:**
   - Igualando las áreas de ambos triángulos:
     $$x(12 - y) = y(24 - x)$$
     $$12x - xy = 24y - xy \implies 12x = 24y \implies x = 2y$$
   - Sustituyendo $x = 2y$ en la ecuación de la circunferencia $\omega_1$ ($x^2 + y^2 = 36$):
     $$(2y)^2 + y^2 = 36 \implies 5y^2 = 36 \implies y^2 = \frac{36}{5}$$
   - El área del rectángulo $EFGH$ de lados $2x$ y $2y$ es:
     $$\text{Área}(EFGH) = (2x)(2y) = 4xy = 4(2y)y = 8y^2 = 8 \cdot \frac{36}{5} = \frac{288}{5}$$

Como $m = 288$ y $n = 5$ son enteros positivos coprimos entre sí, tenemos que $m + n = 288 + 5 = 293$.

\boxed{293}