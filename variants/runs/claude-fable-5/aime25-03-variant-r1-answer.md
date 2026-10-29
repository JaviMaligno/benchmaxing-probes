Para resolverlo, busco primero las cantidades posibles $(m, b, k)$ de mango, banana y kiwi con $m + b + k = 10$, $m > b > k \geq 1$:

- $k=1$: necesito $m > b > 1$ con $m + b = 9$, es decir $m = 9-b > b$, o sea $b < 4.5$: da $(7,2,1)$, $(6,3,1)$, $(5,4,1)$.
- $k=2$: $m + b = 8$ con $m > b > 2$, o sea $b < 4$: da $(5,3,2)$.
- $k=3$: $m + b = 7$ con $m > b > 3$: imposible.

Para cada reparto, el número de asignaciones a los 10 miembros (distinguibles) es el coeficiente multinomial $\binom{10}{m,\,b,\,k}$:

- $(7,2,1)$: $\dfrac{10!}{7!\,2!\,1!} = 360$
- $(6,3,1)$: $\dfrac{10!}{6!\,3!\,1!} = 840$
- $(5,4,1)$: $\dfrac{10!}{5!\,4!\,1!} = 1260$
- $(5,3,2)$: $\dfrac{10!}{5!\,3!\,2!} = 2520$

Sumando: $N = 360 + 840 + 1260 + 2520 = 4980$, y el resto al dividir entre $1000$ es:

$$\boxed{980}$$