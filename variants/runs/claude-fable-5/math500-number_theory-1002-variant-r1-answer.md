Resolvemos el sistema de congruencias:

- $x \equiv 2 \pmod{7}$
- $x \equiv 8 \pmod{11}$
- $x \equiv 8 \pmod{13}$

**Paso 1:** Como $x \equiv 8$ tanto módulo 11 como módulo 13, se cumple $x \equiv 8 \pmod{143}$ (ya que $11 \cdot 13 = 143$). Entonces $x = 143k + 8$.

**Paso 2:** Imponemos la condición módulo 7. Como $143 \equiv 3 \pmod 7$ y $8 \equiv 1 \pmod 7$:

$$3k + 1 \equiv 2 \pmod 7 \implies 3k \equiv 1 \pmod 7 \implies k \equiv 5 \pmod 7$$

(porque $3 \cdot 5 = 15 \equiv 1 \pmod 7$).

**Paso 3:** Con $k = 7m + 5$:

$$x = 143(7m + 5) + 8 = 1001m + 723$$

**Paso 4:** Buscamos el mayor valor menor que 3000. Con $m = 2$: $x = 2002 + 723 = 2725$. Con $m = 3$ ya daría $3726 > 3000$.

**Verificación:** $2725 = 7 \cdot 389 + 2$ ✓, $2725 = 11 \cdot 247 + 8$ ✓, $2725 = 13 \cdot 209 + 8$ ✓.

$$\boxed{2725}$$