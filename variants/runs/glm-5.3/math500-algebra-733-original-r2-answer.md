Voy a resolver el problema paso a paso.

## Paso 1: Identificar los términos comunes

Ambas funciones comparten exactamente los mismos tres términos:
$$e^{3x^2-|\lfloor x \rfloor|!}, \qquad \binom{22+735235|\lfloor x \rfloor|}{2356}, \qquad \phi(|\lfloor x \rfloor|+1)$$

Estos términos (con las funciones piso, factorial, binomial y phi) parecen intimidantes, pero aparecen **idénticos** en $f$ y en $g$. Son una distracción: en cualquier intersección $f(x)=g(x)$ se cancelan automáticamente.

## Paso 2: Plantear la ecuación de intersección

La condición $f(x) = g(x)$ se reduce a igualar solo las partes polinomiales:
$$72x^4+3x^3-6x^2+2x+1 = 72x^4+4x^3-11x^2-6x+13$$

Los términos $72x^4$ se cancelan:
$$3x^3-6x^2+2x+1 = 4x^3-11x^2-6x+13$$

## Paso 3: Reordenar

$$0 = x^3 - 5x^2 - 8x + 12$$

## Paso 4: Factorizar el polinomio cúbico

Pruebo $x=1$: $\;1 - 5 - 8 + 12 = 0$ ✓, así que $(x-1)$ es factor:
$$x^3 - 5x^2 - 8x + 12 = (x-1)(x^2 - 4x - 12) = (x-1)(x-6)(x+2)$$

## Paso 5: Encontrar las raíces

Las intersecciones ocurren en:
$$x = -2, \quad x = 1, \quad x = 6$$

(Verificación de $x=6$: $f$ y $g$ difieren en $-x^3+5x^2+8x-12 = -216+180+48-12 = 0$ ✓)

## Paso 6: El mayor valor de $x$

De las tres intersecciones, la mayor es $x = 6$.

$$\boxed{6}$$