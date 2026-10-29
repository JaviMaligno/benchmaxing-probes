# Desarrollo paso a paso

**Análisis de la primera rama** $(x \le 4)$: $g(x) = 4 - x$ es estrictamente decreciente, con rango $[0, \infty)$.

**Análisis de la segunda rama** $(x > 4)$: $g(x) = -x^3 + 3x^2 + 4x$. Su derivada es
$$g'(x) = -3x^2 + 6x + 4,$$
cuyas raíces son $x = 1 \pm \tfrac{\sqrt{21}}{3} \approx -0.53$ y $2.53$. Para $x > 4$ se tiene $g'(x) < 0$ (por ejemplo $g'(4) = -20$), así que la rama es estrictamente decreciente. Como $g(4^+) = 0$ (límite: $-64+48+16=0$), su rango es $(-\infty, 0)$.

Los rangos $[0,\infty)$ y $(-\infty,0)$ son disjuntos y cubren todo $\mathbb{R}$, así que $g$ es biyectiva y $g^{-1}$ es una función bien definida.

**Cálculo de $g^{-1}(0)$:** la segunda rama solo da valores negativos, así que usamos la primera:
$$4 - x = 0 \implies x = 4 \quad (\text{válido, pues } 4 \le 4).$$
Por tanto $g^{-1}(0) = 4$.

**Cálculo de $g^{-1}(12)$:** como $12 > 0$, solo puede venir de la primera rama:
$$4 - x = 12 \implies x = -8 \quad (\text{válido, pues } -8 \le 4).$$
Verificación: $g(-8) = 4 - (-8) = 12$. ✓ Por tanto $g^{-1}(12) = -8$.

**Suma:**
$$g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4.$$

$$\boxed{-4}$$