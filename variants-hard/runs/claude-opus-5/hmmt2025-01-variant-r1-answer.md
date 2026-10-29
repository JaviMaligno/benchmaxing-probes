## Razonamiento

**Factorización:** $11! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7 \cdot 11$

**Restricción:** un divisor que termina en 3 es impar y no múltiplo de 5, así que no puede contener factores 2 ni 5. Por tanto debe ser divisor de $3^4 \cdot 7 \cdot 11$, es decir de la forma $3^a \cdot 7^b \cdot 11^c$ con $a \le 4$, $b,c \le 1$.

**Dígitos de las unidades:**
- $3^a$: $1, 3, 9, 7, 1$ para $a = 0,1,2,3,4$
- $7^b$: $1, 7$
- $11^c$: $1, 1$ (no afecta)

**Casos** (producto $\equiv 3 \pmod{10}$):
- $b=0$: necesito $3^a \equiv 3$ → $a = 1$
- $b=1$: necesito $3^a \cdot 7 \equiv 3$; como $7^{-1} \equiv 3 \pmod{10}$, queda $3^a \equiv 9$ → $a = 2$

**Divisores** (con $c=0$ o $c=1$):
- $3$, $3 \cdot 11 = 33$
- $3^2 \cdot 7 = 63$, $63 \cdot 11 = 693$

**Suma:** $3 + 33 + 63 + 693 = 792$

Verificación: todos terminan en 3 ✓

\boxed{792}