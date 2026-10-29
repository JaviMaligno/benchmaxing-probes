Para encontrar el grado del polinomio $p(x)$, observamos primero que cada uno de los tres sumandos es un polinomio de grado $2$ en $x$. Por lo tanto, la suma $p(x)$ es un polinomio de grado a lo sumo $2$.

Evaluemos el polinomio $p(x)$ en los tres valores distintos $x = a$, $x = b$ y $x = c$:

1. Para $x = a$:
\[p(a) = \frac{(a - b)(a - c)}{(a - b)(a - c)} + \frac{(a - a)(a - c)}{(b - a)(b - c)} + \frac{(a - a)(a - b)}{(c - a)(c - b)} = 1 + 0 + 0 = 1.\]

2. Para $x = b$:
\[p(b) = \frac{(b - b)(b - c)}{(a - b)(a - c)} + \frac{(b - a)(b - c)}{(b - a)(b - c)} + \frac{(b - a)(b - b)}{(c - a)(c - b)} = 0 + 1 + 0 = 1.\]

3. Para $x = c$:
\[p(c) = \frac{(c - b)(c - c)}{(a - b)(a - c)} + \frac{(c - a)(c - c)}{(b - a)(b - c)} + \frac{(c - a)(c - b)}{(c - a)(c - b)} = 0 + 0 + 1 = 1.\]

Definamos ahora el polinomio $q(x) = p(x) - 1$. Como $p(x)$ tiene grado a lo sumo $2$, el polinomio $q(x)$ también tiene grado a lo sumo $2$. Sin embargo, sabemos que:
\[q(a) = q(b) = q(c) = 0.\]

Dado que $a, b$ y $c$ son números reales distintos, $q(x)$ tiene al menos tres raíces distintas. Un polinomio no nulo de grado a lo sumo $2$ puede tener como máximo dos raíces; por consiguiente, $q(x)$ debe ser idénticamente el polinomio cero, es decir, $q(x) = 0$ para todo $x$.

De esto se deduce que $p(x) = 1$ para todo $x$. Como $p(x)$ es un polinomio constante no nulo, su grado es $0$.

\boxed{0}