## Planteamiento

Sea $a_i = A_1A_i$ y $\theta = \angle A_iA_1A_{i+1}$, con $\cos\theta = \tfrac{12}{13}$, $\sin\theta = \tfrac{5}{13}$.

**Producto de radios.** Del área:
$$\tfrac12 a_i a_{i+1}\cdot \tfrac{5}{13} = 1 \implies a_i a_{i+1} = \tfrac{26}{5}\quad (2\le i\le 10).$$

Como todos los productos consecutivos son iguales, $a_i = a_{i+2}$, así que solo hay dos valores:
$$a_2=a_4=\cdots=a_{10}=x,\qquad a_3=a_5=\cdots=a_{11}=y,\qquad xy=\tfrac{26}{5}.$$

**Los nueve lados internos.** Por ley de cosenos, para $2\le i\le 10$:
$$A_iA_{i+1}^2 = x^2+y^2-2xy\cdot\tfrac{12}{13} = x^2+y^2-\tfrac{48}{5}.$$

Con $s=x+y$: $x^2+y^2 = s^2 - \tfrac{52}{5}$, luego
$$A_iA_{i+1} = \sqrt{s^2-20},$$
igual para los nueve lados.

**Perímetro.** Los lados restantes son $A_1A_2 + A_{11}A_1 = x+y = s$:
$$9\sqrt{s^2-20} + s = 20.$$

## Resolución

$$81(s^2-20) = (20-s)^2 \implies 80s^2+40s-2020=0 \implies 4s^2+2s-101=0,$$
$$s=\frac{-2+\sqrt{4+1616}}{8}=\frac{18\sqrt5-2}{8}=\frac{9\sqrt5-1}{4}.$$

(Verificación: $s\approx 4.7812$, $9\sqrt{s^2-20}\approx 15.219$, suma $=20$. ✓)

Así $m=9$, $n=5$, $p=1$, $q=4$, y $m+n+p+q=19$.

\boxed{19}