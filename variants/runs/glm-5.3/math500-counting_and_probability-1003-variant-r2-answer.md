Planteemos el problema paso a paso.

**Paso 1: Distribución de un dado.**
Sea $p$ la probabilidad de la cara $F$ y $q$ la de su cara opuesta. Las otras cuatro caras tienen probabilidad $1/6$ cada una, así que:
$$p + q = 1 - 4\cdot\frac{1}{6} = \frac{1}{3}.$$

Sin pérdida de generalidad (por simetría del dado), tomemos $F=1$ y su opuesta $6$.

**Paso 2: Probabilidad de que dos dados sumen 7.**
Las parejas que suman 7 son $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$. Las cuatro caras "neutras" aportan $1/36$ cada pareja, y las parejas que involucran a $F$ y su opuesta aportan $pq$ cada una:
$$P(\text{suma}=7) = 2pq + 4\cdot\frac{1}{36} = 2pq + \frac{1}{9}.$$

**Paso 3: Resolver para $pq$.**
$$2pq + \frac{1}{9} = \frac{71}{450} \implies 2pq = \frac{71}{450} - \frac{50}{450} = \frac{21}{450} \implies pq = \7/300.$$

**Paso 4: Hallar $p$ y $q$.**
Con $p+q = \frac{1}{3}$ y $pq = \frac{7}{300}$, son las raíces de:
$$x^2 - \frac{1}{3}x + \frac{7}{300} = 0 \implies x = \frac{\frac{1}{3} \pm \sqrt{\frac{1}{9} - \frac{28}{300}}}{2} = \frac{\frac{1}{3} \pm \frac{4}{30}}{2},$$
es decir, $x = \frac{7}{30}$ o $x = \frac{1}{10}$.

Como $p > \frac{1}{6} = \frac{5}{30}$, debe ser $p = \frac{7}{30}$ (y en efecto $q = \frac{1}{10} < \frac{1}{6}$ ✓).

**Paso 5: Verificación.**
$2pq + \frac{1}{9} = \frac{14}{300} + \frac{1}{9} = \frac{21}{450} + \frac{50}{450} = \frac{71}{450}$ ✓.

Entonces $p = \frac{m}{n} = \frac{7}{30}$ con $\gcd(7,30)=1$, y $m+n = 37$.

\boxed{37}