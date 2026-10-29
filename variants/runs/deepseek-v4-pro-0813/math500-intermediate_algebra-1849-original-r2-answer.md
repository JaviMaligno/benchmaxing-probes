Voy a resolver el problema paso a paso.

**1. Dominio de la ecuación**

La ecuación es:

$$\log(kx) = 2\log(x+2)$$

Para que los logaritmos estén definidos:

- $kx > 0$
- $x + 2 > 0$, es decir, $x > -2$

**2. Manipulación algebraica**

$$\log(kx) = 2\log(x+2) = \log\big((x+2)^2\big)$$

Como el logaritmo es inyectivo:

$$kx = (x+2)^2$$

$$x^2 + 4x + 4 = kx$$

$$x^2 + (4-k)x + 4 = 0$$

**3. Condiciones para las soluciones**

Las soluciones de la cuadrática deben cumplir $x > -2$ y además $kx > 0$.

El discriminante es:

$$\Delta = (4-k)^2 - 16 = k^2 - 8k = k(k-8)$$

Para que haya soluciones reales: $\Delta \ge 0$, es decir $k \le 0$ o $k \ge 8$.

**4. Análisis de número de soluciones**

- Si $\Delta < 0$: no hay soluciones reales.
- Si $\Delta = 0$: una solución doble de la cuadrática. Ocurre para $k = 0$ o $k = 8$.
- Si $\Delta > 0$: dos soluciones distintas de la cuadrática.

**Caso $k = 0$:**

La ecuación original es $\log(0 \cdot x) = 2\log(x+2)$. Pero $\log(0)$ no está definido, así que $k=0$ no es válido. De hecho, $kx = 0$ nunca cumple $kx > 0$.

**Caso $k = 8$:**

La cuadrática es:

$$x^2 - 4x + 4 = (x-2)^2 = 0$$

Solución doble: $x = 2$. Verificamos:

- $x = 2 > -2$ ✓
- $kx = 8 \cdot 2 = 16 > 0$ ✓

Entonces $k = 8$ da exactamente una solución real.

**Caso $\Delta > 0$, es decir $k < 0$ o $k > 8$:**

La cuadrática tiene dos raíces:

$$x = \frac{k-4 \pm \sqrt{k(k-8)}}{2}$$

**Subcaso $k > 8$:**

El producto de las raíces es $4 > 0$ y la suma es $k - 4 > 4 > 0$. Por tanto ambas raíces son positivas, así que ambas cumplen $x > -2$. Además $kx > 0$ porque $k > 8 > 0$ y $x > 0$.

Luego para $k > 8$ hay **dos** soluciones, exactamente una no.

**Subcaso $k < 0$:**

El producto de las raíces es $4 > 0$, así que ambas tienen el mismo signo. La suma es $k - 4 < -4 < 0$, así que ambas son negativas.

Veamos cuándo son mayores que $-2$.

Las raíces son:

$$x = \frac{k-4 \pm \sqrt{k(k-8)}}{2}$$

Para $k < 0$, la raíz más grande es la de signo $+$. Necesitamos que esta cumpla $x > -2$. La raíz menor siempre será más negativa que la mayor, así que con que la mayor sea $> -2$, la menor también lo será.

Imponemos a la raíz mayor:

$$\frac{k-4 + \sqrt{k(k-8)}}{2} > -2$$

$$k - 4 + \sqrt{k(k-8)} > -4$$

$$k + \sqrt{k(k-8)} > 0$$

Sea $k < 0$. Escribimos $k = -m$ con $m > 0$:

$$-m + \sqrt{m(m+8)} > 0$$

$$\sqrt{m(m+8)} > m$$

$$m(m+8) > m^2$$

$$8m > 0 \quad \Rightarrow \quad m > 0$$

Esto es cierto siempre que $m > 0$. Por tanto **ambas raíces** cumplen $x > -2$ para todo $k < 0$.

Además, para $k < 0$ y $x < 0$ (ambas raíces son negativas), se cumple $kx > 0$ porque el producto de dos negativos es positivo. 

Entonces, para $k < 0$, ambas raíces son soluciones válidas. Luego hay **dos** soluciones, no exactamente una.

**Conclusión del conteo:**

- $k = 8$: exactamente una solución.
- $k < 0$: dos soluciones.
- $k > 8$: dos soluciones.
- $0 < k < 8$: ninguna.
- $k = 0$: no definida.

Por tanto, en el intervalo $[-500, 500]$, el único valor que da exactamente una solución real es $k = 8$.

El número de valores enteros es **1**.

\boxed{1}