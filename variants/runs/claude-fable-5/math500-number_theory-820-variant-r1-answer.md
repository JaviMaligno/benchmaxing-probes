Analicemos la factorización: $2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$, es decir, 5 primos distintos.

Para cada primo $p$ de estos cinco, si $m = \prod p^{a_p}$ y $n = \prod p^{b_p}$:

- $\gcd(m,n) = 2310$ implica $\min(a_p, b_p) = 1$,
- $\mathrm{lcm}[m,n] = 2310^3$ implica $\max(a_p, b_p) = 3$.

Por lo tanto, para cada primo uno de los exponentes es $1$ y el otro es $3$ (no hay más opciones, porque el mínimo debe ser exactamente 1 y el máximo exactamente 3). Esto da $2$ elecciones por primo, es decir $2^5 = 32$ pares ordenados $(m,n)$.

Como en cada primo los exponentes de $m$ y $n$ difieren, nunca ocurre $m = n$. Por simetría, exactamente la mitad de los pares cumple $m < n$, lo que da $32/2 = 16$ valores posibles para $m$.

$$\boxed{16}$$