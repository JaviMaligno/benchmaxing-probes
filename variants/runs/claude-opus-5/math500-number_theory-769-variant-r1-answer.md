## Reducción módulo 11

**Paso 1: Reducir las bases.**
- $117 = 11\cdot 10 + 7 \Rightarrow 117 \equiv 7 \pmod{11}$
- $194 = 11\cdot 17 + 7 \Rightarrow 194 \equiv 7 \pmod{11}$

Entonces $117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$.

**Paso 2: Potencias de 7 módulo 11.**

Como $7^5 \equiv -1$:
- $7^2 = 49 \equiv 5$
- $7^3 \equiv 35 \equiv 2$
- $7^5 \equiv 7^2\cdot 7^3 \equiv 5\cdot 2 = 10 \equiv -1$

Por el pequeño teorema de Fermat, $7^{10} \equiv 1 \pmod{11}$, así que el orden es 10.

**Paso 3: Reducir los exponentes módulo 10.**
- $36 \equiv 6 \Rightarrow 7^{36} \equiv 7^6 \equiv 7^5\cdot 7 \equiv -7 \equiv 4$
- $38 \equiv 8 \Rightarrow 7^{38} \equiv 7^8 \equiv 7^5\cdot 7^3 \equiv -2 \equiv 9$

**Paso 4: Sumar.**
$$4 + 9 = 13 \equiv 2 \pmod{11}$$

\boxed{2}