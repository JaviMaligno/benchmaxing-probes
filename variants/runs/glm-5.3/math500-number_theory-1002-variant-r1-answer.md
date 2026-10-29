Vamos por pasos.

**Paso 1: Unificar las dos últimas condiciones.**
Como $x \equiv 8 \pmod{11}$ y $x \equiv 8 \pmod{13}$, y dado que $\gcd(11,13)=1$, se concluye que:
$$x \equiv 8 \pmod{143} \quad (11 \cdot 13 = 143)$$
Es decir, $x = 8 + 143k$ para algún entero $k$.

**Paso 2: Imponer la condición módulo 7.**
Como $143 \equiv 3 \pmod 7$ y $8 \equiv 1 \pmod 7$:
$$8 + 143k \equiv 1 + 3k \pmod 7$$
Queremos que esto sea $\equiv 2 \pmod 7$:
$$3k \equiv 1 \pmod 7$$
El inverso de $3$ módulo $7$ es $5$ (pues $3\cdot 5 = 15 \equiv 1$). Entonces:
$$k \equiv 5 \pmod 7 \quad \Rightarrow \quad k = 5 + 7m$$

**Paso 3: Solución general.**
$$x = 8 + 143(5 + 7m) = 8 + 715 + 1001m = 723 + 1001m$$
donde $1001 = 7 \cdot 11 \cdot 13$ es el módulo combinado. Las soluciones positivas son $723, 1724, 2725, 3726, \dots$

**Paso 4: Elegir la mayor menor que 3000.**
La mayor solución por debajo de $3000$ es $2725$ (la siguiente, $3726$, ya se pasa).

**Verificación de $2725$:**
- $2725 = 7 \cdot 389 + 2$ ✓ (resto $2$)
- $2725 = 11 \cdot 247 + 8$ ✓ (resto $8$)
- $2725 = 13 \cdot 209 + 8$ ✓ (resto $8$)

$\boxed{2725}$