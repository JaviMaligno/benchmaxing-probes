## Planteamiento

La ecuación es palindrómica, así que $x=0$ no es raíz y puedo dividir entre $x^2$:

$$\left(x^2+\frac{1}{x^2}\right)+2p\left(x+\frac1x\right)-q=0$$

Con $y=x+\dfrac1x$ se tiene $x^2+\dfrac1{x^2}=y^2-2$, luego

$$y^2+2py-2-q=0 \quad\Longrightarrow\quad q=y^2+2py-2.$$

## Condición de raíz real

Para $x$ real, $y=x+\frac1x$ recorre exactamente $|y|\ge 2$ (y recíprocamente, todo $y$ con $|y|\ge2$ proviene de un $x$ real).

- Si $y\ge 2$: $f(y)=y^2+2py-2$ es creciente ahí (vértice en $y=-p\le 0$), y $f(2)=2+4p\ge 2>1$. Imposible con $q\le 1$.
- Si $y\le -2$: $f$ es decreciente en $(-\infty,-2]$ pues $-2<-p$. Entonces su recorrido es $[f(-2),\infty)=[\,2-4p,\ \infty)$.

Por tanto existe raíz real con $0\le q\le 1$ exactamente cuando

$$q\ge 2-4p,\qquad 0\le q\le 1,$$

lo que requiere $2-4p\le 1$, es decir $p\ge \tfrac14$.

## Área

$$T=\{(p,q): \tfrac14\le p\le 1,\ \max(0,2-4p)\le q\le 1\}$$

- Para $\tfrac14\le p\le \tfrac12$: altura $=1-(2-4p)=4p-1$, y $\displaystyle\int_{1/4}^{1/2}(4p-1)\,dp=\big[2p^2-p\big]_{1/4}^{1/2}=0-\left(-\tfrac18\right)=\tfrac18.$
- Para $\tfrac12\le p\le 1$: altura $=1$, aportando $\tfrac12$.

$$\text{Área}=\frac18+\frac12=\frac58$$

$$\boxed{\dfrac{5}{8}}$$