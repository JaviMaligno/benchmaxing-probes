Primero resolvemos la congruencia:

$$14u \equiv 46 \pmod{100}$$

Simplificamos dividiendo por el máximo común divisor de $14$ y $46$, que es $2$, pero como el módulo es $100$, dividimos toda la congruencia por $2$:

$$7u \equiv 23 \pmod{50}$$

Ahora necesitamos el inverso de $7$ módulo $50$. Como $7 \cdot 43 = 301 = 50 \cdot 6 + 1$, entonces $7^{-1} \equiv 43 \pmod{50}$.

Multiplicamos ambos lados por $43$:

$$u \equiv 23 \cdot 43 \pmod{50}$$

Calculamos $23 \cdot 43 = 989$. Ahora reducimos módulo $50$:

$$989 = 50 \cdot 19 + 39$$

Así que:

$$u \equiv 39 \pmod{50}$$

Las soluciones módulo $100$ son:

$$u = 39 \quad \text{y} \quad u = 39 + 50 = 89$$

Los dos menores son $39$ y $89$.

Su promedio es:

$$\frac{39 + 89}{2} = \frac{128}{2} = 64$$

\boxed{64}