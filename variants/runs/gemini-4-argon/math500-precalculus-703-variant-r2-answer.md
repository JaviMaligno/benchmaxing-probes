Para encontrar la suma de todos los posibles valores de $\varphi$, primero simplificamos la ecuación dada:
\[w^{10} - w^9 + w^8 - w^7 + w^6 - w^5 + w^4 - w^3 + w^2 - w + 1 = 0.\]

Notamos que el lado izquierdo es una serie geométrica de 11 términos con razón $-w$. Como $w = -1$ no es solución (al sustituir $w = -1$ obtenemos $11 \neq 0$), podemos multiplicar ambos lados de la ecuación por $w + 1$:
\[(w + 1)(w^{10} - w^9 + w^8 - w^7 + w^6 - w^5 + w^4 - w^3 + w^2 - w + 1) = 0\]
\[w^{11} + 1 = 0 \implies w^{11} = -1, \quad \text{con } w \neq -1.\]

Sustituyendo la forma polar $w = \rho e^{i \varphi}$ en $w^{11} = -1$:
\[\rho^{11} e^{i 11\varphi} = e^{i \pi}.\]

Comparando los módulos, como $\rho > 0$, tenemos $\rho^{11} = 1 \implies \rho = 1$.

Comparando los argumentos, obtenemos:
\[11\varphi = \pi + 2k\pi = (2k + 1)\pi \implies \varphi = \frac{(2k + 1)\pi}{11}, \quad k \in \mathbb{Z}.\]

Dado que $0 \le \varphi < 2\pi$, los valores enteros de $k$ deben cumplir:
\[0 \le \frac{(2k + 1)\pi}{11} < 2\pi \implies 0 \le 2k + 1 < 22 \implies k \in \{0, 1, 2, \dots, 10\}.\]

De estos 11 valores, debemos excluir aquel que corresponde a $w = -1$, es decir, $\varphi = \pi$ (que ocurre cuando $k = 5$).

Por lo tanto, la suma de todos los valores posibles de $\varphi$ es la suma de los 11 ángulos menos $\pi$:
\[\sum_{\substack{k=0 \\ k \neq 5}}^{10} \frac{(2k + 1)\pi}{11} = \left( \frac{\pi}{11} \sum_{k=0}^{10} (2k + 1) \right) - \pi = \frac{\pi}{11} (11^2) - \pi = 11\pi - \pi = 10\pi.\]

\boxed{10\pi}