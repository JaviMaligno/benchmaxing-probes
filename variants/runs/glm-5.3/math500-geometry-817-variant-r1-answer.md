**Planteamiento**

Coloco $O$ en el origen, con $OM$ sobre el eje $x$ positivo y $ON$ sobre el eje $y$ positivo, ambos de longitud 20.

- **Semicírculo grande:** diámetro $OM$, de $(0,0)$ a $(20,0)$, así que su centro es $C_1=(10,0)$ y su radio es $r_1=10$.
- **Semicírculo pequeño:** diámetro sobre $ON$ con un extremo en $N=(0,20)$. Si su radio es $r$, el otro extremo del diámetro es $(0,20-2r)$, así que su centro es $C_2=(0,20-r)$.

**Condición de tangencia**

Como los semicírculos son tangentes exteriores, la distancia entre centros es $r_1+r_2 = 10+r$:

$$|C_1C_2| = \sqrt{10^2 + (20-r)^2} = 10 + r$$

**Resolución**

Elevando al cuadrado:

$$100 + (20-r)^2 = (10+r)^2$$
$$100 + 400 - 40r + r^2 = 100 + 20r + r^2$$
$$400 - 40r = 20r$$
$$400 = 60r \implies r = \frac{20}{3}$$

**Verificación:** con $r=\frac{20}{3}$, el centro pequeño es $\left(0,\frac{40}{3}\right)$ y la distancia entre centros es $\sqrt{100+\frac{1600}{9}}=\frac{50}{3}=10+\frac{20}{3}$ ✓. El punto de tangencia $\left(4,8\right)$ está dentro del cuarto de círculo ✓.

$$\boxed{\dfrac{20}{3}}$$