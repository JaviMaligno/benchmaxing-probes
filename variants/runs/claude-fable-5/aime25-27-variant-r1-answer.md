## Planteamiento

Sea $x_i = B_1B_i$ para $2 \le i \le 11$, y sea $\theta = \angle B_iB_1B_{i+1}$ con $\cos\theta = \tfrac45$, por lo que $\sin\theta = \tfrac35$.

**Condición de área:** $\tfrac12 x_i x_{i+1}\sin\theta = 1 \Rightarrow x_i x_{i+1} = \tfrac{10}{3}$ para todo $i$.

Como $x_i x_{i+1} = x_{i+1}x_{i+2} = \tfrac{10}{3}$, se tiene $x_{i+2} = x_i$. Así las longitudes alternan: $x_2 = x_4 = \cdots = a$ y $x_3 = x_5 = \cdots = x_{11} = b$, con $ab = \tfrac{10}{3}$.

**Lados del polígono:** por ley de cosenos, cada lado $B_iB_{i+1}$ (hay 9 de ellos, de $B_2B_3$ a $B_{10}B_{11}$) mide $s$ con
$$s^2 = a^2 + b^2 - 2ab\cos\theta = a^2+b^2 - 2\cdot\tfrac{10}{3}\cdot\tfrac45 = a^2+b^2-\tfrac{16}{3}.$$

**Perímetro:** $B_1B_2 + B_1B_{11} + 9s = a + b + 9s = 20$.

## Resolución

Sea $u = a+b$. Entonces
$$s^2 = u^2 - 2ab - \tfrac{16}{3} = u^2 - \tfrac{20}{3} - \tfrac{16}{3} = u^2 - 12.$$

De $9s = 20 - u$:
$$81(u^2-12) = (20-u)^2 = 400 - 40u + u^2$$
$$80u^2 + 40u - 1372 = 0 \quad\Longrightarrow\quad 20u^2 + 10u - 343 = 0.$$

Entonces
$$u = \frac{-10 + \sqrt{100 + 4\cdot 20\cdot 343}}{40} = \frac{-10+\sqrt{27540}}{40} = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85}-5}{20}.$$

**Verificación:** $u \approx 3.899$, $s^2 = u^2 - 12 \approx 3.2$, $9s \approx 16.1$, y $u + 9s \approx 20$ ✓. Además $u^2 - 4ab \approx 15.2 - 13.33 > 0$, así que $a, b$ existen como reales positivos distintos (consistente con la no convexidad).

Así $B_1B_2 + B_1B_{11} = \dfrac{9\sqrt{85}-5}{20}$, con $m=9$, $n=85$ (libre de cuadrados), $p=5$, $q=20$, sin primo común a $m, p, q$.

$$m+n+p+q = 9+85+5+20 = \boxed{119}$$