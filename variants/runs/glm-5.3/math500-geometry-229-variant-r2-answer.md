## Planteamiento

**Primer paralelogramo** (líneas $y=px+r$, $y=px+s$, $y=qx+r$, $y=qx+s$):

Los vértices sobre el eje $y$ son $(0,r)$ y $(0,s)$. El tercer vértice es la intersección de $y=px+r$ con $y=qx+s$:
$$x = \frac{s-r}{p-q}.$$

Vectores de lados desde $(0,r)$: $\vec{a} = (0,\,s-r)$ y $\vec{b} = \left(\frac{s-r}{p-q},\,\frac{p(s-r)}{p-q}\right)$.

$$\text{Área}_1 = \left|\det(\vec a, \vec b)\right| = \frac{(s-r)^2}{|p-q|} = 8.$$

**Segundo paralelogramo** (líneas $y=px-s$, $y=qx-s$ con las de altura $r$):

Análogo, con vértices $(0,r)$ y $(0,-s)$:
$$\text{Área}_2 = \frac{(r+s)^2}{|p-q|} = 50.$$

## Resolución

Dividiendo ambas ecuaciones:
$$\frac{(r+s)^2}{(s-r)^2} = \frac{50}{8} = \frac{25}{4} \quad\Longrightarrow\quad \frac{r+s}{|s-r|} = \frac{5}{2}.$$

Tomando $s>r$: $2(r+s) = 5(s-r)$, de donde $s = \frac{7r}{3}$. Entonces:
$$|p-q| = \frac{(s-r)^2}{8} = \frac{(4r/3)^2}{8} = \frac{2r^2}{9}.$$

Para que $|p-q|$ sea entero, $r = 3k$ (con $k$ entero positivo), lo que da $s = 7k$ y $|p-q| = 2k^2$.

Minimizando la suma:
$$p+q+r+s \ge \underbrace{1}_{p} + \underbrace{(2k^2+1)}_{q} + 3k + 7k = 2k^2 + 10k + 2,$$

que es mínima para $k=1$: $r=3$, $s=7$, $|p-q|=2$.

**Verificación** con $p=3$, $q=1$, $r=3$, $s=7$:
- Área 1: $\dfrac{(7-3)^2}{|3-1|} = \dfrac{16}{2} = 8$ ✓
- Área 2: $\dfrac{(7+3)^2}{|3-1|} = \dfrac{100}{2} = 50$ ✓
- Suma: $3+1+3+7 = 14$.

$$\boxed{14}$$