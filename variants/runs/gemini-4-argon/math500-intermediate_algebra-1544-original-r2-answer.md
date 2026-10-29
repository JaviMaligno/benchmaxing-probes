Para determinar el número de ecuaciones cuadráticas de la forma $x^2 + ax + b = 0$ que cumplen la condición dada, sea $f(x) = x^2 - 2$ y sea $S$ el conjunto de raíces distintas de la ecuación cuadrática. 

Dado que una ecuación cuadrática tiene a lo sumo dos raíces distintas (contando multiplicidades, tiene exactamente dos raíces que determinan de manera única los coeficientes $a$ y $b$), el conjunto $S$ puede tener $1$ o $2$ elementos. La condición de que siempre que $c \in S$ se cumpla que $f(c) = c^2 - 2 \in S$ equivale a decir que $f(S) \subseteq S$.

Analizamos los casos según el tamaño de $S$:

**Caso 1: $|S| = 1$ (la ecuación tiene una raíz doble $r$).**
En este caso, $S = \{r\}$ y la ecuación es de la forma $(x - r)^2 = 0$. Para que $f(r) \in S$, debe cumplirse que $f(r) = r$:
$$r^2 - 2 = r \implies r^2 - r - 2 = 0 \implies (r - 2)(r + 1) = 0$$
Por lo tanto, $r = 2$ o $r = -1$. Esto nos da **2** ecuaciones cuadráticas:
1. $(x - 2)^2 = x^2 - 4x + 4 = 0$
2. $(x + 1)^2 = x^2 + 2x + 1 = 0$

---

**Caso 2: $|S| = 2$ (la ecuación tiene dos raíces distintas $r_1 \neq r_2$).**
En este caso, $S = \{r_1, r_2\}$ y la ecuación es $(x - r_1)(x - r_2) = 0$. La condición $f(S) \subseteq S$ puede ocurrir de tres maneras distintas:

* **Subcaso 2a: Ambas raíces son puntos fijos de $f$, es decir, $f(r_1) = r_1$ y $f(r_2) = r_2$.**
  Como los únicos puntos fijos de $f(x) = x^2 - 2$ son $2$ y $-1$, el conjunto de raíces debe ser $S = \{2, -1\}$. Esto nos da **1** ecuación cuadrática:
  3. $(x - 2)(x + 1) = x^2 - x - 2 = 0$

* **Subcaso 2b: Una raíz es un punto fijo de $f$ y la otra se mapea en ella ($f(r_1) = r_1$ y $f(r_2) = r_1$ con $r_2 \neq r_1$).**
  * Si $r_1 = 2$, entonces $f(r_2) = 2 \implies r_2^2 - 2 = 2 \implies r_2^2 = 4$. Como $r_2 \neq 2$, tenemos $r_2 = -2$, lo que da $S = \{2, -2\}$.
  * Si $r_1 = -1$, entonces $f(r_2) = -1 \implies r_2^2 - 2 = -1 \implies r_2^2 = 1$. Como $r_2 \neq -1$, tenemos $r_2 = 1$, lo que da $S = \{-1, 1\}$.
  
  Esto nos da **2** ecuaciones cuadráticas:
  4. $(x - 2)(x + 2) = x^2 - 4 = 0$
  5. $(x + 1)(x - 1) = x^2 - 1 = 0$

* **Subcaso 2c: Las dos raíces forman un ciclo de longitud 2, es decir, $f(r_1) = r_2$ y $f(r_2) = r_1$ con $r_1 \neq r_2$.**
  En este caso, $r_1$ y $r_2$ satisfacen $f(f(x)) = x$, pero no $f(x) = x$. Calculamos:
  $$f(f(x)) - x = (x^2 - 2)^2 - 2 - x = x^4 - 4x^2 - x + 2$$
  Como las raíces de $f(x) - x = x^2 - x - 2$ también anulan a $f(f(x)) - x$, factorizamos el polinomio dividiendo por $x^2 - x - 2$:
  $$x^4 - 4x^2 - x + 2 = (x^2 - x - 2)(x^2 + x - 1)$$
  Las dos raíces de $x^2 + x - 1 = 0$ son distintas y forman el único ciclo de orden 2. Esto nos da **1** ecuación cuadrática:
  6. $x^2 + x - 1 = 0$

---

Sumando todas las posibilidades encontradas ($2 + 1 + 2 + 1$), obtenemos un total de $6$ ecuaciones cuadráticas.

\boxed{6}