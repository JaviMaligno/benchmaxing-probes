Primero identifico las distribuciones posibles de sabores. Necesito $m + b + k = 10$ con $m > b > k \geq 1$:

- $(7, 2, 1)$
- $(6, 3, 1)$
- $(5, 4, 1)$
- $(5, 3, 2)$

(Combinaciones como $(4,3,3)$ o $(6,2,2)$ no sirven porque la desigualdad debe ser estricta.)

Para cada distribución, cuento las asignaciones con coeficientes multinomiales:

- $(7,2,1)$: $\dfrac{10!}{7!\,2!\,1!} = 360$
- $(6,3,1)$: $\dfrac{10!}{6!\,3!\,1!} = 840$
- $(5,4,1)$: $\dfrac{10!}{5!\,4!\,1!} = 1260$
- $(5,3,2)$: $\dfrac{10!}{5!\,3!\,2!} = 2520$

Sumando: $N = 360 + 840 + 1260 + 2520 = 4980$.

El residuo al dividir entre 1000 es:

$$\boxed{980}$$