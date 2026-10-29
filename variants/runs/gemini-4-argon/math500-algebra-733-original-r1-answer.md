Para hallar los puntos de intersección de las gráficas de $f(x)$ y $g(x)$, igualamos ambas funciones:

$$f(x) = g(x)$$

Observamos que los primeros cuatro términos en ambas expresiones son idénticos y están bien definidos para todo número real $x$:
$$e^{3x^2-|\lfloor x \rfloor|!}+\binom{22+735235|\lfloor x \rfloor |}{2356}+\phi(|\lfloor x \rfloor|+1)+72x^4$$

Al restar estos términos comunes de ambos lados de la ecuación, obtenemos:

$$3x^3 - 6x^2 + 2x + 1 = 4x^3 - 11x^2 - 6x + 13$$

Pasamos todos los términos al lado derecho para igualar a cero:

$$0 = (4x^3 - 3x^3) + (-11x^2 + 6x^2) + (-6x - 2x) + (13 - 1)$$
$$x^3 - 5x^2 - 8x + 12 = 0$$

Buscamos raíces racionales evaluando en divisores de $12$. Probando con $x = 1$:
$$1^3 - 5(1)^2 - 8(1) + 12 = 1 - 5 - 8 + 12 = 0$$

Por lo tanto, $(x - 1)$ es un factor. Factorizando el polinomio cúbico:
$$(x - 1)(x^2 - 4x - 12) = 0$$

Factorizamos el término cuadrático restante:
$$(x - 1)(x - 6)(x + 2) = 0$$

Las soluciones son $x = -2$, $x = 1$ y $x = 6$. El mayor valor de $x$ en el que las gráficas se intersecan es $6$.

\boxed{6}