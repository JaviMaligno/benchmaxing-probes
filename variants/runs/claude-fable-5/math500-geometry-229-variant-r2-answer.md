## Solución

**Vértices sobre el eje y.** Las rectas $y=px+r$ y $y=qx+r$ se cortan en $(0,r)$, y las rectas $y=px+s$, $y=qx+s$ se cortan en $(0,s)$. Los otros dos vértices se obtienen de $px+r=qx+s$, es decir $x=\frac{s-r}{p-q}$.

**Área del primer paralelogramo.** Tomando como base el segmento vertical de longitud $|r-s|$ y como "altura" la distancia horizontal $\left|\frac{s-r}{p-q}\right|$:
$$\frac{(r-s)^2}{|p-q|}=8.$$

**Área del segundo paralelogramo.** Reemplazando $s$ por $-s$:
$$\frac{(r+s)^2}{|p-q|}=50.$$

**Dividiendo las ecuaciones:**
$$\left(\frac{r+s}{r-s}\right)^2=\frac{50}{8}=\frac{25}{4}\quad\Rightarrow\quad \frac{r+s}{|r-s|}=\frac{5}{2}.$$

Suponiendo $r>s$: $2(r+s)=5(r-s)\Rightarrow 3r=7s$, así que $r=7k$, $s=3k$ para algún entero positivo $k$. (El caso $s>r$ es simétrico y da la misma suma.)

**Sustituyendo en la primera ecuación:**
$$\frac{(7k-3k)^2}{|p-q|}=8\quad\Rightarrow\quad |p-q|=2k^2.$$

**Minimizar.** Con $k=1$: $r=7$, $s=3$, y $|p-q|=2$. Los enteros positivos más pequeños con diferencia 2 son $p=3$, $q=1$ (o viceversa).

Verificación: $\frac{(7-3)^2}{2}=8$ ✓ y $\frac{(7+3)^2}{2}=50$ ✓.

Por lo tanto $p+q+r+s = 3+1+7+3 = 14$.

$$\boxed{14}$$