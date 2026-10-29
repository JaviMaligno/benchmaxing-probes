**Planteamiento.** Sea $n=23$. Por linealidad de la expectativa,

$$E\left[\sum_{k=1}^{n}(g(g(k))-k)^2\right]=\sum_{k=1}^{n}E\big[(g(g(k))-k)^2\big].$$

**Paso 1: valorar un $k$ fijo.** Sea $j=g(k)$. Como los valores $g(1),\dots,g(n)$ son independientes y uniformes en $\{1,\dots,n\}$:

- Si $j=k$ (probabilidad $\tfrac1n$): entonces $g(g(k))=g(k)=k$, y el término es $0$.
- Si $j\neq k$ (probabilidad $\tfrac{n-1}n$): $g(j)$ es independiente de $g(k)$ y uniforme en $\{1,\dots,n\}$, así que $g(g(k))$ es uniforme en $\{1,\dots,n\}$.

Por lo tanto,
$$E\big[(g(g(k))-k)^2\big]=\frac{n-1}{n}\cdot\frac{1}{n}\sum_{i=1}^{n}(i-k)^2.$$

**Paso 2: sumar sobre $k$.** La esperanza total es
$$\frac{n-1}{n}\cdot\frac1n\sum_{k=1}^{n}\sum_{i=1}^{n}(i-k)^2
=\frac{n-1}{n^2}\sum_{d=1}^{n-1}2d^2(n-d).$$

**Paso 3: calcular con $n=23$.**
$$\sum_{d=1}^{22}d^2=\frac{22\cdot 23\cdot 45}{6}=3795,\qquad
\sum_{d=1}^{22}d^3=\left(\frac{22\cdot 23}{2}\right)^2=253^2=64009.$$
Entonces
$$\sum_{d=1}^{22}2d^2(23-d)=2\left(23\cdot 3795-64009\right)=2(87285-64009)=2\cdot 23276=46552.$$
Finalmente,
$$E=\frac{22}{23\cdot 23}\cdot 46552=\frac{22\cdot 2024}{23}=22\cdot 2024=44248,$$
ya que $46552=23\cdot 2024$.

*(Comprobación con $n=2$: hay 4 funciones y la suma media da $\tfrac12$, que coincide con la fórmula $\tfrac{2-1}{4}\cdot 2=\tfrac12$.)*

\boxed{44248}