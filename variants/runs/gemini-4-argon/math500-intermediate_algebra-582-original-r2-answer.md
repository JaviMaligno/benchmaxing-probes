Para encontrar el valor de la suma pedida, primero observamos que $x = 0$ no es una raíz de la ecuación $x^{10} + (13x - 1)^{10} = 0$, ya que $0^{10} + (-1)^{10} = 1 \neq 0$.

Hacemos el cambio de variable $y = \frac{1}{x}$. Dividiendo la ecuación original entre $x^{10}$, obtenemos:
\[1 + \left(13 - \frac{1}{x}\right)^{10} = 0 \implies (y - 13)^{10} + 1 = 0.\]

Las raíces de esta nueva ecuación en $y$ son $y_k = \frac{1}{r_k}$ y $\overline{y}_k = \frac{1}{\overline{r}_k}$ para $k = 1, 2, 3, 4, 5$. Por lo tanto, la expresión que deseamos calcular se transforma en:
\[\sum_{k=1}^5 \frac{1}{r_k\overline{r}_k} = \sum_{k=1}^5 y_k\overline{y}_k = \sum_{k=1}^5 |y_k|^2.\]

Resolvemos ahora la ecuación $(y - 13)^{10} = -1$. Las raíces décimas de $-1$ son de la forma $e^{\pm i\theta_k}$, donde:
\[\theta_k = \frac{(2k - 1)\pi}{10}, \quad \text{para } k = 1, 2, 3, 4, 5.\]

Así, los pares de raíces conjugadas son:
\[y_k = 13 + \cos\theta_k + i\sin\theta_k \quad \text{y} \quad \overline{y}_k = 13 + \cos\theta_k - i\sin\theta_k.\]

Calculamos el producto $y_k\overline{y}_k$ para cada $k$:
\[y_k\overline{y}_k = (13 + \cos\theta_k)^2 + \sin^2\theta_k = 169 + 26\cos\theta_k + \cos^2\theta_k + \sin^2\theta_k = 170 + 26\cos\theta_k.\]

Sumando para $k = 1, 2, 3, 4, 5$:
\[\sum_{k=1}^5 y_k\overline{y}_k = \sum_{k=1}^5 (170 + 26\cos\theta_k) = 5 \cdot 170 + 26\sum_{k=1}^5 \cos\theta_k = 850 + 26\sum_{k=1}^5 \cos\theta_k.\]

Evaluamos la suma de los cosenos usando la identidad $\cos(\pi - \alpha) = -\cos\alpha$:
\[\sum_{k=1}^5 \cos\theta_k = \cos\frac{\pi}{10} + \cos\frac{3\pi}{10} + \cos\frac{5\pi}{10} + \cos\frac{7\pi}{10} + \cos\frac{9\pi}{10}.\]
Dado que $\cos\frac{9\pi}{10} = -\cos\frac{\pi}{10}$, $\cos\frac{7\pi}{10} = -\cos\frac{3\pi}{10}$ y $\cos\frac{5\pi}{10} = \cos\frac{\pi}{2} = 0$, todos los términos se cancelan y la suma de los cosenos es $0$.

Finalmente, obtenemos:
\[\sum_{k=1}^5 \frac{1}{r_k\overline{r}_k} = 850 + 26(0) = 850.\]

\boxed{850}