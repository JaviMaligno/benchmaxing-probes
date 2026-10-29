## Planteamiento

Por interpolación de Lagrange, con los nodos $m = 1, \dots, 2029$:

$$g(x) = \sum_{\substack{m=1 \\ m \text{ cuadrado}}}^{2029} \prod_{k \neq m} \frac{x-k}{m-k}.$$

Los cuadrados perfectos en $\{1,\dots,2029\}$ son $j^2$ con $1 \le j \le 45$ (pues $45^2 = 2025$).

## Coeficiente de $x^{2027}$ en cada término

- El numerador $\prod_{k\neq m}(x-k)$ tiene grado $2028$, y su coeficiente de $x^{2027}$ es $-\sum_{k\neq m} k = -(S - m)$, donde $S = \frac{2029\cdot 2030}{2}$.
- El denominador es $\prod_{k\neq m}(m-k) = (-1)^{2029-m}(m-1)!\,(2029-m)!$.

Así, el coeficiente buscado es
$$c=\sum_{m=j^2} \frac{-(S-m)}{(-1)^{2029-m}(m-1)!\,(2029-m)!}.$$

## Reducción módulo $p = 2029$

Como $p$ es primo y $S = \frac{p(p+1)}{2} \equiv 0 \pmod p$, el numerador de cada término es $\equiv m$.

Para el denominador, de $(p-1)! = (m-1)!\prod_{j=m}^{p-1} j$ y $\prod_{j=m}^{p-1} j \equiv (-1)^{p-m}(p-m)! \pmod p$, junto con Wilson $(p-1)! \equiv -1$, se obtiene
$$(m-1)!\,(p-m)! \equiv -(-1)^{p-m} \pmod p,$$
y por tanto
$$(-1)^{p-m}(m-1)!\,(p-m)! \equiv -1 \pmod p.$$

Cada término vale entonces $\dfrac{m}{-1} = -m \pmod{2029}$, de modo que
$$c \equiv -\sum_{j=1}^{45} j^2 = -\frac{45\cdot 46 \cdot 91}{6} = -31395 \pmod{2029}.$$

## Cálculo final

$31395 = 15\cdot 2029 + 960$, así que $c \equiv -960 \equiv 2029 - 960 = 1069 \pmod{2029}$.

Como los denominadores involucrados solo contienen factores menores que $2029$, $q$ es invertible módulo $2029$ y $s \equiv p\,q^{-1} \equiv c \pmod{2029}$.

$$\boxed{1069}$$