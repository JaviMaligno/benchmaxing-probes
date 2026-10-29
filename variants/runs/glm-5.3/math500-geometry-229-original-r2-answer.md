## Desarrollo

**Fórmula general del área.** Para el paralelogramo delimitado por $y=ax+t_1$, $y=ax+t_2$, $y=bx+s_1$, $y=bx+s_2$, tomando dos lados adyacentes desde un vértice, ambos vectores lados son proporcionales a $(1,a)$ y $(1,b)$, con factores $\frac{s_2-s_1}{a-b}$ y $\frac{t_1-t_2}{a-b}$. El producto cruz da:

$$\text{Área}=\frac{|s_2-s_1|\,|t_2-t_1|}{|a-b|}$$

**Aplicando a los dos paralelogramos** (con $m=|a-b|\ge 1$, pues $a\neq b$):

- Primero: las intersecciones al origen de cada familia son $c,d$, así que $\dfrac{(d-c)^2}{m}=18$.
- Segundo: las intersecciones son $c$ y $-d$, así que $\dfrac{(c+d)^2}{m}=72$.

**Relación entre $c$ y $d$.** Dividiendo ambas ecuaciones:

$$\frac{(c+d)^2}{(d-c)^2}=4 \;\Longrightarrow\; c+d = 2|d-c|$$

- Si $d>c$: $\;c+d=2(d-c)\Rightarrow d=3c$.
- Si $c>d$: $\;c=3d$.

**Condición de cuadrado perfecto.** Con $d=3c$: $(d-c)^2=4c^2=18m$, es decir $m=\frac{2c^2}{9}$. Para que $m$ sea entero se necesita $3\mid c$; escribiendo $c=3j$:

$$c=3j,\quad d=9j,\quad m=2j^2,\quad c+d=12j.$$

**Minimizando $a+b+c+d$.** Con $|a-b|=m=2j^2$, la suma mínima de $a+b$ (enteros positivos) es $1+(1+2j^2)=2+2j^2$. Entonces:

$$a+b+c+d = 2+2j^2+12j,$$

que es creciente en $j\ge 1$, así que el mínimo está en $j=1$:

$$a+b+c+d = 2+2+12 = 16.$$

**Verificación** con $(a,b,c,d)=(1,3,3,9)$:
- Primer paralelogramo: $\frac{(9-3)^2}{|1-3|}=\frac{36}{2}=18$ ✓
- Segundo: $\frac{(3+9)^2}{|1-3|}=\frac{144}{2}=72$ ✓
- Suma: $1+3+3+9=16$ ✓

$$\boxed{16}$$