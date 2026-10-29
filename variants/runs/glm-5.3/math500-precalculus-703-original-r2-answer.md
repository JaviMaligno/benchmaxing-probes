**Paso 1: Factorizar el polinomio.**

El polinomio $z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1$ es una suma geométrica alternada de 9 términos. Multiplicando por $(z+1)$:

$$(z+1)(z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1) = z^9 + 1.$$

**Paso 2: Hallar las raíces.**

Las raíces de $z^9 + 1 = 0$ son $z = e^{i(2k+1)\pi/9}$ para $k = 0, 1, \dots, 8$. De ellas hay que excluir $z = -1$ (que corresponde a $(2k+1)\pi/9 = \pi$, es decir $k = 4$), porque cancela con el factor $(z+1)$.

**Paso 3: Listar los ángulos.**

Las raíces del polinomio original son, con $r = 1 > 0$ y $\theta \in [0, 2\pi)$:

$$\theta = \frac{\pi}{9},\ \frac{3\pi}{9},\ \frac{5\pi}{9},\ \frac{7\pi}{9},\ \frac{11\pi}{9},\ \frac{13\pi}{9},\ \frac{15\pi}{9},\ \frac{17\pi}{9}.$$

**Paso 4: Sumar.**

$$\text{Suma} = \frac{\pi}{9}(1 + 3 + 5 + 7 + 11 + 13 + 15 + 17) = \frac{\pi}{9}\cdot 72 = 8\pi.$$

(La suma de los 9 impares de 1 a 17 es $9^2 = 81$; quitando el 9 excluido queda $72$.)

$$\boxed{8\pi}$$