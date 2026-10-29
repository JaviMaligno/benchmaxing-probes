## Planteamiento

Evalúo el polinomio en tres puntos: $p=f(0)$, $q=f(1/2)$, $r=f(1)$, donde $|p|,|q|,|r|\le 1$.

$$p=c,\qquad q=\tfrac{a}{4}+\tfrac{b}{2}+c,\qquad r=a+b+c$$

Despejando los coeficientes:

$$c=p,\qquad a=2p-4q+2r,\qquad b=-3p+4q-r$$

## Cota superior

Entonces
$$|a|+|b|+|c|\le |2p-4q+2r|+|3p-4q+r|+|p|,$$
que es una función convexa de $(p,q,r)$ en el cubo $[-1,1]^3$, así que su máximo se alcanza en un vértice. Por simetría basta tomar $p=1$:

| $(p,q,r)$ | $a$ | $b$ | $c$ | suma |
|---|---|---|---|---|
| $(1,1,1)$ | $0$ | $0$ | $1$ | $1$ |
| $(1,1,-1)$ | $-4$ | $-2$ | $1$ | $7$ |
| $(1,-1,1)$ | $8$ | $-8$ | $1$ | $17$ |
| $(1,-1,-1)$ | $4$ | $6$ | $1$ | $11$ |

El máximo posible es $17$.

## El caso de igualdad se alcanza

Con $(p,q,r)=(1,-1,1)$ se obtiene $f(x)=8x^2-8x+1$ (el polinomio de Chebyshev trasladado a $[0,1]$). Su vértice está en $x=1/2$ con $f(1/2)=-1$, y en los extremos $f(0)=f(1)=1$, de modo que $|f(x)|\le 1$ en todo $[0,1]$. Aquí $|a|+|b|+|c|=8+8+1=17$.

$$\boxed{17}$$