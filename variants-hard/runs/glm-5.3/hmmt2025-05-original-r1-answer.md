# Resolución

**Paso 1: Definir las cantidades clave.**

Sea $\alpha = \sqrt{3}+\sqrt{2}$ y $\beta = \sqrt{3}-\sqrt{2}$. Calculamos:
- $\alpha - \beta = 2\sqrt{2}$, $\quad \alpha + \beta = 2\sqrt{3}$, $\quad \alpha\beta = 1$
- $\alpha^2 = 5+2\sqrt{6}$, $\quad \beta^2 = 5-2\sqrt{6}$, $\quad$ entonces $\alpha^2 - \beta^2 = 4\sqrt{6}$

**Paso 2: Descartar grados 1 y 2.**

*Grado 1:* $P(x) = x + c$ da $P(\alpha)-P(\beta) = \alpha - \beta = 2\sqrt{2} \neq 0$. Imposible.

*Grado 2:* $P(x) = x^2 + bx + c$ da
$$P(\alpha)-P(\beta) = (\alpha^2-\beta^2) + b(\alpha-\beta) = 4\sqrt{6} + 2b\sqrt{2} = 2\sqrt{2}\,(2\sqrt{3} + b).$$
Esto se anula solo si $b = -2\sqrt{3}$, que no es entero. Imposible.

**Paso 3: Analizar el grado 3.**

Sea $P(x) = x^3 + bx^2 + cx + d$. Primero:
$$\alpha^3 - \beta^3 = (\alpha-\beta)(\alpha^2 + \alpha\beta + \beta^2) = 2\sqrt{2}\,(10 + 1) = 22\sqrt{2}.$$

Entonces
$$P(\alpha) - P(\beta) = 22\sqrt{2} + 4b\sqrt{6} + 2c\sqrt{2} = (22+2c)\sqrt{2} + 4b\sqrt{6}.$$

Como $\sqrt{2}$ y $\sqrt{6}$ son linealmente independientes sobre $\mathbb{Q}$, esto se anula si y solo si $c = -11$ y $b = 0$.

**Paso 4: Verificar que $Q(x) = x^3 - 11x + d$ funciona.**

Usando $(\sqrt{3}\pm\sqrt{2})^3 = 9\sqrt{3} \pm 11\sqrt{2}$:
$$Q(\alpha) = (9\sqrt{3}+11\sqrt{2}) - 11(\sqrt{3}+\sqrt{2}) = -2\sqrt{3},$$
$$Q(\beta) = (9\sqrt{3}-11\sqrt{2}) - 11(\sqrt{3}-\sqrt{2}) = -2\sqrt{3}.$$

Efectivamente $Q(\alpha) = Q(\beta)$ para cualquier entero $d$. El grado mínimo es $3$.

**Paso 5: Calcular $Q(10) - Q(0)$.**

$$Q(10) - Q(0) = (1000 - 110 + d) - d = 890.$$

El valor no depende de $d$, así que es único.

$$\boxed{890}$$