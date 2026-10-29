## Planteamiento

Sea $a_i = B_1B_i$. Con $\cos\theta = \tfrac45$ se tiene $\sin\theta = \tfrac35$, y el área de cada triángulo da:

$$\tfrac12 a_i a_{i+1}\cdot\tfrac35 = 1 \implies a_i a_{i+1} = \tfrac{10}{3}\quad (2\le i\le 10)$$

Como el producto es constante, $a_i = a_{i+2}$: los radios alternan entre dos valores. Sea $x = a_2 = a_4 = \cdots = a_{10}$ y $y = a_3 = a_5 = \cdots = a_{11}$, con $xy = \tfrac{10}{3}$.

## Lados del polígono

Por el teorema del coseno, cada uno de los 9 lados $B_iB_{i+1}$ ($2\le i\le 10$) mide

$$s^2 = x^2 + y^2 - 2xy\cdot\tfrac45 = x^2+y^2 - \tfrac{16}{3}$$

es decir, los nueve son iguales. Los dos lados restantes son $B_1B_2 = x$ y $B_1B_{11} = y$.

## Perímetro

Con $u = x+y$: $x^2+y^2 = u^2 - 2\cdot\tfrac{10}{3} = u^2-\tfrac{20}{3}$, luego

$$s = \sqrt{u^2 - \tfrac{20}{3} - \tfrac{16}{3}} = \sqrt{u^2-12}$$

El perímetro es $9s + u = 20$, o sea $9\sqrt{u^2-12} = 20-u$. Elevando al cuadrado:

$$81u^2 - 972 = u^2 - 40u + 400 \implies 80u^2 + 40u - 1372 = 0 \implies 20u^2 + 10u - 343 = 0$$

$$u = \frac{-10 + \sqrt{100 + 27440}}{40} = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85}-5}{20}$$

(Se descarta la raíz negativa; se verifica $u\approx 3.899$, con $u^2 > 12$ y $20-u>0$.)

Así $m=9$, $n=85$, $p=5$, $q=20$, con $85$ libre de cuadrados y $\gcd(9,5,20)=1$.

$$m+n+p+q = 9+85+5+20 = 119$$

\boxed{119}