Para hallar el valor de $x$, analicemos la configuración geométrica paso a paso:

1. **Orientación de los tres triángulos congruentes:**
   Sea $ABC$ el triángulo equilátero grande de lado $L = 9$. Cualquier triángulo equilátero en su interior con lados paralelos a los de $ABC$ puede tener la misma orientación que $ABC$ o la orientación opuesta (invertida). 
   Para que cada uno de los tres triángulos de lado $x$ tenga **un único vértice** sobre uno de los lados de $ABC$ y esté completamente contenido en $ABC$, deben tener la orientación opuesta (invertida) respecto a $ABC$.

2. **Posición de los lados que encierran el triángulo central:**
   Consideremos uno de los tres triángulos congruentes de lado $x$, cuyo vértice inferior se apoya sobre el lado $BC$ del triángulo grande. Como sus lados son paralelos a los de $ABC$, el lado opuesto a dicho vértice es paralelo a $BC$ y se encuentra a una distancia perpendicular de $BC$ igual a la altura de un triángulo equilátero de lado $x$, es decir:
   $$d = \frac{\sqrt{3}}{2}x$$
   Por la simetría rotacional del arreglo en molinete (*pinwheel*), los tres lados interiores de los tres triángulos congruentes son paralelos a $BC$, $CA$ y $AB$ respectivamente, y cada uno se encuentra a una distancia perpendicular $d = \frac{\sqrt{3}}{2}x$ del lado correspondiente de $ABC$.

3. **Relación entre los lados y el triángulo central:**
   El triángulo equilátero central de lado $s = 2$ está delimitado precisamente por las rectas que contienen estos tres lados interiores (y tiene la misma orientación que $ABC$).
   Cuando desplazamos cada uno de los tres lados de un triángulo equilátero de lado $L$ hacia el interior una distancia perpendicular $d = \frac{\sqrt{3}}{2}x$, la longitud del lado disminuye en $x$ por cada uno de los tres desplazamientos. En efecto, si verificamos que los vértices se tocan correctamente:
   - Si usamos coordenadas $(u, v, w)$ que representan las distancias a los lados $BC, CA, AB$ medidas en unidades de $\frac{\sqrt{3}}{2}$ (de modo que $u + v + w = 9$), los tres triángulos están definidos por:
     - $T_1: u \le x,\; v \le 2x,\; w \le 9 - 2x$ (con vértice $(0, 2x, 9-2x)$ en $BC$ y vértice $(x, x, 9-2x)$ sobre el lado $v = x$ de $T_2$),
     - $T_2: v \le x,\; w \le 2x,\; u \le 9 - 2x$,
     - $T_3: w \le x,\; u \le 2x,\; v \le 9 - 2x$.
   - La región central encerrada por $T_1, T_2, T_3$ está dada por $u \ge x,\; v \ge x,\; w \ge x$, que es un triángulo equilátero de lado $L - 3x$.

4. **Cálculo de $x$:**
   Igualando la longitud del lado del triángulo central a $2$:
   $$L - 3x = s \implies 9 - 3x = 2 \implies 3x = 7 \implies x = \frac{7}{3}$$

\boxed{\frac{7}{3}}