Para calcular el producto $PA \cdot PB \cdot PC \cdot PD$, procedemos paso a paso:

1. **Área del cuadrado:**
   Sea $s$ la longitud del lado del cuadrado $ABCD$. El punto $P$ en el interior del cuadrado lo divide en cuatro triángulos: $\triangle PAB$, $\triangle PBC$, $\triangle PCD$ y $\triangle PDA$. La suma de sus áreas es igual al área total del cuadrado:
   $$s^2 = 1 + 2 + 3 + 4 = 10 \implies s = \sqrt{10}$$

2. **Alturas de los triángulos:**
   Las sumas de las áreas de los pares de triángulos opuestos son iguales a la mitad del área del cuadrado:
   $$\text{Área}(\triangle PAB) + \text{Área}(\triangle PCD) = \frac{1}{2}s^2 = 5$$
   $$\text{Área}(\triangle PBC) + \text{Área}(\triangle PDA) = \frac{1}{2}s^2 = 5$$
   Por lo tanto, los pares de triángulos opuestos deben tener áreas $\{1, 4\}$ y $\{2, 3\}$.

   Ubicamos el cuadrado en el plano cartesiano con vértices en $(0,0)$, $(s,0)$, $(s,s)$ y $(0,s)$, y sea $P = (x, y)$. Sin pérdida de generalidad, podemos asignar las distancias de $P$ a los lados del cuadrado de modo que:
   - Las alturas correspondientes a las áreas $2$ y $3$ sean $x$ y $s - x$:
     $$\frac{1}{2} s x = 2 \implies x = \frac{4}{s}$$
     $$\frac{1}{2} s (s - x) = 3 \implies s - x = \frac{6}{s}$$
   - Las alturas correspondientes a las áreas $1$ y $4$ sean $y$ y $s - y$:
     $$\frac{1}{2} s y = 1 \implies y = \frac{2}{s}$$
     $$\frac{1}{2} s (s - y) = 4 \implies s - y = \frac{8}{s}$$

3. **Distancias desde $P$ a los vértices:**
   Sustituyendo $s^2 = 10$, calculamos los cuadrados de las coordenadas y distancias a los lados:
   $$x^2 = \frac{16}{s^2} = \frac{16}{10} = \frac{8}{5}, \quad (s - x)^2 = \frac{36}{s^2} = \frac{36}{10} = \frac{18}{5}$$
   $$y^2 = \frac{4}{s^2} = \frac{4}{10} = \frac{2}{5}, \quad (s - y)^2 = \frac{64}{s^2} = \frac{64}{10} = \frac{32}{5}$$

   Por el teorema de Pitágoras, los cuadrados de las distancias desde $P$ hasta los cuatro vértices son las cuatro combinaciones posibles de sumas:
   - $d_1^2 = x^2 + y^2 = \frac{8}{5} + \frac{2}{5} = 2 \implies d_1 = \sqrt{2}$
   - $d_2^2 = (s - x)^2 + y^2 = \frac{18}{5} + \frac{2}{5} = 4 \implies d_2 = 2$
   - $d_3^2 = (s - x)^2 + (s - y)^2 = \frac{18}{5} + \frac{32}{5} = 10 \implies d_3 = \sqrt{10}$
   - $d_4^2 = x^2 + (s - y)^2 = \frac{8}{5} + \frac{32}{5} = 8 \implies d_4 = 2\sqrt{2}$

4. **Producto final:**
   Multiplicando las cuatro distancias obtenemos:
   $$PA \cdot PB \cdot PC \cdot PD = \sqrt{2} \cdot 2 \cdot \sqrt{10} \cdot 2\sqrt{2} = 8\sqrt{10}$$

\boxed{8\sqrt{10}}