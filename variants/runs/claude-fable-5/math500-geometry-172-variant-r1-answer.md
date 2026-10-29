## Solución

Coloco coordenadas: $Q=(0,0)$, $R=(r,0)$, $P=(p_1,p_2)$. El área de $PQR$ es $\tfrac12 r p_2 = 270$, así que $r p_2 = 540$.

**Puntos clave:**
- Centroide: $G = \left(\frac{p_1+r}{3}, \frac{p_2}{3}\right)$.
- $U$ es el punto medio de $PQ$: $U = \left(\frac{p_1}{2}, \frac{p_2}{2}\right)$.
- La recta por $G$ paralela a $QR$ es $y = \frac{p_2}{3}$. Su intersección con $PQ$ (parametrizada como $(tp_1, tp_2)$) ocurre en $t=\tfrac13$, así que $M = \left(\frac{p_1}{3}, \frac{p_2}{3}\right)$.

**Área de $UMG$:**

Los puntos $M$ y $G$ están ambos sobre la recta $y = \frac{p_2}{3}$, así que uso $MG$ como base:

$$MG = \left|\frac{p_1+r}{3} - \frac{p_1}{3}\right| = \frac{r}{3}$$

La altura es la distancia vertical de $U$ a esa recta:

$$h = \left|\frac{p_2}{2} - \frac{p_2}{3}\right| = \frac{p_2}{6}$$

Por lo tanto:

$$[UMG] = \frac{1}{2}\cdot\frac{r}{3}\cdot\frac{p_2}{6} = \frac{r p_2}{36} = \frac{540}{36} = 15$$

$$\boxed{15}$$