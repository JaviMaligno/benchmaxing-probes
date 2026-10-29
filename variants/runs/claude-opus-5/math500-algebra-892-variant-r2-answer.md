## Planteamiento

Hay que lograr que el recorrido (rango) de $g$ sea todo $\mathbb{R}$.

**Caso $b=0$:** $g(x)=0$ para todo $x$, el rango es $\{0\}$. No sirve.

**Caso $b>0$** (el relevante para buscar el valor más grande):

- **Rama cuadrática** ($x \ge b$): $bx^2$ es creciente en $[b,\infty)$ porque $b>0$, así que su rango es
$$[b\cdot b^2,\ \infty) = [b^3,\ \infty).$$

- **Rama lineal** ($x < b$): $bx+6b$ tiene pendiente $b>0$, es creciente, y su rango es
$$(-\infty,\ b\cdot b + 6b) = (-\infty,\ b^2+6b).$$

Para que la unión sea $\mathbb{R}$, la recta debe cubrir todos los valores por debajo de $b^3$:
$$b^3 \le b^2 + 6b.$$

Dividiendo por $b>0$:
$$b^2 - b - 6 \le 0 \quad\Longrightarrow\quad (b-3)(b+2)\le 0 \quad\Longrightarrow\quad -2 \le b \le 3.$$

Con $b>0$ queda $0 < b \le 3$, luego el máximo candidato es $b=3$.

## Verificación con $b=3$

- Para $x\ge 3$: $3x^2$ recorre $[27,\infty)$.
- Para $x<3$: $3x+18$ recorre $(-\infty,27)$.

La unión es $(-\infty,27)\cup[27,\infty)=\mathbb{R}$, así que toda recta horizontal corta la gráfica. Para $b>3$ se tendría $b^3 > b^2+6b$ y quedaría el hueco $[b^2+6b,\ b^3)$ sin cubrir.

\boxed{3}