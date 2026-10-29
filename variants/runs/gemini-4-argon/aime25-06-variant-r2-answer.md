Para resolver este problema paso a paso, utilizaremos las propiedades de un trapecio isósceles circunscrito a una circunferencia:

1. **Altura del trapecio:**
   Dado que la circunferencia de radio $r = 5$ está inscrita en el trapecio y es tangente a sus cuatro lados (incluyendo las dos bases paralelas), la altura $h$ del trapecio es igual al diámetro de la circunferencia:
   $$h = 2r = 2(5) = 10$$

2. **Suma de las bases ($a + b$):**
   El área $A$ de un trapecio con bases paralelas $a$ y $b$ y altura $h$ viene dada por la fórmula:
   $$A = \frac{a + b}{2} \cdot h$$
   Sustituyendo $A = 160$ y $h = 10$:
   $$160 = \frac{a + b}{2} \cdot 10 \implies 160 = 5(a + b) \implies a + b = 32$$

3. **Producto de las bases ($ab$):**
   Por el teorema de Pitot, en cualquier cuadrilátero circunscrito a una circunferencia, la suma de las longitudes de los lados opuestos es igual. Como el trapecio es isósceles, sus dos lados no paralelos tienen la misma longitud $c$, por lo que:
   $$2c = a + b \implies c = \frac{a + b}{2}$$
   Al trazar la altura desde un vértice de la base menor hacia la base mayor, se forma un triángulo rectángulo cuya hipotenusa es $c$, un cateto es la altura $h$ y el otro cateto es $\frac{|a - b|}{2}$. Aplicando el teorema de Pitágoras:
   $$c^2 = h^2 + \left(\frac{a - b}{2}\right)^2$$
   Sustituyendo $c = \frac{a + b}{2}$:
   $$\left(\frac{a + b}{2}\right)^2 - \left(\frac{a - b}{2}\right)^2 = h^2$$
   Desarrollando el lado izquierdo obtenemos la identidad $\frac{4ab}{4} = ab$, de modo que:
   $$ab = h^2 = 10^2 = 100$$

4. **Cálculo de $a^2 + b^2$:**
   Usando la identidad algebraica $a^2 + b^2 = (a + b)^2 - 2ab$:
   $$a^2 + b^2 = 32^2 - 2(100) = 1024 - 200 = 824$$

\boxed{824}