## Solución

Sea $x_i = B_1B_i$ para $i = 2, \dots, 11$, y sea $\theta = \angle B_i B_1 B_{i+1}$ con $\cos\theta = \tfrac45$, de modo que $\sin\theta = \tfrac35$ (el polígono es no convexo porque los triángulos se solapan, pero las relaciones métricas valen igual).

**Áreas.** Para cada $i$: $\tfrac12 x_i x_{i+1} \sin\theta = 1$, es decir $x_i x_{i+1} = \tfrac{10}{3}$. Como el producto de términos consecutivos es constante, $x_{i+2} = x_i$: los valores alternan entre $a = x_2 = x_4 = \cdots$ y $b = x_3 = x_5 = \cdots = x_{11}$, con $ab = \tfrac{10}{3}$. Buscamos $s = a + b = B_1B_2 + B_1B_{11}$.

**Lados.** Por ley de cosenos, para $2 \le i \le 10$:
$$B_iB_{i+1}^2 = x_i^2 + x_{i+1}^2 - 2\cdot\tfrac{10}{3}\cdot\tfrac45 = a^2 + b^2 - \tfrac{16}{3} = (a+b)^2 - \tfrac{20}{3} - \tfrac{16}{3} = s^2 - 12.$$

**Perímetro.** Hay 9 lados iguales $B_2B_3, \dots, B_{10}B_{11}$ más $B_1B_2 + B_{11}B_1 = s$:
$$s + 9\sqrt{s^2 - 12} = 20 \implies 81(s^2 - 12) = (20 - s)^2.$$

Esto da $80s^2 + 40s - 1372 = 0$, es decir $20s^2 + 10s - 343 = 0$:
$$s = \frac{-10 + \sqrt{100 + 27440}}{40} = \frac{-10 + \sqrt{27540}}{40} = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85} - 5}{20}.$$

**Verificación:** $s \approx 3.90$, luego $9\sqrt{s^2 - 12} \approx 9(1.79) \approx 16.1$ y $3.90 + 16.1 = 20$ ✓. Además $s^2 > \tfrac{40}{3}$, así que existen $a, b$ reales positivos con $ab = \tfrac{10}{3}$ ✓.

Con $m = 9$, $n = 85$ (libre de cuadrados), $p = 5$, $q = 20$ (ningún primo divide a los tres de $m, p, q$):
$$m + n + p + q = 9 + 85 + 5 + 20 = 119.$$

$$\boxed{119}$$