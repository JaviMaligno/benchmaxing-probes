Vamos a resolverlo paso a paso.

## Paso 1: Encontrar las distribuciones posibles de sabores

Sea $m$, $b$, $k$ el número de miembros que eligieron mango, plátano y kiwi respectivamente. Necesitamos:
- $m + b + k = 10$
- $m > b > k \geq 1$

Enumeramos por el valor de $k$:

**Si $k = 1$:** entonces $m + b = 9$ con $m > b > 1$:
- $b = 2 \Rightarrow m = 7$ ✓ → $(7, 2, 1)$
- $b = 3 \Rightarrow m = 6$ ✓ → $(6, 3, 1)$
- $b = 4 \Rightarrow m = 5$ ✓ → $(5, 4, 1)$
- $b = 5 \Rightarrow m = 4$ ✗ (no es $m > b$)

**Si $k = 2$:** entonces $m + b = 8$ con $m > b > 2$:
- $b = 3 \Rightarrow m = 5$ ✓ → $(5, 3, 2)$
- $b = 4 \Rightarrow m = 4$ ✗

**Si $k = 3$:** entonces $m + b = 7$ con $m > b > 3$: no hay opciones ($b=4$ daría $m=3$). ✗

Las únicas distribuciones son: $(7,2,1)$, $(6,3,1)$, $(5,4,1)$, $(5,3,2)$.

## Paso 2: Contar las asignaciones para cada distribución

Como los 10 miembros son distinguibles, el número de asignaciones para cada distribución es el coeficiente multinomial $\binom{10}{m, b, k} = \frac{10!}{m!\, b!\, k!}$:

| $(m, b, k)$ | Cálculo | Resultado |
|---|---|---|
| $(7, 2, 1)$ | $\frac{10!}{7!\,2!\,1!} = \frac{3628800}{10080}$ | $360$ |
| $(6, 3, 1)$ | $\frac{10!}{6!\,3!\,1!} = \frac{3628800}{4320}$ | $840$ |
| $(5, 4, 1)$ | $\frac{10!}{5!\,4!\,1!} = \frac{3628800}{2880}$ | $1260$ |
| $(5, 3, 2)$ | $\frac{10!}{5!\,3!\,2!} = \frac{3628800}{1440}$ | $2520$ |

## Paso 3: Sumar y calcular el resto

$$N = 360 + 840 + 1260 + 2520 = 4980$$

$$4980 \bmod 1000 = \boxed{980}$$