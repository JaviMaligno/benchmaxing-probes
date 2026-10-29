Para encontrar las intersecciones, igualamos f(x) = g(x). Los términos que dependen de ⌊x⌋ — la exponencial $e^{3x^2-|\lfloor x \rfloor|!}$, el coeficiente binomial y la función $\phi$ — son idénticos en ambas funciones, igual que el término $72x^4$, así que se cancelan todos. Queda:

$$3x^3-6x^2+2x+1 = 4x^3-11x^2-6x+13$$

Pasando todo a un lado:

$$0 = x^3 - 5x^2 - 8x + 12$$

Probamos raíces racionales: $x=1$ da $1-5-8+12=0$, así que $(x-1)$ es factor. Dividiendo:

$$x^3-5x^2-8x+12 = (x-1)(x^2-4x-12) = (x-1)(x-6)(x+2)$$

Las soluciones son $x = -2, 1, 6$. Como los términos cancelados están bien definidos y son iguales en ambas funciones para cualquier $x$ (en particular en $x=6$, donde $|\lfloor x \rfloor|! = 720$), las tres son intersecciones válidas, y la mayor es:

$$\boxed{6}$$