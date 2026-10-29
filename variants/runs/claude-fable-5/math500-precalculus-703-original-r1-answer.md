El polinomio es la suma alternante $z^8 - z^7 + \cdots - z + 1$, que se puede escribir como

$$\frac{z^9 + 1}{z + 1},$$

ya que $(z+1)(z^8 - z^7 + \cdots + 1) = z^9 + 1$.

Por lo tanto, las raíces del polinomio son las soluciones de $z^9 = -1$ excluyendo $z = -1$.

**Raíces de $z^9 = -1$:** como $-1 = e^{i\pi}$, las soluciones son
$$z = e^{i\theta}, \quad \theta = \frac{(2k+1)\pi}{9}, \quad k = 0, 1, \dots, 8,$$
todas con $r = 1$.

**Exclusión:** la raíz $z = -1$ corresponde a $\theta = \pi$, que ocurre cuando $k = 4$.

**Suma de todos los $\theta$:**
$$\sum_{k=0}^{8} \frac{(2k+1)\pi}{9} = \frac{\pi}{9}\sum_{k=0}^{8}(2k+1) = \frac{\pi}{9} \cdot 81 = 9\pi.$$

Restando el valor excluido $\theta = \pi$:
$$9\pi - \pi = 8\pi.$$

$$\boxed{8\pi}$$