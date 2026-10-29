## Planteamiento

**Primer paralelogramo** (rectas $y=ax+c$, $y=ax+d$, $y=bx+c$, $y=bx+d$):

Dos vértices son $(0,c)$ y $(0,d)$, con lo que un lado "vertical" mide $|d-c|$. Los otros vértices salen de $ax+c=bx+d$, es decir $x=\frac{d-c}{a-b}$.

Tomando como base el segmento sobre el eje $y$ (longitud $|d-c|$) y como altura la distancia horizontal $\left|\frac{d-c}{a-b}\right|$:

$$\text{Área}=\frac{(d-c)^2}{|a-b|}=18$$

**Segundo paralelogramo** (con $-d$ en lugar de $d$): el mismo cálculo con $d\to -d$ da

$$\frac{(-d-c)^2}{|a-b|}=\frac{(c+d)^2}{|a-b|}=72$$

## Relación entre $c$ y $d$

Dividiendo las dos ecuaciones:

$$\frac{(c+d)^2}{(d-c)^2}=4\;\Longrightarrow\; c+d=2|d-c|$$

Como $c,d>0$, si $d>c$: $c+d=2(d-c)\Rightarrow 3c=d$. (El caso $c>d$ da $d=\tfrac{c}{3}$, simétrico.)

## Minimizar la suma

Con $d=3c$ y $e=|a-b|$:

$$\frac{(2c)^2}{e}=18\;\Longrightarrow\; 4c^2=18e\;\Longrightarrow\; 2c^2=9e$$

Luego $9\mid 2c^2$, así que $3\mid c$. El menor valor es $c=3$, que da $e=2$ y $d=9$.

Con $|a-b|=2$ y $a,b$ enteros positivos, el mínimo de $a+b$ es $1+3=4$.

$$a+b+c+d=3+1+3+9=16$$

Verificación con $a=3,b=1,c=3,d=9$: $\frac{(9-3)^2}{2}=18$ ✓ y $\frac{(3+9)^2}{2}=72$ ✓.

(Para $c=6$ se obtendría $d=18$, ya mucho mayor.)

\boxed{16}