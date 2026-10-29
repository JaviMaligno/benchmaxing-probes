**Razonamiento**

Los vértices forman el grupo $\mathbb{F}_2^n$ y moverse por una arista equivale a sumar un vector de peso exactamente $k$. Por tanto, la componente de $x$ es la clase lateral $x + V_{n,k}$, donde $V_{n,k}$ es el subespacio generado por todos los vectores de peso $k$, y
$$c_{n,k} = 2^{\,n - \dim V_{n,k}}.$$

*Caso $k < n$:* existen dos vectores de peso $k$ cuyos soportes comparten $k-1$ posiciones; su suma es $e_i + e_j$. Así $V_{n,k}$ contiene todos los vectores de peso 2, que generan el subespacio de peso par (dimensión $n-1$).
- Si $k$ es par, $V_{n,k}$ es exactamente ese subespacio: $c_{n,k} = 2$.
- Si $k$ es impar, añadir un vector de peso impar da todo $\mathbb{F}_2^n$: $c_{n,k} = 1$.

*Caso $k = n$:* hay un único vector de peso $n$ (el de unos), luego $\dim V = 1$ y $c_{n,n} = 2^{n-1}$.

(Comprobación: $G_{3,2}$ tiene $k=2$ par con $k<n$, o sea 2 componentes ✓.)

**Suma por fila**, con $m = n-1$: $\;2^{n-1} + \lceil m/2\rceil + 2\lfloor m/2\rfloor$

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| total | 1 | 3 | 7 | 12 | 22 | 39 | 73 | 138 | 268 | 525 |

Sumando: $1+3+7+12+22+39+73+138+268+525 = 1088$.

\boxed{1088}