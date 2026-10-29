**Razonamiento:**

Sea $p$ la probabilidad de la cara $F$ y $q$ la de su opuesta ($7-F$). Las otras cuatro caras tienen probabilidad $1/6$ cada una, así que:

$$p + q = 1 - 4\cdot\tfrac{1}{6} = \tfrac{1}{3}$$

Con dos dados, las parejas que suman 7 son $(F,\,7-F)$, $(7-F,\,F)$, y las cuatro combinaciones de las caras restantes (por ejemplo $(2,5)$ y $(5,2)$, $(3,4)$ y $(4,3)$, según cuál sea $F$):

$$P(\text{suma } 7) = 2pq + 4\left(\tfrac{1}{6}\cdot\tfrac{1}{6}\right) = 2pq + \tfrac{1}{9}$$

Igualamos a $\tfrac{71}{450}$:

$$2pq = \tfrac{71}{450} - \tfrac{50}{450} = \tfrac{21}{450} = \tfrac{7}{150} \implies pq = \tfrac{7}{300}$$

Con $q = \tfrac{1}{3} - p$:

$$p\left(\tfrac{1}{3} - p\right) = \tfrac{7}{300} \implies 300p^2 - 100p + 7 = 0$$

El discriminante es $10000 - 8400 = 1600$, así que:

$$p = \frac{100 \pm 40}{600} \implies p = \tfrac{7}{30} \quad \text{o} \quad p = \tfrac{1}{10}$$

Como $p > \tfrac{1}{6}$, tenemos $p = \tfrac{7}{30}$ (y $q = \tfrac{1}{10}$). Verificación: $2\cdot\tfrac{7}{30}\cdot\tfrac{1}{10} + \tfrac{1}{9} = \tfrac{7}{150} + \tfrac{1}{9} = \tfrac{21}{450} + \tfrac{50}{450} = \tfrac{71}{450}$ ✓

Con $m = 7$, $n = 30$ (coprimos): $m + n = 37$.

\boxed{37}