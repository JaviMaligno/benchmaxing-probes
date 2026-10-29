## Planteamiento

Buscamos minimizar $a^4 + 6b^2 + 9c^4$ con la restricción $abc = 3$.

**Reparto de términos para AM-GM.** Para que el producto geométrico dependa solo de $abc$, necesitamos que las potencias de $a$, $b$ y $c$ coincidan. Si usamos $x$ copias de $a^4$, $y$ copias de un múltiplo de $b^2$ y $z$ copias de $c^4$, hace falta $4x = 2y = 4z$; con $x = z = 1$ sale $y = 2$.

Así, dividimos $6b^2 = 3b^2 + 3b^2$ y aplicamos AM-GM a cuatro términos:

$$a^4 + 3b^2 + 3b^2 + 9c^4 \ge 4\sqrt[4]{a^4 \cdot 3b^2 \cdot 3b^2 \cdot 9c^4} = 4\sqrt[4]{81\,a^4b^4c^4}$$

Como $\sqrt[4]{81} = 3$:

$$a^4 + 6b^2 + 9c^4 \ge 4 \cdot 3 \cdot abc = 12 \cdot 3 = 36.$$

**Caso de igualdad.** Se requiere $a^4 = 3b^2 = 9c^4$. Tomando $a^4 = 9$ obtenemos $a = \sqrt{3}$, $b^2 = 3 \Rightarrow b = \sqrt{3}$, y $c^4 = 1 \Rightarrow c = 1$. Esto cumple la restricción: $abc = \sqrt{3}\cdot\sqrt{3}\cdot 1 = 3$ ✓

Verificación directa: $9 + 6(3) + 9(1) = 9 + 18 + 9 = 36$.

Como la cota se alcanza, el mínimo es efectivamente $36$.

$$\boxed{36}$$