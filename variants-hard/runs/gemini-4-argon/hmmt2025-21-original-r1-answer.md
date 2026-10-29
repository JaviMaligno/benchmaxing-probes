Para calcular la longitud de $AD$, podemos situar los triángulos en un sistema de coordenadas cartesianas.

1. **Ubicación de los puntos sobre la recta $BC$:**
   Colocamos el punto $B$ en el origen $(0,0)$ y hacemos que la recta que contiene a los puntos $B, E, F$ y $C$ coincida con el eje $x$ positivo. A partir de las longitudes dadas ($BE = 14$, $EF = 15$, $FC = 16$), obtenemos las coordenadas de cada punto:
   - $B = (0, 0)$
   - $E = (14, 0)$
   - $F = (14 + 15, 0) = (29, 0)$
   - $C = (29 + 16, 0) = (45, 0)$

2. **Coordenadas de los vértices $A$ y $D$:**
   El lado del triángulo equilátero $\triangle ABC$ mide $BC = 45$. Situando $\triangle ABC$ en el semiplano superior ($y > 0$), las coordenadas del vértice $A$ son:
   $$A = \left(\frac{45}{2}, \frac{45\sqrt{3}}{2}\right)$$

   Por su parte, el triángulo equilátero $\triangle DEF$ tiene lado $EF = 15$. Como el punto $D$ se encuentra en el interior de $\triangle ABC$, también está en el semiplano superior ($y > 0$). Su coordenada en $x$ es el punto medio del segmento $EF$ y su coordenada en $y$ es la altura de $\triangle DEF$:
   $$D = \left(\frac{14 + 29}{2}, \frac{15\sqrt{3}}{2}\right) = \left(\frac{43}{2}, \frac{15\sqrt{3}}{2}\right)$$

3. **Cálculo de la distancia $AD$:**
   Calculamos las diferencias entre las coordenadas de $A$ y $D$:
   $$\Delta x = \frac{45}{2} - \frac{43}{2} = \frac{2}{2} = 1$$
   $$\Delta y = \frac{45\sqrt{3}}{2} - \frac{15\sqrt{3}}{2} = \frac{30\sqrt{3}}{2} = 15\sqrt{3}$$

   Aplicando la fórmula de la distancia entre dos puntos:
   $$AD = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{1^2 + (15\sqrt{3})^2} = \sqrt{1 + 225 \cdot 3} = \sqrt{1 + 675} = \sqrt{676} = 26$$

\boxed{26}