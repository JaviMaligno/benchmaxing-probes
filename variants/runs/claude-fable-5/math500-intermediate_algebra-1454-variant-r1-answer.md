## Resolución

**Paso 1: Simplificar el tercer radical.**

Completando cuadrados:
$$a^2 + b^2 - 70a - 80b + 2825 = (a-35)^2 + (b-40)^2,$$
ya que $35^2 + 40^2 = 1225 + 1600 = 2825$. La expresión se convierte en
$$\sqrt{a^2 + 15^2} + \sqrt{b^2 + 20^2} + \sqrt{(35-a)^2 + (40-b)^2}.$$

**Paso 2: Interpretar como suma de longitudes de vectores.**

Elijo los vectores
$$v_1 = (15,\, a), \quad v_2 = (b,\, 20), \quad v_3 = (35-a,\, 40-b).$$

Sus normas son exactamente los tres términos, y su suma es
$$v_1 + v_2 + v_3 = (50 + b - a,\; 60 + a - b),$$
cuyas coordenadas suman siempre $110$.

**Paso 3: Aplicar la desigualdad triangular (Minkowski).**

$$|v_1| + |v_2| + |v_3| \ge |v_1 + v_2 + v_3| = \sqrt{(50+t)^2 + (60-t)^2}, \quad t = b-a.$$

Minimizando sobre $t$: la derivada da $2(50+t) - 2(60-t) = 0 \Rightarrow t = 5$, con valor
$$\sqrt{55^2 + 55^2} = 55\sqrt{2}.$$

**Paso 4: Verificar que la igualdad se alcanza.**

La igualdad requiere que $v_1, v_2, v_3$ sean paralelos con pendiente $1$ (dirección de $(55,55)$):
- $v_1 = (15, a)$ con pendiente $1 \Rightarrow a = 15$,
- $v_2 = (b, 20)$ con pendiente $1 \Rightarrow b = 20$,
- $v_3 = (35-15,\, 40-20) = (20, 20)$ ✓.

Ambos valores cumplen $0 \le a \le 35$ y $0 \le b \le 40$. Comprobación directa:
$$\sqrt{225+225} + \sqrt{400+400} + \sqrt{400+400} = 15\sqrt{2} + 20\sqrt{2} + 20\sqrt{2} = 55\sqrt{2}.$$

$$\boxed{55\sqrt{2}}$$