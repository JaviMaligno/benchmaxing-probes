Reduzco las bases módulo 11:

- $129 = 11 \cdot 11 + 8$, así que $129 \equiv 8 \pmod{11}$.
- $96 = 11 \cdot 8 + 8$, así que $96 \equiv 8 \pmod{11}$.

Entonces $129^{34} + 96^{38} \equiv 8^{34} + 8^{38} \pmod{11}$.

Por el pequeño teorema de Fermat, $8^{10} \equiv 1 \pmod{11}$, de modo que solo importan los exponentes módulo 10: $34 \equiv 4$ y $38 \equiv 8$.

Calculo las potencias:
- $8^2 = 64 \equiv 9 \pmod{11}$
- $8^4 \equiv 9^2 = 81 \equiv 4 \pmod{11}$
- $8^8 \equiv 4^2 = 16 \equiv 5 \pmod{11}$

Por lo tanto $8^{34} + 8^{38} \equiv 4 + 5 = 9 \pmod{11}$.

$$\boxed{9}$$