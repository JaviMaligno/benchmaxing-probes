## Planteamiento

**Fórmula del área.** Para un paralelogramo delimitado por las rectas $y=ax+p$, $y=ax+q$, $y=bx+p$, $y=bx+q$, los vértices son las intersecciones $L_a^p\cap L_b^p=(0,p)$, $L_a^q\cap L_b^q=(0,q)$, etc. Tomando como lados los vectores $\frac{q-p}{a-b}(1,a)$ y $\frac{p-q}{a-b}(1,b)$, el área es:

$$\text{Área}=\left|\det\begin{pmatrix}\frac{q-p}{a-b} & \frac{p-q}{a-b}\\ a & b\end{pmatrix}\right|=\frac{(p-q)^2}{|a-b|}$$

**Aplicación a los dos paralelogramos:**

$$\frac{(c-d)^2}{|a-b|}=18 \qquad\qquad \frac{(c+d)^2}{|a-b|}=72$$

**Relación entre $c$ y $d$.** Dividiendo ambas ecuaciones:

$$\left(\frac{c+d}{|c-d|}\right)^2=\frac{72}{18}=4 \;\Rightarrow\; \frac{c+d}{|c-d|}=2$$

- Si $d>c$: $c+d=2(d-c)\Rightarrow d=3c$
- Si $c>d$: $c+d=2(c-d)\Rightarrow c=3d$

**Condición de integraridad.** Con $d=3c$ (el otro caso es simétrico):

$$|a-b|=\frac{(c+d)^2}{72}=\frac{16c^2}{72}=\frac{2c^2}{9}$$

Como $a,b$ son enteros, $9\mid 2c^2$, es decir $3\mid c$. Sea $c=3k$ con $k\ge 1$:

- $c=3k$, $d=9k$, luego $c+d=12k$
- $|a-b|=2k^2$

**Minimización.** Con $|a-b|=2k^2$ y $a,b\ge 1$, el mínimo de $a+b$ es $2+2k^2$ (tomando el menor igual a 1). Por tanto:

$$a+b+c+d \ge (2+2k^2)+12k = 2k^2+12k+2$$

que es creciente en $k\ge 1$, así que $k=1$:

$$a+b+c+d = 2+2+12 = 16$$

**Verificación con $(a,b,c,d)=(1,3,3,9)$:**
- Primer paralelogramo: $\frac{(3-9)^2}{|1-3|}=\frac{36}{2}=18$ ✓
- Segundo: $\frac{(3+9)^2}{|1-3|}=\frac{144}{2}=72$ ✓ (comprobado también por determinante directo con los cuatro vértices)

\boxed{16}