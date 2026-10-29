Para resolver la congruencia lineal:
$$22x \equiv 38 \pmod{100}$$

**Paso 1: Simplificar la congruencia**
Calculamos el máximo común divisor de $22$ y $100$, que es $\gcd(22, 100) = 2$. Como $2$ divide a $38$, podemos dividir toda la congruencia (incluido el módulo) entre $2$:
$$11x \equiv 19 \pmod{50}$$

**Paso 2: Encontrar el inverso multiplicativo de $11$ módulo $50$**
Buscamos un número que multiplicado por $11$ sea congruente con $1 \pmod{50}$. Observamos que:
$$11 \times 9 = 99 \equiv -1 \pmod{50}$$
Por lo tanto, multiplicando ambos lados de la congruencia por $-9$:
$$-99x \equiv -171 \pmod{50}$$
$$x \equiv -171 \pmod{50}$$

**Paso 3: Reducir el resultado módulo $50$**
Sumamos múltiplos de $50$ a $-171$ para obtener el menor residuo positivo:
$$-171 + 4 \times 50 = -171 + 200 = 29$$
Así que la solución general es:
$$x \equiv 29 \pmod{50}$$

**Paso 4: Hallar las dos soluciones enteras positivas más pequeñas y su promedio**
Las soluciones positivas tienen la forma $x = 29 + 50k$ para $k \ge 0$:
- Para $k = 0$: $x_1 = 29$
- Para $k = 1$: $x_2 = 29 + 50 = 79$

El promedio de estas dos soluciones es:
$$\frac{29 + 79}{2} = \frac{108}{2} = 54$$

\boxed{54}