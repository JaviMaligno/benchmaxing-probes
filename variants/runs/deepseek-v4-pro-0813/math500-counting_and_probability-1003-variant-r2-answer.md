Sea $p$ la probabilidad de sacar la cara $F$. Entonces la cara opuesta tiene probabilidad $q$, y las otras cuatro caras tienen probabilidad $1/6$ cada una.

Como las probabilidades deben sumar 1:

$$p + q + \frac{4}{6} = 1 \quad\Rightarrow\quad p + q = \frac{1}{3}.$$

Además, $p > 1/6$ y $q < 1/6$.

Ahora, al lanzar dos dados, la suma es $7$ cuando una cara es opuesta de la otra. Las parejas que suman $7$ son tres pares de caras opuestas.

Sea $F$ con opuesta $F'$. Para que la suma sea $7$:

- $F$ en el primer dado y $F'$ en el segundo: probabilidad $pq$.
- $F'$ en el primer dado y $F$ en el segundo: probabilidad $qp = pq$.
- Cada uno de los otros dos pares opuestos: cada par contribuye $2 \cdot \frac16 \cdot \frac16 = \frac{1}{18}$.

Por lo tanto:

$$P(\text{suma } 7) = 2pq + 2\left(\frac{1}{18}\right) = 2pq + \frac{1}{9}.$$

Se nos da que esta probabilidad es $\frac{71}{450}$:

$$2pq + \frac19 = \frac{71}{450}.$$

Restando $\frac19 = \frac{50}{450}$:

$$2pq = \frac{21}{450} = \frac{7}{150}.$$

Así:

$$pq = \frac{7}{300}.$$

Tenemos el sistema:

$$p + q = \frac13, \qquad pq = \frac{7}{300}.$$

Las raíces de $t^2 - \frac13 t + \frac{7}{300} = 0$ son:

$$t^2 - \frac13 t + \frac{7}{300}=0.$$

Multiplicando por $300$:

$$300t^2 - 100t + 7 = 0.$$

Usando la fórmula cuadrática:

$$t = \frac{100 \pm \sqrt{10000 - 8400}}{600} = \frac{100 \pm \sqrt{1600}}{600} = \frac{100 \pm 40}{600}.$$

Las raíces son:

$$t = \frac{140}{600} = \frac{7}{30}, \qquad t = \frac{60}{600} = \frac{1}{10}.$$

Como $p > 1/6$, y

$$\frac16 = \frac{5}{30} < \frac{7}{30},$$

entonces $p = \frac{7}{30}$.

Entonces $m = 7$ y $n = 30$, y

$$m + n = 37.$$

\boxed{37}