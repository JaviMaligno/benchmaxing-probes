## Planteamiento

La identidad clave: si $x = t + \dfrac{1}{t}$, entonces
$$g(x) = \left(t+\tfrac1t\right)^3 - 3\left(t+\tfrac1t\right) = t^3 + \tfrac{1}{t^3}.$$

Como $\dfrac{n^2+1}{n} = n + \dfrac1n$, tomando $t=n$ se obtiene por inducción
$$g^k\!\left(\frac{n^2+1}{n}\right) = n^{3^k} + n^{-3^k}.$$

## Reducción a una condición aritmética

Para $n=1$ el valor es siempre $2$, y $c^{72}=2$ es imposible.

Para $n\ge 2$ y $k\ge 1$ se tiene $0 < n^{-3^k} \le 2^{-3} = \tfrac18$. Dado que $n^{3^k}$ y $c^{72}$ son enteros, si $n^{3^k} \ne c^{72}$ entonces
$$\left|n^{3^k} + n^{-3^k} - c^{72}\right| \ge 1 - \tfrac18 > \tfrac{1}{100}.$$

Por tanto es necesario que $n^{3^k} = c^{72}$, y entonces el error es exactamente $n^{-3^k}$, que cumple $n^{-3^k} < \tfrac1{100}$ en cuanto $n^{3^k} > 100$ (automático si $n\ge 2$, $k\ge 2$).

## Resolver $n^{3^k} = c^{72}$

Si $a_p = v_p(n)$, la condición equivale a $72 \mid 3^k a_p$ para todo primo $p$. Como $72 = 8\cdot 9$ y $3^k$ es impar:

- $8 \mid a_p$ siempre es necesario.
- La parte $9$: si $k\ge 2$, $9\mid 3^k$ y no impone nada; si $k=1$, hace falta $3\mid a_p$.

Con $k\ge 2$, la condición es simplemente que $n$ sea una potencia octava perfecta (el caso $k=1$ exigiría $24\mid a_p$, es decir $n\ge 2^{24}$, peor).

El menor $n>1$ que es potencia octava es $n = 2^8 = 256$.

## Verificación

Con $n=256$, $k=2$, $c=2$:
$$g^2\!\left(\frac{256^2+1}{256}\right) = 256^{9} + 256^{-9} = 2^{72} + 2^{-72},$$
y $\left|2^{72}+2^{-72} - 2^{72}\right| = 2^{-72} < \dfrac{1}{100}$. ✓

\boxed{256}