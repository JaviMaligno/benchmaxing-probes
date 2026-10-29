## Solución

**Paso 1: Reducir la ecuación recíproca.** Como $x=0$ da $1 \ne 0$, podemos dividir entre $x^2$:
$$x^2 + \frac{1}{x^2} + 2p\left(x + \frac{1}{x}\right) - q = 0.$$

Con la sustitución $t = x + \tfrac{1}{x}$ (que satisface $x^2 + \tfrac{1}{x^2} = t^2 - 2$), la ecuación se vuelve
$$t^2 + 2pt - (q+2) = 0.$$

Existe una $x$ real si y solo si existe una raíz $t$ con $|t| \ge 2$, porque $x + \tfrac1x$ toma exactamente los valores de módulo $\ge 2$.

**Paso 2: Analizar las raíces en $t$.** Las raíces son
$$t = -p \pm \sqrt{p^2 + q + 2}.$$

- Raíz positiva: $-p + \sqrt{p^2+q+2} \ge 2 \iff p^2+q+2 \ge (2+p)^2 \iff q \ge 2 + 4p$, imposible pues $q \le 1$.
- Raíz negativa: $-p - \sqrt{p^2+q+2} \le -2 \iff \sqrt{p^2+q+2} \ge 2 - p \iff q \ge 2 - 4p$ (válido pues $2-p>0$).

Por tanto, $(p,q) \in T$ si y solo si $q \ge 2 - 4p$ dentro del cuadrado unitario.

**Paso 3: Calcular el área.** La recta $q = 2 - 4p$ corta el cuadrado en $(\tfrac14, 1)$ y $(\tfrac12, 0)$. El área de la región $q \ge 2-4p$ en $[0,1]^2$ es
$$\int_{1/4}^{1/2} (4p - 1)\,dp + \int_{1/2}^{1} 1\,dp = \frac{1}{8} + \frac{1}{2} = \frac{5}{8}.$$

$$\boxed{\dfrac{5}{8}}$$