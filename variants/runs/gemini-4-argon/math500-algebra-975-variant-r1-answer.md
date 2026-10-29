Para encontrar los valores reales de $x$ que no están en el dominio de la función

$$g(x)=\frac{1}{|x^2-x-6|+|x^2-10x+21|}$$

debemos identificar los valores de $x$ que hacen que el denominador sea igual a cero, ya que la división por cero no está definida.

**Paso 1: Igualar el denominador a cero.**
$$|x^2-x-6| + |x^2-10x+21| = 0$$

**Paso 2: Analizar la propiedad del valor absoluto.**
Sabemos que el valor absoluto de cualquier número real es siempre mayor o igual a cero ($|a| \ge 0$). Por lo tanto, la suma de dos valores absolutos solo puede ser igual a cero si **ambas** expresiones dentro de los valores absolutos son iguales a cero simultáneamente:
1. $x^2 - x - 6 = 0$
2. $x^2 - 10x + 21 = 0$

**Paso 3: Resolver la primera ecuación cuadrática.**
Factorizamos $x^2 - x - 6 = 0$:
$$(x - 3)(x + 2) = 0$$
Las soluciones son $x = 3$ y $x = -2$.

**Paso 4: Resolver la segunda ecuación cuadrática.**
Factorizamos $x^2 - 10x + 21 = 0$:
$$(x - 3)(x - 7) = 0$$
Las soluciones son $x = 3$ y $x = 7$.

**Paso 5: Encontrar la intersección de las soluciones.**
El único valor de $x$ que satisface ambas ecuaciones al mismo tiempo es $x = 3$. Para cualquier otro valor de $x$, al menos uno de los términos en el denominador será estrictamente positivo, haciendo que la suma sea distinta de cero.

Por lo tanto, el único valor real de $x$ que no está en el dominio de $g(x)$ es $3$.

\boxed{3}