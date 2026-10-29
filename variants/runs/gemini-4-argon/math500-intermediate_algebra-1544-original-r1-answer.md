Para encontrar el número de ecuaciones cuadráticas de la forma $x^2 + ax + b = 0$ que cumplen la propiedad de que si $c$ es una raíz, entonces $f(c) = c^2 - 2$ también es una raíz, analicemos el conjunto $S$ de raíces distintas de la ecuación.

Dado que una ecuación cuadrática tiene a lo sumo dos raíces distintas, el tamaño de $S$ puede ser $|S| = 1$ o $|S| = 2$, y la función $f(x) = x^2 - 2$ debe enviar cada elemento de $S$ a un elemento de $S$.

### Caso 1: La ecuación tiene una única raíz repetida ($|S| = 1$)
Sea $r$ la única raíz, de modo que la ecuación es $(x - r)^2 = 0$. Para que $f(r)$ también sea raíz, debemos tener $f(r) = r$:
$$r^2 - 2 = r \implies r^2 - r - 2 = 0 \implies (r - 2)(r + 1) = 0$$
Por lo tanto, $r = 2$ o $r = -1$. Esto nos da **2** ecuaciones cuadráticas:
1. $(x - 2)^2 = x^2 - 4x + 4 = 0$
2. $(x + 1)^2 = x^2 + 2x + 1 = 0$

---

### Caso 2: La ecuación tiene dos raíces distintas ($|S| = 2$)
Sean $r_1$ y $r_2$ las dos raíces distintas ($r_1 \neq r_2$). Como $f(r_1) \in \{r_1, r_2\}$ y $f(r_2) \in \{r_1, r_2\}$, tenemos tres subcasos posibles:

#### Subcaso 2a: Ambas raíces son puntos fijos de $f$
Aquí $f(r_1) = r_1$ y $f(r_2) = r_2$. Como vimos en el Caso 1, los únicos puntos fijos de $f(x) = x^2 - 2$ son $2$ y $-1$. Así, el conjunto de raíces debe ser $S = \{2, -1\}$, lo que nos da **1** ecuación cuadrática:
3. $(x - 2)(x + 1) = x^2 - x - 2 = 0$

#### Subcaso 2b: Una raíz es un punto fijo y la otra se envía a ella
Sin pérdida de generalidad, supongamos que $f(r_1) = r_1$ y $f(r_2) = r_1$ con $r_2 \neq r_1$.
Como $r_1^2 - 2 = r_1$ y $r_2^2 - 2 = r_1$, tenemos que $r_2^2 = r_1^2$. Al ser $r_2 \neq r_1$, necesariamente $r_2 = -r_1$.
- Si $r_1 = 2$, entonces $r_2 = -2$, lo que da $S = \{2, -2\}$.
- Si $r_1 = -1$, entonces $r_2 = 1$, lo que da $S = \{-1, 1\}$.

Esto nos proporciona **2** ecuaciones cuadráticas adicionales:
4. $(x - 2)(x + 2) = x^2 - 4 = 0$
5. $(x - 1)(x + 1) = x^2 - 1 = 0$

#### Subcaso 2c: La función $f$ intercambia las dos raíces
Aquí $f(r_1) = r_2$ y $f(r_2) = r_1$, es decir:
$$r_1^2 - 2 = r_2$$
$$r_2^2 - 2 = r_1$$
Restando la segunda ecuación de la primera, obtenemos:
$$r_1^2 - r_2^2 = r_2 - r_1 \implies (r_1 - r_2)(r_1 + r_2 + 1) = 0$$
Como $r_1 \neq r_2$, dividimos por $r_1 - r_2$ y obtenemos $r_2 = -r_1 - 1$. Sustituyendo esto en la primera ecuación:
$$r_1^2 - 2 = -r_1 - 1 \implies r_1^2 + r_1 - 1 = 0$$
Por simetría, $r_2$ también satisface $x^2 + x - 1 = 0$ (cuyas raíces son distintas, $\frac{-1 \pm \sqrt{5}}{2}$). Esto determina de forma única el conjunto $S = \{r_1, r_2\}$ y nos da **1** ecuación cuadrática más:
6. $x^2 + x - 1 = 0$

---

### Conclusión
Sumando todos los casos posibles, el número total de ecuaciones cuadráticas es $2 + 1 + 2 + 1 = 6$.

\boxed{6}