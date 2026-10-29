Para encontrar el valor de $r^2 + s^2$, podemos resolver el problema paso a paso utilizando las propiedades geométricas de un trapecio isósceles circunscrito a un círculo:

1. **Altura del trapecio:**
   Como el círculo inscrito es tangente a los cuatro lados (incluyendo las dos bases paralelas), la altura $h$ del trapecio es igual al diámetro del círculo. Dado que el radio es $R = 3$:
   $$h = 2R = 2(3) = 6$$

2. **Suma de las bases ($r + s$):**
   El área $A$ de un trapecio está dada por la fórmula $A = \frac{r+s}{2} \cdot h$. Sabemos que $A = 72$ y $h = 6$, por lo que:
   $$72 = \frac{r+s}{2} \cdot 6$$
   $$\frac{r+s}{2} = 12 \implies r + s = 24$$

3. **Longitud de los lados no paralelos y producto de las bases ($rs$):**
   En cualquier cuadrilátero tangencial (que tiene un círculo inscrito), la suma de las longitudes de los lados opuestos es igual. Como el trapecio es isósceles, sus dos lados no paralelos tienen la misma longitud $l$. Por lo tanto:
   $$l + l = r + s \implies 2l = 24 \implies l = 12$$

   Si trazamos las alturas desde los vértices de la base menor hasta la base mayor, se forman dos triángulos rectángulos congruentes en los extremos, cada uno con hipotenusa $l$, altura $h$ y base $\frac{|r-s|}{2}$. Aplicando el teorema de Pitágoras:
   $$\left(\frac{r-s}{2}\right)^2 + h^2 = l^2$$
   Como $l = \frac{r+s}{2}$, podemos sustituir:
   $$\left(\frac{r-s}{2}\right)^2 + h^2 = \left(\frac{r+s}{2}\right)^2$$
   Desarrollando los cuadrados y simplificando obtenemos la relación clásica $rs = h^2$:
   $$h^2 = \frac{(r+s)^2 - (r-s)^2}{4} = \frac{4rs}{4} = rs$$
   Dado que $h = 6$:
   $$rs = 6^2 = 36$$

4. **Cálculo de $r^2 + s^2$:**
   Utilizando la identidad algebraica $r^2 + s^2 = (r+s)^2 - 2rs$:
   $$r^2 + s^2 = (24)^2 - 2(36) = 576 - 72 = 504$$

\boxed{504}