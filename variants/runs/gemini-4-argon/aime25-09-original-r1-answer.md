Para encontrar el punto de intersección en el cuarto cuadrante entre la parábola original $P_1: y = x^2 - 4$ y su imagen rotada $P_2$, podemos usar una rotación inversa.

### Paso 1: Ecuación de la parábola rotada
Un punto $(x, y)$ pertenece a la parábola $P_2$ (rotada $60^\circ$ en sentido antihorario alrededor del origen) si y solo si al rotar $(x, y)$ un ángulo de $60^\circ$ en sentido horario alrededor del origen, el punto resultante $(x', y')$ pertenece a la parábola original $P_1$.

Las fórmulas para rotar un punto $(x, y)$ un ángulo de $60^\circ$ en sentido horario son:
$$x' = x \cos(60^\circ) + y \sin(60^\circ) = \frac{1}{2}x + \frac{\sqrt{3}}{2}y$$
$$y' = -x \sin(60^\circ) + y \cos(60^\circ) = -\frac{\sqrt{3}}{2}x + \frac{1}{2}y$$

Para que $(x, y)$ esté en la intersección de ambas parábolas, debe cumplir simultáneamente:
1. $y = x^2 - 4$
2. $y' = (x')^2 - 4$

### Paso 2: Factorización del sistema
Restando ambas ecuaciones obtenemos:
$$y - y' = x^2 - (x')^2 = (x - x')(x + x')$$

Expresemos $y - y'$, $x - x'$ y $x + x'$ en términos de $x$ e $y$:
$$y - y' = y - \left(-\frac{\sqrt{3}}{2}x + \frac{1}{2}y\right) = \frac{\sqrt{3}}{2}x + \frac{1}{2}y$$
$$x - x' = x - \left(\frac{1}{2}x + \frac{\sqrt{3}}{2}y\right) = \frac{1}{2}x - \frac{\sqrt{3}}{2}y$$
$$x + x' = x + \left(\frac{1}{2}x + \frac{\sqrt{3}}{2}y\right) = \frac{3}{2}x + \frac{\sqrt{3}}{2}y = \sqrt{3}\left(\frac{\sqrt{3}}{2}x + \frac{1}{2}y\right) = \sqrt{3}(y - y')$$

Sustituyendo $x + x' = \sqrt{3}(y - y')$ en la diferencia de las ecuaciones:
$$y - y' = \sqrt{3}(x - x')(y - y')$$
$$(y - y')\left(\sqrt{3}(x - x') - 1\right) = 0$$

Esto divide las soluciones en dos casos:

### Paso 3: Análisis de los casos en el cuarto cuadrante ($x > 0, y < 0$)

**Caso 1:** $y - y' = 0$
$$\frac{\sqrt{3}}{2}x + \frac{1}{2}y = 0 \implies y = -\sqrt{3}x \implies x = -\frac{y}{\sqrt{3}}$$
*(Geométricamente, como la parábola original es simétrica respecto al eje $y$, los puntos sobre la recta $y = -\sqrt{3}x$ cumplen que $(x', y') = (-x, y)$, por lo que pertenecen automáticamente a ambas parábolas).*

Sustituyendo $x = -\frac{y}{\sqrt{3}}$ en $y = x^2 - 4$:
$$y = \frac{y^2}{3} - 4 \implies y^2 - 3y - 12 = 0$$

Las soluciones para $y$ son:
$$y = \frac{3 \pm \sqrt{9 - 4(1)(-12)}}{2} = \frac{3 \pm \sqrt{57}}{2}$$

Como buscamos un punto en el cuarto cuadrante ($x > 0$ e $y < 0$), y sabemos que $y = -\sqrt{3}x$, la condición $x > 0$ equivale a $y < 0$. Dado que $\sqrt{57} > 3$, la única solución con $y < 0$ en este caso es:
$$y = \frac{3 - \sqrt{57}}{2}$$
Para este valor, $x = \frac{\sqrt{19} - \sqrt{3}}{2} > 0$, por lo que el punto está efectivamente en el cuarto cuadrante.

**Caso 2:** $\sqrt{3}(x - x') = 1$
$$\sqrt{3}\left(\frac{1}{2}x - \frac{\sqrt{3}}{2}y\right) = 1 \implies \sqrt{3}x - 3y = 2 \implies \sqrt{3}x = 3y + 2$$
Si el punto estuviera en el cuarto cuadrante ($x > 0, y < 0$), sustituyendo $y = x^2 - 4$ obtenemos $3x^2 - \sqrt{3}x - 10 = 0$, cuya única raíz positiva es $x = \frac{\sqrt{3} + \sqrt{123}}{6}$. Sin embargo, para esta raíz se tiene $3y = \sqrt{3}x - 2 = \frac{3 + \sqrt{369}}{6} - 2 > 0$, lo que da un punto en el primer cuadrante (y la raíz negativa da un punto en el tercer cuadrante).

### Paso 4: Cálculo de $a + b + c$
La coordenada $y$ del único punto de intersección en el cuarto cuadrante es:
$$y = \frac{3 - \sqrt{57}}{2}$$

Comparando con la forma $\frac{a - \sqrt{b}}{c}$, identificamos $a = 3$, $b = 57$ y $c = 2$ (donde $a$ y $c$ son enteros positivos coprimos). Por lo tanto:
$$a + b + c = 3 + 57 + 2 = 62$$

\boxed{62}