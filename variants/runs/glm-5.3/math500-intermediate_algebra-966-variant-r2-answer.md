Voy a resolver el problema paso a paso.

## Planteamiento

Minimizar $f = a^4 + 6b^2 + 9c^4$ sujeto a $abc = 3$, con $a,b,c > 0$.

**Método de Lagrange.** Con $\nabla f = \lambda \nabla g$:
- $\partial f/\partial a = 4a^3 = \lambda bc$
- $\partial f/\partial b = 12b = \lambda ac$
- $\partial f/\partial c = 36c^3 = \lambda ab$

Multiplicando cada ecuación por su variable respectiva y usando $abc = 3$:
$$4a^4 = 12b^2 = 36c^4 = 3\lambda,$$
es decir, $a^4 = 3b^2 = 9c^4$.

**Resolviendo el sistema.** De $a^4 = 9c^4$ se obtiene $a = \sqrt{3}\,c$. De $3b^2 = 9c^4$ se obtiene $b = \sqrt{3}\,c^2$. Sustituyendo en $abc = 3$:
$$(\sqrt{3}\,c)(\sqrt{3}\,c^2)(c) = 3c^4 = 3 \implies c = 1,$$
de donde $a = b = \sqrt{3}$.

**Valor de $f$:**
$$f = (\sqrt{3})^4 + 6(\sqrt{3})^2 + 9(1)^4 = 9 + 18 + 9 = 36.$$

## Verificación con AM-GM ponderado

Con pesos $w_1 = \tfrac14,\ w_2 = \tfrac12,\ w_3 = \tfrac14$ (elegidos para que $4w_1 = 2w_2 = 4w_3$):
$$a^4 + 6b^2 + 9c^4 \geq \frac{(a^4/w_1)^{w_1}(6b^2/w_2)^{w_2}(9c^4/w_3)^{w_3}}{1}$$

El exponente de cada variable coincide con $abc$, así que el lado derecho es constante:
$$\frac{6^{1/2}\,9^{1/4}}{(1/4)^{1/4}(1/2)^{1/2}(1/4)^{1/4}} \cdot abc = \frac{\sqrt{6}\cdot\sqrt{3}}{\tfrac{1}{2}\cdot\tfrac{1}{\sqrt{2}}}\cdot 3 = 2\sqrt{36}\cdot 3 = 36.$$

La igualdad se alcanza exactamente cuando $4a^4 = 12b^2 = 36c^4$ con $abc = 3$, o sea en $a = b = \sqrt{3}$, $c = 1$ (se verifica: $4a^4 = 12b^2 = 36c^4 = 36$). Como la cota es global, este es el mínimo.

$$\boxed{36}$$