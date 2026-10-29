Para hallar el valor de la suma pedida, primero reescribimos la ecuación dada. Observamos que $x = 0$ no es una raíz, ya que $0^{10} + (0 - 1)^{10} = 1 \neq 0$. Dividiendo ambos lados de la ecuación entre $x^{10}$, obtenemos:
\[1 + \left(11 - \frac{1}{x}\right)^{10} = 0.\]

Realizamos el cambio de variable $y = \frac{1}{x}$. Si $s_k$ y $\overline{s}_k$ son raíces complejas conjugadas de la ecuación original para $k = 1, 2, 3, 4, 5$, entonces $y_k = \frac{1}{s_k}$ y $\overline{y}_k = \frac{1}{\overline{s}_k}$ son los pares de raíces complejas conjugadas de la ecuación transformada:
\[(11 - y)^{10} = -1.\]

La expresión que deseamos calcular se transforma en:
\[\sum_{k=1}^5 \frac{1}{s_k \overline{s}_k} = \sum_{k=1}^5 y_k \overline{y}_k.\]

Sea $z = 11 - y$. Entonces la ecuación se convierte en $z^{10} + 1 = 0$. Sus 10 raíces vienen dadas en 5 pares de complejos conjugados $z_k, \overline{z}_k$ (para $k = 1, \dots, 5$), donde ninguna raíz es real porque $z^{10} = -1$.

Para cada raíz $z_k$, como $z_k^{10} = -1$, su módulo cumple $|z_k|^{10} = |-1| = 1$, por lo que $|z_k| = 1$, es decir:
\[z_k \overline{z}_k = |z_k|^2 = 1.\]

Expresando $y_k$ y $\overline{y}_k$ en términos de $z_k$ y $\overline{z}_k$ ($y_k = 11 - z_k$ y $\overline{y}_k = 11 - \overline{z}_k$), tenemos que para cada $k$:
\[y_k \overline{y}_k = (11 - z_k)(11 - \overline{z}_k) = 121 - 11(z_k + \overline{z}_k) + z_k \overline{z}_k = 122 - 11(z_k + \overline{z}_k).\]

Sumando sobre los 5 pares de raíces conjugadas:
\[\sum_{k=1}^5 y_k \overline{y}_k = \sum_{k=1}^5 122 - 11 \sum_{k=1}^5 (z_k + \overline{z}_k).\]

Dado que $\sum_{k=1}^5 (z_k + \overline{z}_k)$ es la suma de las 10 raíces del polinomio $z^{10} + 1 = 0$, por las relaciones de Vieta esta suma es igual a $0$ (el coeficiente de $z^9$ cambiado de signo). Por lo tanto:
\[\sum_{k=1}^5 \frac{1}{s_k \overline{s}_k} = 5 \times 122 - 11(0) = 610.\]

\boxed{610}