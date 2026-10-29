## Resolución

**Combinar las dos últimas congruencias**

Como $n \equiv 10 \pmod{11}$ y $n \equiv 10 \pmod{13}$, y $\gcd(11,13)=1$:
$$n \equiv 10 \pmod{143}$$

**Incorporar la primera congruencia**

Escribimos $n = 143k + 10$ y pedimos $n \equiv 5 \pmod 7$. Como $143 \equiv 3 \pmod 7$ y $10 \equiv 3 \pmod 7$:
$$3k + 3 \equiv 5 \pmod 7 \;\Longrightarrow\; 3k \equiv 2 \pmod 7$$

El inverso de $3$ módulo $7$ es $5$, luego $k \equiv 10 \equiv 3 \pmod 7$.

**Forma general**

Con $k = 7m + 3$:
$$n = 143(7m+3) + 10 = 1001m + 439$$

**Mayor valor menor que 2010**

- $m = 0 \to 439$
- $m = 1 \to 1440$
- $m = 2 \to 2441 > 2010$

**Verificación de $1440$:** $1440 = 7\cdot205 + 5$, $\;1440 = 11\cdot130 + 10$, $\;1440 = 13\cdot110 + 10$. ✓

\boxed{1440}