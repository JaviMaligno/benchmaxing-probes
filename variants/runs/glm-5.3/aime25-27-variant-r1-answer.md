# Planteamiento

Como todos los triángulos comparten el vértice $B_1$, mido las distancias desde $B_1$: sea $r_j = B_1B_j$.

**Paso 1: Las distancias alternan.**

De $\cos(\angle B_iB_1B_{i+1}) = \frac45$ se sigue $\sin = \frac35$, y el área $1$ da
$$\tfrac12 r_i r_{i+1}\cdot \tfrac35 = 1 \implies r_i r_{i+1} = \tfrac{10}{3} \quad (2\le i\le 10).$$

Entonces $r_2r_3 = r_3r_4 \Rightarrow r_2 = r_4$, etc., así que
$$r_2=r_4=r_6=r_8=r_{10} = a, \qquad r_3=r_5=r_7=r_9=r_{11} = b, \qquad ab = \tfrac{10}{3}.$$

**Paso 2: Los nueve lados intermedios son iguales.**

Por el teorema del coseno, cada lado $B_iB_{i+1}$ ($2\le i\le 10$) vale
$$c = \sqrt{a^2+b^2 - 2ab\cdot\tfrac45}.$$
Con $s = a+b$ y $ab = \frac{10}{3}$:
$$c^2 = s^2 - 2ab - \tfrac85 ab = s^2 - \tfrac{10}{3}\cdot\tfrac{18}{5} = s^2 - 12.$$

*(Nota: la condición de polígono simple y no convexo garantiza que tal configuración existe — una "espiral" de $9$ pasos de ángulo $\alpha=\arccos\frac45\approx 36.87°$ que gira $\approx 331.8°<360°$ alrededor de $B_1$, haciendo a $B_1$ un vértice reentrante — pero no afecta las longitudes.)*

**Paso 3: Usar el perímetro.**

El perímetro es $a + 9c + b = 20$, es decir:
$$s + 9\sqrt{s^2 - 12} = 20 \implies \sqrt{s^2-12} = \tfrac{20-s}{9}.$$

Elevando al cuadrado:
$$81(s^2 - 12) = (20-s)^2 \implies 80s^2 + 40s - 1372 = 0 \implies 20s^2 + 10s - 343 = 0.$$

**Paso 4: Resolver.**

$$s = \frac{-10 + \sqrt{100 + 27440}}{40} = \frac{-10 + \sqrt{27540}}{40} = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85}-5}{20}.$$

(Tomando la raíz positiva; se verifican las condiciones $20-s>0$ y $s^2\ge 12$.)

**Verificación numérica:** $s \approx 3.8988$, $c = \sqrt{s^2-12} \approx 1.789$, perímetro $\approx 3.8988 + 9(1.789) = 20$ ✓. Además $\{a,b\}$ son reales positivos ($ab = \frac{10}{3}$, discriminante $s^2 - \frac{40}{3} > 0$) ✓.

**Paso 5: Concluir.**

$$B_1B_2 + B_1B_{11} = \frac{m\sqrt{n}-p}{q} = \frac{9\sqrt{85} - 5}{20}$$

con $m=9$, $n=85$ (libre de cuadrados, $85=5\cdot 17$), $p=5$, $q=20$; ningún primo divide a los tres.

$$m+n+p+q = 9+85+5+20 = \boxed{119}$$