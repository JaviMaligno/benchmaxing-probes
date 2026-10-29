## Planteamiento

Sea $a_i = B_1B_i$. Con $\cos\theta = \tfrac45$ se tiene $\sin\theta = \tfrac35$, y el área de cada triángulo da

$$\tfrac12 a_i a_{i+1}\cdot \tfrac35 = 1 \quad\Longrightarrow\quad a_i a_{i+1} = \tfrac{10}{3}, \qquad 2\le i\le 10.$$

Como todos los productos consecutivos son iguales, $a_2 = a_4 = \cdots = a_{10} = x$ y $a_3 = a_5 = \cdots = a_{11} = y$, con

$$xy = \frac{10}{3}.$$

(Esta alternancia de radios es justamente lo que produce el polígono no convexo.)

## Lados del polígono

Los nueve lados $B_iB_{i+1}$ ($2\le i\le 10$) son todos iguales por la ley de cosenos:

$$B_iB_{i+1} = \sqrt{x^2+y^2 - 2xy\cdot\tfrac45} = \sqrt{x^2+y^2-\tfrac{16}{3}}.$$

Los dos lados restantes son $B_1B_2 = x$ y $B_1B_{11} = y$. Sea $s = x+y$; entonces $x^2+y^2 = s^2 - \tfrac{20}{3}$ y

$$x^2+y^2-\tfrac{16}{3} = s^2 - 12.$$

## Ecuación del perímetro

$$s + 9\sqrt{s^2-12} = 20 \quad\Longrightarrow\quad 81(s^2-12) = (20-s)^2$$

$$80s^2 + 40s - 1772 + 0 = 0 \;\Rightarrow\; 20s^2 + 10s - 343 = 0.$$

$$s = \frac{-10+\sqrt{100 + 27440}}{40} = \frac{-10+\sqrt{27540}}{40} = \frac{18\sqrt{85}-10}{40} = \frac{9\sqrt{85}-5}{20}.$$

Verificación: $s \approx 3.8988$, $\sqrt{s^2-12}\approx 1.7890$, y $3.8988 + 9(1.7890) \approx 20$. ✓ Además $s^2 - 4xy \approx 1.87 > 0$, así que $x,y$ son reales y positivos.

Con $m=9$, $n=85$, $p=5$, $q=20$ (con $85$ libre de cuadrados y $\gcd(9,5,20)=1$):

$$m+n+p+q = 9+85+5+20 = 119.$$

\boxed{119}