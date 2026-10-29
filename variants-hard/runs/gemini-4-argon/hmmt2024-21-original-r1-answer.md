Para hallar el valor de $x$, analicemos la geometría de la configuración paso a paso:

1. **Orientación de los tres triángulos congruentes:**
   Sea $\triangle ABC$ el triángulo equilátero grande de lado $6$. Dado que los tres triángulos equiláteros congruentes de lado $x$ tienen sus lados paralelos a los de $\triangle ABC$ y cada uno tiene un único vértice sobre uno de los lados de $\triangle ABC$, estos tres triángulos deben estar orientados de forma invertida respecto a $\triangle ABC$ (con un vértice apuntando hacia el lado correspondiente de $\triangle ABC$ y el lado opuesto a dicho vértice paralelo a ese mismo lado de $\triangle ABC$).

2. **Posición del triángulo equilátero central:**
   Cada uno de los tres triángulos de lado $x$ tiene un vértice sobre un lado de $\triangle ABC$ y un vértice sobre un lado de otro de los tres triángulos. De este modo, los lados de los tres triángulos que son opuestos a los vértices apoyados sobre el borde de $\triangle ABC$ delimitan entre sí el triángulo equilátero central de lado $1$, el cual tiene la misma orientación que $\triangle ABC$.

3. **Relación entre las alturas (Teorema de Viviani):**
   Sea $h = \frac{\sqrt{3}}{2}$ la altura de un triángulo equilátero de lado $1$.
   - La altura del triángulo equilátero grande de lado $6$ es $H = 6h$.
   - La altura de cada uno de los tres triángulos equiláteros de lado $x$ es $h_x = xh$. Como cada uno tiene un vértice sobre un lado de $\triangle ABC$, la recta que contiene a su lado opuesto se encuentra a una distancia perpendicular igual a $xh$ de dicho lado de $\triangle ABC$.
   - Por el teorema de Viviani, para cualquier punto interior del triángulo equilátero central de lado $1$, la suma de sus distancias perpendiculares a los tres lados de $\triangle ABC$ es igual a la altura total $6h$.
   - Al restar las distancias $xh$ desde cada uno de los tres lados de $\triangle ABC$ hasta los tres lados del triángulo central, obtenemos que la suma de las distancias desde dicho punto a los tres lados del triángulo central (que es igual a la altura $1 \cdot h$ del triángulo central) cumple:
     $$1 \cdot h = 6h - 3(xh)$$

4. **Cálculo de $x$:**
   Dividiendo toda la ecuación entre $h$:
   $$1 = 6 - 3x \implies 3x = 5 \implies x = \frac{5}{3}$$

\boxed{\frac{5}{3}}