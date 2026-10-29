Planteamos la condición: si $f(x)=\dfrac{p(x)}{q(x)}$ con $p,q$ cuadráticos, entonces $p(n)-n^3 q(n)=0$ para $n=1,2,3,4,5$.

El polinomio $r(x) = p(x) - x^3 q(x)$ tiene grado a lo más 5 y se anula en $1,2,3,4,5$, así que

$$p(x) - x^3 q(x) = k(x-1)(x-2)(x-3)(x-4)(x-5)$$

para alguna constante $k$. Expandiendo el producto:

$$(x-1)(x-2)(x-3)(x-4)(x-5) = x^5 - 15x^4 + 85x^3 - 225x^2 + 274x - 120.$$

Escribiendo $q(x) = ax^2 + bx + c$ y comparando coeficientes de $x^5$, $x^4$ y $x^3$ (donde $p$ no contribuye):

- $x^5$: $-a = k \Rightarrow a = -k$
- $x^4$: $-b = -15k \Rightarrow b = 15k$
- $x^3$: $-c = 85k \Rightarrow c = -85k$

Y de los términos de grado bajo, $p(x) = k(-225x^2 + 274x - 120)$, así que $p(0) = -120k$ y $q(0) = c = -85k$.

Por lo tanto:

$$f(0) = \frac{p(0)}{q(0)} = \frac{-120k}{-85k} = \frac{120}{85} = \frac{24}{17}.$$

$$\boxed{\dfrac{24}{17}}$$