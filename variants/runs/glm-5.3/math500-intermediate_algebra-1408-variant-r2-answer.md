## Planteamiento

Denotemos $a = w + \dfrac{1}{w} = \dfrac{\sqrt{5}-1}{2}$ y $s_n = w^n + \dfrac{1}{w^n}$.

**Paso 1: Una identidad clave para $a$.**

Calculamos:
$$a^2 = \left(\frac{\sqrt{5}-1}{2}\right)^2 = \frac{6-2\sqrt{5}}{4} = \frac{3-\sqrt{5}}{2},$$
$$a^2 + a = \frac{3-\sqrt{5}}{2} + \frac{\sqrt{5}-1}{2} = \frac{2}{2} = 1.$$
Es decir, $a^2 = 1 - a$. (De hecho $a = 2\cos 72°$, ya que $\cos 72° = \frac{\sqrt{5}-1}{4}$.)

**Paso 2: Recurrencia para $s_n$.**

Multiplicando $w^n + w^{-n} = s_n$ por $a = w + w^{-1}$:
$$a\,s_n = w^{n+1} + w^{-(n+1)} + w^{n-1} + w^{-(n-1)} = s_{n+1} + s_{n-1},$$
de donde $s_{n+1} = a\,s_n - s_{n-1}$, con $s_0 = 2$ y $s_1 = a$.

**Paso 3: Calcular $s_5$.**

- $s_2 = a^2 - 2 = (1-a) - 2 = -1 - a$
- $s_3 = a\,s_2 - s_1 = a(-1-a) - a = -2a - a^2 = -2a - (1-a) = -1 - a$... 

revisemos: $s_3 = -2a - a^2 = -2a - (1-a) = -a - 1$. ✔️ (coincide con $2\cos 216° = -\frac{1+\sqrt{5}}{2}$)

- $s_4 = a\,s_3 - s_2 = a(-a-1) - (-1-a) = -a^2 - a + 1 + a = 1 - a^2 = 1 - (1-a) = a$
- $s_5 = a\,s_4 - s_3 = a^2 - (-a-1) = (1-a) + a + 1 = 2$

**Paso 4: Conclusión.**

Sea $u = w^5$. Entonces $u + \dfrac{1}{u} = s_5 = 2$, es decir:
$$u^2 - 2u + 1 = 0 \implies (u-1)^2 = 0 \implies u = 1.$$
Por lo tanto $w^5 = 1$, y así:
$$w^{95} + \frac{1}{w^{95}} = (w^5)^{19} + \frac{1}{(w^5)^{19}} = 1 + 1 = 2.$$

$\boxed{2}$