## Planteamiento

Defino $a = \log_x y$, $b = \log_y z$, $c = \log_z x$. Por la regla de la cadena de logaritmos, $abc = 1$, así que $c = \frac{1}{ab}$.

**Ecuación 2:** como $\log_y x = \frac{1}{a}$:
$$\log_{1/a} z = -3 \;\Rightarrow\; z = \left(\tfrac{1}{a}\right)^{-3} = a^3$$

**Ecuación 3:** $\log_z y = \frac{1}{b}$ y $\log_x z = \log_x y \cdot \log_y z = ab$, luego:
$$\frac{1}{b} + ab = 16$$

**Ecuación 1:** $a + b + \frac{1}{ab} = 8$.

## Resolución

Sea $u = ab$. De la ecuación 3: $\frac{1}{b} = 16 - u$, es decir $b = \frac{1}{16-u}$ y por tanto $a = \frac{u}{b} = u(16-u)$.

Sustituyo en la ecuación 1:
$$u(16-u) + \frac{1}{16-u} + \frac{1}{u} = 8$$

Multiplicando por $u(16-u)$ y llamando $s = u(16-u)$:
$$s^2 + (16-u) + u = 8s \;\Rightarrow\; s^2 - 8s + 16 = 0 \;\Rightarrow\; (s-4)^2 = 0 \;\Rightarrow\; s = 4$$

Pero $a = u(16-u) = s = 4$, así que directamente:
$$a = \log_x y = 4 \quad\Rightarrow\quad z = a^3 = 64$$

(De $u^2 - 16u + 4 = 0$ sale $u = 8 \pm 2\sqrt{15}$, lo que da dos valores válidos de $b$, pero en ambos casos $a = 4$.)

## Verificación

Con $a = 4$: $\log_y x = \frac{1}{4}$, y $\log_{1/4} 64 = -3$ porque $(1/4)^{-3} = 64$. ✓
Con $b = 2 \pm \frac{\sqrt{15}}{2}$ se cumplen $\frac{1}{b} + 4b = 16$ y $4 + b + \frac{1}{4b} = 8$. ✓

$$\boxed{z = 64}$$