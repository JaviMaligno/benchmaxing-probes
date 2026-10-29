Analicemos cuándo la gráfica de $g$ cubre todos los valores reales (es decir, cuándo $g$ es sobreyectiva).

**Caso $b > 0$:**

- Para $x \geq b$: la rama $bx^2$ es creciente en $[b, \infty)$ (ya que $b > 0$), así que toma los valores $[b \cdot b^2, \infty) = [b^3, \infty)$.
- Para $x < b$: la rama $bx + 6b$ es creciente con límite superior en $x \to b^-$, así que toma los valores $(-\infty, b^2 + 6b)$.

Para que la unión cubra todo $\mathbb{R}$, no debe haber hueco entre ambas ramas:
$$b^2 + 6b \geq b^3.$$

Dividiendo entre $b > 0$:
$$b + 6 \geq b^2 \quad\Longleftrightarrow\quad b^2 - b - 6 \leq 0 \quad\Longleftrightarrow\quad (b-3)(b+2) \leq 0,$$

lo cual da $-2 \leq b \leq 3$. Combinado con $b > 0$: $0 < b \leq 3$.

**Casos $b = 0$ y $b < 0$:** si $b = 0$, entonces $g \equiv 0$ y no cubre nada más que $y=0$. Si $b < 0$, cualquier valor válido sería menor que $3$, así que no mejora el máximo.

**Verificación con $b = 3$:** la rama cuadrática cubre $[27, \infty)$ y la lineal cubre $(-\infty, 27)$, de modo que juntas cubren todo $\mathbb{R}$. ✓

$$\boxed{3}$$