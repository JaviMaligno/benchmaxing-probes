# Resolución paso a paso

**Paso 1: Establecer las probabilidades.**

Sea $p$ la probabilidad de la cara $F$ y $q$ la de su cara opuesta. Las cuatro caras restantes tienen probabilidad $1/6$ cada una, así que:

$$p + q + 4\cdot\frac{1}{6} = 1 \implies p + q = \frac{2}{3}$$

**Paso 2: Probabilidad de obtener suma 7 con dos dados.**

Las parejas ordenadas que suman 7 son $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$. La cara $F$ y su opuesta $7-F$ forman dos de estas parejas ordenadas; las otras cuatro involucran solo caras "normales":

- Parejas con $F$ y su opuesta: contribuyen $pq + qp = 2pq$
- Las otras cuatro parejas: contribuyen $4 \cdot \frac{1}{6}\cdot\frac{1}{6} = \frac{4}{36} = \frac{1}{9}$

Entonces:

$$2pq + \frac{1}{9} = \frac{47}{288}$$

**Paso 3: Resolver para $pq$.**

$$2pq = \frac{47}{288} - \frac{32}{288} = \frac{15}{288} \implies pq = \frac{15}{576} = \frac{5}{192}$$

**Paso 4: Hallar $p$ y $q$.**

Con $p+q = \frac{2}{3}$ y $pq = \frac{5}{192}$, resolvemos la ecuación cuadrática. El discriminante:

$$\left(\frac{2}{3}\right)^2 - 4\cdot\frac{5}{192} = \frac{4}{9} - \frac{20}{192} = \frac{256}{576} - \frac{60}{576} = \frac{196}{576} = \frac{49}{144}$$

$$\sqrt{\frac{49}{144}} = \frac{7}{12}$$

Como $p > q$:

$$p = \frac{\frac{2}{3} + \frac{7}{12}}{2} = \frac{\frac{15}{12}}{2} = \frac{15}{24} = \frac{5}{8}$$

(y en efecto $q = \frac{1}{24} < \frac{1}{6} < \frac{5}{8} = p$, consistente con el enunciado).

**Paso 5: Conclusión.**

$p = \frac{5}{8}$ con $\gcd(5,8)=1$, así que $m+n = 5+8$.

$$\boxed{13}$$