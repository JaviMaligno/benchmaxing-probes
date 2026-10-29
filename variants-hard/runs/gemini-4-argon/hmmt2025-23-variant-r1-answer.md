Para encontrar el producto $QW \cdot QX \cdot QY \cdot QZ$, comencemos determinando el área y el lado del cuadrado $WXYZ$.

1. **Área y lado del cuadrado:**
   Como el punto $Q$ está en el interior del cuadrado $WXYZ$, la suma de las áreas de los cuatro triángulos $\triangle QWX$, $\triangle QXY$, $\triangle QYZ$ y $\triangle QZW$ es igual al área total del cuadrado. Sea $s$ la longitud del lado del cuadrado:
   $$s^2 = 3 + 4 + 6 + 7 = 20 \implies s = \sqrt{20}$$

2. **Ubicación de las áreas y coordenadas de $Q$:**
   Las alturas desde $Q$ hacia cualquier par de lados opuestos del cuadrado suman $s$. Por lo tanto, la suma de las áreas de dos triángulos opuestos es igual a:
   $$\frac{1}{2} s \cdot h_1 + \frac{1}{2} s \cdot h_3 = \frac{1}{2} s (h_1 + h_3) = \frac{1}{2} s^2 = 10$$
   Observando las áreas dadas $\{3, 4, 6, 7\}$, los únicos pares que suman $10$ son $\{3, 7\}$ y $\{4, 6\}$. 

   Sin pérdida de generalidad, situemos el cuadrado en el plano cartesiano con vértices en $(0,0)$, $(s,0)$, $(s,s)$ y $(0,s)$, y sea $Q = (x, y)$. Las distancias de $Q$ a los cuatro lados son $x$, $s-x$, $y$ y $s-y$. Podemos asignar:
   - $\frac{1}{2} s x = 3 \implies x = \frac{6}{s}$
   - $\frac{1}{2} s (s-x) = 7 \implies s-x = \frac{14}{s}$
   - $\frac{1}{2} s y = 4 \implies y = \frac{8}{s}$
   - $\frac{1}{2} s (s-y) = 6 \implies s-y = \frac{12}{s}$

3. **Cálculo de las distancias a los vértices:**
   Elevando al cuadrado y sustituyendo $s^2 = 20$, obtenemos:
   $$x^2 = \frac{36}{20} = \frac{9}{5}, \quad (s-x)^2 = \frac{196}{20} = \frac{49}{5}$$
   $$y^2 = \frac{64}{20} = \frac{16}{5}, \quad (s-y)^2 = \frac{144}{20} = \frac{36}{5}$$

   Los cuadrados de las distancias desde $Q$ hasta los cuatro vértices del cuadrado son las sumas de los términos anteriores:
   - $d_1^2 = x^2 + y^2 = \frac{9}{5} + \frac{16}{5} = \frac{25}{5} = 5$
   - $d_2^2 = (s-x)^2 + y^2 = \frac{49}{5} + \frac{16}{5} = \frac{65}{5} = 13$
   - $d_3^2 = (s-x)^2 + (s-y)^2 = \frac{49}{5} + \frac{36}{5} = \frac{85}{5} = 17$
   - $d_4^2 = x^2 + (s-y)^2 = \frac{9}{5} + \frac{36}{5} = \frac{45}{5} = 9$

4. **Producto final:**
   Multiplicando las cuatro distancias:
   $$QW \cdot QX \cdot QY \cdot QZ = \sqrt{5} \cdot \sqrt{13} \cdot \sqrt{17} \cdot \sqrt{9} = 3\sqrt{5 \cdot 13 \cdot 17} = 3\sqrt{1105}$$

\boxed{3\sqrt{1105}}