## Planteamiento

Las rectas se agrupan en dos pares de paralelas (pendiente $a$ y pendiente $b$).

**Área del primer paralelogramo.** Los vértices se obtienen intersecando:
- $ax+c=bx+c \Rightarrow (0,c)$
- $ax+d=bx+d \Rightarrow (0,d)$
- $ax+c=bx+d \Rightarrow x=\tfrac{d-c}{a-b}$

Tomando los vectores desde $(0,c)$: $(0,\,d-c)$ y $\left(\tfrac{d-c}{a-b},\,\tfrac{a(d-c)}{a-b}\right)$, el producto cruz da

$$\text{Área}=\frac{(d-c)^2}{|a-b|}=18.$$

**Segundo paralelogramo.** Es el mismo cálculo con $d \to -d$:

$$\frac{(c+d)^2}{|a-b|}=72.$$

## Resolución

Dividiendo: $\dfrac{(c+d)^2}{(d-c)^2}=4 \Rightarrow c+d=2|d-c|$.

- Si $d>c$: $c+d=2d-2c \Rightarrow d=3c$.
- Si $c>d$: $c=3d$ (caso simétrico).

Con $d=3c$: $(d-c)^2=4c^2$, luego $\dfrac{4c^2}{|a-b|}=18 \Rightarrow |a-b|=\dfrac{2c^2}{9}$.

Para que $|a-b|$ sea entero positivo, $c$ debe ser múltiplo de $3$. Con $c=3$: $d=9$ y $|a-b|=2$. El mínimo de $a+b$ con $|a-b|=2$ y enteros positivos es $a=1,b=3$ (o viceversa), es decir $4$.

$$a+b+c+d=1+3+3+9=16.$$

Valores mayores de $c$ (p. ej. $c=6 \Rightarrow d=18$, $|a-b|=8$) dan sumas mucho mayores, y el caso $c=3d$ produce la misma suma $16$.

\boxed{16}