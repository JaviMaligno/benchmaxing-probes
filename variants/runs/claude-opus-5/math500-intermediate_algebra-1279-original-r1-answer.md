## Planteamiento

Multiplico por $P(x)=(x^2-1)(x^2-2)(x^2-3)(x^2-4)$:

$$\sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j) = (2010x-4)\,P(x)$$

Es decir, el polinomio

$$Q(x) = (2010x-4)P(x) - \sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j) = 0.$$

## Grado y coeficientes

- La suma de la izquierda tiene grado $6$ (en $x$), así que no afecta a los términos $x^9$ ni $x^8$.
- $P(x) = x^8 - 10x^6 + 35x^4 - 50x^2 + 24$ solo tiene potencias **pares**.
- Por tanto $2010x\,P(x)$ aporta solo potencias impares: el coeficiente de $x^9$ es $2010$.
- Y $-4P(x)$ aporta solo potencias pares: el coeficiente de $x^8$ es $-4$.

Así $Q$ tiene grado exactamente $9$, con

$$Q(x) = 2010x^9 - 4x^8 + \cdots$$

## Validez de las raíces

Ninguna raíz es espuria: si $x^2=k$ con $k\in\{1,2,3,4\}$, entonces
$Q(x) = -k\prod_{j\neq k}(k-j) \neq 0$, luego los polos no se cuelan como soluciones. Las $9$ raíces de $Q$ son exactamente las soluciones complejas de la ecuación original.

## Suma por Vieta

$$\sum x_i = -\frac{-4}{2010} = \frac{4}{2010} = \frac{2}{1005}$$

$$\boxed{\dfrac{2}{1005}}$$