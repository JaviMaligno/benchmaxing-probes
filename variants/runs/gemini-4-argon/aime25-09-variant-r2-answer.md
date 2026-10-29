Para hallar la coordenada $y$ del punto de intersección en el cuarto cuadrante, podemos utilizar las propiedades de simetría de la parábola o las ecuaciones de rotación.

### Paso 1: Ecuación de la parábola rotada y simetría
La parábola original $P$ tiene por ecuación:
$$y = x^2 - 5$$
Esta parábola es simétrica respecto al eje $y$, lo que significa que si un punto $(-x, y)$ pertenece a $P$, el punto $(x, y)$ también pertenece a $P$.

Un punto $(x, y)$ pertenece a la parábola rotada $60^\circ$ en sentido antihorario, $P'$, si y solo si al rotar $(x, y)$ un ángulo de $60^\circ$ en sentido horario alrededor del origen obtenemos un punto $(x_0, y_0)$ que pertenece a la parábola original $P$.

Las fórmulas para rotar $(x, y)$ un ángulo de $60^\circ$ en sentido horario ($-60^\circ$) son:
$$x_0 = x \cos(-60^\circ) - y \sin(-60^\circ) = \frac{1}{2}x + \frac{\sqrt{3}}{2}y$$
$$y_0 = x \sin(-60^\circ) + y \cos(-60^\circ) = -\frac{\sqrt{3}}{2}x + \frac{1}{2}y$$

Observemos que si buscamos un punto de intersección tal que $(x_0, y_0) = (-x, y)$ (el simétrico de $(x, y)$ en la parábola original $P$), ambas condiciones $y = x^2 - 5$ e $y_0 = x_0^2 - 5$ se cumplen simultáneamente. Igualando $y_0 = y$:
$$-\frac{\sqrt{3}}{2}x + \frac{1}{2}y = y \implies \frac{1}{2}y = -\frac{\sqrt{3}}{2}x \implies y = -\sqrt{3}x$$
Verificamos que con $y = -\sqrt{3}x$ también se cumple $x_0 = -x$:
$$x_0 = \frac{1}{2}x + \frac{\sqrt{3}}{2}(-\sqrt{3}x) = \frac{1}{2}x - \frac{3}{2}x = -x$$
Geométricamente, esto se debe a que la recta $y = -\sqrt{3}x$ (que forma un ángulo de $-60^\circ$ con el eje $x$ positivo) es la bisectriz entre los ejes de simetría de $P$ y $P'$.

### Paso 2: Intersección en el cuarto cuadrante
Sustituimos $x = -\frac{y}{\sqrt{3}}$ (o $y = -\sqrt{3}x$) en la ecuación de la parábola original $y = x^2 - 5$:
$$-\sqrt{3}x = x^2 - 5 \implies x^2 + \sqrt{3}x - 5 = 0$$

Resolvemos esta ecuación cuadrática para $x$:
$$x = \frac{-\sqrt{3} \pm \sqrt{(\sqrt{3})^2 - 4(1)(-5)}}{2} = \frac{-\sqrt{3} \pm \sqrt{23}}{2}$$

En el cuarto cuadrante se cumple que $x > 0$ e $y < 0$. Como $\sqrt{23} > \sqrt{3}$, la única solución con $x > 0$ es:
$$x = \frac{\sqrt{23} - \sqrt{3}}{2}$$

Calculamos ahora la coordenada $y$ correspondiente usando $y = -\sqrt{3}x$:
$$y = -\sqrt{3}\left(\frac{\sqrt{23} - \sqrt{3}}{2}\right) = \frac{3 - \sqrt{69}}{2}$$
Como $\sqrt{69} > 3$, tenemos $y < 0$, por lo que este punto está efectivamente en el cuarto cuadrante.

### Paso 3: Cálculo de $a + b + c$
Comparando $y = \frac{3 - \sqrt{69}}{2}$ con la forma $\frac{a - \sqrt{b}}{c}$, identificamos:
- $a = 3$
- $b = 69$
- $c = 2$

Aquí $a$, $b$ y $c$ son enteros positivos y $\operatorname{mcd}(3, 2) = 1$. Por lo tanto:
$$a + b + c = 3 + 69 + 2 = 74$$

\boxed{74}