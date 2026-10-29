Para encontrar el valor de la suma pedida, realizamos primero un cambio de variable que simplifique la expresión de las raíces.

Dado que $x = 0$ claramente no es solución de la ecuación $x^{10} + (13x - 1)^{10} = 0$, podemos dividir ambos lados de la ecuación entre $x^{10}$:
\[1 + \left(13 - \frac{1}{x}\right)^{10} = 0\]

Definimos $y = \frac{1}{x}$. Como las raíces de la ecuación original son $r_k$ y $\overline{r}_k$ para $k = 1, 2, 3, 4, 5$, las raíces de la nueva ecuación en términos de $y$ serán $y_k = \frac{1}{r_k}$ y $\overline{y}_k = \frac{1}{\overline{r}_k}$. De este modo, la suma que buscamos se transforma en:
\[\sum_{k=1}^5 \frac{1}{r_k \overline{r}_k} = \sum_{k=1}^5 y_k \overline{y}_k\]

Reescribimos la ecuación en función de $y$:
\[(y - 13)^{10} + 1 = 0\]

Hacemos ahora la traslación $z = y - 13$, con lo cual obtenemos:
\[z^{10} + 1 = 0 \implies z^{10} = -1\]

Las 10 raíces de $z^{10} = -1$ se agrupan en 5 pares de complejos conjugados $z_k$ y $\overline{z}_k$ ($k = 1, \dots, 5$) que se encuentran sobre la circunferencia unitaria, por lo que cumplen:
1. $z_k \overline{z}_k = |z_k|^2 = 1$ para todo $k \in \{1, 2, 3, 4, 5\}$.
2. Por las relaciones de Vieta aplicadas al polinomio $z^{10} + 1 = 0$, la suma de todas las raíces es igual a cero (ya que el coeficiente de $z^9$ es $0$):
   \[\sum_{k=1}^5 (z_k + \overline{z}_k) = 0\]

Expresando $y_k$ y $\overline{y}_k$ en términos de $z_k$ y $\overline{z}_k$, tenemos $y_k = 13 + z_k$ y $\overline{y}_k = 13 + \overline{z}_k$. Calculamos cada producto $y_k \overline{y}_k$:
\[y_k \overline{y}_k = (13 + z_k)(13 + \overline{z}_k) = 169 + 13(z_k + \overline{z}_k) + z_k \overline{z}_k = 169 + 13(z_k + \overline{z}_k) + 1 = 170 + 13(z_k + \overline{z}_k)\]

Finalmente, sumamos para $k = 1, 2, 3, 4, 5$:
\[\sum_{k=1}^5 y_k \overline{y}_k = \sum_{k=1}^5 \left(170 + 13(z_k + \overline{z}_k)\right) = 5 \cdot 170 + 13 \sum_{k=1}^5 (z_k + \overline{z}_k) = 850 + 13(0) = 850\]

\boxed{850}