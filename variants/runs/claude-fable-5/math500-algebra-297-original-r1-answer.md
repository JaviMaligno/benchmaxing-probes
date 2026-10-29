Voy a resolver el sistema por sustitución.

**Planteamiento.** De la primera ecuación, $x^2 = y + 8$. De la segunda, $5x = 44 - y^2$, es decir $x = \dfrac{44 - y^2}{5}$.

Sustituyendo en $x^2 = y + 8$:

$$\frac{(44 - y^2)^2}{25} = y + 8 \;\Longrightarrow\; (44 - y^2)^2 = 25y + 200$$

Expandiendo:

$$y^4 - 88y^2 + 1936 = 25y + 200 \;\Longrightarrow\; y^4 - 88y^2 - 25y + 1736 = 0$$

**Verificación de raíces distintas.** Factorizando: $y = -7$ es raíz ($2401 - 4312 + 175 + 1736 = 0$), y al dividir queda $y^3 - 7y^2 - 39y + 248$, que tiene la raíz $y = 8$. El factor restante es $y^2 + y - 31$, cuyo discriminante es $1 + 124 = 125 > 0$, así que sus dos raíces son reales, irracionales y distintas de $-7$ y $8$.

Las cuatro raíces son distintas, y cada valor de $y$ determina un único $x$ mediante $x = \frac{44 - y^2}{5}$, de modo que las cuatro soluciones $(x, y)$ son distintas.

**Producto.** Por las fórmulas de Vieta, el producto de las raíces del polinomio mónico de grado 4 es el término independiente: $1736$. Comprobación directa: $(-7)(8)(-31) = 1736$, donde $-31$ es el producto de las raíces de $y^2 + y - 31$.

$$\boxed{1736}$$