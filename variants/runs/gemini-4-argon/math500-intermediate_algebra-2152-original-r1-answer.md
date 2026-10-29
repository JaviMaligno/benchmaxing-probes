Para encontrar el grado del polinomio $p(x)$, analicemos su comportamiento evaluándolo en los valores $x = a$, $x = b$ y $x = c$:

1. **Observación del grado máximo:**
   El polinomio $p(x)$ es la suma de tres polinomios cuadráticos en $x$. Por lo tanto, el grado de $p(x)$ es a lo sumo $2$.

2. **Evaluación en puntos específicos:**
   Dado que $a$, $b$ y $c$ son números reales distintos, los denominadores son todos distintos de cero:
   - Para $x = a$:
     \[p(a) = \frac{(a - b)(a - c)}{(a - b)(a - c)} + \frac{(a - a)(a - c)}{(b - a)(b - c)} + \frac{(a - a)(a - b)}{(c - a)(c - b)} = 1 + 0 + 0 = 1.\]
   - Para $x = b$:
     \[p(b) = \frac{(b - b)(b - c)}{(a - b)(a - c)} + \frac{(b - a)(b - c)}{(b - a)(b - c)} + \frac{(b - a)(b - b)}{(c - a)(c - b)} = 0 + 1 + 0 = 1.\]
   - Para $x = c$:
     \[p(c) = \frac{(c - b)(c - c)}{(a - b)(a - c)} + \frac{(c - a)(c - c)}{(b - a)(b - c)} + \frac{(c - a)(c - b)}{(c - a)(c - b)} = 0 + 0 + 1 = 1.\]

3. **Conclusión mediante el teorema fundamental del álgebra:**
   Definamos el polinomio auxiliar $q(x) = p(x) - 1$. Como $p(x)$ tiene grado a lo sumo $2$, el polinomio $q(x)$ también tiene grado a lo sumo $2$.
   Sin embargo, sabemos que:
   \[q(a) = q(b) = q(c) = 0.\]
   Esto significa que $q(x)$ tiene al menos tres raíces distintas ($a, b, c$). Dado que cualquier polinomio no nulo de grado a lo sumo $2$ puede tener como máximo $2$ raíces, concluimos que $q(x)$ debe ser idénticamente el polinomio cero ($q(x) = 0$ para todo $x$).

   Por lo tanto, $p(x) = 1$ para todo $x \in \mathbb{R}$. Al ser un polinomio constante distinto de cero, su grado es $0$.

\boxed{0}