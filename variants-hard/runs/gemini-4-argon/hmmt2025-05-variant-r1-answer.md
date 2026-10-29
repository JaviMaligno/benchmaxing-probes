Para encontrar el único valor posible de $R(6) - R(1)$, definamos primero $\alpha = \sqrt{5} + \sqrt{3}$ y $\beta = \sqrt{5} - \sqrt{3}$. 

Observemos las siguientes propiedades básicas de $\alpha$ y $\beta$:
$$\alpha + \beta = 2\sqrt{5}$$
$$\alpha - \beta = 2\sqrt{3} \neq 0$$
$$\alpha\beta = (\sqrt{5})^2 - (\sqrt{3})^2 = 5 - 3 = 2$$

La condición $F(\alpha) = F(\beta)$ equivale a $F(\alpha) - F(\beta) = 0$. Como $\alpha \neq \beta$, podemos dividir entre $\alpha - \beta$. Para cada entero $k \ge 1$, definamos:
$$u_k = \frac{\alpha^k - \beta^k}{\alpha - \beta}$$

Calculemos los primeros términos de esta sucesión:
- Para $k = 1$:
  $$u_1 = \frac{\alpha - \beta}{\alpha - \beta} = 1$$
- Para $k = 2$:
  $$u_2 = \frac{\alpha^2 - \beta^2}{\alpha - \beta} = \alpha + \beta = 2\sqrt{5}$$
- Para $k = 3$:
  $$u_3 = \frac{\alpha^3 - \beta^3}{\alpha - \beta} = \alpha^2 + \alpha\beta + \beta^2 = (\alpha + \beta)^2 - \alpha\beta = (2\sqrt{5})^2 - 2 = 20 - 2 = 18$$

Analicemos el grado mínimo posible para un polinomio mónico no constante $R(x) \in \mathbb{Z}[x]$ tal que $R(\alpha) = R(\beta)$:

1. **Grado 1:** Si $R(x) = x + c$ con $c \in \mathbb{Z}$, entonces:
   $$\frac{R(\alpha) - R(\beta)}{\alpha - \beta} = u_1 = 1 \neq 0$$
   Por lo tanto, no existen tales polinomios de grado 1.

2. **Grado 2:** Si $R(x) = x^2 + ax + b$ con $a, b \in \mathbb{Z}$, entonces:
   $$\frac{R(\alpha) - R(\beta)}{\alpha - \beta} = u_2 + a u_1 = 2\sqrt{5} + a = 0$$
   Como $\sqrt{5}$ es irracional y $a \in \mathbb{Z}$, esto es imposible.

3. **Grado 3:** Si $R(x) = x^3 + ax^2 + bx + c$ con $a, b, c \in \mathbb{Z}$, entonces:
   $$\frac{R(\alpha) - R(\beta)}{\alpha - \beta} = u_3 + a u_2 + b u_1 = 18 + 2a\sqrt{5} + b = 0$$
   Dado que $a, b \in \mathbb{Z}$ y $\sqrt{5}$ es irracional, esta igualdad se cumple si y solo si:
   $$2a = 0 \implies a = 0$$
   $$18 + b = 0 \implies b = -18$$

Por consiguiente, el grado mínimo posible es $3$, y todo polinomio $R \in \mathcal{T}$ de grado mínimo tiene la forma:
$$R(x) = x^3 - 18x + c$$
donde $c$ es una constante entera arbitraria.

Finalmente, calculamos $R(6) - R(1)$:
$$R(6) = 6^3 - 18(6) + c = 216 - 108 + c = 108 + c$$
$$R(1) = 1^3 - 18(1) + c = 1 - 18 + c = -17 + c$$
$$R(6) - R(1) = (108 + c) - (-17 + c) = 125$$

\boxed{125}