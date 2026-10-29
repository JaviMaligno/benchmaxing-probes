Para determinar la suma de todos los posibles valores de $r^2$, establecemos un sistema de coordenadas cartesianas tridimensional con origen en el punto $X = (0, 0, 0)$. 

Dado que las cuerdas $\overline{PQ}$, $\overline{RS}$ y $\overline{TU}$ son mutuamente perpendiculares y se intersecan en $X$, podemos alinear los ejes coordenados $x, y, z$ con estas tres cuerdas, orientando el sentido positivo de cada eje desde $X$ hacia los puntos $P, R$ y $T$, respectivamente. De este modo, las coordenadas de estos tres puntos son:
$$P = (1, 0, 0), \quad R = (0, 2, 0), \quad T = (0, 0, 3)$$

Sea $O = (x_0, y_0, z_0)$ el centro de la esfera. Como $OX = \sqrt{2}$, la distancia al cuadrado desde el centro $O$ hasta el origen $X$ cumple:
$$x_0^2 + y_0^2 + z_0^2 = OX^2 = 2$$

La ecuación de la esfera de centro $O$ y radio $r$ es:
$$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2$$

Dado que $P, R$ y $T$ pertenecen a la esfera, sustituimos las coordenadas de cada punto en la ecuación:

1. Para $P(1, 0, 0)$:
$$(1 - x_0)^2 + y_0^2 + z_0^2 = r^2 \implies 1 - 2x_0 + (x_0^2 + y_0^2 + z_0^2) = r^2$$
Usando $x_0^2 + y_0^2 + z_0^2 = 2$, obtenemos:
$$3 - 2x_0 = r^2 \implies x_0 = \frac{3 - r^2}{2}$$

2. Para $R(0, 2, 0)$:
$$x_0^2 + (2 - y_0)^2 + z_0^2 = r^2 \implies 4 - 4y_0 + (x_0^2 + y_0^2 + z_0^2) = r^2$$
$$6 - 4y_0 = r^2 \implies y_0 = \frac{6 - r^2}{4}$$

3. Para $T(0, 0, 3)$:
$$x_0^2 + y_0^2 + (3 - z_0)^2 = r^2 \implies 9 - 6z_0 + (x_0^2 + y_0^2 + z_0^2) = r^2$$
$$11 - 6z_0 = r^2 \implies z_0 = \frac{11 - r^2}{6}$$

Sustituyendo estas expresiones para $x_0, y_0, z_0$ en la relación $x_0^2 + y_0^2 + z_0^2 = 2$ y definiendo $u = r^2$, tenemos:
$$\left(\frac{3 - u}{2}\right)^2 + \left(\frac{6 - u}{4}\right)^2 + \left(\frac{11 - u}{6}\right)^2 = 2$$

Multiplicamos toda la ecuación por el mínimo común múltiplo de los denominadores ($4, 16, 36$), que es $144$:
$$36(u - 3)^2 + 9(u - 6)^2 + 4(u - 11)^2 = 288$$

Desarrollamos cada término:
$$36(u^2 - 6u + 9) + 9(u^2 - 12u + 36) + 4(u^2 - 22u + 121) = 288$$
$$(36 + 9 + 4)u^2 - (216 + 108 + 88)u + (324 + 324 + 484) = 288$$
$$49u^2 - 412u + 1132 = 288$$
$$49u^2 - 412u + 844 = 0$$

Verificamos que ambas soluciones sean reales y cumplan la condición de que $X$ esté en el interior de la esfera ($r^2 = u > OX^2 = 2$):
- El discriminante dividido entre $4$ es $\Delta/4 = 206^2 - 49 \cdot 844 = 42436 - 41356 = 1080 > 0$, por lo que existen dos raíces reales distintas.
- Ambas raíces son $u = \frac{206 \pm \sqrt{1080}}{49} \approx \frac{206 \pm 32.86}{49}$, las cuales son mayores que $2$, garantizando que $X$ se encuentra estrictamente dentro de la esfera en ambos casos.

Por las fórmulas de Vieta, la suma de los posibles valores de $u = r^2$ es:

\boxed{\frac{412}{49}}