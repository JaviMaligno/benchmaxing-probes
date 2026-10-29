## Planteamiento

Por linealidad de la esperanza:

$$E\left[\sum_{x=1}^{25}(f(f(x))-x)^2\right] = \sum_{x=1}^{25} E\left[(f(f(x))-x)^2\right]$$

**Distribución de $f(f(x))$ para $x$ fijo.** Sea $a = f(x)$:

- Si $a = x$ (probabilidad $\tfrac{1}{25}$), entonces $f(f(x)) = f(x) = x$, y el término vale 0.
- Si $a \neq x$ (cada valor con probabilidad $\tfrac{1}{25}$), entonces $f(a)$ es independiente de $f(x)$ y uniforme en $\{1,\dots,25\}$.

Por tanto, para cada $y$ (incluido $y = x$, donde el término se anula de todos modos):

$$P(f(f(x)) = y, \; f(x) \neq x) = \frac{24}{25}\cdot\frac{1}{25} = \frac{24}{625}$$

Entonces:

$$E\left[(f(f(x))-x)^2\right] = \frac{24}{625}\sum_{y=1}^{25}(y-x)^2$$

## Suma doble

$$E = \frac{24}{625}\sum_{x=1}^{25}\sum_{y=1}^{25}(y-x)^2 = \frac{24}{625}\left(2\cdot 25\sum_{x}x^2 - 2\left(\sum_x x\right)^2\right)$$

Con $\sum x = 325$ y $\sum x^2 = \frac{25\cdot 26\cdot 51}{6} = 5525$:

$$\sum_{x,y}(y-x)^2 = 2\cdot 25\cdot 5525 - 2\cdot 325^2 = 276250 - 211250 = 65000$$

## Resultado

$$E = \frac{24}{625}\cdot 65000 = 24\cdot 104 = 2496$$

$$\boxed{2496}$$