## Planteamiento

Para que la gráfica corte **toda** recta horizontal, el recorrido (imagen) de $f$ debe ser todo $\mathbb{R}$.

Buscamos el mayor $a$, así que basta analizar $a>0$.

**Rama cuadrática ($x \geq a$):** como $a>0$, en $x\ge a>0$ la función $ax^2$ es creciente, con valor mínimo en $x=a$:
$$f(a) = a\cdot a^2 = a^3 \quad\Longrightarrow\quad \text{imagen} = [a^3, \infty).$$

**Rama lineal ($x < a$):** $ax+2a$ con pendiente $a>0$ es creciente, y se aproxima (sin alcanzar) al valor en $x=a$:
$$a\cdot a + 2a = a^2+2a \quad\Longrightarrow\quad \text{imagen} = (-\infty,\, a^2+2a).$$

## Condición de cobertura

$$(-\infty,\, a^2+2a) \cup [a^3, \infty) = \mathbb{R} \iff a^3 \leq a^2+2a.$$

Dividiendo entre $a>0$:
$$a^2 \leq a+2 \iff a^2-a-2\leq 0 \iff (a-2)(a+1)\leq 0 \iff -1\leq a \leq 2.$$

Junto con $a>0$, queda $0 < a \leq 2$. El mayor valor es $a=2$.

## Verificación con $a=2$

- $x\geq 2$: $2x^2$ recorre $[8,\infty)$.
- $x<2$: $2x+4$ recorre $(-\infty, 8)$.

La unión es exactamente $\mathbb{R}$, sin huecos. Para $a>2$ se tendría $a^3 > a^2+2a$ y las horizontales $y\in[a^2+2a,\ a^3)$ no se cortarían.

\boxed{2}