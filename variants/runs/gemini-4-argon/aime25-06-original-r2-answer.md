Para resolver este problema paso a paso, utilizamos las propiedades geométricas de un trapecio isósceles circunscrito a un círculo:

1. **Altura del trapecio:**
   Dado que el círculo está inscrito y es tangente a los cuatro lados del trapecio, la altura $h$ del trapecio es igual al diámetro del círculo. Como el radio del círculo es $3$, tenemos:
   $$h = 2 \times 3 = 6$$

2. **Suma de las bases paralelas ($r + s$):**
   El área $A$ de un trapecio se calcula mediante la fórmula $A = \frac{r+s}{2} \cdot h$. Sabemos que $A = 72$ y $h = 6$:
   $$72 = \frac{r+s}{2} \cdot 6$$
   $$\frac{r+s}{2} = 12 \implies r + s = 24$$

3. **Longitud de los lados no paralelos:**
   Por el teorema de Pitot, en todo cuadrilátero circunscrito a una circunferencia, la suma de las longitudes de los lados opuestos es igual. Como el trapecio es isósceles, sus dos lados no paralelos tienen la misma longitud, que llamaremos $L$:
   $$L + L = r + s$$
   $$2L = 24 \implies L = 12$$

4. **Producto de las bases ($r \cdot s$) o diferencia de las bases ($r - s$):**
   Trazando las alturas desde los vértices de la base menor hacia la base mayor, se forman dos triángulos rectángulos congruentes en los extremos, cada uno con hipotenusa $L = 12$, un cateto igual a la altura $h = 6$ y el otro cateto de longitud $\frac{|r-s|}{2}$. Aplicando el teorema de Pitágoras:
   $$\left(\frac{r-s}{2}\right)^2 + h^2 = L^2$$
   $$\frac{(r-s)^2}{4} + 6^2 = 12^2$$
   $$\frac{(r-s)^2}{4} + 36 = 144$$
   $$\frac{(r-s)^2}{4} = 108 \implies (r-s)^2 = 432$$

5. **Cálculo de $r^2 + s^2$:**
   Usando la identidad algebraica $(r+s)^2 + (r-s)^2 = 2(r^2 + s^2)$, despejamos $r^2 + s^2$:
   $$r^2 + s^2 = \frac{(r+s)^2 + (r-s)^2}{2}$$
   Sustituyendo $r+s = 24$ y $(r-s)^2 = 432$:
   $$r^2 + s^2 = \frac{24^2 + 432}{2} = \frac{576 + 432}{2} = \frac{1008}{2} = 504$$

\boxed{504}