## Planteamiento

Sea $n=25$. Fijamos $x$ y escribimos $y=f(x)$, $z=f(y)=f(f(x))$.

**Caso 1: $y = x$** (probabilidad $1/n$). Entonces $f(f(x))=f(x)=x$, y el término aporta $0$.

**Caso 2: $y \neq x$** (probabilidad $\frac{n-1}{n}$). Como $y\neq x$, el valor $f(y)$ es independiente de $f(x)$, así que condicionado a esto, $z$ es uniforme en $\{1,\dots,n\}$.

Por lo tanto
$$
\mathbb{E}\big[(f(f(x))-x)^2\big] = \frac{n-1}{n}\cdot\frac{1}{n}\sum_{u=1}^{n}(u-x)^2 .
$$

## Suma sobre $x$

$$
\mathbb{E}\left[\sum_{x=1}^{n}(f(f(x))-x)^2\right] = \frac{n-1}{n^2}\sum_{x=1}^{n}\sum_{u=1}^{n}(u-x)^2 .
$$

La doble suma se expande como
$$
\sum_{x,u}(u^2-2ux+x^2) = 2n\sum_{x} x^2 - 2\Big(\sum_x x\Big)^2 .
$$

Con $n=25$: $\sum x = 325$ y $\sum x^2 = \frac{25\cdot 26\cdot 51}{6} = 5525$.

$$
2(25)(5525) - 2(325)^2 = 276250 - 211250 = 65000 .
$$

## Resultado

$$
\frac{24}{625}\cdot 65000 = 24 \cdot 104 = 2496 .
$$

$\boxed{2496}$