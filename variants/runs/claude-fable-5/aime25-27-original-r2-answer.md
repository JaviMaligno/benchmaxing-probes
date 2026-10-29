**Respuesta: 19**

Razonamiento:

Sea $x_i = A_1A_i$ para $2 \le i \le 11$. Como $\cos\theta = \frac{12}{13}$, entonces $\sin\theta = \frac{5}{13}$ (el polígono es no convexo precisamente porque el ángulo se repite 9 veces, sumando más de $2\pi$ si fuera convexo, lo cual es consistente).

**Condición de área:** $\frac{1}{2} x_i x_{i+1} \cdot \frac{5}{13} = 1 \Rightarrow x_i x_{i+1} = \frac{26}{5}$ para todo $i$.

Esto fuerza que los valores alternen: $x_2 = x_4 = \cdots = a$ y $x_3 = x_5 = \cdots = x_{11} = b$, con $ab = \frac{26}{5}$.

**Lados del polígono:** Por la ley de cosenos, para $2 \le i \le 10$:
$$A_iA_{i+1}^2 = x_i^2 + x_{i+1}^2 - 2x_ix_{i+1}\cdot\tfrac{12}{13} = a^2 + b^2 - \tfrac{48}{5} = (a+b)^2 - \tfrac{52}{5} - \tfrac{48}{5} = (a+b)^2 - 20.$$

**Perímetro:** Con $s = a+b$:
$$a + b + 9\sqrt{s^2 - 20} = 20 \Rightarrow 9\sqrt{s^2-20} = 20 - s.$$

Elevando al cuadrado: $81s^2 - 1620 = 400 - 40s + s^2$, es decir $80s^2 + 40s - 2020 = 0$, o bien $4s^2 + 2s - 101 = 0$:
$$s = \frac{-2 + \sqrt{4 + 1616}}{8} = \frac{-2 + 18\sqrt{5}}{8} = \frac{9\sqrt{5} - 1}{4}.$$

Entonces $A_1A_2 + A_1A_{11} = a + b = \frac{9\sqrt{5}-1}{4}$, con $m=9$, $n=5$, $p=1$, $q=4$ (ningún primo divide a 9, 1 y 4 a la vez).

$$m+n+p+q = 9+5+1+4 = \boxed{19}$$