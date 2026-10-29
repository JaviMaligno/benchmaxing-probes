## Planteamiento

Necesitamos que el rango de $g$ sea todo $\mathbb{R}$ (cada recta horizontal $y=k$ se alcanza al menos una vez).

**Caso $b=0$:** $g\equiv 0$, el rango es $\{0\}$. No sirve.

**Caso $b>0$** (es el relevante, pues buscamos el mayor $b$):

- **Rama cuadrática** ($x \ge b$): $bx^2$ es creciente en $[b,\infty)$ porque $b>0$, así que su rango es $[b\cdot b^2,\infty) = [b^3,\infty)$.
- **Rama lineal** ($x < b$): $bx+6b$ es creciente, y al acercarse a $x=b$ tiende (sin alcanzarlo) a $b^2+6b$. Su rango es $(-\infty,\,b^2+6b)$.

La unión $(-\infty,\,b^2+6b)\cup[b^3,\infty)$ cubre $\mathbb{R}$ si y solo si no queda hueco:
$$b^3 \le b^2+6b$$

Dividiendo por $b>0$:
$$b^2 - b - 6 \le 0 \quad\Longrightarrow\quad (b-3)(b+2)\le 0 \quad\Longrightarrow\quad -2 \le b \le 3$$

Por tanto, para $b>0$ la condición es $b\le 3$.

**Verificación en $b=3$:**
- $x\ge 3$: $3x^2$ da $[27,\infty)$.
- $x<3$: $3x+18$ da $(-\infty,27)$.

La unión es exactamente $\mathbb{R}$, sin huecos. Para $b>3$ aparecería el hueco $[b^2+6b,\ b^3)$.

\boxed{3}