Para resolver el problema paso a paso, podemos interpretar geométricamente las ecuaciones en el plano complejo, identificando $z = x + yi$ con el punto $(x, y) \in \mathbb{R}^2$.

**Paso 1: Analizar la primera ecuación**
$$|25+20i-z| = 5 \iff |z - (25+20i)| = 5$$
Esta ecuación representa una circunferencia con centro en $C = (25, 20)$ y radio $R = 5$.

**Paso 2: Analizar la segunda ecuación**
$$|z-4-k| = |z-3i-k| \iff |z - (k+4)| = |z - (k+3i)|$$
El conjunto de puntos $z$ que equidistan de $A = (k+4, 0)$ y $B = (k, 3)$ es la mediatriz del segmento $AB$, que es una línea recta. Sustituyendo $z = x + yi$ y elevando al cuadrado ambos lados:
$$(x - k - 4)^2 + y^2 = (x - k)^2 + (y - 3)^2$$

Desarrollando los cuadrados:
$$(x - k)^2 - 8(x - k) + 16 + y^2 = (x - k)^2 + y^2 - 6y + 9$$

Restando $(x - k)^2 + y^2$ en ambos lados:
$$-8x + 8k + 16 = -6y + 9$$

Reordenando los términos en la forma general de una recta $Ax + By + C = 0$:
$$8x - 6y - (8k + 7) = 0$$

**Paso 3: Condición de solución única**
Para que el sistema tenga exactamente una solución compleja $z$, la recta debe ser tangente a la circunferencia. Esto ocurre si y solo si la distancia desde el centro de la circunferencia $C = (25, 20)$ hasta la recta es igual al radio $R = 5$.

Usando la fórmula de la distancia de un punto a una recta:
$$d = \frac{|8(25) - 6(20) - (8k + 7)|}{\sqrt{8^2 + (-6)^2}} = 5$$

Simplificando la expresión:
$$\frac{|200 - 120 - 8k - 7|}{\sqrt{64 + 36}} = 5$$
$$\frac{|73 - 8k|}{10} = 5$$
$$|73 - 8k| = 50$$

**Paso 4: Hallar los valores posibles de $k$ y su suma**
De la ecuación con valor absoluto obtenemos dos casos:
1. $73 - 8k = 50 \implies 8k = 23 \implies k_1 = \frac{23}{8}$
2. $73 - 8k = -50 \implies 8k = 123 \implies k_2 = \frac{123}{8}$

La suma de todos los valores posibles de $k$ es:
$$k_1 + k_2 = \frac{23}{8} + \frac{123}{8} = \frac{146}{8} = \frac{73}{4}$$

Como $73$ y $4$ son enteros positivos primos entre sí ($\text{mcd}(73, 4) = 1$), tenemos que $m = 73$ y $n = 4$. Por lo tanto, $m + n = 73 + 4 = 77$.

\boxed{77}