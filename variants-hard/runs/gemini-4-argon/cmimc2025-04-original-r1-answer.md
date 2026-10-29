Para resolver el sistema de ecuaciones y encontrar el valor de $z$, podemos hacer un cambio de variable para simplificar las expresiones logarítmicas.

Definamos las siguientes variables:
$$a = \log_x y, \quad b = \log_y z, \quad c = \log_z x$$

Por las propiedades del cambio de base de los logaritmos, sabemos que:
1. $abc = \log_x y \cdot \log_y z \cdot \log_z x = 1$
2. $\log_z y = \frac{1}{\log_y z} = \frac{1}{b} = ac$
3. $\log_x z = \frac{1}{\log_z x} = \frac{1}{c} = ab$
4. $\log_y x = \frac{1}{\log_x y} = \frac{1}{a}$

Sustituyendo estas expresiones en la primera y tercera ecuación del sistema original, obtenemos:
$$a + b + c = 8 \quad \text{(Ecuación 1)}$$
$$ac + ab = 16 \quad \text{(Ecuación 3)}$$

Factorizando $a$ en la Ecuación 3:
$$a(b + c) = 16$$

De la Ecuación 1 sabemos que $b + c = 8 - a$. Sustituyendo esto en la expresión anterior:
$$a(8 - a) = 16$$
$$8a - a^2 = 16$$
$$a^2 - 8a + 16 = 0$$
$$(a - 4)^2 = 0 \implies a = 4$$

Como $a = \log_x y = 4$, entonces tenemos que:
$$\log_y x = \frac{1}{a} = \frac{1}{4}$$

Finalmente, sustituimos $\log_y x = \frac{1}{4}$ en la segunda ecuación del sistema original:
$$\log_{\log_y x} z = -3$$
$$\log_{1/4} z = -3$$

Por definición de logaritmo, despejamos $z$:
$$z = \left(\frac{1}{4}\right)^{-3} = 4^3 = 64$$

\boxed{64}