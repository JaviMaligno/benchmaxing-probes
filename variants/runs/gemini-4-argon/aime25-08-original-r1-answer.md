Para resolver el sistema de ecuaciones en el plano complejo, interpretamos geométricamente cada una de las ecuaciones escribiendo $z = x + yi$, con $x, y \in \mathbb{R}$.

**Paso 1: Analizar la primera ecuación**
$$|25+20i-z| = 5 \iff |z - (25+20i)| = 5$$
Esta ecuación representa una circunferencia en el plano cartesiano con centro en $C(25, 20)$ y radio $R = 5$.

**Paso 2: Analizar la segunda ecuación**
$$|z - (k+4)| = |z - (k+3i)|$$
Dado que $k$ es un número real, esta ecuación representa el lugar geométrico de los puntos $z = (x, y)$ que equidistan de los puntos $A(k+4, 0)$ y $B(k, 3)$, es decir, la mediatriz del segmento $AB$.

Elevando al cuadrado ambos lados y sustituyendo $z = x + yi$:
$$(x - k - 4)^2 + y^2 = (x - k)^2 + (y - 3)^2$$
Desarrollando respecto a $(x - k)$ y $y$:
$$(x - k)^2 - 8(x - k) + 16 + y^2 = (x - k)^2 + y^2 - 6y + 9$$
Simplificando los términos cuadráticos:
$$-8x + 8k + 16 = -6y + 9$$
$$8x - 6y - (8k + 7) = 0$$

**Paso 3: Condición de solución única**
El sistema tiene exactamente una solución compleja $z$ si y solo si la recta $8x - 6y - (8k + 7) = 0$ es tangente a la circunferencia de centro $C(25, 20)$ y radio $R = 5$.

La distancia del centro $C(25, 20)$ a la recta debe ser igual al radio $R = 5$:
$$\frac{|8(25) - 6(20) - (8k + 7)|}{\sqrt{8^2 + (-6)^2}} = 5$$

Calculamos los valores numéricos:
$$\frac{|200 - 120 - 8k - 7|}{\sqrt{64 + 36}} = 5$$
$$\frac{|73 - 8k|}{10} = 5$$
$$|8k - 73| = 50$$

**Paso 4: Hallar la suma de los valores posibles de $k$**
De la ecuación con valor absoluto obtenemos dos valores posibles para $k$:
1. $8k_1 - 73 = 50 \implies k_1 = \frac{123}{8}$
2. $8k_2 - 73 = -50 \implies k_2 = \frac{23}{8}$

Sumando ambos valores:
$$k_1 + k_2 = \frac{123}{8} + \frac{23}{8} = \frac{146}{8} = \frac{73}{4}$$

Como $m = 73$ y $n = 4$ son enteros positivos coprimos, tenemos que:
$$m + n = 73 + 4 = 77$$

\boxed{77}