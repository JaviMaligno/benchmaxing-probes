## Planteamiento

Ambas funciones comparten exactamente los mismos términos "complicados":

$$e^{3x^2-|\lfloor x \rfloor|!}+\binom{22+735235|\lfloor x \rfloor |}{2356}+\phi(|\lfloor x \rfloor|+1)+72x^4$$

Al igualar $f(x)=g(x)$, todos esos términos se cancelan (son idénticos para cada $x$), así que la ecuación se reduce a los polinomios restantes:

$$3x^3-6x^2+2x+1 = 4x^3-11x^2-6x+13$$

## Resolución

$$0 = x^3 - 5x^2 - 8x + 12$$

Probando $x=1$: $1-5-8+12=0$, así que $(x-1)$ es factor:

$$x^3-5x^2-8x+12 = (x-1)(x^2-4x-12) = (x-1)(x-6)(x+2)$$

Las raíces son $x=-2,\ 1,\ 6$.

## Verificación de dominio

Hay que comprobar que en $x=6$ los términos cancelados están realmente definidos:

- $|\lfloor 6 \rfloor|! = 720$ → el exponente $3(36)-720$ es finito.
- $\binom{22+735235\cdot 6}{2356} = \binom{4411432}{2356}$ → bien definido.
- $\phi(|\lfloor 6\rfloor|+1) = \phi(7) = 1+2+3+4+5+6 = 21$ → definido.

Todo está definido, por lo que $x=6$ es una intersección válida y es la mayor.

\boxed{6}