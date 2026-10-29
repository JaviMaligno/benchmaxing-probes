## Planteamiento

Buscamos las ternas $(m, b, k)$ con $m + b + k = 10$, $m > b > k \ge 1$:

- $k = 1$: $m + b = 9$ con $m > b > 1$ → $(7,2,1)$, $(6,3,1)$, $(5,4,1)$
- $k = 2$: $m + b = 8$ con $m > b > 2$ → $(5,3,2)$
- $k = 3$: $m + b = 7$ con $m > b > 3$ → ninguna

## Conteo de asignaciones

Para cada terna, el número de formas de asignar los sabores a los 10 miembros distinguibles es el coeficiente multinomial $\dfrac{10!}{m!\,b!\,k!}$:

- $(7,2,1)$: $\dfrac{3628800}{5040 \cdot 2 \cdot 1} = 360$
- $(6,3,1)$: $\dfrac{3628800}{720 \cdot 6 \cdot 1} = 840$
- $(5,4,1)$: $\dfrac{3628800}{120 \cdot 24 \cdot 1} = 1260$
- $(5,3,2)$: $\dfrac{3628800}{120 \cdot 6 \cdot 2} = 2520$

## Total

$$N = 360 + 840 + 1260 + 2520 = 4980$$

El resto al dividir entre 1000 es $980$.

\boxed{980}