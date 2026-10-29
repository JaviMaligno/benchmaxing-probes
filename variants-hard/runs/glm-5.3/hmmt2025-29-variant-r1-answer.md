# Planteamiento

Coloco el rectángulo en coordenadas: $Q=(0,0)$, $R=(30,0)$, $S=(30,h)$, $P=(0,h)$, donde $h=PQ$ es lo que buscamos. Sea $Y=(x,y)$ y definamos:
$$u = y \ (\text{distancia de } Y \text{ a } QR), \qquad v = h - y \ (\text{distancia de } Y \text{ a } PS).$$

**Condición del ángulo recto.** Como $\angle PYQ = 90^\circ$, por el teorema de Tales $Y$ está en la circunferencia de diámetro $PQ$, lo que da $x^2 + (u-\tfrac h2)^2 = \tfrac{h^2}{4}$, es decir:
$$x^2 = uv. \tag{1}$$

# Triángulo $QYR$ (radio circunscrito 25, agudo)

Sea $\gamma = \angle QYR$, el ángulo opuesto al lado $QR=30$. Por la ley de senos extendida:
$$\sin\gamma = \frac{30}{2\cdot 25} = \frac35, \qquad \cos\gamma = \frac45 \ (\text{agudo}).$$

Con $\vec{YQ}=(-x,-u)$, $\vec{YR}=(30-x,-u)$, el producto punto da $YQ\cdot YR = u^2 - x(30-x)$. Además, de $R = \frac{abc}{4K}$ con área $K = 15u$:
$$|YQ|\,|YR| = 2\cdot 25 \cdot u = 50u.$$

Entonces $\cos\gamma = \frac{u^2 - x(30-x)}{50u} = \frac45$, y usando (1):
$$u^2 - 30x + x^2 = 40u \implies u(u+v) - 30x = 40u \implies u(h - 40) = 30x. \tag{2}$$

# Triángulo $PYS$ (radio circunscrito 17, agudo)

Sea $\gamma' = \angle PYS$, opuesto a $PS = 30$:
$$\sin\gamma' = \frac{30}{2\cdot 17} = \frac{15}{17}, \qquad \cos\gamma' = \frac{8}{17}.$$

De forma análoga, con $\vec{YP}=(-x, v)$, $\vec{YS}=(30-x, v)$, área $15v$, y $|YP|\,|YS| = 34v$:
$$\frac{v^2 - x(30-x)}{34v} = \frac{8}{17} \implies v^2 - 30x + x^2 = 16v \implies v(h - 16) = 30x. \tag{3}$$

# Resolución

Multiplicando (2) y (3):
$$uv\,(h-40)(h-16) = 900\,x^2.$$

Por (1), $uv = x^2$, y como $Y$ es interior $x \neq 0$, así que:
$$(h-40)(h-16) = 900 \implies h^2 - 56h + 640 = 900 \implies h^2 - 56h - 260 = 0.$$

$$h = \frac{56 \pm \sqrt{3136 + 1040}}{2} = \frac{56 \pm \sqrt{4176}}{2} = 28 \pm 6\sqrt{29}.$$

Como $h > 0$, tomamos $h = 28 + 6\sqrt{29}$.

**Verificación.** Con $h = 28 + 6\sqrt{29}$: $(h-40)(h-16) = 6(\sqrt{29}-2)\cdot 6(\sqrt{29}+2) = 36\cdot 25 = 900$ ✓. Se obtiene $x = 15 + \tfrac{70}{\sqrt{29}} \approx 28.0 \in (0,30)$, $u \approx 41.36$, $v \approx 18.96$, con $u+v = h$ ✓, $x^2 = uv$ ✓, radios $25$ y $17$ ✓, y todos los ángulos agudos ✓.

$$\boxed{28 + 6\sqrt{29}}$$