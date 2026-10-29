## Resolución

Sea $\alpha = \arccos x$, $\beta = \arccos 2x$, $\gamma = \arccos 4x$, con $\alpha + \beta + \gamma = \pi$.

Entonces $\gamma = \pi - (\alpha + \beta)$, y tomando coseno:
$$\cos\gamma = -\cos(\alpha+\beta) = \sin\alpha\sin\beta - \cos\alpha\cos\beta.$$

Sustituyendo $\cos\alpha = x$, $\cos\beta = 2x$, $\cos\gamma = 4x$:
$$4x = \sqrt{1-x^2}\sqrt{1-4x^2} - 2x^2,$$
es decir,
$$2x^2 + 4x = \sqrt{(1-x^2)(1-4x^2)}.$$

Elevando al cuadrado:
$$4x^4 + 16x^3 + 16x^2 = 4x^4 - 5x^2 + 1,$$
$$16x^3 + 21x^2 - 1 = 0.$$

Este es el polinomio cúbico con coeficientes enteros (irreducible salvo múltiplos escalares, pues la cúbica mínima está determinada hasta un factor constante), así que:
$$|a| + |b| + |c| + |d| = 16 + 21 + 0 + 1 = 38.$$

$$\boxed{38}$$