## Solución

**Factorización de las desigualdades**

Con $x+y+z=87$:

- $x-yz < y-zx \iff (x-y) + z(x-y) < 0 \iff (x-y)(1+z) < 0$
- $y-zx < z-xy \iff (y-z) + x(y-z) < 0 \iff (y-z)(1+x) < 0$

**Casos según los signos**

1. $1+z>0$, $1+x>0$: entonces $x<y$ y $y<z$, es decir $-1 < x < y < z$. Como $x>-1$ y la suma es $87$, la región está **acotada**.
2. $1+z<0$, $1+x<0$: obliga a $z<y<x<-1$, luego $x+y+z<-3$, imposible con suma $87$. Vacío.
3. $1+z>0$, $1+x<0$: da $x<-1<z<y$, región no acotada.
4. $1+z<0$, $1+x>0$: da $z<-1<x$, $y<z$, también no acotada.

La única región de área finita es la del caso 1.

**Vértices del triángulo**

Las fronteras son $x=-1$, $x=y$, $y=z$ sobre el plano:

- $x=-1,\ x=y$: $(-1,-1,89)$
- $x=-1,\ y=z$: $(-1,44,44)$
- $x=y=z$: $(29,29,29)$

**Área**

Desde $(29,29,29)$:
$$\mathbf{v}_1 = (-30,-30,60),\qquad \mathbf{v}_2 = (-30,15,15)$$
$$\mathbf{v}_1\times\mathbf{v}_2 = (-1350,-1350,-1350),\qquad |\mathbf{v}_1\times\mathbf{v}_2| = 1350\sqrt3$$
$$\text{Área} = \tfrac12\cdot 1350\sqrt3 = 675\sqrt3$$

Así $a=675$, $b=3$, y $a+b=678$.

\boxed{678}