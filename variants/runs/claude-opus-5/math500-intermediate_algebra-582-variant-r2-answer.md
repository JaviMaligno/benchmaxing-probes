## Planteamiento

Como $x=0$ no es raíz, divido entre $x^{10}$:

$$\left(\frac{11x-1}{x}\right)^{10} = -1$$

Defino $w = \dfrac{11x-1}{x} = 11 - \dfrac1x$, de modo que $w^{10} = -1$.

## Despejar $1/x$

De la relación anterior: $\dfrac1x = 11 - w$, donde $w$ recorre las 10 raíces de $w^{10}+1=0$.

Para cada raíz $s$ con su conjugada $\bar s$:

$$\frac{1}{s\bar s} = \left|\frac1s\right|^2 = |11-w|^2$$

## Sumar

Los dos elementos de un par conjugado dan el mismo valor de $|11-w|^2$, y la suma pedida toma un término por par. Por tanto es la mitad de la suma sobre las 10 raíces:

$$\sum_{k=1}^{5}\frac{1}{s_k\bar s_k} = \frac12\sum_{w^{10}=-1}|11-w|^2$$

Desarrollando, con $|w|=1$:

$$|11-w|^2 = (11-w)(11-\bar w) = 121 - 11(w+\bar w) + 1 = 122 - 11(w+\bar w)$$

El conjunto de raíces de $w^{10}+1=0$ es cerrado bajo conjugación y la suma de sus raíces es $0$ (el coeficiente de $w^9$ es nulo), así que $\sum w = \sum \bar w = 0$:

$$\sum_{w^{10}=-1}|11-w|^2 = 10\cdot 122 - 11\cdot 0 = 1220$$

Finalmente:

$$\frac{1220}{2} = 610$$

$$\boxed{610}$$