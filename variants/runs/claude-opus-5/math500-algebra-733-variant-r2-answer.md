## Planteamiento

Los dos primeros tres términos de $p$ y $q$ son idénticos:
$$e^{2x^2-|\lfloor x\rfloor|!}+\binom{19+735235|\lfloor x\rfloor|}{2356}+\phi(|\lfloor x\rfloor|+1)+51x^4$$

Por tanto, al igualar $p(x)=q(x)$, todo eso se cancela (son distracciones) y queda:

$$3x^3-4x^2+5x+2 = 4x^3-7x^2-8x+17$$

## Resolución

$$0 = x^3 - 3x^2 - 13x + 15$$

Probando $x=1$: $1-3-13+15=0$ ✓

Factorizando:
$$x^3-3x^2-13x+15 = (x-1)(x^2-2x-15) = (x-1)(x-5)(x+3)$$

Las raíces son $x=-3,\ 1,\ 5$.

## Verificación de dominio

En $x=5$: $\lfloor x\rfloor = 5$, de modo que $|\lfloor x\rfloor|! = 120$, el coeficiente binomial $\binom{19+3676175}{2356}$ está bien definido, y $\phi(6)$ también. Ambas funciones existen allí, así que la intersección es válida.

\boxed{5}