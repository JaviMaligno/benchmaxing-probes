Para encontrar el promedio de las dos soluciones enteras positivas más pequeñas de la congruencia:

$$14u \equiv 46 \pmod{100}$$

**Paso 1: Simplificar la congruencia**
Observamos que el máximo común divisor de $14$ y $100$ es $\text{mcd}(14, 100) = 2$, el cual también divide a $46$. Dividimos toda la congruencia (incluido el módulo) entre $2$:

$$7u \equiv 23 \pmod{50}$$

**Paso 2: Despejar $u$ usando el inverso modular**
Buscamos el inverso multiplicativo de $7$ módulo $50$. Notamos que:
$$7 \times 7 = 49 \equiv -1 \pmod{50}$$

Por lo tanto, el inverso de $7$ módulo $50$ es $-7$ (o equivalentemente $43$). Multiplicamos ambos lados de la congruencia por $-7$:

$$(-7)(7u) \equiv (-7)(23) \pmod{50}$$
$$-49u \equiv -161 \pmod{50}$$

Como $-49 \equiv 1 \pmod{50}$ y $-161 = -4(50) + 39 \equiv 39 \pmod{50}$, obtenemos:

$$u \equiv 39 \pmod{50}$$

**Paso 3: Encontrar las dos soluciones enteras positivas más pequeñas**
Las soluciones enteras positivas son de la forma $u = 39 + 50k$ para $k \in \{0, 1, 2, \dots\}$.
- Para $k = 0$: $u_1 = 39$
- Para $k = 1$: $u_2 = 39 + 50 = 89$

**Paso 4: Calcular el promedio**
El promedio de las dos soluciones más pequeñas es:

$$\frac{39 + 89}{2} = \frac{128}{2} = 64$$

\boxed{64}