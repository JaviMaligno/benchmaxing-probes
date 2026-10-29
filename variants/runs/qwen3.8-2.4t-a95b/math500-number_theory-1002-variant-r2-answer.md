Buscamos el mayor entero $n < 3000$ tal que:
- $n \equiv 2 \pmod{7}$
- $n \equiv 8 \pmod{11}$
- $n \equiv 8 \pmod{13}$

**Paso 1: Combinar las condiciones módulo 11 y 13**

Como $n \equiv 8 \pmod{11}$ y $n \equiv 8 \pmod{13}$, y $\gcd(11,13)=1$, tenemos:
$$n \equiv 8 \pmod{143}$$

**Paso 2: Aplicar la condición módulo 7**

Escribimos $n = 143k + 8$. Como $143 \equiv 3 \pmod{7}$ y $8 \equiv 1 \pmod{7}$:
$$n \equiv 3k + 1 \pmod{7}$$

Necesitamos $3k + 1 \equiv 2 \pmod{7}$, es decir, $3k \equiv 1 \pmod{7}$. El inverso de $3$ módulo $7$ es $5$ (pues $3 \times 5 = 15 \equiv 1$), así que:
$$k \equiv 5 \pmod{7}$$

**Paso 3: Solución general**

Con $k = 7m + 5$:
$$n = 143(7m+5) + 8 = 1001m + 723$$

**Paso 4: Encontrar el mayor menor que 3000**

$$1001m + 723 < 3000 \implies 1001m < 2277 \implies m \leq 2$$

Para $m = 2$: $n = 2002 + 723 = 2725$.

**Verificación:** $2725 = 7(389)+2$ ✓, $2725 = 11(247)+8$ ✓, $2725 = 13(209)+8$ ✓

$$\boxed{2725}$$