## Razonamiento

Sea $f(t) = t^2 - 4t + 6$. La condición exige que $f$ envíe el conjunto de raíces de la ecuación dentro de sí mismo. (Si solo consideráramos raíces reales, toda ecuación sin raíces reales cumpliría vacuamente la condición y habría infinitas; por eso se consideran todas las raíces, incluidas las complejas.)

**Caso 1: raíz doble $t$.** Entonces $f(t)$ debe ser raíz, es decir $f(t) = t$:
$$t^2 - 4t + 6 = t \iff t^2 - 5t + 6 = 0 \iff t = 2 \text{ o } t = 3.$$
Obtenemos $(x-2)^2 = x^2 - 4x + 4$ y $(x-3)^2 = x^2 - 6x + 9$. **(2 ecuaciones)**

**Caso 2: raíces distintas $a \neq b$.** Entonces $f(a), f(b) \in \{a, b\}$. Subcasos:

- **Ambas fijas:** $f(a)=a$, $f(b)=b$. Los puntos fijos son $2$ y $3$, así que $\{a,b\} = \{2,3\}$: la ecuación $x^2 - 5x + 6 = 0$. **(1 ecuación)**

- **Una fija, la otra mapea a la fija:** digamos $f(b)=b$ (con $b \in \{2,3\}$) y $f(a)=b$, $a \neq b$.
  - $b=2$: $a^2 - 4a + 6 = 2 \Rightarrow (a-2)^2 = 0 \Rightarrow a = 2$, contradicción.
  - $b=3$: $a^2 - 4a + 6 = 3 \Rightarrow a^2 - 4a + 3 = 0 \Rightarrow a = 1$ (descartando $a=3$).
  
  Verificación con raíces $\{1, 3\}$: $f(1) = 3$ ✓ y $f(3) = 3$ ✓. Ecuación $x^2 - 4x + 3 = 0$. **(1 ecuación)**

- **Intercambio:** $f(a) = b$, $f(b) = a$. Entonces $f(f(t)) = t$ para ambas raíces, sin ser puntos fijos. Calculando:
$$f(f(t)) - t = t^4 - 8t^3 + 24t^2 - 33t + 18 = (t^2 - 5t + 6)(t^2 - 3t + 3).$$
El factor $t^2 - 5t + 6$ da los puntos fijos (ya contados). El factor $t^2 - 3t + 3 = 0$ da raíces complejas $a = \frac{3 + i\sqrt{3}}{2}$, $b = \frac{3 - i\sqrt{3}}{2}$. Como $a^2 = 3a - 3$, se tiene $f(a) = 3a - 3 - 4a + 6 = 3 - a = b$ ✓ (y simétricamente $f(b) = a$). Ecuación $x^2 - 3x + 3 = 0$. **(1 ecuación)**

**Total:** $x^2-4x+4$, $x^2-6x+9$, $x^2-5x+6$, $x^2-4x+3$ y $x^2-3x+3$.

$$\boxed{5}$$