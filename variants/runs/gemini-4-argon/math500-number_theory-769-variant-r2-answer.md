Para hallar el residuo cuando $117^{36}+194^{38}$ se divide entre $11$, utilizamos aritmética modular paso a paso:

1. **Reducimos las bases módulo $11$:**
   - $117 = 11 \times 10 + 7 \implies 117 \equiv 7 \pmod{11}$
   - $194 = 11 \times 17 + 7 = 187 + 7 \implies 194 \equiv 7 \pmod{11}$

   Por lo tanto, la expresión es congruente a:
   $$117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$$

2. **Aplicamos el pequeño teorema de Fermat:**
   Como $11$ es primo y $\text{mcd}(7, 11) = 1$, sabemos que $7^{10} \equiv 1 \pmod{11}$. Reducimos los exponentes módulo $10$:
   - $7^{36} = (7^{10})^3 \cdot 7^6 \equiv 1^3 \cdot 7^6 = 7^6 \pmod{11}$
   - $7^{38} = (7^{10})^3 \cdot 7^8 \equiv 1^3 \cdot 7^8 = 7^8 \pmod{11}$

3. **Calculamos las potencias restantes módulo $11$:**
   - $7^2 = 49 = 11 \times 4 + 5 \equiv 5 \pmod{11}$
   - $7^6 = (7^2)^3 \equiv 5^3 = 125 = 11 \times 11 + 4 \equiv 4 \pmod{11}$
   - $7^8 = 7^6 \cdot 7^2 \equiv 4 \times 5 = 20 = 11 \times 1 + 9 \equiv 9 \pmod{11}$

4. **Sumamos los resultados:**
   $$7^6 + 7^8 \equiv 4 + 9 = 13 \equiv 2 \pmod{11}$$

\boxed{2}