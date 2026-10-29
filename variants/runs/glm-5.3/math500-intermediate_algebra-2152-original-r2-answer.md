## Solución paso a paso

**Paso 1: Evaluar $p(x)$ en los puntos $a$, $b$ y $c$.**

Si sustituimos $x = a$ en la expresión:
- El primer término vale $\frac{(a-b)(a-c)}{(a-b)(a-c)} = 1$
- El segundo término tiene el factor $(x-a) = 0$, así que vale $0$
- El tercer término también tiene el factor $(x-a) = 0$, así que vale $0$

Por lo tanto, $p(a) = 1$. Con el mismo argumento:
$$p(a) = 1, \qquad p(b) = 1, \qquad p(c) = 1.$$

**Paso 2: Considerar el polinomio auxiliar.**

Cada término de $p(x)$ es un cociente de polinomios de grado 2, así que $p(x)$ es un polinomio de grado a lo más $2$ (los denominadores son constantes distintas de cero, pues $a$, $b$, $c$ son distintos).

Definimos $q(x) = p(x) - 1$. Entonces $q(x)$ es un polinomio de grado a lo más $2$ que cumple:
$$q(a) = q(b) = q(c) = 0.$$

**Paso 3: Concluir que $q$ es idénticamente cero.**

Un polinomio distinto de cero de grado $\le 2$ tiene a lo más $2$ raíces. Pero $q$ tiene las tres raíces distintas $a$, $b$, $c$. La única posibilidad es que $q(x) \equiv 0$.

Por lo tanto:
$$p(x) = 1 \quad \text{para todo } x.$$

(Esto es exactamente lo que dice la fórmula de interpolación de Lagrange: la suma de los polinomios base de Lagrange es la función constante $1$.)

**Paso 4: Determinar el grado.**

El polinomio $p(x)$ es la constante $1$, que tiene grado $0$.

\[
\boxed{0}
\]