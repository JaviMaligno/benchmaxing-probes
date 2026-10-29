## Solución

Sea $\alpha = \sqrt{5}+\sqrt{3}$ y $\beta = \sqrt{5}-\sqrt{3}$. Datos útiles: $\alpha+\beta = 2\sqrt{5}$, $\alpha\beta = 2$, $\alpha^2+\beta^2 = 16$.

**Grado 1:** $F(x)=x+c$ da $F(\alpha)-F(\beta) = \alpha-\beta = 2\sqrt{3} \neq 0$. No sirve.

**Grado 2:** $F(x)=x^2+bx+c$ da
$$F(\alpha)-F(\beta) = (\alpha-\beta)(\alpha+\beta+b) = 2\sqrt{3}\,(2\sqrt{5}+b),$$
que nunca es cero con $b$ entero. No sirve.

**Grado 3:** $F(x)=x^3+ax^2+bx+c$ da
$$F(\alpha)-F(\beta) = (\alpha-\beta)\big(\alpha^2+\alpha\beta+\beta^2 + a(\alpha+\beta) + b\big) = (\alpha-\beta)(18 + 2a\sqrt{5} + b).$$
Para que se anule necesitamos $a=0$ y $b=-18$. Entonces todo elemento de $\mathcal{T}$ de grado mínimo es
$$R(x) = x^3 - 18x + c, \quad c \in \mathbb{Z}.$$

**Cálculo final:** la constante $c$ se cancela:
$$R(6)-R(1) = (216 - 108) - (1 - 18) = 108 + 17 = 125.$$

$$\boxed{125}$$