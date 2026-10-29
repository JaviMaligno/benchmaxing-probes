Para resolver la congruencia

$$14u \equiv 46 \pmod{100}$$

podemos seguir los siguientes pasos:

1. **Simplificar la congruencia:**
   Observamos que $14$, $46$ y el módulo $100$ son todos divisibles entre $\text{mcd}(14, 100) = 2$. Dividiendo toda la congruencia (incluido el módulo) entre $2$, obtenemos una congruencia equivalente:
   $$7u \equiv 23 \pmod{50}$$

2. **Despejar $u$ usando el inverso modular:**
   Buscamos el inverso multiplicativo de $7$ módulo $50$. Notamos que:
   $$7 \times 7 = 49 \equiv -1 \pmod{50}$$
   Por lo tanto, el inverso de $7$ módulo $50$ es $-7 \equiv 43 \pmod{50}$ (o simplemente podemos multiplicar ambos lados por $7$ y cambiar el signo). Multiplicando ambos lados de la congruencia por $7$:
   $$49u \equiv 7 \times 23 \pmod{50}$$
   $$-u \equiv 161 \pmod{50}$$

   Como $161 = 3 \times 50 + 11$, tenemos que $161 \equiv 11 \pmod{50}$:
   $$-u \equiv 11 \pmod{50}$$
   Multiplicando por $-1$:
   $$u \equiv -11 \equiv 39 \pmod{50}$$

3. **Encontrar las dos soluciones enteras positivas más pequeñas:**
   Las soluciones generales tienen la forma $u = 39 + 50k$, donde $k$ es un número entero. Para obtener las dos soluciones enteras positivas más pequeñas, tomamos $k = 0$ y $k = 1$:
   - Para $k = 0$: $u_1 = 39$
   - Para $k = 1$: $u_2 = 39 + 50 = 89$

4. **Calcular el promedio:**
   El promedio de estas dos soluciones es:
   $$\frac{39 + 89}{2} = \frac{128}{2} = 64$$

\boxed{64}