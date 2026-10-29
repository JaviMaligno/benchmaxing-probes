## Planteamiento

Buscamos $x$ tal que:
- $x \equiv 2 \pmod 7$
- $x \equiv 8 \pmod{11}$
- $x \equiv 8 \pmod{13}$

**Paso 1: combinar las dos últimas congruencias.**

Como el resto es $8$ en ambos casos y $\gcd(11,13)=1$:
$$x \equiv 8 \pmod{143}$$

Es decir, $x = 8 + 143k$.

**Paso 2: imponer la congruencia módulo 7.**

Reducimos módulo 7: $143 = 20\cdot 7 + 3$, así que $143 \equiv 3$, y $8 \equiv 1$:
$$1 + 3k \equiv 2 \pmod 7 \quad\Longrightarrow\quad 3k \equiv 1 \pmod 7$$

El inverso de $3$ módulo $7$ es $5$ (pues $3\cdot 5 = 15 \equiv 1$), luego $k \equiv 5 \pmod 7$, o sea $k = 5 + 7m$.

**Paso 3: solución general.**
$$x = 8 + 143(5 + 7m) = 723 + 1001m$$

**Paso 4: buscar el mayor valor menor que 3000.**

Los valores son $723,\ 1724,\ 2725,\ 3726,\dots$ El mayor por debajo de $3000$ es $2725$.

**Verificación:** $2725 = 7\cdot 389 + 2$; $2725 = 11\cdot 247 + 8$; $2725 = 13\cdot 209 + 8$. ✓

$$\boxed{2725}$$