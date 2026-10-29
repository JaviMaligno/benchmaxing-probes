## Razonamiento

**Reducir las bases módulo 11:**
- $117 = 11 \cdot 10 + 7 \Rightarrow 117 \equiv 7 \pmod{11}$
- $194 = 11 \cdot 17 + 7 \Rightarrow 194 \equiv 7 \pmod{11}$

Entonces $117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$.

**Usar el pequeño teorema de Fermat:** $7^{10} \equiv 1 \pmod{11}$, así que los exponentes se reducen módulo 10:
- $36 \equiv 6 \pmod{10} \Rightarrow 7^{36} \equiv 7^6$
- $38 \equiv 8 \pmod{10} \Rightarrow 7^{38} \equiv 7^8$

**Calcular las potencias:**
- $7^2 = 49 \equiv 5$
- $7^3 \equiv 5 \cdot 7 = 35 \equiv 2$
- $7^5 \equiv 7^2 \cdot 7^3 \equiv 5 \cdot 2 = 10 \equiv -1$
- $7^6 \equiv -1 \cdot 7 = -7 \equiv 4$
- $7^8 \equiv 7^5 \cdot 7^3 \equiv (-1)(2) = -2 \equiv 9$

**Sumar:** $4 + 9 = 13 \equiv 2 \pmod{11}$

\boxed{2}