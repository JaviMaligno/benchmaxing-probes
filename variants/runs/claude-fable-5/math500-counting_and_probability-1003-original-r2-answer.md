Sea $p$ la probabilidad de la cara $F$ y $q$ la de su cara opuesta. Como las otras cuatro caras tienen probabilidad $1/6$ cada una, debe cumplirse:

$$p + q + 4\cdot\tfrac{1}{6} = 1 \implies p + q = \tfrac{1}{3}$$

**Probabilidad de suma 7.** Las caras opuestas suman 7, así que la suma 7 ocurre cuando un dado muestra una cara y el otro muestra su opuesta. Los pares opuestos son $(F, \text{opuesta de }F)$ y otros dos pares con probabilidad $1/6$ cada cara:

$$P(\text{suma }7) = 2pq + 4\cdot\tfrac{1}{6}\cdot\tfrac{1}{6} = 2pq + \tfrac{1}{9}$$

Igualando a $\tfrac{47}{288}$:

$$2pq = \tfrac{47}{288} - \tfrac{32}{288} = \tfrac{15}{288} = \tfrac{5}{96} \implies pq = \tfrac{5}{192}$$

**Resolviendo el sistema.** Con $p+q = \tfrac13$ y $pq = \tfrac{5}{192}$, $p$ y $q$ son raíces de:

$$t^2 - \tfrac{1}{3}t + \tfrac{5}{192} = 0$$

El discriminante es $\tfrac{1}{9} - \tfrac{5}{48} = \tfrac{16}{144} - \tfrac{15}{144} = \tfrac{1}{144}$, así que:

$$t = \frac{\tfrac{1}{3} \pm \tfrac{1}{12}}{2} = \frac{5}{24} \ \text{o}\ \frac{1}{8}$$

Como $p > \tfrac16$, tenemos $p = \tfrac{5}{24}$ (y $q = \tfrac18 < \tfrac16$, consistente). Entonces $m=5$, $n=24$, primos entre sí.

$$\boxed{29}$$