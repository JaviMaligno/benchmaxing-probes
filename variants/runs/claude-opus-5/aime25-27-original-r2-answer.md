## Solución

**Lados desde $A_1$.** Sea $r_i = A_1A_i$. Como $\cos\theta = \tfrac{12}{13}$, entonces $\sin\theta = \tfrac{5}{13}$, y de $[\triangle A_iA_1A_{i+1}] = 1$:

$$\tfrac12 r_i r_{i+1}\cdot \tfrac{5}{13} = 1 \implies r_i r_{i+1} = \tfrac{26}{5}, \quad 2\le i\le 10.$$

El producto es constante, así que los $r_i$ alternan: $r_2=r_4=\cdots=r_{10}=a$ y $r_3=r_5=\cdots=r_{11}=b$, con $ab=\tfrac{26}{5}$.

**Lados $A_iA_{i+1}$.** Por la ley de cosenos, todos los nueve lados $A_2A_3,\dots,A_{10}A_{11}$ miden lo mismo:

$$\ell^2 = a^2+b^2-2ab\cdot\tfrac{12}{13} = a^2+b^2-\tfrac{48}{5}.$$

Con $s=a+b$ se tiene $a^2+b^2 = s^2 - \tfrac{52}{5}$, luego

$$\ell^2 = s^2 - \tfrac{52}{5}-\tfrac{48}{5} = s^2-20.$$

**Perímetro.** Los lados son los nueve iguales más $A_1A_2+A_1A_{11}=a+b=s$:

$$9\sqrt{s^2-20} + s = 20 \implies 81(s^2-20) = (20-s)^2.$$

$$81s^2-1620 = s^2-40s+400 \implies 80s^2+40s-2020=0 \implies 4s^2+2s-101=0.$$

$$s = \frac{-2+\sqrt{4+1616}}{8} = \frac{-2+18\sqrt5}{8} = \frac{9\sqrt5-1}{4}.$$

(Se verifica $s<20$, consistente con la ecuación original.)

Así $m=9$, $n=5$, $p=1$, $q=4$, y $m+n+p+q = 19$.

\boxed{19}