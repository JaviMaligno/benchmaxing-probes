## Solución

Sea $x_i = A_1 A_i$ para $2 \le i \le 11$, y sea $\theta = \angle A_i A_1 A_{i+1}$ con $\cos\theta = \tfrac{12}{13}$, de donde $\sin\theta = \tfrac{5}{13}$.

**Condición de área.** Para cada $i$:
$$[\triangle A_i A_1 A_{i+1}] = \tfrac{1}{2} x_i x_{i+1} \sin\theta = 1 \implies x_i x_{i+1} = \frac{26}{5}.$$

Como $x_i x_{i+1}$ es constante, los valores alternan: $x_2 = x_4 = \cdots = a$ y $x_3 = x_5 = \cdots = x_{11} = b$, con $ab = \tfrac{26}{5}$.

**Lados del polígono.** Por ley de cosenos, para $2 \le i \le 10$:
$$A_i A_{i+1}^2 = x_i^2 + x_{i+1}^2 - 2x_i x_{i+1}\cdot\frac{12}{13} = a^2 + b^2 - 2\cdot\frac{26}{5}\cdot\frac{12}{13} = a^2+b^2-\frac{48}{5}.$$

Los $9$ lados $A_2A_3, \ldots, A_{10}A_{11}$ tienen todos la misma longitud $s = \sqrt{a^2+b^2-\tfrac{48}{5}}$.

**Perímetro.** Con $t = a+b$ (que es lo que buscamos, pues $A_1A_2 + A_1A_{11} = a+b$):
$$s^2 = (a+b)^2 - 2ab - \frac{48}{5} = t^2 - \frac{52}{5} - \frac{48}{5} = t^2 - 20.$$

El perímetro da $t + 9\sqrt{t^2-20} = 20$, es decir $9\sqrt{t^2-20} = 20 - t$. Elevando al cuadrado:
$$81(t^2-20) = 400 - 40t + t^2 \implies 80t^2 + 40t - 2020 = 0 \implies 4t^2 + 2t - 101 = 0.$$

Entonces:
$$t = \frac{-2 + \sqrt{4 + 1616}}{8} = \frac{-2 + \sqrt{1620}}{8} = \frac{-2 + 18\sqrt{5}}{8} = \frac{9\sqrt{5} - 1}{4}.$$

(La no convexidad del polígono es consistente con esta raíz: $t < 20$ garantiza $20 - t > 0$.)

Así $m = 9$, $n = 5$, $p = 1$, $q = 4$, y:
$$m+n+p+q = 9+5+1+4 = 19.$$

$$\boxed{19}$$