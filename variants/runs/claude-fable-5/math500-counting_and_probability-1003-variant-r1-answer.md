Para resolver esto, planteo las probabilidades de cada cara.

**Configuración.** Sea $p$ la probabilidad de la cara $F$ y $q$ la de la cara opuesta. Como las otras cuatro caras tienen probabilidad $1/6$ cada una, la suma total da:

$$p + q + 4\cdot\tfrac{1}{6} = 1 \quad\Rightarrow\quad p + q = \tfrac{1}{3}$$

**Probabilidad de sumar 7.** Al lanzar dos dados, la suma es 7 solo cuando salen caras opuestas entre sí (porque las caras opuestas suman 7). Los pares que la logran son:

- $F$ en un dado y su opuesta en el otro: contribuye $2pq$.
- Los otros dos pares de caras opuestas (cuatro caras con probabilidad $1/6$): cada par contribuye $2\cdot\tfrac{1}{6}\cdot\tfrac{1}{6}$, y hay dos pares, es decir $\tfrac{4}{36} = \tfrac{1}{9}$.

Entonces:

$$2pq + \tfrac{1}{9} = \tfrac{71}{450}$$

$$2pq = \tfrac{71}{450} - \tfrac{50}{450} = \tfrac{21}{450} = \tfrac{7}{150} \quad\Rightarrow\quad pq = \tfrac{7}{300}$$

**Resolver el sistema.** $p$ y $q$ son raíces de $t^2 - \tfrac{1}{3}t + \tfrac{7}{300} = 0$, es decir $300t^2 - 100t + 7 = 0$:

$$t = \frac{100 \pm \sqrt{10000 - 8400}}{600} = \frac{100 \pm 40}{600}$$

Las raíces son $\tfrac{140}{600} = \tfrac{7}{30}$ y $\tfrac{60}{600} = \tfrac{1}{10}$. Como $p > \tfrac{1}{6}$, tenemos $p = \tfrac{7}{30}$ (y efectivamente $q = \tfrac{1}{10} < \tfrac{1}{6}$).

Con $m = 7$ y $n = 30$ coprimos, $m + n = 37$.

$$\boxed{37}$$