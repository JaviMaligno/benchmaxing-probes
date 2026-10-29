## Planteamiento

Para las rectas $y=px+r$, $y=px+s$, $y=qx+r$, $y=qx+s$, los vértices son:

- $(0,r)$ — intersección de $y=px+r$ con $y=qx+r$
- $(0,s)$ — intersección de $y=px+s$ con $y=qx+s$
- $\left(\frac{s-r}{p-q},\ \cdot\right)$ y $\left(\frac{r-s}{p-q},\ \cdot\right)$ — las otras dos

Tomando como base el segmento vertical en $x=0$, de longitud $|s-r|$, la altura horizontal es $\left|\frac{s-r}{p-q}\right|$, así que

$$\text{Área} = \frac{(s-r)^2}{|p-q|} = 8$$

Para el segundo paralelogramo basta sustituir $s \to -s$:

$$\frac{(r+s)^2}{|p-q|} = 50$$

## Resolución

Sea $d=|p-q|$. Dividiendo las ecuaciones:

$$\frac{(r+s)^2}{(s-r)^2} = \frac{50}{8} = \frac{25}{4} \quad\Longrightarrow\quad \frac{r+s}{|s-r|} = \frac{5}{2}$$

Suponiendo $s>r$ (ambos positivos): $2(s+r) = 5(s-r)$, luego $7r = 3s$, es decir $r=3k$, $s=7k$.

Entonces $(s-r)^2 = 16k^2 = 8d$, de donde $d = 2k^2$.

Minimizamos $p+q+r+s = (p+q) + 10k$:

- **$k=1$:** $r=3$, $s=7$, $d=|p-q|=2$. La suma mínima de enteros positivos con diferencia 2 es $p=1$, $q=3$ (o viceversa), dando $p+q=4$.
- Total: $4+3+7 = 14$.

Para $k\ge 2$ ya se tiene $10k \ge 20 > 14$, así que no mejora.

**Verificación** con $p=1,q=3,r=3,s=7$: $\frac{(7-3)^2}{2} = 8$ ✓ y $\frac{(3+7)^2}{2} = 50$ ✓.

$$\boxed{14}$$