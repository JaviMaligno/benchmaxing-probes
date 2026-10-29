# Resolución paso a paso

**Condición de suryectividad.** Para que la gráfica de $y=f(x)$ corte a toda recta horizontal, el rango de $f$ debe ser todo $\mathbb{R}$.

Analizo cada tramo de la función por separado.

## Caso 1: $a > 0$

**Tramo $x \ge a$:** $f(x)=ax^2$ con $a>0$ es una parábola creciente en $x\ge a>0$. Su mínimo está en $x=a$:
$$f(a)=a^3,$$
así que este tramo recubre $[a^3,+\infty)$.

**Tramo $x < a$:** $f(x)=ax+2a$ es una recta creciente (pendiente $a>0$). Cuando $x\to -\infty$, $f\to-\infty$; cuando $x\to a^-$:
$$f(x)\to a\cdot a + 2a = a^2+2a.$$
Este tramo recubre $(-\infty,\, a^2+2a)$.

**Unión de los rangos:**
$$(-\infty,\, a^2+2a)\;\cup\;[a^3,\,+\infty) \stackrel{!}{=} \mathbb{R}.$$

No debe haber huecos, lo que exige:
$$a^2+2a \ge a^3 \iff a(a^2-a-2)\le 0 \iff a(a-2)(a+1)\le 0.$$

Como $a>0$, esto equivale a $(a-2)(a+1)\le 0$, es decir:
$$0 < a \le 2.$$

## Caso 2: $a < 0$

**Tramo $x \ge a$:** $ax^2\le 0$ con máximo $f(0)=0$ (y $0\ge a$, así que $x=0$ pertenece a este tramo). Recubre $(-\infty, 0]$.

**Tramo $x < a$:** recta con pendiente negativa; cuando $x\to-\infty$, $f\to+\infty$, y cerca de $a$ tiende a $a^2+2a$. Recubre $(a^2+2a, +\infty)$.

La unión es todo $\mathbb{R}$ solo si $a^2+2a\le 0$, es decir, $-2\le a<0$. Por tanto en este caso $a\le 0$ en el mejor escenario: no supera al caso positivo.

## Verificación del máximo

Con $a=2$:
- Tramo $x\ge 2$: $f(x)=2x^2$ recubre $[8,+\infty)$.
- Tramo $x<2$: $f(x)=2x+4$ recubre $(-\infty, 8)$.

La unión es exactamente $\mathbb{R}$: toda recta horizontal se corta al menos una vez. ✓

Por lo tanto, el mayor valor posible de $a$ es:

$$\boxed{2}$$