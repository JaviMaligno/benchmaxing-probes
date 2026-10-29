## Planteamiento

Buscamos $n < 2010$ con:
- $n \equiv 5 \pmod 7$
- $n \equiv 10 \pmod{11}$
- $n \equiv 10 \pmod{13}$

**Paso 1: combinar las dos últimas congruencias.**

Como $n \equiv 10$ módulo $11$ y módulo $13$, y $\gcd(11,13)=1$:
$$n \equiv 10 \pmod{143}, \qquad \text{es decir } n = 143k + 10.$$

**Paso 2: imponer la condición módulo 7.**

Dado que $143 = 7\cdot20 + 3$, tenemos $143 \equiv 3 \pmod 7$:
$$3k + 3 \equiv 5 \pmod 7 \;\Longrightarrow\; 3k \equiv 2 \pmod 7.$$

El inverso de $3$ módulo $7$ es $5$ (pues $15 \equiv 1$), así que:
$$k \equiv 5\cdot 2 = 10 \equiv 3 \pmod 7.$$

**Paso 3: maximizar bajo la cota.**

$$143k + 10 < 2010 \;\Longrightarrow\; k < \frac{2000}{143} \approx 13{,}98 \;\Longrightarrow\; k \le 13.$$

Los valores admisibles son $k \in \{3, 10\}$; el mayor es $k = 10$, que da
$$n = 143\cdot 10 + 10 = 1440.$$

**Verificación:** $1440 = 7\cdot205 + 5$, $1440 = 11\cdot130 + 10$, $1440 = 13\cdot110 + 10$. ✓

\boxed{1440}