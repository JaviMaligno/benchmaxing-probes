# Resolución paso a paso

## Planteamiento

Sea
$$A = \arccos x, \quad B = \arccos 2x, \quad C = \arccos 4x,$$
con la condición $A + B + C = \pi$.

Entonces $A + B = \pi - C$, y tomando coseno en ambos lados:
$$\cos(A+B) = \cos(\pi - C) = -\cos C = -4x.$$

## Aplicar la fórmula del coseno de una suma

$$\cos(A+B) = \cos A \cos B - \sin A \sin B = 2x^2 - \sqrt{1-x^2}\sqrt{1-4x^2}.$$

Igualando con $-4x$:
$$\sqrt{1-x^2}\sqrt{1-4x^2} = 2x^2 + 4x.$$

## Elevar al cuadrado

$$(1-x^2)(1-4x^2) = (2x^2+4x)^2$$
$$1 - 5x^2 + 4x^4 = 4x^4 + 16x^3 + 16x^2.$$

Cancelando $4x^4$ y ordenando:
$$16x^3 + 21x^2 - 1 = 0.$$

## Verificar que esta es la polinomio mínima

**Verificación de consistencia:** el polinomio tiene una raíz $x \approx 0.203$, que cumple $|4x| \le 1$ (dominio válido) y $2x^2+4x > 0$ (necesario al despejar la raíz cuadrada). Se comprueba numéricamente que $\arccos(0.203) + \arccos(0.406) + \arccos(0.812) \approx \pi$. ✓

**Irreducibilidad sobre $\mathbb{Q}$:** los posibles candidatos a raíz racional son $\pm 1, \pm\tfrac12, \pm\tfrac14, \pm\tfrac18, \pm\tfrac1{16}$, y ninguna anula $16x^3+21x^2-1$ (por ejemplo, en $x=-1$: $-16+21-1=4\neq 0$; en $x=\tfrac14$: $\tfrac14+\tfrac{21}{16}-1\neq 0$). Al ser de grado 3 sin raíces racionales, es irreducible, y como $\gcd(16,21,1)=1$, es primitiva.

Por tanto, es el polinomio mínimo de $x$, y cualquier cúbica con coeficientes enteros que tenga a $x$ como raíz debe ser un múltiplo entero suyo. El valor mínimo de $|a|+|b|+|c|+|d|$ se obtiene con el propio polinomio:

$$|16| + |21| + |0| + |-1| = 16+21+1 = 38.$$

\boxed{38}