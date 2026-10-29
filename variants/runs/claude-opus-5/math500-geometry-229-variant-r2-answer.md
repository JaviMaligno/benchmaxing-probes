## Planteamiento

**Área del primer paralelogramo.** Las rectas $y=px+r$ y $y=qx+r$ se cortan en $(0,r)$; las rectas $y=px+s$ y $y=qx+s$ se cortan en $(0,s)$. Estos dos puntos forman una diagonal de longitud $|r-s|$ sobre el eje $y$.

Los otros dos vértices: $px+r=qx+s$ da $x=\dfrac{s-r}{p-q}$, y análogamente $x=\dfrac{r-s}{p-q}$. Cada uno está a distancia horizontal $\dfrac{|r-s|}{|p-q|}$ del eje $y$.

Sumando los dos triángulos que la diagonal determina:

$$\text{Área}=2\cdot\frac12\,|r-s|\cdot\frac{|r-s|}{|p-q|}=\frac{(r-s)^2}{|p-q|}=8$$

**Área del segundo paralelogramo.** Es el mismo cálculo con $s\to -s$:

$$\frac{(r+s)^2}{|p-q|}=50$$

## Resolución

Dividiendo las dos ecuaciones:

$$\frac{(r+s)^2}{(r-s)^2}=\frac{50}{8}=\frac{25}{4}\quad\Longrightarrow\quad \frac{r+s}{|r-s|}=\frac52$$

Suponiendo $r>s$ (son positivos, así que $r+s>0$): $2(r+s)=5(r-s)\Rightarrow 7s=3r$, es decir $r=7t$, $s=3t$.

Sustituyendo en la primera ecuación: $(4t)^2=8|p-q|\Rightarrow |p-q|=2t^2$.

Para minimizar tomamos $t=1$: $r=7$, $s=3$, $|p-q|=2$.

Con $p,q$ enteros positivos que difieren en $2$, el mínimo de $p+q$ es $1+3=4$.

**Verificación** con $p=1,q=3,r=7,s=3$:
- $\dfrac{(7-3)^2}{|1-3|}=\dfrac{16}{2}=8$ ✓
- $\dfrac{(7+3)^2}{|1-3|}=\dfrac{100}{2}=50$ ✓

Por tanto $p+q+r+s=1+3+7+3=14$.

\boxed{14}