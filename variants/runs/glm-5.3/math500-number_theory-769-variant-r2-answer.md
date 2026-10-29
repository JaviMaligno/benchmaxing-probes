# Solución paso a paso

**Paso 1: Reducir las bases módulo 11.**

- $117 = 11 \cdot 10 + 7$, así que $117 \equiv 7 \pmod{11}$.
- $194 = 11 \cdot 17 + 7$, así que $194 \equiv 7 \pmod{11}$.

Por lo tanto:
$$117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$$

**Paso 2: Aplicar el pequeño teorema de Fermat.**

Como $\gcd(7, 11) = 1$ y $11$ es primo, tenemos $7^{10} \equiv 1 \pmod{11}$. Entonces solo importan los exponentes módulo 10:

- $36 = 10 \cdot 3 + 6$, así que $7^{36} \equiv 7^{6} \pmod{11}$.
- $38 = 10 \cdot 3 + 8$, así que $7^{38} \equiv 7^{8} \pmod{11}$.

**Paso 3: Calcular las potencias.**

- $7^2 = 49 \equiv 5 \pmod{11}$
- $7^4 \equiv 5^2 = 25 \equiv 3 \pmod{11}$
- $7^6 = 7^4 \cdot 7^2 \equiv 3 \cdot 5 = 15 \equiv 4 \pmod{11}$
- $7^8 = 7^4 \cdot 7^4 \equiv 3 \cdot 3 = 9 \pmod{11}$

**Paso 4: Sumar.**

$$7^{36} + 7^{38} \equiv 4 + 9 = 13 \equiv 2 \pmod{11}$$

**Verificación:** $7^{36}+7^{38} = 7^{36}(1 + 7^2) = 7^{36} \cdot 50 \equiv 7^6 \cdot 6 \equiv 4 \cdot 6 = 24 \equiv 2 \pmod{11}$ ✓

El residuo es $\boxed{2}$.