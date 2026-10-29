## Planteamiento

Queremos que $g$ sea sobreyectiva: que su rango sea todo $\mathbb{R}$, para que toda recta horizontal $y = c$ se cruce con la gráfica.

Estudiamos los dos tramos:

**Tramo parabólico** ($x \ge b$): $y = bx^2$.
**Tramo lineal** ($x < b$): $y = bx + 6b$.

## Caso $b > 0$

- **Recta** ($x < b$): como $b>0$, cuando $x \to -\infty$ tenemos $bx + 6b \to -\infty$, y cuando $x \to b^-$ el valor tiende a $b^2 + 6b$. Por continuidad, la recta recorre $\left(-\infty,\ b^2+6b\right)$.
- **Parábola** ($x \ge b$): con $b>0$, el dominio $x \ge b > 0$ está a la derecha del vértice, así que $bx^2$ es creciente ahí. Su valor mínimo es $b\cdot b^2 = b^3$ (en $x=b$) y tiende a $+\infty$. Recorre $\left[b^3,\ \infty\right)$.

Para que la unión cubra todo $\mathbb{R}$, los intervalos deben solaparse o al menos tocarse:
$$b^2 + 6b \ \ge\ b^3 \iff b^3 - b^2 - 6b \le 0 \iff b(b-3)(b+2) \le 0.$$

Con $b>0$ esto exige $0 < b \le 3$.

## Caso $b = 0$

$g(x) \equiv 0$: su rango es $\{0\}$, no cubre todas las horizontales. Queda descartado.

## Caso $b < 0$

- **Parábola** ($x \ge b$): ahora $x = 0$ pertenece al dominio (pues $0 \ge b$), y $bx^2 \le 0$ con máximo $0$ en $x=0$, tendiendo a $-\infty$. Recorre $(-\infty, 0]$.
- **Recta** ($x < b$): con $b<0$, cuando $x \to -\infty$ la recta tiende a $+\infty$; recorre $\left(b^2+6b,\ \infty\right)$.

La unión es $\mathbb{R}$ si $b^2 + 6b \le 0$, es decir $b \in [-6, 0)$; también funcionan estos valores, pero son todos menores que $3$.

## Conclusión

El mayor valor admisible viene del caso $b>0$. Comprobación con $b = 3$:
- Recta: $3x + 18$ en $x < 3$ recorre $(-\infty, 27)$,
- Parábola: $3x^2$ en $x \ge 3$ recorre $[27, \infty)$,

y juntos cubren todo $\mathbb{R}$. Para $b > 3$ queda el hueco $(b^2+6b,\ b^3)$.

$$\boxed{3}$$