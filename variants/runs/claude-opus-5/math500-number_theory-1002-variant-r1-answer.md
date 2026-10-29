## Planteamiento

Buscamos $x$ con:
- $x \equiv 2 \pmod 7$
- $x \equiv 8 \pmod{11}$
- $x \equiv 8 \pmod{13}$

**Paso 1.** Como el resto es $8$ tanto módulo $11$ como módulo $13$, se combinan directamente:
$$x \equiv 8 \pmod{143}, \qquad 143 = 11 \cdot 13$$

Así que $x = 8 + 143k$.

**Paso 2.** Imponemos la condición módulo $7$. Dado que $143 \equiv 3 \pmod 7$ y $8 \equiv 1 \pmod 7$:
$$1 + 3k \equiv 2 \pmod 7 \;\Longrightarrow\; 3k \equiv 1 \pmod 7$$

El inverso de $3$ módulo $7$ es $5$ (pues $3 \cdot 5 = 15 \equiv 1$), luego $k \equiv 5 \pmod 7$.

**Paso 3.** Con $k = 5 + 7m$:
$$x = 8 + 143(5 + 7m) = 723 + 1001m$$

La solución general es $x \equiv 723 \pmod{1001}$, con $1001 = 7 \cdot 11 \cdot 13$.

**Paso 4.** Buscamos el mayor valor menor que $3000$:
- $m = 2$: $x = 723 + 2002 = 2725$
- $m = 3$: $x = 3726 > 3000$

**Verificación** de $2725$:
- $2725 = 7 \cdot 389 + 2$ ✓
- $2725 = 11 \cdot 247 + 8$ ✓
- $2725 = 13 \cdot 209 + 8$ ✓

$$\boxed{2725}$$