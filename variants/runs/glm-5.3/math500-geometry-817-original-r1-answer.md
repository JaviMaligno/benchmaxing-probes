## Solución

**Configuración del problema**

El semicírculo grande tiene su diámetro sobre el radio $AQ$; como es tangente a la circunferencia en $A$, su diámetro es exactamente $QA = 14$, así que su radio es $7$ y su centro es $C_1$, a distancia $7$ de $Q$ sobre $AQ$.

El semicírculo pequeño tiene su diámetro sobre el radio $BQ$ y es tangente a la circunferencia en $B$. Llamemos $r$ a su radio y $t$ a la distancia de su centro $C_2$ hasta $Q$.

**Condición 1: tangencia con la circunferencia grande**

Como el semicírculo pequeño es tangente interiormente a la circunferencia en $B$:
$$t + r = 14 \quad\Rightarrow\quad t = 14 - r$$

**Condición 2: tangencia entre los dos semicírculos**

Colocando $Q$ en el origen, $AQ$ sobre el eje $x$ y $BQ$ sobre el eje $y$:
- Centro del semicírculo grande: $C_1 = (7, 0)$, radio $7$
- Centro del semicírculo pequeño: $C_2 = (0, t)$, radio $r$

Como son tangentes exteriores, la distancia entre centros es la suma de los radios:
$$\sqrt{7^2 + t^2} = 7 + r$$

**Resolviendo**

Sustituyendo $t = 14 - r$ y elevando al cuadrado:
$$49 + (14 - r)^2 = (7 + r)^2$$
$$49 + 196 - 28r + r^2 = 49 + 14r + r^2$$
$$196 - 28r = 14r$$
$$196 = 42r$$
$$r = \frac{14}{3}$$

**Verificación:** con $r = \frac{14}{3}$, tenemos $t = \frac{28}{3}$, y $\sqrt{49 + \frac{784}{9}} = \sqrt{\frac{1225}{9}} = \frac{35}{3} = 7 + \frac{14}{3}$ ✓. Además, el punto de tangencia $\left(\frac{14}{5}, \frac{28}{5}\right)$ está sobre ambos arcos de los semicírculos ✓.

$$\boxed{\dfrac{14}{3}}$$