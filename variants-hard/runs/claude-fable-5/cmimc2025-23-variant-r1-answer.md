## Planteamiento con coordenadas

Coloco $P = (-1, 0)$ y $Q = (1, 0)$, de modo que $PQ = 2$.

**Puntos $R, S$:** intersección de los círculos de radio $2$ centrados en $P$ y $Q$. Están en el eje $y$: $y^2 = 4 - 1 = 3$, así que $R = (0, \sqrt{3})$ y $S = (0, -\sqrt{3})$, con $RS = 2\sqrt{3}$.

**Puntos $T, U$:** intersección de los círculos de radio $2\sqrt{3}$ centrados en $R$ y $S$. Están en el eje $x$: $x^2 + 3 = 12$, luego $x = \pm 3$. Con el orden pedido $T, P, Q, U$: $T = (-3, 0)$, $U = (3, 0)$, con $TU = 6$.

**Puntos $V, W$:** intersección de los círculos de radio $6$ centrados en $T$ y $U$. Están en el eje $y$: $9 + y^2 = 36$, luego $y = \pm 3\sqrt{3}$. Como $V$ está del mismo lado que $R$: $V = (0, 3\sqrt{3})$.

## Área del pentágono $PRUVT$

Vértices en orden: $P(-1,0)$, $R(0,\sqrt{3})$, $U(3,0)$, $V(0,3\sqrt{3})$, $T(-3,0)$. Es un polígono simple (con vértice cóncavo en $R$). Aplico la fórmula del zapatero (shoelace):

$$
\begin{aligned}
2A &= \big[(-1)(\sqrt{3}) - 0\big] + \big[0 - 3\sqrt{3}\big] + \big[3\cdot 3\sqrt{3} - 0\big] + \big[0 - (-3)(3\sqrt{3})\big] + 0 \\
&= -\sqrt{3} - 3\sqrt{3} + 9\sqrt{3} + 9\sqrt{3} = 14\sqrt{3}
\end{aligned}
$$

Por lo tanto $A = 7\sqrt{3}$.

$$\boxed{7\sqrt{3}}$$