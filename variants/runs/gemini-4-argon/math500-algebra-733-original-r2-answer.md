Para encontrar el mayor valor de $x$ en el que las gráficas de $f(x)$ y $g(x)$ se intersecan, igualamos ambas funciones:

$$f(x) = g(x)$$

Observamos que los términos $e^{3x^2-|\lfloor x \rfloor|!}$, $\binom{22+735235|\lfloor x \rfloor |}{2356}$, $\phi(|\lfloor x \rfloor|+1)$ y $72x^4$ están bien definidos para cualquier número real $x$ y son idénticos en ambas funciones. Al restarlos en ambos lados de la ecuación, obtenemos:

$$3x^3 - 6x^2 + 2x + 1 = 4x^3 - 11x^2 - 6x + 13$$

Pasando todos los términos al lado derecho para igualar a cero:

$$0 = (4x^3 - 3x^3) + (-11x^2 + 6x^2) + (-6x - 2x) + (13 - 1)$$
$$x^3 - 5x^2 - 8x + 12 = 0$$

Probamos raíces enteras que dividan al término independiente $12$. Evaluando en $x = 1$:

$$1^3 - 5(1)^2 - 8(1) + 12 = 1 - 5 - 8 + 12 = 0$$

Por lo tanto, $(x - 1)$ es un factor. Factorizando el polinomio cúbico:

$$(x - 1)(x^2 - 4x - 12) = 0$$

Factorizamos el término cuadrático restante:

$$(x - 1)(x - 6)(x + 2) = 0$$

Las soluciones de la ecuación son $x = -2$, $x = 1$ y $x = 6$. El mayor valor de $x$ en el que las gráficas se intersecan es $6$.

\boxed{6}