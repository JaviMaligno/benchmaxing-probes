**Paso 1:** Como $x \equiv 10 \pmod{11}$ y $x \equiv 10 \pmod{13}$, y $11$ y $13$ son coprimos, el teorema chino del resto da:
$$x \equiv 10 \pmod{143}$$
es decir, $x = 143k + 10$.

**Paso 2:** Imponemos la condición módulo $7$:
$$143k + 10 \equiv 5 \pmod 7$$
Como $143 \equiv 3 \pmod 7$ y $10 \equiv 3 \pmod 7$:
$$3k + 3 \equiv 5 \pmod 7 \implies 3k \equiv 2 \pmod 7$$
El inverso de $3$ módulo $7$ es $5$ (pues $3\cdot 5 = 15 \equiv 1$), así que:
$$k \equiv 5 \cdot 2 = 10 \equiv 3 \pmod 7$$

**Paso 3:** Con $k = 7m + 3$:
$$x = 143(7m+3) + 10 = 1001m + 439$$

**Paso 4:** Buscamos el mayor valor menor que $2010$:
- $m=0$: $x = 439$
- $m=1$: $x = 1440$
- $m=2$: $x = 2441 > 2010$

**Verificación de $1440$:** $1440 = 7\cdot 205 + 5$, $1440 = 11\cdot 130 + 10$, $1440 = 13\cdot 110 + 10$. ✓

$$\boxed{1440}$$