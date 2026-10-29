## Planteamiento

La expresión es una suma geométrica alternada:

$$w^{10} - w^9 + \cdots - w + 1 = \sum_{k=0}^{10} (-w)^k = \frac{1-(-w)^{11}}{1+w} = \frac{w^{11}+1}{w+1}$$

válida para $w \neq -1$.

## Resolución

La ecuación equivale entonces a $w^{11} = -1$ con $w \neq -1$.

Las soluciones de $w^{11} = -1$ son
$$w = e^{i(2k+1)\pi/11}, \qquad k = 0,1,\dots,10,$$
todas de módulo $\rho = 1$, con argumentos $\varphi = \frac{(2k+1)\pi}{11} \in [0, 2\pi)$.

El valor $k=5$ da $\varphi = \pi$, es decir $w=-1$, que hay que descartar.

## Suma

$$\sum_{k=0}^{10} \frac{(2k+1)\pi}{11} = \frac{\pi}{11}\cdot 121 = 11\pi$$

Quitando el término $\pi$ correspondiente a $k=5$:

$$11\pi - \pi = 10\pi$$

\boxed{10\pi}