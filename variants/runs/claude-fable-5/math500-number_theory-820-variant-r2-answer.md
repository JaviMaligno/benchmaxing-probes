Factorizamos: $2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$, cinco primos distintos.

Para cada primo $p$, si $m$ tiene exponente $a$ y $n$ tiene exponente $b$, necesitamos $\min(a,b) = 1$ (por el mcd) y $\max(a,b) = 3$ (por el mcm). Es decir, para cada uno de los 5 primos, los exponentes de $m$ y $n$ son exactamente $\{1, 3\}$ en algún orden: 2 opciones por primo.

Esto da $2^5 = 32$ pares ordenados $(m, n)$. Como en cada primo los exponentes de $m$ y $n$ difieren, nunca ocurre $m = n$, así que exactamente la mitad de los pares cumple $m < n$: $32 / 2 = 16$.

$$\boxed{16}$$