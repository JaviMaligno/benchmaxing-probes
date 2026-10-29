Reduzco las bases módulo 11:

- $117 = 11 \cdot 10 + 7$, así que $117 \equiv 7 \pmod{11}$.
- $194 = 11 \cdot 17 + 7$, así que $194 \equiv 7 \pmod{11}$.

Por lo tanto, $117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$.

Por el pequeño teorema de Fermat, $7^{10} \equiv 1 \pmod{11}$. Entonces:

- $7^{36} = 7^{30} \cdot 7^6 \equiv 7^6 \pmod{11}$
- $7^{38} = 7^{30} \cdot 7^8 \equiv 7^8 \pmod{11}$

Calculo potencias de 7 módulo 11:

- $7^2 = 49 \equiv 5$
- $7^3 \equiv 5 \cdot 7 = 35 \equiv 2$
- $7^5 \equiv 7^2 \cdot 7^3 \equiv 5 \cdot 2 = 10 \equiv -1$
- $7^6 \equiv 7^5 \cdot 7 \equiv -7 \equiv 4$
- $7^8 \equiv 7^5 \cdot 7^3 \equiv -2 \equiv 9$

Sumando: $7^{36} + 7^{38} \equiv 4 + 9 = 13 \equiv 2 \pmod{11}$.

$$\boxed{2}$$