Para encontrar el polinomio mónico no constante $Q(x)$ con coeficientes enteros de grado mínimo tal que $Q(\sqrt{3}+\sqrt{2}) = Q(\sqrt{3}-\sqrt{2})$, definamos:
$$\alpha = \sqrt{3} + \sqrt{2} \quad \text{y} \quad \beta = \sqrt{3} - \sqrt{2}$$

Observamos primero las siguientes propiedades básicas de $\alpha$ y $\beta$:
1. $\alpha - \beta = 2\sqrt{2}$
2. $\alpha + \beta = 2\sqrt{3}$
3. $\alpha\beta = (\sqrt{3})^2 - (\sqrt{2})^2 = 3 - 2 = 1$

Calculemos la diferencia $\alpha^k - \beta^k$ para los primeros enteros positivos $k$:
- Para $k = 1$:
  $$\alpha - \beta = 2\sqrt{2}$$
- Para $k = 2$:
  $$\alpha^2 - \beta^2 = (\alpha - \beta)(\alpha + \beta) = (2\sqrt{2})(2\sqrt{3}) = 4\sqrt{6}$$
- Para $k = 3$:
  $$\alpha^3 - \beta^3 = (\alpha - \beta)^3 + 3\alpha\beta(\alpha - \beta) = (2\sqrt{2})^3 + 3(1)(2\sqrt{2}) = 16\sqrt{2} + 6\sqrt{2} = 22\sqrt{2}$$

Dado que $\sqrt{2}$ y $\sqrt{6}$ son linealmente independientes sobre $\mathbb{Q}$:
- Ningún polinomio mónico de grado $1$, $P(x) = x + c$, cumple la condición, pues $P(\alpha) - P(\beta) = 2\sqrt{2} \neq 0$.
- Ningún polinomio mónico de grado $2$, $P(x) = x^2 + ax + c$, cumple la condición, pues $P(\alpha) - P(\beta) = 4\sqrt{6} + 2a\sqrt{2} \neq 0$ para todo $a \in \mathbb{Z}$.

Para un polinomio mónico de grado $3$, $Q(x) = x^3 + bx^2 + ax + c$, tenemos:
$$Q(\alpha) - Q(\beta) = (\alpha^3 - \beta^3) + b(\alpha^2 - \beta^2) + a(\alpha - \beta) = (22 + 2a)\sqrt{2} + 4b\sqrt{6}$$

Para que $Q(\alpha) - Q(\beta) = 0$ con $a, b \in \mathbb{Z}$, la independencia lineal de $\sqrt{2}$ y $\sqrt{6}$ sobre $\mathbb{Q}$ exige que:
$$4b = 0 \implies b = 0$$
$$22 + 2a = 0 \implies a = -11$$

Por lo tanto, el grado mínimo posible es $3$ y cualquier polinomio $Q \in \mathcal{S}$ de grado mínimo tiene la forma:
$$Q(x) = x^3 - 11x + c$$
donde $c \in \mathbb{Z}$.

Finalmente, calculamos $Q(10) - Q(0)$:
$$Q(10) - Q(0) = 10^3 - 11(10) = 1000 - 110 = 890$$

\boxed{890}