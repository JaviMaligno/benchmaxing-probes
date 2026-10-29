## Planteamiento

Una línea horizontal $y = c$ interseca la gráfica de $f$ si y solo si existe algún $x$ con $f(x) = c$. Por lo tanto, la condición del problema equivale a que **el rango de $f$ sea todo $\mathbb{R}$**.

Estudio por casos según el signo de $a$.

## Caso $a = 0$

$f(x) = 0$ para todo $x$: el rango es $\{0\}$, no cubre ninguna otra línea horizontal. **Falla.**

## Caso $a > 0$

- **Rama $x \ge a$:** como $a>0$, esta rama vive en $x>0$, donde $ax^2$ es creciente. El mínimo es $f(a)=a^3$, así que su rango es $[a^3,\infty)$.
- **Rama $x < a$:** la recta $ax+2a$ tiene pendiente positiva; tiende a $-\infty$ cuando $x\to-\infty$ y su supremo (no alcanzado, pues $x<a$ es estricto) es $a^2+2a$. Rango: $(-\infty,\,a^2+2a)$.

El rango total es $(-\infty,\,a^2+2a)\cup[a^3,\infty)$, que es todo $\mathbb{R}$ si y solo si no hay hueco:

$$a^3 \le a^2+2a \iff a(a-2)(a+1)\le 0.$$

Como $a>0$, esto equivale a $0 < a \le 2$.

## Caso $a < 0$

- **Rama $x \ge a$:** ahora el dominio incluye a $x=0$, y $ax^2 \to -\infty$ cuando $|x|\to\infty$. Rango: $(-\infty,0]$.
- **Rama $x<a$:** pendiente negativa; cuando $x\to-\infty$, $ax+2a\to+\infty$, y su ínfimo (no alcanzado) es $a^2+2a$. Rango: $(a^2+2a,\infty)$.

El rango total es $(-\infty,0]\cup(a^2+2a,\infty)$, que es todo $\mathbb{R}$ si y solo si $a^2+2a\le 0$, es decir, $-2\le a<0$.

## Conclusión

Los valores válidos son $a\in[-2,\,0)\cup(0,\,2]$. El mayor de ellos es $a=2$.

**Verificación en $a=2$:** $f(x)=2x+4$ en $x<2$ cubre $(-\infty,8)$, y $f(x)=2x^2$ en $x\ge 2$ cubre $[8,\infty)$: la unión es $\mathbb{R}$. Para cualquier $a>2$ aparece el hueco $(a^2+2a,\;a^3)$, no vacío.

$$\boxed{2}$$