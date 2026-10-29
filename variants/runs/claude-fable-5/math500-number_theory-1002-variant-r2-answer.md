Resolvemos el sistema de congruencias:

- $x \equiv 2 \pmod{7}$
- $x \equiv 8 \pmod{11}$
- $x \equiv 8 \pmod{13}$

**Paso 1:** Como $x \equiv 8$ tanto módulo 11 como módulo 13, y $\text{mcd}(11,13)=1$, se cumple $x \equiv 8 \pmod{143}$ (ya que $11 \cdot 13 = 143$). Entonces $x = 8 + 143k$.

**Paso 2:** Imponemos la condición módulo 7. Como $143 \equiv 3 \pmod{7}$ y $8 \equiv 1 \pmod{7}$:

$$1 + 3k \equiv 2 \pmod{7} \implies 3k \equiv 1 \pmod{7}$$

El inverso de 3 módulo 7 es 5 (pues $3 \cdot 5 = 15 \equiv 1$), así que $k \equiv 5 \pmod{7}$.

**Paso 3:** Con $k = 5$: $x = 8 + 143 \cdot 5 = 723$. La solución general es $x \equiv 723 \pmod{1001}$ (donde $1001 = 7 \cdot 11 \cdot 13$).

**Paso 4:** Los valores son $723, 1724, 2725, 3726, \dots$ El mayor por debajo de 3000 es 2725.

**Verificación:** $2725 = 7 \cdot 389 + 2$ ✓, $2725 = 11 \cdot 247 + 8$ ✓, $2725 = 13 \cdot 209 + 8$ ✓.

$$\boxed{2725}$$