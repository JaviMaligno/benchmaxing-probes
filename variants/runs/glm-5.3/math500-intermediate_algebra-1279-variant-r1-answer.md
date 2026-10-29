# Planteamiento

Multiplico la ecuación por $P(x) = (x^2-1)(x^2-2)(x^2-3)(x^2-4)$ para obtener un polinomio.

**Paso 1: Expandir $P(x)$.** Con $y = x^2$:
$$(y-1)(y-2)(y-3)(y-4) = y^4 - 10y^3 + 35y^2 - 50y + 24,$$
verificando con Vieta: suma de raíces $= 1+2+3+4 = 10$, pares $= 35$, triples $= 50$, producto $= 24$. Así:
$$P(x) = x^8 - 10x^6 + 35x^4 - 50x^2 + 24.$$

**Paso 2: Estructura de la ecuación polinomial.** Al multiplicar, el lado izquierdo es
$$E(x) = \sum_{k=1}^{4} k\prod_{j\neq k}(x^2 - j),$$
un polinomio **par** de grado $\le 6$ (cada término tiene grado 6). La ecuación queda:
$$E(x) = 2022x\,P(x) - 4P(x) \quad\Longrightarrow\quad 2022x\,P(x) - 4P(x) - E(x) = 0.$$

**Paso 3: Grado y coeficientes clave.** El término $2022x\,P(x)$ tiene grado 9 con coeficiente líder $2022$, así que el polinomio tiene grado 9 y por lo tanto 9 raíces complejas.

- Coeficiente de $x^9$: solo proviene de $2022x\,P(x)$, que es $2022$.
- Coeficiente de $x^8$: como $P$ es par, $2022xP$ solo tiene potencias impares, y $E$ solo llega a $x^6$. La única contribución es $-4P(x)$, que da $-4$.

**Paso 4: Vieta.** La suma de las 9 raíces es:
$$-\frac{(-4)}{2022} = \frac{4}{2022} = \frac{2}{1011}.$$

**Paso 5: Verificar que no hay raíces espurias.** En un polo $x_0 \in \{\pm1,\pm\sqrt2,\pm\sqrt3,\pm2\}$, se tiene $P(x_0)=0$ pero $E(x_0) = k_0\prod_{j\neq k_0}(x_0^2-j)\neq 0$, así que los polos **no** son raíces del polinomio. Las 9 raíces del polinomio son exactamente las raíces de la ecuación original.

$$\boxed{\dfrac{2}{1011}}$$