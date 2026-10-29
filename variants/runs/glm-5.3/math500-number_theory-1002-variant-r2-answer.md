**Paso 1:** Como $x \equiv 8 \pmod{11}$ y $x \equiv 8 \pmod{13}$, y $\gcd(11,13)=1$, entonces $x \equiv 8 \pmod{143}$.

**Paso 2:** Escribo $x = 143k + 8$ y impongo la condición módulo $7$:
$$143k + 8 \equiv 2 \pmod 7$$
Como $143 \equiv 3 \pmod 7$ y $8 \equiv 1 \pmod 7$:
$$3k + 1 \equiv 2 \pmod 7 \implies 3k \equiv 1 \pmod 7$$
El inverso de $3$ módulo $7$ es $5$ (pues $3\cdot 5 = 15 \equiv 1$), así que $k \equiv 5 \pmod 7$.

**Paso 3:** Con $k = 7m + 5$:
$$x = 143(7m+5) + 8 = 1001m + 723$$

**Paso 4:** Los valores positivos son $723,\ 1724,\ 2725,\ 3726,\dots$ El mayor menor que $3000$ es $2725$.

**Verificación:** $2725 = 7\cdot 389 + 2$ ✓; $2725 = 11\cdot 247 + 8$ ✓; $2725 = 13\cdot 209 + 8$ ✓.

$$\boxed{2725}$$