Para encontrar el promedio de las dos soluciones enteras positivas más pequeñas de la congruencia

$$22x \equiv 38 \pmod{100},$$

resolvemos paso a paso:

1. **Simplificar la congruencia:**
   Observamos que el máximo común divisor de $22$, $38$ y $100$ es $\text{mcd}(22, 100) = 2$. Dividimos toda la congruencia (incluido el módulo) entre $2$:
   $$11x \equiv 19 \pmod{50}$$

2. **Encontrar el inverso modular de $11$ módulo $50$:**
   Buscamos un entero $k$ tal que $11k \equiv 1 \pmod{50}$. Notamos que $11 \times 9 = 99 \equiv -1 \pmod{50}$, por lo que al multiplicar por $-9$ obtenemos:
   $$11 \times (-9) = -99 \equiv 1 \pmod{50}$$

3. **Despejar $x$:**
   Multiplicamos ambos lados de la congruencia $11x \equiv 19 \pmod{50}$ por $-9$:
   $$x \equiv 19 \times (-9) \pmod{50}$$
   $$x \equiv -171 \pmod{50}$$
   Como $-171 = -4 \times 50 + 29$, tenemos:
   $$x \equiv 29 \pmod{50}$$

4. **Hallar las dos soluciones enteras positivas más pequeñas:**
   Las soluciones enteras positivas son de la forma $x = 29 + 50k$ para $k \ge 0$:
   - Para $k = 0$: $x_1 = 29$
   - Para $k = 1$: $x_2 = 29 + 50 = 79$

5. **Calcular el promedio:**
   El promedio de $29$ y $79$ es:
   $$\frac{29 + 79}{2} = \frac{108}{2} = 54$$

\boxed{54}