## Razonamiento

**Paso 1: Definir la sucesión auxiliar.**

Sea $w_n = z^n + \dfrac{1}{z^n}$. Del producto
$$\left(z^n + z^{-n}\right)\left(z + z^{-1}\right) = z^{n+1} + z^{-(n+1)} + z^{n-1} + z^{-(n-1)},$$
se obtiene la recurrencia:
$$w_{n+1} = x\, w_n - w_{n-1}, \quad \text{donde } x = z + \frac{1}{z} = \frac{1+\sqrt{5}}{2} = \varphi.$$

**Paso 2: Calcular los primeros términos.**

Con $w_0 = 2$ y $w_1 = \varphi$, y usando que $\varphi^2 = \varphi + 1$:

- $w_2 = \varphi^2 - 2 = (\varphi + 1) - 2 = \varphi - 1$
- $w_3 = \varphi(\varphi - 1) - \varphi = \varphi^2 - 2\varphi = 1 - \varphi$
- $w_4 = \varphi(1 - \varphi) - (\varphi-1) = 1 - \varphi^2 = -\varphi$
- $w_5 = \varphi(-\varphi) - (1 - \varphi) = -\varphi^2 - 1 + \varphi = -(\varphi+1) - 1 + \varphi = -2$

**Paso 3: Consecuencia de $w_5 = -2$.**

De $z^5 + z^{-5} = -2$, multiplicando por $z^5$:
$$z^{10} + 2z^5 + 1 = 0 \implies (z^5 + 1)^2 = 0 \implies z^5 = -1,$$
y por tanto $z^{10} = 1$.

**Paso 4: Reducir el exponente 85.**

Como $85 = 80 + 5$ con $80 = 8 \cdot 10$:
$$z^{85} = (z^{10})^8 \cdot z^5 = 1 \cdot (-1) = -1.$$

Entonces:
$$z^{85} + \frac{1}{z^{85}} = -1 + (-1) = -2.$$

*(Verificación numérica: $|z|=1$ y $\cos\theta = \cos 36°$, así que $z^{85}+z^{-85} = 2\cos(3060°) = 2\cos(180°) = -2$.)* ✓

$$\boxed{-2}$$