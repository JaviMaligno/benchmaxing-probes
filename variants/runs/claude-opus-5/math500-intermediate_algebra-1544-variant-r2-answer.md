## Planteamiento

Sea $f(t) = t^2 - 4t + 6$. Si $S$ es el conjunto de raíces (en $\mathbb{C}$), la condición es $f(S) \subseteq S$.

**Puntos fijos:** $f(t) = t \iff t^2 - 5t + 6 = 0 \iff t \in \{2, 3\}$.

## Caso 1: raíz doble, $S = \{t\}$

Necesariamente $f(t) = t$, así que $t = 2$ o $t = 3$:
$$(x-2)^2 = 0, \qquad (x-3)^2 = 0$$
→ **2 ecuaciones**.

## Caso 2: dos raíces distintas, $S = \{a, b\}$

Las posibilidades para $f|_S$ son: identidad, intercambio, o constante.

**(a) Identidad:** $a, b$ son puntos fijos, luego $\{a,b\} = \{2,3\}$:
$$x^2 - 5x + 6 = 0$$

**(b) Intercambio:** $f(a) = b$, $f(b) = a$. Restando las ecuaciones:
$$(a-b)(a+b) - 4(a-b) = -(a-b) \implies a + b = 3.$$
Sumándolas: $a^2 + b^2 - 4(a+b) + 12 = a+b \implies a^2+b^2 = 3$, de donde $ab = \frac{9-3}{2} = 3$:
$$x^2 - 3x + 3 = 0$$
(raíces $\frac{3 \pm i\sqrt3}{2}$; se verifica que $f$ las intercambia, y los coeficientes son reales).

**(c) Constante:** digamos $f(a) = f(b) = a$. Entonces $a$ es fijo, $a \in \{2,3\}$.
- $a = 2$: $b^2 - 4b + 4 = 0 \Rightarrow b = 2 = a$, descartado.
- $a = 3$: $b^2 - 4b + 3 = 0 \Rightarrow b = 1$ (o $b=3$, descartado). Así $S = \{1,3\}$:
$$x^2 - 4x + 3 = 0$$

→ **3 ecuaciones**.

## Total

$$(x-2)^2,\quad (x-3)^2,\quad x^2-5x+6,\quad x^2-4x+3,\quad x^2-3x+3$$

\boxed{5}