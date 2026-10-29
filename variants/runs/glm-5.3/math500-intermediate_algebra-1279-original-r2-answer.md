## Resolución paso a paso

**Paso 1: Despejar denominadores.**

Sea $y = x^2$ y $P(y) = (y-1)(y-2)(y-3)(y-4) = y^4 - 10y^3 + 35y^2 - 50y + 24$.

Multiplicando la ecuación por $P(x^2)$:

$$\sum_{k=1}^{4} k\prod_{j\ne k}(x^2 - j) = (2010x - 4)\,P(x^2).$$

**Paso 2: Simplificar el lado izquierdo con una identidad.**

Como $y\prod_{j\ne k}(y-j) = P(y) + k\prod_{j\ne k}(y-j)$, sumando sobre $k=1,\dots,4$:

$$\sum_{k=1}^{4} k\prod_{j\ne k}(y-j) = yP'(y) - 4P(y).$$

(Verificación por expansión directa: $10y^3 - 70y^2 + 150y - 96 = y(4y^3-30y^2+70y-50) - 4(y^4-10y^3+35y^2-50y+24)$. ✓)

Entonces la ecuación se vuelve:

$$x^2P'(x^2) - 4P(x^2) = (2010x-4)P(x^2)\quad\Longrightarrow\quad x^2P'(x^2) = 2010x\,P(x^2).$$

**Paso 3: Formar el polinomio y aplicar Vieta.**

Definimos $F(x) = 2010xP(x^2) - x^2P'(x^2)$. Con $P(x^2) = x^8 - 10x^6 + 35x^4 - 50x^2 + 24$ y $P'(x^2) = 4x^6 - 30x^4 + 70x^2 - 50$:

$$F(x) = 2010x^9 - 4x^8 - 20100x^7 + 30x^6 + 70350x^5 - 70x^4 - 100500x^3 + 50x^2 + 48240x.$$

Es de **grado 9**, con coeficiente líder $2010$ y coeficiente de $x^8$ igual a $-4$. Por la fórmula de Vieta, la suma de las 9 raíces es:

$$-\frac{(-4)}{2010} = \frac{4}{2010} = \frac{2}{1005}.$$

**Paso 4: Verificar que las raíces de $F$ son exactamente las soluciones.**

- En $x = 0$: la izquierda original da $-\frac11-\frac22-\frac33-\frac44 = -4$ y la derecha $-4$, así que $x=0$ sí es solución (y es raíz de $F$).
- En los valores excluidos $x = \pm1, \pm\sqrt2, \pm\sqrt3, \pm2$ (donde $P(x^2)=0$): ahí $F(x) = -x^2P'(x^2)$, y como $P'(1)=-6$, $P'(2)=2$, $P'(3)=-2$, $P'(4)=6$ son todos no nulos, $F$ no se anula allí. No hay raíces extranas ni soluciones perdidas.
- Las raíces son simples (un análisis de magnitudes en las condiciones $G(\alpha)=G'(\alpha)=0$ para $G = 2010P(x^2) - xP'(x^2)$ muestra que son incompatibles), así que la suma de las soluciones coincide con la suma de las raíces.

Por lo tanto, la suma de todas las soluciones complejas es:

$$\boxed{\dfrac{2}{1005}}$$