## Planteamiento

Buscamos ecuaciones $x^2 + ax + b = 0$ tales que la función $f(c) = c^2 - 2$ envíe el conjunto de raíces en sí mismo.

**Caso 1: raíz doble $r$.** Necesitamos $f(r) = r$:
$$r^2 - 2 = r \implies r^2 - r - 2 = 0 \implies r = 2 \text{ o } r = -1.$$
Esto da **2 ecuaciones**: $(x-2)^2 = 0$ y $(x+1)^2 = 0$.

**Caso 2: raíces distintas $r \neq s$.** Hay varias formas en que $f$ puede actuar:

**(a) Ambas fijas:** $f(r) = r$, $f(s) = s$. Entonces $r, s \in \{2, -1\}$, distintas, así que las raíces son $\{2, -1\}$. **1 ecuación**.

**(b) Intercambio:** $f(r) = s$, $f(s) = r$. Restando $r^2 - 2 = s$ y $s^2 - 2 = r$:
$$r^2 - s^2 = s - r \implies (r-s)(r+s) = -(r-s) \implies r + s = -1.$$
Sustituyendo $s = -1 - r$ en $r^2 - 2 = s$: $r^2 + r - 1 = 0$, con raíces $r = \frac{-1 \pm \sqrt{5}}{2}$, que son precisamente $r$ y $s$ (suman $-1$). **1 ecuación**.

**(c) Ambas van a la misma raíz fija:** $f(r) = r$ y $f(s) = r$ con $s \neq r$. Entonces $r \in \{2, -1\}$ y $s^2 = r + 2$:
- $r = 2$: $s^2 = 4 \implies s = -2$ (pues $s \neq 2$). Raíces $\{2, -2\}$: se verifica $f(-2) = 2$ ✓. **1 ecuación**.
- $r = -1$: $s^2 = 1 \implies s = 1$ (pues $s \neq -1$). Raíces $\{-1, 1\}$: se verifica $f(1) = -1$ ✓. **1 ecuación**.

No hay más configuraciones posibles (el caso $f(r) = s$, $f(s) = s$ es el mismo conjunto que (c) con los papeles invertidos).

## Conteo total

$$2 + 1 + 1 + 1 + 1 = 6$$

$$\boxed{6}$$