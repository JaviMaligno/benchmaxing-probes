Para encontrar el mayor valor de $x$ en el que las gráficas de $p(x)$ y $q(x)$ se intersecan, igualamos ambas funciones:

$$p(x) = q(x)$$

Observamos que los primeros cuatro términos de ambas funciones:
$$e^{2x^2-|\lfloor x \rfloor|!} + \binom{19+735235|\lfloor x \rfloor |}{2356} + \phi(|\lfloor x \rfloor|+1) + 51x^4$$
son idénticos y están bien definidos para cualquier número real $x$ (ya que $|\lfloor x \rfloor|$ es siempre un entero no negativo). Al restar estos términos comunes de ambos lados de la ecuación, obtenemos:

$$3x^3 - 4x^2 + 5x + 2 = 4x^3 - 7x^2 - 8x + 17$$

Pasando todos los términos al lado derecho para igualar a cero:

$$x^3 - 3x^2 - 13x + 15 = 0$$

Probamos raíces enteras que dividan a $15$. Evaluando en $x = 1$:
$$(1)^3 - 3(1)^2 - 13(1) + 15 = 1 - 3 - 13 + 15 = 0$$

Por lo tanto, $(x - 1)$ es un factor. Factorizando el polinomio cúbico:

$$(x - 1)(x^2 - 2x - 15) = 0$$
$$(x - 1)(x - 5)(x + 3) = 0$$

Las soluciones son $x = -3$, $x = 1$ y $x = 5$. El mayor de estos valores es $5$.

\boxed{5}