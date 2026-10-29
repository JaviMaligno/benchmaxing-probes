## Solución

Dado que $x=0$ no es raíz, divido la ecuación entre $x^2$:
$$x^2 + \frac{1}{x^2} + a\left(x + \frac{1}{x}\right) - b = 0.$$

Con la sustitución $t = x + \frac{1}{x}$, se tiene $x^2 + \frac{1}{x^2} = t^2 - 2$, y la ecuación queda:
$$t^2 + at - (b+2) = 0, \qquad \text{es decir} \qquad b = t^2 + at - 2.$$

Para que exista una raíz real $x$, debe existir $t$ real con $|t| \ge 2$ (ese es el rango de $x + 1/x$ para $x$ real).

**Análisis del rango de $b$.** Sea $f(t) = t^2 + at - 2$ con $0 \le a \le 1$.

- Para $t \le -2$: $f'(t) = 2t + a < 0$, así que $f$ es decreciente ahí; su mínimo en ese intervalo es $f(-2) = 2 - 2a$, y $f \to \infty$ cuando $t \to -\infty$. Rango: $[2-2a, \infty)$.
- Para $t \ge 2$: $f$ es creciente, con mínimo $f(2) = 2 + 2a$. Rango: $[2+2a, \infty)$, que está contenido en el anterior.

Por lo tanto, la ecuación tiene raíz real si y solo si
$$b \ge 2 - 2a.$$

**Área en el cuadrado unitario.** La recta $b = 2 - 2a$ corta $b=1$ en $a = \tfrac12$ y $b=0$ en $a=1$. La región $b \ge 2-2a$ dentro de $[0,1]^2$ es el triángulo con vértices $(\tfrac12, 1)$, $(1,1)$ y $(1,0)$, cuya área es
$$\frac{1}{2} \cdot \frac{1}{2} \cdot 1 = \frac{1}{4}.$$

$$\boxed{\dfrac{1}{4}}$$