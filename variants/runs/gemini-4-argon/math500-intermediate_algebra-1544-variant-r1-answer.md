Para encontrar el número de ecuaciones cuadráticas de la forma $x^2 + px + q = 0$ tales que si $t$ es una raíz, entonces $f(t) = t^2 - 4t + 6$ también es una raíz, observemos primero que podemos reescribir $f(t)$ completando el cuadrado:
$$f(t) = (t - 2)^2 + 2$$

Haciendo el cambio de variable $u = t - 2$, tenemos que:
$$f(t) - 2 = (t - 2)^2 = u^2$$

Por lo tanto, si $S$ es el conjunto de raíces de la ecuación cuadrática $x^2 + px + q = 0$ (donde $1 \le |S| \le 2$), la condición de que $f(S) \subseteq S$ equivale a que el conjunto trasladado $U = \{t - 2 : t \in S\}$ cumpla que $g(U) \subseteq U$ bajo la aplicación $g(u) = u^2$.

Analizamos los casos según el número de raíces distintas (es decir, el tamaño de $U$):

**Caso 1: La ecuación tiene una única raíz repetida ($|U| = 1$).**
Sea $U = \{u_1\}$. Para que $g(U) \subseteq U$, $u_1$ debe ser un punto fijo de $g$:
$$u_1^2 = u_1 \implies u_1 = 0 \quad \text{o} \quad u_1 = 1$$
- Si $u_1 = 0$, entonces $t = 2$, lo que da la ecuación $(x - 2)^2 = x^2 - 4x + 4 = 0$.
- Si $u_1 = 1$, entonces $t = 3$, lo que da la ecuación $(x - 3)^2 = x^2 - 6x + 9 = 0$.

**Caso 2: La ecuación tiene dos raíces distintas ($|U| = 2$).**
Sea $U = \{u_1, u_2\}$ con $u_1 \neq u_2$. Hay tres subcasos posibles para la acción de $g$ sobre $U$:

1. **Ambos elementos son puntos fijos ($g(u_1) = u_1$ y $g(u_2) = u_2$):**
   Como los únicos puntos fijos son $0$ y $1$, tenemos $U = \{0, 1\}$, por lo que $S = \{2, 3\}$. Esto corresponde a la ecuación $(x - 2)(x - 3) = x^2 - 5x + 6 = 0$.

2. **Un elemento es un punto fijo y el otro se envía a él ($g(u_1) = u_1$ y $g(u_2) = u_1$ con $u_2 \neq u_1$):**
   - Si $u_1 = 0$, entonces $u_2^2 = 0 \implies u_2 = 0 = u_1$, lo cual no da dos raíces distintas.
   - Si $u_1 = 1$, entonces $u_2^2 = 1 \implies u_2 = -1$ (ya que $u_2 \neq 1$). Así, $U = \{-1, 1\}$ y $S = \{1, 3\}$, lo que corresponde a la ecuación $(x - 1)(x - 3) = x^2 - 4x + 3 = 0$.

3. **Los dos elementos forman un ciclo de longitud 2 ($g(u_1) = u_2$ y $g(u_2) = u_1$ con $u_1 \neq u_2$):**
   Entonces $u_1^4 = u_1$. Como $u_1$ no es un punto fijo ($u_1 \neq 0, 1$), dividimos por $u_1(u_1 - 1)$ y obtenemos:
   $$u_1^2 + u_1 + 1 = 0$$
   Las raíces de esta ecuación son las raíces cúbicas primitivas de la unidad, $\omega$ y $\omega^2$, que efectivamente cumplen $\omega^2 = \omega^2$ y $(\omega^2)^2 = \omega^4 = \omega$.
   Así, $U = \{\omega, \omega^2\}$ y $S = \{2 + \omega, 2 + \omega^2\}$, lo que da la ecuación:
   $$(x - 2 - \omega)(x - 2 - \omega^2) = (x - 2)^2 + (x - 2) + 1 = x^2 - 3x + 3 = 0$$

Sumando todos los casos, encontramos $2 + 1 + 1 + 1 = 5$ ecuaciones cuadráticas que cumplen la propiedad.

\boxed{5}