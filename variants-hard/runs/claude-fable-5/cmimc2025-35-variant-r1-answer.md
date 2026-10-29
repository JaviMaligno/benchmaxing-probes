**Planteamiento.** Por linealidad de la esperanza, basta calcular $E[(g(g(k))-k)^2]$ para cada $k$ fijo y sumar.

**Distribución de $g(g(k))$ para $k$ fijo.** Sea $j = g(k)$, uniforme en $\{1,\dots,23\}$:

- Con probabilidad $\tfrac{1}{23}$, $g(k)=k$, y entonces $g(g(k)) = g(k) = k$, de modo que el término vale $0$.
- Con probabilidad $\tfrac{1}{23}$ para cada $j \neq k$: como $g(j)$ es independiente de $g(k)$, el valor $g(g(k)) = g(j)$ es uniforme en $\{1,\dots,23\}$.

Por tanto, condicionado a $g(k)\neq k$ (probabilidad $\tfrac{22}{23}$), $g(g(k))$ es uniforme en $\{1,\dots,23\}$.

**Cálculo.** Con $U$ uniforme en $\{1,\dots,23\}$:
$$E\Big[\sum_{k=1}^{23}(g(g(k))-k)^2\Big] = \frac{22}{23}\sum_{k=1}^{23} E[(U-k)^2] = \frac{22}{23^2}\sum_{k=1}^{23}\sum_{j=1}^{23}(j-k)^2.$$

La suma doble es
$$\sum_{j,k}(j-k)^2 = 2n\sum_{j} j^2 - 2\Big(\sum_j j\Big)^2,$$
con $n=23$, $\sum j = 276$, $\sum j^2 = \frac{23\cdot 24\cdot 47}{6} = 4324$:
$$2\cdot 23\cdot 4324 - 2\cdot 276^2 = 198904 - 152352 = 46552.$$

Finalmente:
$$\frac{22}{529}\cdot 46552 = 22\cdot 88 = 1936,$$
ya que $46552 = 529\cdot 88$.

$$\boxed{1936}$$