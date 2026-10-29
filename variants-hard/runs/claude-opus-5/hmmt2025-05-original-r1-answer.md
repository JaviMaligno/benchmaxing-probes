## Planteamiento

Sean $\alpha=\sqrt3+\sqrt2$ y $\beta=\sqrt3-\sqrt2$. Entonces
$$\alpha+\beta=2\sqrt3,\qquad \alpha\beta=1,\qquad \alpha^2+\beta^2=10,\qquad \alpha-\beta=2\sqrt2\neq0 .$$

**Grado 1:** $P(x)=x+c$ da $\alpha=\beta$: imposible.

**Grado 2:** $P(x)=x^2+bx+c$ exige $(\alpha^2-\beta^2)+b(\alpha-\beta)=0$, es decir $\alpha+\beta+b=0$, o sea $b=-2\sqrt3\notin\mathbb{Z}$: imposible.

**Grado 3:** $P(x)=x^3+bx^2+cx+d$. La condición $P(\alpha)=P(\beta)$, dividida entre $\alpha-\beta$, queda
$$\alpha^2+\alpha\beta+\beta^2+b(\alpha+\beta)+c=0\;\Longrightarrow\;11+2\sqrt3\,b+c=0 .$$
Como $b,c$ son enteros, necesariamente $b=0$ y $c=-11$. Luego
$$Q(x)=x^3-11x+d .$$

**Verificación:** $\alpha^3=9\sqrt3+11\sqrt2$, de modo que $\alpha^3-11\alpha=-2\sqrt3$; análogamente $\beta^3=9\sqrt3-11\sqrt2$ y $\beta^3-11\beta=-2\sqrt3$. Coinciden, así que el grado mínimo es $3$.

## Cálculo

El término constante $d$ se cancela:
$$Q(10)-Q(0)=(1000-110+d)-d=890 .$$

\boxed{890}