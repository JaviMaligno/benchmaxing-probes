Para encontrar la suma de todos los valores posibles de $\varphi$, observamos que la ecuación dada es una serie geométrica de razón $-w$:
\[w^{10} - w^9 + w^8 - w^7 + w^6 - w^5 + w^4 - w^3 + w^2 - w + 1 = 0.\]

Multiplicando ambos lados por $w + 1$ (notando que $w = -1$ no es solución, ya que al sustituir $w = -1$ la suma resulta ser $11 \neq 0$), obtenemos:
\[(w + 1)(w^{10} - w^9 + w^8 - \dots - w + 1) = w^{11} + 1 = 0, \quad \text{con } w \neq -1.\]

Por lo tanto, las soluciones satisfacen $w^{11} = -1$ y $w \neq -1$. Sustituyendo la forma polar $w = \rho e^{i \varphi}$:
\[\rho^{11} e^{i 11\varphi} = -1 = 1 \cdot e^{i(2k+1)\pi}, \quad k \in \mathbb{Z}.\]

Como $\rho > 0$, se deduce que $\rho = 1$. Para que el ángulo cumpla $0 \le \varphi < 2\pi$, los valores posibles de $\varphi$ vienen dados por:
\[\varphi_k = \frac{(2k + 1)\pi}{11}, \quad \text{para } k = 0, 1, 2, \dots, 10.\]

La condición $w \neq -1$ excluye el ángulo $\varphi = \pi$, el cual corresponde a $k = 5$ (puesto que $\varphi_5 = \frac{11\pi}{11} = \pi$).

Calculamos primero la suma de los $11$ ángulos y luego restamos $\pi$:
\[\sum_{k=0}^{10} \frac{(2k + 1)\pi}{11} = \frac{\pi}{11} \sum_{k=0}^{10} (2k + 1) = \frac{\pi}{11} \cdot 11^2 = 11\pi.\]

Excluyendo el valor $\varphi_5 = \pi$, la suma de todos los valores posibles de $\varphi$ es:
\[11\pi - \pi = 10\pi.\]

\boxed{10\pi}