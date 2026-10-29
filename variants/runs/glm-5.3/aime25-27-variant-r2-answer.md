## Razonamiento

**1. Radios desde $B_1$.** Sea $r_j = B_1B_j$ para $2 \le j \le 11$. En cada triángulo $B_iB_1B_{i+1}$ el ángulo en $B_1$ cumple $\cos\theta = \frac45$, luego $\sin\theta = \frac35$. El área es
$$\tfrac12 r_i r_{i+1}\sin\theta = \tfrac{3}{10}r_ir_{i+1} = 1 \implies r_ir_{i+1} = \tfrac{10}{3}\quad (2\le i\le 10).$$

**2. Los radios alternan.** De $r_ir_{i+1}=r_{i+1}r_{i+2}$ se sigue $r_{i+2}=r_i$. Así, para $2\le j\le 11$ los índices pares tienen $r_j = a$ y los impares $r_j = b$, con $ab = \frac{10}{3}$.

**3. Los 9 lados intermedios son iguales.** Por ley de cosenos, para cada $i$:
$$B_iB_{i+1} = \sqrt{a^2+b^2-2ab\cos\theta} = \sqrt{a^2+b^2-\tfrac{16}{3}} =: s.$$

**4. Ecuación del perímetro.** El perímetro es $r_2 + 9s + r_{11} = (a+b) + 9s = 20$. Sea $u = a+b$; entonces $a^2+b^2 = u^2 - \frac{20}{3}$, de modo que
$$s = \sqrt{u^2 - \tfrac{20}{3} - \tfrac{16}{3}} = \sqrt{u^2 - 12},\qquad u + 9\sqrt{u^2-12} = 20.$$

**5. Resolver.** Elevando al cuadrado: $81(u^2-12) = (20-u)^2$, es decir,
$$80u^2 + 40u - 1372 = 0 \implies 20u^2 + 10u - 343 = 0.$$
$$u = \frac{-10 + \sqrt{100 + 27440}}{40} = \frac{-10 + \sqrt{27540}}{40} = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85}-5}{20}.$$
(Comprobación: $u \approx 3.899$, y $\sqrt{u^2-12}\approx 1.789$, con $3.899 + 9\cdot 1.789 = 20$ ✓; además $u^2 \ge 4ab = \frac{40}{3}$, así que existen $a,b>0$ reales y el abanico de $9\cdot 36.87^\circ < 360^\circ$ alrededor de $B_1$ produce un polígono simple no convexo.)

**6. Conclusión.** $B_1B_2 + B_1B_{11} = r_2 + r_{11} = a + b = u = \frac{m\sqrt{n}-p}{q}$ con $m=9$, $n=85$ ($=5\cdot 17$, libre de cuadrados), $p=5$, $q=20$ (ningún primo divide a $9,5,20$).

Por lo tanto $m+n+p+q = 9+85+5+20$:

$$\boxed{119}$$