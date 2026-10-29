Para encontrar el número de ecuaciones cuadráticas de la forma $x^2 + px + q = 0$ que cumplen con la propiedad dada, sea $g(t) = t^2 - 4t + 6$. La condición establece que si $t$ pertenece al conjunto de raíces $S$ de la ecuación cuadrática, entonces $g(t)$ también pertenece a $S$ (es decir, $g(S) \subseteq S$).

Notemos que podemos reescribir $g(t)$ completando el cuadrado:
$$g(t) - 2 = t^2 - 4t + 4 = (t - 2)^2$$

Realizando el cambio de variable $u = t - 2$ (de modo que $t = u + 2$), la transformación $t \mapsto g(t)$ sobre las raíces de la ecuación original equivale a la transformación
$$u \mapsto u^2$$
sobre el conjunto $U$ de raíces del polinomio trasladado $(u + 2)^2 + p(u + 2) + q = 0$.

Como la ecuación es cuadrática, el conjunto de sus raíces $U$ tiene tamaño $1$ (una raíz doble) o tamaño $2$ (dos raíces distintas), y debe cumplir que para todo $u \in U$, se tiene $u^2 \in U$. Analizamos los casos posibles:

**Caso 1: La ecuación tiene una única raíz (raíz doble), $U = \{u_1\}$.**
Para que $u_1^2 \in U$, debe cumplirse que $u_1^2 = u_1$, cuyas soluciones son $u_1 = 0$ y $u_1 = 1$.
1. Si $u_1 = 0$, entonces $t_1 = 2$ (raíz doble), lo que da la ecuación $(x - 2)^2 = x^2 - 4x + 4 = 0$.
2. Si $u_1 = 1$, entonces $t_1 = 3$ (raíz doble), lo que da la ecuación $(x - 3)^2 = x^2 - 6x + 9 = 0$.

**Caso 2: La ecuación tiene dos raíces distintas, $U = \{u_1, u_2\}$ con $u_1 \neq u_2$.**
Existen tres configuraciones posibles para que $U$ sea invariante bajo $u \mapsto u^2$:

- **Subcaso 2a: Ambas raíces son puntos fijos ($u_1^2 = u_1$ y $u_2^2 = u_2$).**
  Como los únicos puntos fijos son $0$ y $1$, tenemos $U = \{0, 1\}$, que corresponde a $S = \{2, 3\}$.
  3. Esto da la ecuación $(x - 2)(x - 3) = x^2 - 5x + 6 = 0$.

- **Subcaso 2b: Una raíz es punto fijo y la otra se mapea en ella ($u_1^2 = u_1$ y $u_2^2 = u_1$ con $u_2 \neq u_1$).**
  - Si $u_1 = 0$, entonces $u_2^2 = 0 \implies u_2 = 0 = u_1$, lo cual es imposible.
  - Si $u_1 = 1$, entonces $u_2^2 = 1$ con $u_2 \neq 1$, por lo que $u_2 = -1$. Así, $U = \{1, -1\}$, que corresponde a $S = \{3, 1\}$.
  4. Esto da la ecuación $(x - 1)(x - 3) = x^2 - 4x + 3 = 0$.

- **Subcaso 2c: Las dos raíces se intercambian ($u_1^2 = u_2$ y $u_2^2 = u_1$ con $u_1 \neq u_2$).**
  Sustituyendo obtenemos $u_1^4 = u_1$. Como $u_1 \notin \{0, 1\}$ (pues de lo contrario sería un punto fijo y $u_2 = u_1$), se tiene $u_1^3 = 1$ con $u_1 \neq 1$. Por tanto, $u_1$ y $u_2$ son las dos raíces cúbicas primitivas de la unidad ($\omega$ y $\omega^2$), que satisfacen $u^2 + u + 1 = 0$.
  5. Sustituyendo $u = x - 2$, obtenemos la ecuación $(x - 2)^2 + (x - 2) + 1 = x^2 - 3x + 3 = 0$.

En total, existen $5$ ecuaciones cuadráticas que satisfacen la propiedad.

\boxed{5}