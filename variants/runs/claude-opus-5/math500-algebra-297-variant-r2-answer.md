## Planteamiento

De $y = x^2 - 7$ obtengo $x^2 = y+7$, y de $y^2 = -9x+45$ obtengo $x = \dfrac{45-y^2}{9}$.

Sustituyendo:

$$\left(\frac{45-y^2}{9}\right)^2 = y+7 \;\Longrightarrow\; (45-y^2)^2 = 81y + 567$$

$$2025 - 90y^2 + y^4 = 81y + 567 \;\Longrightarrow\; y^4 - 90y^2 - 81y + 1458 = 0$$

## Verificación de raíces distintas

Cada valor de $y$ determina un único $x = \frac{45-y^2}{9}$, así que las soluciones $(x,y)$ se corresponden con las raíces en $y$. Factorizo para confirmar que no hay raíces repetidas:

- $y = 9$ es raíz: $6561 - 7290 - 729 + 1458 = 0$, luego $y^4 - 90y^2 - 81y + 1458 = (y-9)(y^3+9y^2-9y-162)$
- $y = -6$ es raíz del cúbico: $-216 + 324 + 54 - 162 = 0$, luego $(y+6)(y^2+3y-27)$
- $y^2 + 3y - 27 = 0$ da $y = \dfrac{-3 \pm \sqrt{117}}{2}$, dos raíces reales distintas

Las cuatro raíces son distintas, así que el producto es el término constante (grado par, coeficiente principal 1):

$$9 \cdot (-6) \cdot (-27) = 1458$$

$\boxed{1458}$