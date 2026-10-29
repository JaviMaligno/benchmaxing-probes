## Planteamiento

Ambas funciones comparten exactamente los mismos términos "decorativos":

$$e^{3x^2-|\lfloor x\rfloor|!}+\binom{22+735235|\lfloor x\rfloor|}{2356}+\phi(|\lfloor x\rfloor|+1)+72x^4$$

Al igualar $f(x)=g(x)$, todos esos términos se cancelan (están definidos para todo $x$ real, ya que $|\lfloor x\rfloor|$ es siempre un entero no negativo), y queda solo la parte polinómica restante:

$$3x^3-6x^2+2x+1 = 4x^3-11x^2-6x+13$$

## Resolución

$$0 = x^3 - 5x^2 - 8x + 12$$

Probando $x=1$: $1-5-8+12=0$, así que $(x-1)$ es factor:

$$x^3-5x^2-8x+12 = (x-1)(x^2-4x-12) = (x-1)(x-6)(x+2)$$

Las raíces son $x=-2$, $x=1$ y $x=6$.

## Verificación del dominio

En $x=6$ se tiene $\lfloor x\rfloor = 6$, por lo que $|\lfloor x\rfloor|! = 720$, el coeficiente binomial es $\binom{4411432}{2356}$ y $\phi(7)$ está bien definido. Todos los términos existen, luego la intersección es real.

\boxed{6}