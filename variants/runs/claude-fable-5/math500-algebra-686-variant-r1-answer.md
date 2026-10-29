## Solución

**Planteamiento:** La serie tiene primer término $3$ y razón $r = \frac{5}{a}$ (ya que $\frac{15/a}{3} = \frac{5}{a}$). Para que converja se necesita $|r| < 1$, es decir, $a > 5$.

**Suma de la serie:**
$$S = \frac{3}{1 - \frac{5}{a}} = \frac{3a}{a-5}$$

**Cuándo es entera:** Escribiendo $3a = 3(a-5) + 15$, se tiene
$$S = 3 + \frac{15}{a-5}$$
así que $a - 5$ debe dividir a $15$. Los divisores de $15$ dan $a - 5 \in \{1, 3, 5, 15\}$, es decir $a \in \{6, 8, 10, 20\}$.

**Verificación de cada caso:**
- $a = 6$: $S = 3 + 15 = 18$ — no es cuadrado perfecto
- $a = 8$: $S = 3 + 5 = 8$ — no es cuadrado perfecto
- $a = 10$: $S = 3 + 3 = 6$ — no es cuadrado perfecto
- $a = 20$: $S = 3 + 1 = 4 = 2^2$ — ✓ cuadrado perfecto

El único valor que produce un cuadrado perfecto es $a = 20$.

$$\boxed{20}$$