## Planteamiento

Sea $f(x) = ax^2 + bx + c$. Evaluamos en los puntos $x = 0, \tfrac12, 1$:

$$f(0) = c, \qquad f\!\left(\tfrac12\right) = \tfrac{a}{4} + \tfrac{b}{2} + c, \qquad f(1) = a + b + c.$$

Resolviendo este sistema para $a, b, c$ en términos de los valores de $f$:

$$a = 2f(0) - 4f\!\left(\tfrac12\right) + 2f(1),$$
$$b = -3f(0) + 4f\!\left(\tfrac12\right) - f(1),$$
$$c = f(0).$$

## Cota superior

Como $|f(0)|, |f(\tfrac12)|, |f(1)| \le 1$, por desigualdad triangular:

$$|a| + |b| + |c| \le (2+3+1)\,|f(0)| + (4+4)\,\left|f\!\left(\tfrac12\right)\right| + (2+1)\,|f(1)| \le 6 + 8 + 3 = 17.$$

## La cota se alcanza

Tomemos $f(x) = 8x^2 - 8x + 1$ (una versión trasladada del polinomio de Chebyshev $T_2$). Entonces:

- $f(0) = 1$, $f\!\left(\tfrac12\right) = -1$, $f(1) = 1$.
- El vértice está en $x = \tfrac12$ con valor $-1$, y el máximo en $[0,1]$ es $1$ en los extremos, así que $|f(x)| \le 1$ para todo $0 \le x \le 1$. ✓

Con este polinomio: $|a| + |b| + |c| = 8 + 8 + 1 = 17$.

$$\boxed{17}$$