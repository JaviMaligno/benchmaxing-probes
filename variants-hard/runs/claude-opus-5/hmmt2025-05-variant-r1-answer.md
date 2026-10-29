## Planteamiento

Sea $\alpha=\sqrt5+\sqrt3$ y $\beta=\sqrt5-\sqrt3$. El automorfismo $\sigma$ de $\mathbb{Q}(\sqrt3,\sqrt5)$ que fija $\sqrt5$ y manda $\sqrt3\mapsto-\sqrt3$ cumple $\sigma(\alpha)=\beta$. Por tanto

$$F(\alpha)=F(\beta)\iff F(\alpha)\text{ es fijo por }\sigma\iff F(\alpha)\in\mathbb{Q}(\sqrt5),$$

es decir, en la base $\{1,\sqrt3,\sqrt5,\sqrt{15}\}$ deben anularse las componentes de $\sqrt3$ y $\sqrt{15}$.

## Potencias de $\alpha$

$$\alpha^0=1,\quad \alpha^1=\sqrt5+\sqrt3,\quad \alpha^2=8+2\sqrt{15},\quad \alpha^3=14\sqrt5+18\sqrt3$$

(las potencias pares solo aportan a $1$ y $\sqrt{15}$; las impares solo a $\sqrt3$ y $\sqrt5$).

## Grados bajos

- **Grado 1:** $x+c_0$ deja componente $\sqrt3$ igual a $1\neq0$.
- **Grado 2:** $x^2+c_1x+c_0$ tiene componente $\sqrt{15}$ igual a $2\neq 0$ (es fija, por ser mónico).
- **Grado 3:** $x^3+c_2x^2+c_1x+c_0$ da componente $\sqrt{15}=2c_2$ y componente $\sqrt3=18+c_1$. Luego $c_2=0$, $c_1=-18$.

Verificación: $\alpha^3-18\alpha=(14\sqrt5+18\sqrt3)-18(\sqrt5+\sqrt3)=-4\sqrt5\in\mathbb{Q}(\sqrt5)$. ✓

Así, los elementos de grado mínimo son $R(x)=x^3-18x+c_0$ con $c_0\in\mathbb{Z}$.

## Cálculo

La constante $c_0$ se cancela en la diferencia:

$$R(6)-R(1)=(216-108)-(1-18)=108+17=125.$$

\boxed{125}