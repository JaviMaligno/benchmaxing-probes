Voy a resolver este problema de geometría analítica paso a paso.

**Área del primer paralelogramo.** Las rectas $y=ax+c$ y $y=ax+d$ son paralelas, igual que $y=bx+c$ y $y=bx+d$. Los vértices se obtienen intersecando rectas de pendientes distintas; por ejemplo, $y=ax+c$ con $y=bx+d$ da $x=\frac{d-c}{a-b}$. Tomando como base el segmento vertical de longitud $|d-c|$ (sobre el eje $y$, entre las ordenadas al origen) y como "altura" la separación horizontal $\left|\frac{d-c}{a-b}\right|$, el área resulta:

$$\text{Área}_1=\frac{(d-c)^2}{|a-b|}=18.$$

**Área del segundo paralelogramo.** Cambiando $d$ por $-d$, la misma fórmula da:

$$\text{Área}_2=\frac{(c+d)^2}{|a-b|}=72.$$

**Relación entre $c$ y $d$.** Dividiendo las dos ecuaciones:

$$\frac{(c+d)^2}{(d-c)^2}=4 \;\Rightarrow\; c+d=2|d-c|.$$

Como $c,d>0$, necesariamente $d>c$ (si $c>d$, se obtendría $c+d=2(c-d)$, es decir $c=3d$, que también es posible por simetría; tomemos $d=3c$ sin pérdida de generalidad, pues el otro caso intercambia los papeles). Con $c+d=2(d-c)$ se obtiene $d=3c$.

**Minimización.** Sustituyendo en la primera ecuación: $(d-c)^2=(2c)^2=4c^2=18|a-b|$, es decir:

$$2c^2=9|a-b|.$$

Como $9\mid 2c^2$ y $\gcd(2,9)=1$, se necesita $3\mid c$. El menor valor es $c=3$, que da $|a-b|=2$. Los enteros positivos más pequeños con diferencia 2 son $a=1,\,b=3$ (o viceversa). Entonces $d=3c=9$.

**Verificación:** $\frac{(9-3)^2}{|1-3|}=\frac{36}{2}=18$ ✓ y $\frac{(3+9)^2}{2}=\frac{144}{2}=72$ ✓.

Por lo tanto, $a+b+c+d=1+3+3+9=16$.

$$\boxed{16}$$