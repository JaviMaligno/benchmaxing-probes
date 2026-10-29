Voy a resolver este problema de probabilidad paso a paso.

**Planteamiento:** Sea $p$ la probabilidad de la cara $F$ y $q$ la de su cara opuesta. Las otras cuatro caras tienen probabilidad $1/6$ cada una, así que:

$$p + q + 4\cdot\tfrac{1}{6} = 1 \implies p + q = \tfrac{1}{3}$$

**Probabilidad de suma 7:** Como las caras opuestas suman 7, la suma 7 solo se obtiene cuando un dado muestra una cara y el otro muestra su opuesta. Hay tres pares de caras opuestas:

- El par $(F, \text{opuesta de } F)$: contribuye $pq + qp = 2pq$.
- Los otros dos pares (cuatro caras con probabilidad $1/6$): contribuyen $4 \cdot \tfrac{1}{6}\cdot\tfrac{1}{6} = \tfrac{4}{36} = \tfrac{1}{9}$.

Entonces:

$$2pq + \tfrac{1}{9} = \tfrac{47}{288}$$

$$2pq = \tfrac{47}{288} - \tfrac{32}{288} = \tfrac{15}{288} \implies pq = \tfrac{15}{576}$$

**Resolviendo el sistema:** $p$ y $q$ son raíces de $x^2 - \tfrac{1}{3}x + \tfrac{15}{576} = 0$:

$$x = \frac{\tfrac{1}{3} \pm \sqrt{\tfrac{1}{9} - \tfrac{60}{576}}}{2} = \frac{\tfrac{1}{3} \pm \sqrt{\tfrac{64}{576} - \tfrac{60}{576}}}{2} = \frac{\tfrac{1}{3} \pm \tfrac{1}{12}}{2}$$

Esto da $x = \tfrac{5}{24}$ o $x = \tfrac{1}{8}$. Como $p > \tfrac{1}{6}$, se tiene $p = \tfrac{5}{24}$ (y $q = \tfrac{1}{8} < \tfrac{1}{6}$, consistente).

Con $m = 5$ y $n = 24$ (coprimos), $m + n = 29$.

$$\boxed{29}$$