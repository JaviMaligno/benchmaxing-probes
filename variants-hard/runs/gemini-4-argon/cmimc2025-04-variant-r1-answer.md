Para resolver el sistema de ecuaciones, definimos las siguientes variables haciendo uso de las propiedades de los logaritmos:
$$a = \log_x y, \qquad b = \log_y z, \qquad c = \log_z x$$

Por la propiedad del cambio de base, sabemos que el producto de estos tres términos cumple:
$$abc = \log_x y \cdot \log_y z \cdot \log_z x = 1$$

Además, usando la relación $\log_u v = \frac{1}{\log_v u}$, podemos reescribir los términos de las ecuaciones dadas en función de $a, b$ y $c$:
$$\log_y x = \frac{1}{a}, \qquad \log_z y = \frac{1}{b}, \qquad \log_x z = \frac{1}{c}$$

**Paso 1: Analizar la primera y la tercera ecuación**

La primera ecuación se traduce directamente en:
$$a + b + c = 10 \implies b + c = 10 - a$$

La tercera ecuación nos dice que $\log_z y + \log_x z = 25$, lo que equivale a:
$$\frac{1}{b} + \frac{1}{c} = 25 \implies \frac{b + c}{bc} = 25$$

Como $abc = 1$, tenemos que $bc = \frac{1}{a}$. Sustituyendo $b + c = 10 - a$ y $bc = \frac{1}{a}$ en la expresión anterior, obtenemos:
$$\frac{10 - a}{1/a} = 25$$
$$a(10 - a) = 25$$
$$10a - a^2 = 25 \implies a^2 - 10a + 25 = 0$$
$$(a - 5)^2 = 0 \implies a = 5$$

*(Nota: Con $a = 5$, se tiene $b + c = 5$ y $bc = \frac{1}{5}$, cuyo discriminante $\Delta = 25 - \frac{4}{5} > 0$ garantiza soluciones reales positivas distintas de $1$ para $x, y, z$).*

**Paso 2: Encontrar el valor de $z$ con la segunda ecuación**

La segunda ecuación es:
$$\log_{\log_y x} z = -3$$

Dado que $\log_y x = \frac{1}{a} = \frac{1}{5}$, sustituimos esta base en el logaritmo:
$$\log_{1/5} z = -3$$

Por definición de logaritmo, despejamos $z$:
$$z = \left(\frac{1}{5}\right)^{-3} = 5^3 = 125$$

\boxed{125}