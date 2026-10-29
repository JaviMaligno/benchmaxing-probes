Trabajamos módulo $11$.

**Paso 1: Reducimos las bases.**
$$117 = 11\cdot 10 + 7 \;\Rightarrow\; 117 \equiv 7 \pmod{11}$$
$$194 = 11\cdot 17 + 7 \;\Rightarrow\; 194 \equiv 7 \pmod{11}$$

**Paso 2: La expresión queda en términos de potencias de 7.**
$$7^{36} + 7^{38} = 7^{36}\left(1 + 7^2\right) = 7^{36}\cdot 50 \equiv 6\cdot 7^{36} \pmod{11}$$
pues $50 = 44 + 6 \equiv 6 \pmod{11}$.

**Paso 3: Simplificamos el exponente con el pequeño teorema de Fermat.**
Como $\gcd(7,11)=1$ y $11$ es primo, $7^{10} \equiv 1 \pmod{11}$. Entonces:
$$7^{36} = 7^{3\cdot 10 + 6} \equiv 7^{6} \pmod{11}$$

**Paso 4: Calculamos $7^6 \pmod{11}$.**
Observamos que $7^5 = 7^4\cdot 7$, con $7^2 = 49 \equiv 5$ y $7^4 \equiv 5^2 = 25 \equiv 3 \pmod{11}$, así que:
$$7^5 \equiv 3\cdot 7 = 21 \equiv -1 \pmod{11}$$
$$7^6 \equiv -1\cdot 7 = -7 \equiv 4 \pmod{11}$$

**Paso 5: Combinamos todo.**
$$6 \cdot 7^{36} \equiv 6\cdot 4 = 24 \equiv 2 \pmod{11}$$

Verificación: $7^{38} = 7^{36}\cdot 49 \equiv 4\cdot 5 = 20 \equiv 9$, y $4 + 9 = 13 \equiv 2 \pmod{11}$. ✓

$$\boxed{2}$$