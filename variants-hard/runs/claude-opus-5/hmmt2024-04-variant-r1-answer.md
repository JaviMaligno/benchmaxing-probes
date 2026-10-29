## Planteamiento

Sea $g(x)=\dfrac{p(x)}{q(x)}$ con $p,q$ cuadráticos, $q(x)=ax^2+bx+c$.

La condición $g(k)=k^3$ implica que el polinomio

$$F(x)=p(x)-x^3q(x)$$

se anula en $x=1,2,3,4,6$. Su grado es 5, con coeficiente principal $-a$, así que

$$p(x)-x^3q(x)=-a(x-1)(x-2)(x-3)(x-4)(x-6).$$

## Comparación de coeficientes

Desarrollando con las funciones simétricas elementales de $\{1,2,3,4,6\}$: $e_1=16$, $e_2=95$, $e_5=144$:

$$-a\left(x^5-16x^4+95x^3-e_3x^2+e_4x-144\right).$$

En el lado izquierdo, $-x^3q(x)=-ax^5-bx^4-cx^3$ (los términos de $p$ solo afectan grados $\le 2$):

- $x^4$: $-b=16a \Rightarrow b=-16a$
- $x^3$: $-c=-95a \Rightarrow c=95a$

## Evaluación en 0

$$p(0)=-a\cdot(-1)(-2)(-3)(-4)(-6)=-a(-144)=144a,\qquad q(0)=c=95a.$$

$$g(0)=\frac{144a}{95a}=\frac{144}{95}.$$

$$\boxed{\dfrac{144}{95}}$$