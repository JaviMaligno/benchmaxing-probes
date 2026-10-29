## Solución

Queremos minimizar $a^4 + 6b^2 + 9c^4$ con la restricción $abc = 3$.

**Estrategia:** dividir la expresión en cuatro términos para aplicar la desigualdad AM-GM de modo que el producto genere potencias iguales de $a$, $b$ y $c$:

$$a^4 + 6b^2 + 9c^4 = a^4 + 3b^2 + 3b^2 + 9c^4.$$

Por AM-GM con cuatro términos:

$$a^4 + 3b^2 + 3b^2 + 9c^4 \ge 4\sqrt[4]{a^4 \cdot 3b^2 \cdot 3b^2 \cdot 9c^4} = 4\sqrt[4]{81\, a^4 b^4 c^4} = 4 \cdot 3\, abc = 12 \cdot 3 = 36.$$

**Verificación de la igualdad:** se necesita $a^4 = 3b^2 = 9c^4$. Tomando $a = \sqrt{3}$, $b = \sqrt{3}$, $c = 1$:
- $abc = \sqrt{3} \cdot \sqrt{3} \cdot 1 = 3$ ✓
- $a^4 + 6b^2 + 9c^4 = 9 + 18 + 9 = 36$ ✓

Por lo tanto, el valor mínimo es

$$\boxed{36}$$