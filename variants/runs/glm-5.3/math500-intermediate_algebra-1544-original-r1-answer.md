# Planteamiento

Sea $g(c) = c^2 - 2$. La condición exige que $g$ lleve el conjunto de raíces $\{r, s\}$ dentro de sí mismo. Analizamos los casos.

## Caso 1: raíz doble $r = s = c$

Como la única raíz es $c$, se necesita $g(c) = c$:
$$c^2 - c - 2 = 0 \implies c = 2 \ \text{o} \ c = -1$$

Esto produce las ecuaciones $x^2 - 4x + 4 = 0$ y $x^2 + 2x + 1 = 0$.

## Caso 2: raíces distintas $r \neq s$

Cualquier aplicación de $\{r,s\}$ en sí mismo es de uno de estos tipos:

**a) Ambos puntos fijos:** $g(r) = r$, $g(s) = s$, así que $r,s \in \{2,-1\}$. Se obtiene $x^2 - x - 2 = 0$, con raíces $\{2, -1\}$.

**b) Intercambio:** $g(r) = s$, $g(s) = r$. Restando $r^2 - s^2 = s - r$ y usando $r \neq s$:
$$r + s = -1$$
Sustituyendo $s = r^2 - 2 = -1 - r$ resulta $r^2 + r - 1 = 0$, con raíces $\frac{-1 \pm \sqrt{5}}{2}$, y $rs = -1$. Se obtiene $x^2 + x - 1 = 0$.

**c) Aplicación constante:** $g(r) = g(s) = r$ (o simétricamente hacia $s$). El valor fijo debe cumplir $r \in \{2, -1\}$, y $s^2 = r + 2$:
- $r = 2$: $s = -2$ → $x^2 - 4 = 0$
- $r = -1$: $s = 1$ → $x^2 - 1 = 0$

## Verificación de las seis ecuaciones

| Ecuación | Raíces | Comprobación |
|---|---|---|
| $x^2 - 4x + 4 = 0$ | $2$ | $g(2) = 2$ ✓ |
| $x^2 + 2x + 1 = 0$ | $-1$ | $g(-1) = -1$ ✓ |
| $x^2 - x - 2 = 0$ | $2, -1$ | $g(2)=2$, $g(-1)=-1$ ✓ |
| $x^2 + x - 1 = 0$ | $\frac{-1\pm\sqrt5}{2}$ | cada raíz va a la otra ✓ |
| $x^2 - 4 = 0$ | $\pm 2$ | $g(-2)=2$, $g(2)=2$ ✓ |
| $x^2 - 1 = 0$ | $\pm 1$ | $g(1)=-1$, $g(-1)=-1$ ✓ |

El análisis cubre todos los tipos de aplicación posibles sobre un conjunto de dos raíces (también sobre los complejos, pues los únicos puntos fijos de $g$ son $2$ y $-1$), así que no hay más casos.

En total: 2 ecuaciones con raíz doble y 4 con raíces distintas.

\boxed{6}