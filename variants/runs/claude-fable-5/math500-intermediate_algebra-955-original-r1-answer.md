## Solución

Sea $p(x) = ax^2 + bx + c$. Evaluamos en tres puntos convenientes: $x = 0$, $x = \tfrac12$ y $x = 1$:

- $p(0) = c$
- $p\!\left(\tfrac12\right) = \tfrac{a}{4} + \tfrac{b}{2} + c$
- $p(1) = a + b + c$

Resolviendo para $a$, $b$, $c$ en términos de estos valores:

$$a = 2p(0) - 4p\!\left(\tfrac12\right) + 2p(1), \qquad b = -3p(0) + 4p\!\left(\tfrac12\right) - p(1), \qquad c = p(0).$$

Como $|p(0)|, |p(\tfrac12)|, |p(1)| \le 1$, por desigualdad triangular:

$$|a| \le 2 + 4 + 2 = 8, \qquad |b| \le 3 + 4 + 1 = 8, \qquad |c| \le 1,$$

de modo que $|a| + |b| + |c| \le 17$.

**La cota se alcanza**: tomemos $p(x) = 8x^2 - 8x + 1$ (el polinomio de Chebyshev $T_2$ trasladado a $[0,1]$). Entonces $p(0) = 1$, $p(\tfrac12) = -1$, $p(1) = 1$, y como el vértice está en $x = \tfrac12$ con valor $-1$, se cumple $|p(x)| \le 1$ en todo $[0,1]$. Además $|a| + |b| + |c| = 8 + 8 + 1 = 17$.

$$\boxed{17}$$