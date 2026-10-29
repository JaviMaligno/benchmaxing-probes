## Solución

**Paso 1: Limpiar denominadores.**
Multiplicando por $\prod_{j=1}^{4}(x^2 - j)$ obtenemos el polinomio

$$P(x) = (2010x-4)\prod_{j=1}^{4}(x^2-j) \;-\; \sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j) = 0.$$

**Paso 2: Verificar que no aparecen raíces extra.**
Si $x^2 = m$ (con $m\in\{1,2,3,4\}$), entonces $P(x) = -m\prod_{j\neq m}(m-j)\neq 0$, así que los polos no son raíces de $P$. Por lo tanto, las raíces de $P$ son exactamente las soluciones de la ecuación original.

**Paso 3: Grado y coeficientes principales.**
- $\prod_{j=1}^{4}(x^2-j)$ es par en $x$, de grado 8 con coeficiente principal $1$ (solo potencias pares).
- $(2010x-4)\cdot(x^8+\cdots)$: el coeficiente de $x^9$ es $2010$; el de $x^8$ es $-4$ (el término $2010x$ solo produce potencias impares, pues no hay $x^7$ en el producto).
- La suma $\sum_k k\prod_{j\neq k}(x^2-j)$ es par en $x$ y de grado 6, así que no aporta a los coeficientes de $x^9$ ni $x^8$.

Entonces $P(x) = 2010x^9 - 4x^8 + (\text{términos de grado}\le 7)$.

**Paso 4: Fórmula de Vieta.**
Para un polinomio de grado 9, la suma de todas las raíces es $-a_8/a_9$:

$$\text{Suma} = -\frac{-4}{2010} = \frac{4}{2010} = \frac{2}{1005}.$$

$\boxed{\dfrac{2}{1005}}$