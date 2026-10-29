**Paso 1: Reducir las bases módulo 11.**
- $117 = 11 \cdot 10 + 7$, así que $117 \equiv 7 \pmod{11}$.
- $194 = 11 \cdot 17 + 7$, así que $194 \equiv 7 \pmod{11}$.

**Paso 2: Usar el pequeño teorema de Fermat.** Como 11 es primo y $\gcd(7,11)=1$, se cumple $7^{10} \equiv 1 \pmod{11}$. Entonces reducimos los exponentes módulo 10:
- $7^{36} \equiv 7^{6} \pmod{11}$
- $7^{38} \equiv 7^{8} \pmod{11}$

**Paso 3: Calcular las potencias.**
- $7^2 = 49 \equiv 5 \pmod{11}$
- $7^4 \equiv 5^2 = 25 \equiv 3 \pmod{11}$
- $7^6 \equiv 7^4 \cdot 7^2 \equiv 3 \cdot 5 = 15 \equiv 4 \pmod{11}$
- $7^8 \equiv 7^6 \cdot 7^2 \equiv 4 \cdot 5 = 20 \equiv 9 \pmod{11}$

**Paso 4: Sumar.**
$$117^{36} + 194^{38} \equiv 4 + 9 = 13 \equiv 2 \pmod{11}$$

$$\boxed{2}$$