## Planteamiento

Sean $m, b, k$ el número de miembros que eligieron mango, banana y kiwi. Las condiciones son:

$$m + b + k = 10, \qquad m > b > k \ge 1$$

## Enumeración de los tripletes

- $k=1$: $m+b=9$ con $m>b>1$ → $(7,2,1)$, $(6,3,1)$, $(5,4,1)$
- $k=2$: $m+b=8$ con $m>b>2$ → $(5,3,2)$ (el caso $4+4$ se descarta)
- $k=3$: $m+b=7$ con $m>b>3$ → imposible

## Conteo de asignaciones

Cada triplete se cuenta con el coeficiente multinomial $\dfrac{10!}{m!\,b!\,k!}$:

| $(m,b,k)$ | Asignaciones |
|---|---|
| $(7,2,1)$ | $\frac{10!}{7!2!1!} = 360$ |
| $(6,3,1)$ | $\frac{10!}{6!3!1!} = 840$ |
| $(5,4,1)$ | $\frac{10!}{5!4!1!} = 1260$ |
| $(5,3,2)$ | $\frac{10!}{5!3!2!} = 2520$ |

$$N = 360 + 840 + 1260 + 2520 = 4980$$

## Resultado

$$4980 = 4\cdot 1000 + 980$$

\boxed{980}