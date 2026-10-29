La suma de Priya es $\frac{mn(mn+1)}{2}$, y la de Tomas es $\left(\sum_{i=1}^m i\right)\left(\sum_{j=1}^n j\right) = \frac{m(m+1)}{2}\cdot\frac{n(n+1)}{2}$.

La diferencia es:
$$\frac{mn(mn+1)}{2} - \frac{mn(m+1)(n+1)}{4} = \frac{mn\big[2mn+2 - (mn+m+n+1)\big]}{4} = \frac{mn(m-1)(n-1)}{4}.$$

Igualando a 2100:
$$m(m-1)\cdot n(n-1) = 8400.$$

Busco factorizar 8400 como producto de dos números de la forma $k(k-1)$: con $m(m-1)=20$ (es decir, $m=5$) queda $n(n-1)=420$, que da $n=21$. Verificación: $20 \cdot 420 = 8400$. ✓

Las demás opciones ($2\cdot4200$, $6\cdot1400$, $12\cdot700$, $30\cdot280$, etc.) no producen cofactores de la forma $k(k-1)$, así que la única solución (salvo intercambio de $m$ y $n$) es $\{m,n\}=\{5,21\}$.

$$m+n = \boxed{26}$$