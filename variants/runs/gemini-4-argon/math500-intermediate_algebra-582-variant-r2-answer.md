Para resolver el problema paso a paso, consideremos primero la ecuación dada:
\[x^{10}+(11x-1)^{10}=0\]

Observamos que $x = 0$ no es una raíz de la ecuación, ya que $0^{10} + (-1)^{10} = 1 \neq 0$. Por lo tanto, podemos realizar el cambio de variable $y = \frac{1}{x}$ (es decir, $x = \frac{1}{y}$). Las raíces para $y$ serán los recíprocos de las raíces originales: $y_k = \frac{1}{s_k}$ y $\overline{y}_k = \frac{1}{\overline{s}_k}$ para $k=1, 2, 3, 4, 5$.

Con este cambio de variable, la suma que deseamos calcular se transforma en:
\[\sum_{k=1}^5 \frac{1}{s_k\overline{s}_k} = \sum_{k=1}^5 y_k\overline{y}_k\]

Sustituyendo $x = \frac{1}{y}$ en la ecuación original, obtenemos:
\[\left(\frac{1}{y}\right)^{10} + \left(\frac{11}{y}-1\right)^{10} = 0\]

Multiplicando toda la ecuación por $y^{10}$:
\[1 + (11-y)^{10} = 0 \implies (y-11)^{10} + 1 = 0\]

Ahora, hagamos una traslación definiendo $z = y - 11$, de modo que $y = z + 11$. La ecuación en términos de $z$ es:
\[z^{10} + 1 = 0 \implies z^{10} = -1\]

Las 10 raíces de esta ecuación son $z_k$ y $\overline{z}_k$ para $k=1, \dots, 5$. 
Dado que $z_k^{10} = -1$, tomando el módulo en ambos lados tenemos $|z_k|^{10} = |-1| = 1$, lo que implica que $|z_k| = 1$. Por lo tanto, para cada $k$:
\[z_k\overline{z}_k = |z_k|^2 = 1\]

Expresando $y_k\overline{y}_k$ en términos de $z_k$:
\[y_k\overline{y}_k = (z_k + 11)(\overline{z}_k + 11) = z_k\overline{z}_k + 11(z_k + \overline{z}_k) + 121\]

Como $z_k\overline{z}_k = 1$, esto se simplifica a:
\[y_k\overline{y}_k = 1 + 11(z_k + \overline{z}_k) + 121 = 122 + 11(z_k + \overline{z}_k)\]

Finalmente, sumamos esta expresión para $k = 1, 2, 3, 4, 5$:
\[\sum_{k=1}^5 y_k\overline{y}_k = \sum_{k=1}^5 122 + 11\sum_{k=1}^5 (z_k + \overline{z}_k)\]

Notamos que $\sum_{k=1}^5 (z_k + \overline{z}_k)$ es la suma de todas las 10 raíces del polinomio $z^{10} + 1 = 0$. Por las fórmulas de Vieta, dado que el coeficiente de $z^9$ es $0$, la suma de todas las raíces es igual a $0$.

Así, la suma buscada es:
\[\sum_{k=1}^5 y_k\overline{y}_k = 5 \times 122 + 11(0) = 610\]

\boxed{610}