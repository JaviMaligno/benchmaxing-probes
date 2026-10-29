## Resolución

Sea $a=\sqrt{3}+\sqrt{2}$ y $b=\sqrt{3}-\sqrt{2}$. La condición es $P(a)-P(b)=0$. Calculo las diferencias de potencias:

- $a-b = 2\sqrt{2}$
- $a^2-b^2 = (a+b)(a-b) = 2\sqrt{3}\cdot 2\sqrt{2} = 4\sqrt{6}$
- $a^3-b^3 = (a-b)(a^2+ab+b^2) = 2\sqrt{2}\,\big[(5+2\sqrt6)+1+(5-2\sqrt6)\big] = 22\sqrt{2}$

**Grado 1:** $P=x+c$ da $P(a)-P(b)=2\sqrt2\neq 0$. Imposible.

**Grado 2:** $P=x^2+c_1x+c_0$ da $4\sqrt6 + 2c_1\sqrt2 = 0$, imposible con $c_1\in\mathbb{Z}$ (pues $\sqrt6$ y $\sqrt2$ son linealmente independientes sobre $\mathbb{Q}$).

**Grado 3:** $P=x^3+c_2x^2+c_1x+c_0$ da
$$22\sqrt{2} + 4c_2\sqrt{6} + 2c_1\sqrt{2} = 0.$$
Por independencia lineal: $c_2=0$ y $22+2c_1=0$, es decir $c_1=-11$. Entonces
$$Q(x)=x^3-11x+c_0$$
funciona para cualquier $c_0$. Verificación: $a^3 = 9\sqrt3+11\sqrt2$, así que $Q(a)= -2\sqrt3+c_0 = Q(b)$. ✓

Como todo $Q$ de grado mínimo tiene esta forma, el valor es único:
$$Q(10)-Q(0) = (1000 - 110 + c_0) - c_0 = 890.$$

$$\boxed{890}$$