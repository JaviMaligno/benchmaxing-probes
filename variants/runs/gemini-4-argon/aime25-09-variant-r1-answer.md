Para hallar el punto de intersección en el cuarto cuadrante entre la parábola original $P: y = x^2 - 5$ y su imagen $P'$ tras una rotación de $60^\circ$ en sentido antihorario alrededor del origen, planteamos las ecuaciones correspondientes.

### Paso 1: Ecuación de la parábola rotada
Un punto $(x, y)$ pertenece a la parábola rotada $P'$ si y solo si al rotarlo $60^\circ$ en sentido horario alrededor del origen se obtiene un punto $(u, v)$ que pertenece a la parábola original $P$.

Aplicando la rotación de $60^\circ$ en sentido horario:
$$u = x \cos 60^\circ + y \sin 60^\circ = \frac{1}{2}x + \frac{\sqrt{3}}{2}y$$
$$v = -x \sin 60^\circ + y \cos 60^\circ = -\frac{\sqrt{3}}{2}x + \frac{1}{2}y$$

Como tanto $(x, y)$ como $(u, v)$ pertenecen a la parábola $P$, se cumplen simultáneamente las ecuaciones:
1. $y = x^2 - 5$
2. $v = u^2 - 5$

### Paso 2: Factorización del sistema
Restando la segunda ecuación de la primera, obtenemos:
$$y - v = x^2 - u^2 = (x - u)(x + u)$$

Expresamos $y - v$ y $x + u$ en función de $x$ e $y$:
$$y - v = y - \left(-\frac{\sqrt{3}}{2}x + \frac{1}{2}y\right) = \frac{\sqrt{3}}{2}x + \frac{1}{2}y$$
$$x + u = x + \left(\frac{1}{2}x + \frac{\sqrt{3}}{2}y\right) = \frac{3}{2}x + \frac{\sqrt{3}}{2}y = \sqrt{3}\left(\frac{\sqrt{3}}{2}x + \frac{1}{2}y\right) = \sqrt{3}(y - v)$$

Por lo tanto, $y - v = \frac{1}{\sqrt{3}}(x + u)$. Sustituyendo esta relación en $y - v = (x - u)(x + u)$, resulta:
$$\frac{1}{\sqrt{3}}(x + u) = (x - u)(x + u)$$
$$(x + u)\left(x - u - \frac{1}{\sqrt{3}}\right) = 0$$

Esto divide las soluciones en dos casos:

### Paso 3: Análisis de los casos en el cuarto cuadrante ($x > 0, y < 0$)

**Caso 1: $x - u = \frac{1}{\sqrt{3}}$**
Sustituyendo $u$:
$$x - \left(\frac{1}{2}x + \frac{\sqrt{3}}{2}y\right) = \frac{1}{\sqrt{3}} \implies \frac{1}{2}x - \frac{\sqrt{3}}{2}y = \frac{1}{\sqrt{3}} \implies 3y = \sqrt{3}x - 2$$
Sustituyendo $y = x^2 - 5$:
$$3(x^2 - 5) = \sqrt{3}x - 2 \implies 3x^2 - \sqrt{3}x - 13 = 0$$
Las raíces son $x = \frac{\sqrt{3} \pm \sqrt{159}}{6}$.
- Para la raíz positiva $x = \frac{\sqrt{3} + \sqrt{159}}{6}$, tenemos $\sqrt{3}x = \frac{3 + \sqrt{477}}{6} > \frac{3 + 21}{6} = 4 > 2$, por lo que $3y = \sqrt{3}x - 2 > 0 \implies y > 0$ (primer cuadrante).
- Para la otra raíz, $x < 0$ (tercer cuadrante).

Por tanto, este caso no aporta puntos en el cuarto cuadrante.

**Caso 2: $x + u = 0$**
Sustituyendo $u$:
$$\frac{3}{2}x + \frac{\sqrt{3}}{2}y = 0 \implies y = -\sqrt{3}x$$
Despejando $x = -\frac{y}{\sqrt{3}}$ y sustituyendo en $y = x^2 - 5$:
$$y = \left(-\frac{y}{\sqrt{3}}\right)^2 - 5 \implies y = \frac{y^2}{3} - 5 \implies y^2 - 3y - 15 = 0$$

Aplicando la fórmula cuadrática:
$$y = \frac{3 \pm \sqrt{(-3)^2 - 4(1)(-15)}}{2} = \frac{3 \pm \sqrt{69}}{2}$$

Como el punto buscado está en el cuarto cuadrante ($y < 0$ y $x = -\frac{y}{\sqrt{3}} > 0$), tomamos la raíz negativa:
$$y = \frac{3 - \sqrt{69}}{2}$$

### Paso 4: Cálculo de $a + b + c$
Comparando $y = \frac{3 - \sqrt{69}}{2}$ con la forma $\frac{a - \sqrt{b}}{c}$, identificamos $a = 3$, $b = 69$ y $c = 2$ (donde $a$ y $c$ son enteros positivos coprimos).

Finalmente:
$$a + b + c = 3 + 69 + 2 = 74$$

\boxed{74}