**Planteamiento:** necesitamos que la unión de los rangos de las dos ramas cubra todo ℝ, para el mayor $b$ posible (claramente $b>0$, pues con $b\le 0$ los valores grandes positivos no se alcanzan).

**Rama lineal** ($x < b$): $g(x) = bx + 6b$ con pendiente $b > 0$, creciente, así que su rango es $(-\infty,\; b^2 + 6b)$ (abierto, porque $x=b$ no está incluido).

**Rama cuadrática** ($x \ge b$): $g(x) = bx^2$ con $b>0$ y $x \ge b > 0$, es creciente en ese dominio, con mínimo en $x = b$: valor $b \cdot b^2 = b^3$. Su rango es $[b^3,\; \infty)$.

**Condición de cobertura:** no debe quedar hueco entre ambos rangos, es decir
$$b^3 \le b^2 + 6b.$$
Dividiendo entre $b > 0$:
$$b^2 - b - 6 \le 0 \quad\Longrightarrow\quad (b-3)(b+2) \le 0 \quad\Longrightarrow\quad -2 \le b \le 3.$$

**Verificación con $b = 3$:** la rama lineal cubre $(-\infty, 27)$ y la cuadrática cubre $[27, \infty)$, de modo que toda recta horizontal es intersecada al menos una vez.

$$\boxed{3}$$