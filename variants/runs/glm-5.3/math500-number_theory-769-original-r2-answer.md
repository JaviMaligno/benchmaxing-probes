Paso a paso:

1. **Reducir las bases módulo 11:**
   - $129 = 11 \cdot 11 + 8 \Rightarrow 129 \equiv 8 \pmod{11}$
   - $96 = 11 \cdot 8 + 8 \Rightarrow 96 \equiv 8 \pmod{11}$

   Entonces $129^{34} + 96^{38} \equiv 8^{34} + 8^{38} \pmod{11}$.

2. **Usar el pequeño teorema de Fermat** (gcd(8,11)=1): $8^{10} \equiv 1 \pmod{11}$.

   - $34 = 3\cdot 10 + 4 \Rightarrow 8^{34} \equiv 8^4 \pmod{11}$
   - $38 = 3\cdot 10 + 8 \Rightarrow 8^{38} \equiv 8^8 \pmod{11}$

3. **Calcular potencias:**
   - $8^2 = 64 \equiv 9 \pmod{11}$
   - $8^4 \equiv 9^2 = 81 \equiv 4 \pmod{11}$
   - $8^8 \equiv 4^2 = 16 \equiv 5 \pmod{11}$

4. **Sumar:** $4 + 5 = 9 \pmod{11}$.

\boxed{9}